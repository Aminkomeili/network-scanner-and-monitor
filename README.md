# Network Scanner and Monitor

This is a Python script for scanning and monitoring a network using the following libraries:

1. scapy for network packet manipulation
2. netifaces for getting network interface information
3. psutil for getting system resource usage information
4. pyshark for live network traffic capture and analysis


## Installation

1. Clone the repository: git clone https://github.com/username/network-scanner-monitor.git
2. Install the required dependencies: 

`pip install -r requirements.txt`

## Usage
### Get network devices information

The get_devices() function returns a list of dictionaries containing the interface name, IP address, and MAC address for each device connected to the network.

```
import network_scanner_monitor
devices = network_scanner_monitor.get_devices()
print(devices)
```

### Monitor network traffic

The monitor_traffic(interface) function captures and prints live network traffic on the specified interface.

```
import network_scanner_monitor
devices = network_scanner_monitor.get_devices()
network_scanner_monitor.monitor_traffic(devices[0]['interface'])
```

### Scan open ports for a device

The scan_ports(ip) function scans for open ports on the specified IP address.
```
import network_scanner_monitor
network_scanner_monitor.scan_ports('192.168.1.1')
```

### Monitor system resource usage

The monitor_system() function prints the current CPU and memory usage every second.
```
import network_scanner_monitor
network_scanner_monitor.monitor_system()
```

### Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

### License

MIT
