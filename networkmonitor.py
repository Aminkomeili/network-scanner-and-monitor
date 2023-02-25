import netifaces
import psutil
import pyshark
from scapy.all import *


# شناسایی آدرس IP و آدرس MAC دستگاه
def get_ip_mac(interface):
    try:
        addrs = netifaces.ifaddresses(interface)
        ip = addrs[netifaces.AF_INET][0]['addr']
        mac = addrs[netifaces.AF_LINK][0]['addr']
        return ip, mac
    except:
        return None, None


# شناسایی تمام دستگاه‌های متصل به شبکه
def get_devices():
    devices = []
    for interface in netifaces.interfaces():
        ip, mac = get_ip_mac(interface)
        if ip and mac:
            devices.append({'interface': interface, 'ip': ip, 'mac': mac})
    return devices


# مانیتورینگ ترافیک شبکه
def monitor_traffic(interface):
    capture = pyshark.LiveCapture(interface=interface)
    for packet in capture.sniff_continuously():
        print(packet)


# اسکن پورت‌های باز برای یک دستگاه
def scan_ports(ip):
    for port in range(1, 65535):
        response = sr1(IP(dst=ip) / TCP(dport=port, flags="S"), timeout=1, verbose=0)
        if response:
            print(f"Port {port} is open on {ip}")


# مانیتورینگ میزان استفاده از پردازنده و حافظه
def monitor_system():
    while True:
        cpu_percent = psutil.cpu_percent()
        mem_percent = psutil.virtual_memory().percent
        print(f"CPU usage: {cpu_percent}%")
        print(f"Memory usage: {mem_percent}%")
        time.sleep(1)


# استفاده از توابع بالا
devices = get_devices()
print(devices)

monitor_traffic(devices[0]['interface'])

scan_ports('192.168.1.0')

monitor_system()
