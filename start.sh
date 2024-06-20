set -e  # Exit immediately if a command exits with a non-zero status.
set -u  # Treat unset variables as an error when substituting.
set -o pipefail  # Consider errors in a pipeline as fatal.

# Ensure the dbus system bus socket directory and symlink are properly set up
mkdir -p /run/dbus
if [ ! -L /run/dbus/system_bus_socket ]; then
    ln -s /host/run/dbus/system_bus_socket /run/dbus/system_bus_socket
else
    echo "Symlink /run/dbus/system_bus_socket already exists."
fi

# Execute the Python script
python polar_HRM.py

# Keep the container running
#balena-idle
