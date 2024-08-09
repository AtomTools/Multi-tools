import subprocess
import requests
import socket
import platform
import concurrent.futures
import re
import whois
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_error(message):
    print(f"Error: {message}")

def ping_ip(ip_address):
    try:
        result = subprocess.run(['ping', ip_address], capture_output=True, text=True, timeout=10)
        print(f"PINGING {ip_address}")
        print(result.stdout)
    except subprocess.TimeoutExpired:
        print_error("Timeout expired. No response received.")
    except Exception as e:
        print_error(str(e))

def get_ip_information(ip_address):
    try:
        api_key = '2cae345f9d5e481ba7c306df400afbb1' 
        response = requests.get(f"https://api.ipgeolocation.io/ipgeo?apiKey={api_key}&ip={ip_address}").json()
        
        print("IP Information")

        ip_info = {
            "IP Address": response.get("ip"),
            "Continent": f"{response.get('continent_name')} ({response.get('continent_code')})",
            "Country": f"{response.get('country_name')} ({response.get('country_code3')})",
            "Region": response.get("state_prov"),
            "City": response.get("city"),
            "Postal Code": response.get("zipcode") if response.get("zipcode") else "Not available",
            "Latitude": response.get("latitude"),
            "Longitude": response.get("longitude"),
            "Time Zone": format_timezone(response.get('time_zone')),
            "ISP": response.get("isp"),
            "Organization": response.get("organization"),
            "Domain": response.get("domain") if response.get("domain") else "Not available",
            "ASN": response.get("asn"),
            "Altitude": response.get("altitude") if response.get("altitude") else "Not available",
            "Threat Level": response.get("threat").get("is_tor") if response.get("threat") else "Not available"
        }

        for key, value in ip_info.items():
            if value:
                print(f"{key}: {value}")

    except Exception as e:
        print_error(str(e))

def format_timezone(timezone_info):
    if timezone_info:
        return f"{timezone_info.get('name')} (UTC{timezone_info.get('offset')})"
    else:
        return ""

def traceroute_ip(ip_address, max_hops=30, timeout=5):
    try:
        if platform.system().lower() == "windows":
            command = ['tracert', '-h', str(max_hops), '-w', str(timeout * 1000), ip_address]
        else:
            command = ['traceroute', '-m', str(max_hops), '-w', str(timeout), ip_address]
        
        result = subprocess.run(command, capture_output=True, text=True)

        print(f"TRACEROUTE {ip_address}")
        print(result.stdout)

    except subprocess.CalledProcessError as cpe:
        print_error(f"Command failed with error: {cpe}")
    except FileNotFoundError:
        print_error("Traceroute command not found. Please ensure it is installed on your system.")
    except Exception as e:
        print_error(str(e))

def reverse_dns_lookup(ip_address, dns_server=None):
    try:
        command = ['nslookup', ip_address]
        if dns_server:
            command.append(dns_server)
        
        result = subprocess.run(command, capture_output=True, text=True)

        print(f"REVERSE DNS LOOKUP {ip_address}")
        print(result.stdout)

    except subprocess.CalledProcessError as cpe:
        print_error(f"Command failed with error: {cpe}")
    except FileNotFoundError:
        print_error("nslookup command not found. Please ensure it is installed on your system.") 
    except Exception as e:
        print_error(str(e))

def scan_port(ip_address, port, timeout=1):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        result = sock.connect_ex((ip_address, port))
        sock.close()
        return port if result == 0 else None
    except Exception as e:
        print_error(f"Error scanning port {port}: {e}")
        return None

def port_scan(ip_address, start_port=1, end_port=1024, timeout=1, max_workers=100):
    open_ports = []
    print(f"Scanning ports on {ip_address} from {start_port} to {end_port}... This may take a while.")
    
    try:
        with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = {executor.submit(scan_port, ip_address, port, timeout): port for port in range(start_port, end_port + 1)}
            for future in concurrent.futures.as_completed(futures):
                port = futures[future]
                if future.result():
                    open_ports.append(port)
                    print(f"Port {port} is open")
        
        print(f"OPEN PORTS ON {ip_address}")
        print(f"Open ports: {open_ports}")
    
    except Exception as e:
        print_error(f"An error occurred during port scanning: {e}")

def whois_lookup(ip_address):
    try:
        if not re.match(r"^\d{1,3}(\.\d{1,3}){3}$", ip_address):
            print_error("Invalid IP address format.")
            return

        result = whois.whois(ip_address)

        print(f"WHOIS LOOKUP {ip_address}")
        
        if result:
            for key, value in result.items():
                if value:
                    if isinstance(value, list):
                        for item in value:
                            print(f"{key}: {item}")
                    else:
                        print(f"{key}: {value}")
        else:
            print("No WHOIS information found for the IP address.")

    except whois.parser.PywhoisError as e:
        print_error(f"WHOIS lookup failed: {e}")
    except Exception as e:
        print_error(str(e))

def blacklist_check(ip_address):
    try:
        response = requests.get(f"https://api.abuseipdb.com/api/v2/check?ipAddress={ip_address}", headers={
            'Key': 'your_abuseipdb_api_key',
            'Accept': 'application/json'
        }).json()
        print(f"BLACKLIST CHECK {ip_address}")
        print(str(response))
    except Exception as e:
        print_error(str(e))

def asn_info(ip_address):
    try:
        response = requests.get(f"https://api.iptoasn.com/v1/as/ip/{ip_address}").json()

        print(f"ASN INFORMATION {ip_address}")
        asn_info_to_display = {
            "IP Range": response.get("announced"),
            "ASN": response.get("as_number"),
            "ASN Organization": response.get("as_description"),
            "Country": response.get("country_code"),
            "Created": response.get("allocated") if response.get("allocated") else "Unknown",
            "Last Updated": response.get("updated") if response.get("updated") else "Unknown",
        }

        for key, value in asn_info_to_display.items():
            print(f"{key}: {value}")

    except requests.RequestException as e:
        print_error(f"Error fetching ASN information: {e}")
    except Exception as e:
        print_error(str(e))

def main():
    clear()
    while True:
        print("1. Ping IP")
        print("2. Get IP Information")
        print("3. Traceroute IP")
        print("4. Reverse DNS Lookup")
        print("5. Port Scan")
        print("6. WHOIS Lookup")
        print("7. Blacklist Check")
        print("8. ASN Information")
        print("9. Exit")
        
        choice = input("Enter your choice: ").strip()
        
        if choice == '1':
            ip_address = input("Enter IP address to ping: ").strip()
            ping_ip(ip_address)
        elif choice == '2':
            ip_address = input("Enter IP address to get information for: ").strip()
            get_ip_information(ip_address)
        elif choice == '3':
            ip_address = input("Enter IP address for traceroute: ").strip()
            traceroute_ip(ip_address)
        elif choice == '4':
            ip_address = input("Enter IP address for reverse DNS lookup: ").strip()
            reverse_dns_lookup(ip_address)
        elif choice == '5':
            ip_address = input("Enter IP address for port scan: ").strip()
            start_port = int(input("Enter starting port number: ").strip())
            end_port = int(input("Enter ending port number: ").strip())
            port_scan(ip_address, start_port, end_port)
        elif choice == '6':
            ip_address = input("Enter IP address for WHOIS lookup: ").strip()
            whois_lookup(ip_address)
        elif choice == '7':
            ip_address = input("Enter IP address for blacklist check: ").strip()
            blacklist_check(ip_address)
        elif choice == '8':
            ip_address = input("Enter IP address for ASN information: ").strip()
            asn_info(ip_address)
        elif choice == '9':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
