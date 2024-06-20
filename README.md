Test container for running bleak (a python lib for bluetooth):

This container just scans and connects to any Polar heart rate monitor, reads the battery level of it and then crashes and restarts.

The purpose is to try and stress the bluetooth implementation and check its robustness to repeated starts.

Example output:
```
root@d2d4607:~# balena logs main_9026354_3055595_74771f7ad3d24327ce0561d4728cba61
Scanning for BLE devices
Connecting to C0:A4:7A:2F:1C:C5: Polar H9 D2735C22...
WARNING:root:Could not determine BlueZ version, bluetoothctl not available, assuming 5.51+
Connected: True
Battery level 100%
Symlink /run/dbus/system_bus_socket already exists.
Scanning for BLE devices
Connecting to C0:A4:7A:2F:1C:C5: Polar H9 D2735C22...
WARNING:root:Could not determine BlueZ version, bluetoothctl not available, assuming 5.51+
Connected: True
Battery level 100%
Symlink /run/dbus/system_bus_socket already exists.
Scanning for BLE devices
Connecting to C0:A4:7A:2F:1C:C5: Polar H9 D2735C22...
WARNING:root:Could not determine BlueZ version, bluetoothctl not available, assuming 5.51+
Connected: True
Battery level 100%
Symlink /run/dbus/system_bus_socket already exists.
Scanning for BLE devices
Connecting to C0:A4:7A:2F:1C:C5: Polar H9 D2735C22...
WARNING:root:Could not determine BlueZ version, bluetoothctl not available, assuming 5.51+
Connected: True
Battery level 100%
Symlink /run/dbus/system_bus_socket already exists.
Scanning for BLE devices
Connecting to C0:A4:7A:2F:1C:C5: Polar H9 D2735C22...
WARNING:root:Could not determine BlueZ version, bluetoothctl not available, assuming 5.51+
Connected: True
Battery level 100%
Symlink /run/dbus/system_bus_socket already exists.
Scanning for BLE devices
Connecting to C0:A4:7A:2F:1C:C5: Polar H9 D2735C22...
WARNING:root:Could not determine BlueZ version, bluetoothctl not available, assuming 5.51+
Connected: True
Battery level 100%
Symlink /run/dbus/system_bus_socket already exists.
Scanning for BLE devices
Connecting to C0:A4:7A:2F:1C:C5: Polar H9 D2735C22...
WARNING:root:Could not determine BlueZ version, bluetoothctl not available, assuming 5.51+
Connected: True
Battery level 100%
Symlink /run/dbus/system_bus_socket already exists.
Scanning for BLE devices
Connecting to C0:A4:7A:2F:1C:C5: Polar H9 D2735C22...
WARNING:root:Could not determine BlueZ version, bluetoothctl not available, assuming 5.51+
Connected: True
Battery level 100%
Symlink /run/dbus/system_bus_socket already exists.
Scanning for BLE devices
Connecting to C0:A4:7A:2F:1C:C5: Polar H9 D2735C22...
WARNING:root:Could not determine BlueZ version, bluetoothctl not available, assuming 5.51+
Connected: True
Battery level 100%
Symlink /run/dbus/system_bus_socket already exists.
Scanning for BLE devices
Connecting to C0:A4:7A:2F:1C:C5: Polar H9 D2735C22...
WARNING:root:Could not determine BlueZ version, bluetoothctl not available, assuming 5.51+
Connected: True
Battery level 100%
Symlink /run/dbus/system_bus_socket already exists.
Scanning for BLE devices
Connecting to C0:A4:7A:2F:1C:C5: Polar H9 D2735C22...
WARNING:root:Could not determine BlueZ version, bluetoothctl not available, assuming 5.51+
Connected: True
Battery level 100%
Symlink /run/dbus/system_bus_socket already exists.
Scanning for BLE devices
Connecting to C0:A4:7A:2F:1C:C5: Polar H9 D2735C22...
WARNING:root:Could not determine BlueZ version, bluetoothctl not available, assuming 5.51+
Connected: True
Battery level 100%
root@d2d4607:~# 
root@d2d4607:~# balena logs main_9026354_3055595_74771f7ad3d24327ce0561d4728cba61
Scanning for BLE devices
Connecting to C0:A4:7A:2F:1C:C5: Polar H9 D2735C22...
WARNING:root:Could not determine BlueZ version, bluetoothctl not available, assuming 5.51+
Connected: True
Battery level 100%
Symlink /run/dbus/system_bus_socket already exists.
Scanning for BLE devices
Connecting to C0:A4:7A:2F:1C:C5: Polar H9 D2735C22...
WARNING:root:Could not determine BlueZ version, bluetoothctl not available, assuming 5.51+
Connected: True
Battery level 100%
Symlink /run/dbus/system_bus_socket already exists.
Scanning for BLE devices
Connecting to C0:A4:7A:2F:1C:C5: Polar H9 D2735C22...
WARNING:root:Could not determine BlueZ version, bluetoothctl not available, assuming 5.51+
Connected: True
Battery level 100%
Symlink /run/dbus/system_bus_socket already exists.
Scanning for BLE devices
Connecting to C0:A4:7A:2F:1C:C5: Polar H9 D2735C22...
WARNING:root:Could not determine BlueZ version, bluetoothctl not available, assuming 5.51+
Connected: True
Battery level 100%
Symlink /run/dbus/system_bus_socket already exists.
Scanning for BLE devices
Connecting to C0:A4:7A:2F:1C:C5: Polar H9 D2735C22...
WARNING:root:Could not determine BlueZ version, bluetoothctl not available, assuming 5.51+
Connected: True
Battery level 100%
Symlink /run/dbus/system_bus_socket already exists.
Scanning for BLE devices
Connecting to C0:A4:7A:2F:1C:C5: Polar H9 D2735C22...
WARNING:root:Could not determine BlueZ version, bluetoothctl not available, assuming 5.51+
Connected: True
Battery level 100%
Symlink /run/dbus/system_bus_socket already exists.
Scanning for BLE devices
Connecting to C0:A4:7A:2F:1C:C5: Polar H9 D2735C22...
WARNING:root:Could not determine BlueZ version, bluetoothctl not available, assuming 5.51+
Connected: True
Battery level 100%
Symlink /run/dbus/system_bus_socket already exists.
Scanning for BLE devices
Connecting to C0:A4:7A:2F:1C:C5: Polar H9 D2735C22...
WARNING:root:Could not determine BlueZ version, bluetoothctl not available, assuming 5.51+
Connected: True
Battery level 100%
Symlink /run/dbus/system_bus_socket already exists.
Scanning for BLE devices
Connecting to C0:A4:7A:2F:1C:C5: Polar H9 D2735C22...
WARNING:root:Could not determine BlueZ version, bluetoothctl not available, assuming 5.51+
Connected: True
Battery level 100%
Symlink /run/dbus/system_bus_socket already exists.
Scanning for BLE devices
Connecting to C0:A4:7A:2F:1C:C5: Polar H9 D2735C22...
WARNING:root:Could not determine BlueZ version, bluetoothctl not available, assuming 5.51+
Connected: True
Battery level 100%
Symlink /run/dbus/system_bus_socket already exists.
Scanning for BLE devices
Connecting to C0:A4:7A:2F:1C:C5: Polar H9 D2735C22...
WARNING:root:Could not determine BlueZ version, bluetoothctl not available, assuming 5.51+
Connected: True
Battery level 100%
Symlink /run/dbus/system_bus_socket already exists.
Scanning for BLE devices
Connecting to C0:A4:7A:2F:1C:C5: Polar H9 D2735C22...
WARNING:root:Could not determine BlueZ version, bluetoothctl not available, assuming 5.51+
Connected: True
Battery level 100%
Symlink /run/dbus/system_bus_socket already exists.
Scanning for BLE devices
Connecting to C0:A4:7A:2F:1C:C5: Polar H9 D2735C22...
WARNING:root:Could not determine BlueZ version, bluetoothctl not available, assuming 5.51+
Connected: True
Battery level 100%
Symlink /run/dbus/system_bus_socket already exists.
Scanning for BLE devices
Connecting to C0:A4:7A:2F:1C:C5: Polar H9 D2735C22...
WARNING:root:Could not determine BlueZ version, bluetoothctl not available, assuming 5.51+
Connected: True
Battery level 100%
Symlink /run/dbus/system_bus_socket already exists.
Scanning for BLE devices
Connecting to C0:A4:7A:2F:1C:C5: Polar H9 D2735C22...
WARNING:root:Could not determine BlueZ version, bluetoothctl not available, assuming 5.51+
Connected: True
Battery level 100%
```
