import os
import asyncio
from asyncio import sleep

from dbus_fast import BusType, MessageType
from dbus_fast.aio import MessageBus
from dbus_fast.message import Message

# work around the bleak 'bug' that the string '0' evaluates to true
if os.environ.get('BLEAK_LOGGING') == '0':
    os.environ['BLEAK_LOGGING'] = ''

from bleak import AdvertisementData, BleakClient, BleakScanner, BLEDevice
from bleak.assigned_numbers import AdvertisementDataType
from bleak.backends.bluezdbus.advertisement_monitor import OrPattern
from bleak.backends.bluezdbus.scanner import BlueZScannerArgs

devices: dict[str, tuple[BLEDevice, AdvertisementData]] = {}


def _received_device(device: BLEDevice, adv_data: AdvertisementData):
    devices[device.address] = (device, adv_data)


"""
Scanning parameters based of original example.
Explanation:
- Core specification version 5.0 | Vol 3, Part C | Section 9.1.1.2
- Core specification supplement Version 11 | Part A | Section 1.3
- Assigned Numbers Document | Section 2.3
- Simple explanation: https://docs.silabs.com/bluetooth/4.0/general/adv-and-scanning/bluetooth-adv-data-basics
"""
scanner = BleakScanner(
    _received_device,
    [],
    scanning_mode='active',
    bluez=BlueZScannerArgs(
        or_patterns=[
            OrPattern(0, AdvertisementDataType.FLAGS, b"\x06"),
            OrPattern(0, AdvertisementDataType.FLAGS, b"\x1a"),
        ]
    )
)

async def _read(device: BLEDevice) -> bool:
    sensor = BleakClient(device)

    try:
        await sensor.connect()

        # read battery
        battery = int.from_bytes(await sensor.read_gatt_char('00002a19-0000-1000-8000-00805f9b34fb'), byteorder='little')
        print(f"{sensor.address}: Battery level {battery}%")

        # # read clock
        # seconds = int.from_bytes(await sensor.read_gatt_char('99db2001-ac2d-11e3-a5e2-0800200c9a66'), byteorder='little')
        # print(f"{sensor.address}: read clock, timestamp in seconds: {seconds}")

        return True
    except Exception as e:
        print(str(e))
    finally:
        if sensor.is_connected:
            await sensor.disconnect()
            print(f"{sensor.address}: disconnected")
    return False


async def _remove_device(device: BLEDevice) -> None:
    """
    https://github.com/bluez/bluez/blob/master/doc/org.bluez.Adapter.rst#void-removedeviceobject-device
    """

    bus = None

    try:
        bus = await MessageBus(bus_type=BusType.SYSTEM).connect()

        response = await bus.call(Message(
            destination='org.bluez',
            path='/org/bluez/hci0',
            interface='org.bluez.Adapter1',
            member='RemoveDevice',
            signature='o',
            body=[device.details['path']]
        ))

        if response.message_type == MessageType.METHOD_RETURN or (
                response.message_type == MessageType.ERROR and response.error_name == 'org.bluez.Error.DoesNotExist'
        ):
            # print(f"{device.address}: Removed device successfully, or device has already been removed")
            return

        message = response.body[0] if len(response.body) > 1 else '{Empty response}'
        error = response.error_name if response.error_name is not None else '{No Error}'

        # print(f"{device.address}: Could not remove device. (Msg: {message}; Err: {error})")
    except Exception as e:
        raise e
    finally:
        if bus and bus.connected:
            bus.disconnect()


async def run() -> None:
    global devices
    global scanner

    stats = {
        'C0:A4:7A:2F:1C:C5': {
            'tries': 0,
            'successful': 0
        }
    }

    for i in range(10):
        devices = {}

        print("Start scanning")

        await scanner.start()
        await sleep(15)
        await scanner.stop()

        print(f"Found {len(devices)} devices in last scan")

        # ... some logic to filter found devices against a whitelist

        # sleep in order to let bluetooth figure out the service and characteristic discovery process
        await sleep(.5)

        for address in devices:
            device = devices[address][0]

            # Ensure the address is in the stats dictionary
            if address not in stats:
                stats[address] = {'tries': 0, 'successful': 0}

            stats[address]['tries'] += 1

            if await _read(device):
                stats[address]['successful'] += 1

            await _remove_device(device)

        # wait for 5 minutes in order to stay close to production environment
        await sleep(15) # originally was 300

    print(stats)

asyncio.run(run())