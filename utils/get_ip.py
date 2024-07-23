import os
import sys
import socket
import requests
from json import JSONDecodeError
from datetime import datetime


def main():
    pass

def ErrorModule(e):
    print(f"Error: {e}")

def Title(title):
    print(f"{title}")

def Reset():
    print("Reset")


Title("Get Your IP")

try:
    print(f"\nYour IP is not sent to anyone.")
    try:
        response = requests.get('https://api.ipify.org?format=json')
        ip_address_public = response.json().get('ip', 'None')
    except (requests.RequestException, JSONDecodeError) as e:
        ip_address_public = "None"
        ErrorModule(e)

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip_address_local = s.getsockname()[0]
        s.close()
    except Exception as e:
        ip_address_local = "None"
        ErrorModule(e)

    try:
        ip_address_ipv6 = []
        all_interfaces = socket.getaddrinfo(socket.gethostname(), None)
        for interface in all_interfaces:
            if interface[0] == socket.AF_INET6:
                ip_address_ipv6.append(interface[4][0])
        ip_address_ipv6 = ' / '.join(ip_address_ipv6) if ip_address_ipv6 else "None"
    except Exception as e:
        ip_address_ipv6 = "None"
        ErrorModule(e)

    print(f"""
IP Public [IPv4] : {ip_address_public}
IP Local  [IPv4] : {ip_address_local}
IPv6 : {ip_address_ipv6}
    """)

    Reset()
except Exception as e:
    ErrorModule(e)


if __name__ == "__main__":
    main()
