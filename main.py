import asyncio
from bleak import BleakScanner, BleakClient
from bleak.exc import BleakError
from collections import defaultdict

BATTERY_LEVEL_CHARACTERISTIC_UUID = "00002a19-0000-1000-8000-00805f9b34fb"
CONNECT_TIMEOUT = 10.0  # seconds

async def scan_and_connect(device_data):
    scanner = BleakScanner()
    devices = await scanner.discover()

    for device in devices:
        try:
            async with BleakClient(device.address, timeout=CONNECT_TIMEOUT) as client:
                device_info = device_data[device.address]
                device_info['successful_connections'] += 1

                try:
                    battery_level = await client.read_gatt_char(BATTERY_LEVEL_CHARACTERISTIC_UUID)
                    battery_percentage = int.from_bytes(battery_level, byteorder='little')
                    print(f"Connected to {device.name}, Battery level: {battery_percentage}%")
                    device_info['successful_battery_reads'] += 1
                except (BleakError, asyncio.exceptions.TimeoutError, asyncio.exceptions.CancelledError, EOFError) as e:
                    print(f"Connected to {device.name}, but failed to read battery level: {e}")
        except (BleakError, asyncio.exceptions.TimeoutError, asyncio.exceptions.CancelledError, EOFError) as e:
            print(f"Failed to connect to {device.name}: {e}")

async def main():
    device_data = defaultdict(lambda: {'successful_connections': 0, 'successful_battery_reads': 0})

    for i in range(10):
        print(f"Attempt {i+1}:")
        await scan_and_connect(device_data)
        print(f"Attempt {i+1} complete.\n")
        await asyncio.sleep(5)  # Delay between scans
    
    print("Final device data:")
    for device_address, info in device_data.items():
        print(f"Device: {device_address}, Successful connections: {info['successful_connections']}, Successful battery reads: {info['successful_battery_reads']}")

if __name__ == "__main__":
    asyncio.run(main())