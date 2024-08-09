import random
import threading
import subprocess
import sys
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def print_error(e):
    print(f"Error: {e}")

def create_files(folder_name, valid_file_name, invalid_file_name):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    
    valid_file_path = os.path.join(folder_name, valid_file_name)
    invalid_file_path = os.path.join(folder_name, invalid_file_name)
    
    with open(valid_file_path, "w") as valid_file, open(invalid_file_path, "w") as invalid_file:
        pass  
    
    return valid_file_path, invalid_file_path

def ip_check(valid_file_path, invalid_file_path):
    global number_valid, number_invalid
    number_1 = random.randint(1, 255)
    number_2 = random.randint(1, 255)
    number_3 = random.randint(1, 255)
    number_4 = random.randint(1, 255)
    ip = f"{number_1}.{number_2}.{number_3}.{number_4}"

    try:
        if sys.platform.startswith("win"):
            result = subprocess.run(['ping', '-n', '1', ip], capture_output=True, text=True, timeout=1)
        elif sys.platform.startswith("linux"):
            result = subprocess.run(['ping', '-c', '1', '-W', '1', ip], capture_output=True, text=True, timeout=1)

        if result.returncode == 0:
            number_valid += 1
            status = "Valid"
            with open(valid_file_path, "a") as valid_file:
                valid_file.write(f"{ip}\n")
        else:
            number_invalid += 1
            status = "Invalid"
            with open(invalid_file_path, "a") as invalid_file:
                invalid_file.write(f"{ip}\n")
        
        print(f"Logs: {number_invalid} invalid - {number_valid} valid | Status: {status} | IP: {ip}")
    except Exception as e:
        number_invalid += 1
        print(f"Logs: {number_invalid} invalid - {number_valid} valid | Status: Invalid | IP: {ip}")
        print_error(e)

def request(valid_file_path, invalid_file_path):
    threads = []
    try:
        for _ in range(threads_number):
            t = threading.Thread(target=ip_check, args=(valid_file_path, invalid_file_path))
            t.start()
            threads.append(t)
    except ValueError:
        print_error("Invalid number of threads")
        sys.exit(1)

    for thread in threads:
        thread.join()

def main():
    folder_name = "ip_data"
    valid_file_name = "ipvalids.txt"
    invalid_file_name = "ipinvalids.txt"
    
    valid_file_path, invalid_file_path = create_files(folder_name, valid_file_name, invalid_file_name)

    try:
        clear()
        global threads_number
        threads_number = int(input("Threads Number -> "))
    except ValueError:
        print_error("Invalid number of threads")
        sys.exit(1)

    while True:
        request(valid_file_path, invalid_file_path)

if __name__ == "__main__":
    main()
