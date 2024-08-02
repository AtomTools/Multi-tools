import random
import string
import requests
import threading


def clear():
    print("\033c", end="")

def main():
    pass

def ErrorModule(e):
    print(f"ERROR: {e}")

def generate_nitro_code():
    code = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
    return code

def nitro_check():
    code_nitro = generate_nitro_code()
    url_nitro = f'https://discord.gift/{code_nitro}'
    
    try:
        response = requests.get(f'https://discordapp.com/api/v9/entitlements/gift-codes/{code_nitro}?with_application=false&with_subscription_plan=true', timeout=1)
        if response.status_code == 200:
            print(f"GEN_VALID Status: Valid | Nitro: {url_nitro}")
        else:
            print(f"GEN_INVALID Status: Invalid | Nitro: {url_nitro}")
    except requests.exceptions.RequestException as e:
        print(f"GEN_ERROR Status: Error - {e}")

def request(threads_number):
    threads = []
    try:
        for _ in range(threads_number):
            t = threading.Thread(target=nitro_check)
            t.start()
            threads.append(t)
    except ValueError:
        print("Invalid input for threads number.")

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    try:
        clear()

        threads_number = int(input("Threads Number: "))

        while True:
            request(threads_number)

    except KeyboardInterrupt:
        print("\nProgram interrupted. Exiting...")
    except Exception as e:
        ErrorModule(e)
