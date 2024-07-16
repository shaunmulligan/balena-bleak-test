# SPDX-FileCopyrightText: 2020 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

"""
This example solicits that devices that provide the current time service connect to it, initiates
pairing and then prints the time every second. Additionally, it includes a Battery Service that always returns 55%.
"""

import time
import adafruit_ble
from adafruit_ble.advertising.standard import SolicitServicesAdvertisement
from adafruit_ble.services.standard import CurrentTimeService, BatteryService
from adafruit_ble.characteristics import Characteristic

class CustomBatteryService(BatteryService):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._fixed_level = 55  # Fixed battery level

    @property
    def level(self):
        return self._fixed_level

# Initialize BLE radio
radio = adafruit_ble.BLERadio()

# Create advertisement
advertisement = SolicitServicesAdvertisement()
advertisement.complete_name = "TimeAndBattery"
advertisement.solicited_services.append(CurrentTimeService)
advertisement.solicited_services.append(CustomBatteryService)
radio.start_advertising(advertisement)

# Wait for a connection
while not radio.connected:
    pass

print("connected")

# Main loop to print current time and battery level
while radio.connected:
    for connection in radio.connections:
        if not connection.paired:
            connection.pair()
            print("paired")
        cts = connection[CurrentTimeService]
        battery_service = CustomBatteryService()
        connection.add_service(battery_service)
        print(f"Current Time: {cts.current_time}")
        print(f"Battery Level: {battery_service.level}%")
    time.sleep(1)

print("disconnected")