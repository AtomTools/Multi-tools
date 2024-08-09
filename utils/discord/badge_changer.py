import requests

def clear():
    # Clear console screen (platform-independent)
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

def setTitle(title):
    # Set the console window title (Windows-specific)
    import os
    if os.name == 'nt':
        os.system(f"title {title}")

def main():
    clear()
    setTitle("HypeSquad Changer")

    print("Which house do you want to be part of:\n")
    print("01 Bravery")
    print("02 Brilliance")
    print("03 Balance\n")

    house = input("Enter your House choice: ").strip()
    token = input("Enter the token: ").strip()

    validity_test = requests.get(
        'https://discordapp.com/api/v6/users/@me',
        headers={'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'}
    )

    if validity_test.status_code != 200:
        print("\nInvalid token")
        input("\nPress ENTER to exit...")
        return

    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'
    }

    house_ids = {
        "1": 1,
        "2": 2,
        "3": 3
    }

    if house not in house_ids:
        print("Invalid Choice")
        input("\nPress ENTER to exit...")
        return

    payload = {'house_id': house_ids[house]}

    r = requests.post(
        'https://discordapp.com/api/v6/hypesquad/online',
        headers=headers,
        json=payload,
        timeout=10
    )

    if r.status_code == 204:
        print("\nHypesquad House changed successfully")
    else:
        print("\nAn error occurred, please retry")

    input("\nPress ENTER to exit")

if __name__ == "__main__":
    main()
