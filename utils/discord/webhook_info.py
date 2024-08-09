import requests
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_info(message):
    print(message)

def print_error(message):
    print(f"[ERROR] {message}")

def info_webhook(webhook_url):
    headers = {
        'Content-Type': 'application/json',
    }

    try:
        response = requests.get(webhook_url, headers=headers)
        response.raise_for_status() 
        webhook_info = response.json()
        clear()
        print("\nInformation Webhook:")

        print(f"ID : {webhook_info.get('id', 'None')}")
        print(f"Token : {webhook_info.get('token', 'None')}")
        print(f"Name : {webhook_info.get('name', 'None')}")
        print(f"Avatar : {webhook_info.get('avatar', 'None')}")
        print(f"Type  : {'bot' if webhook_info.get('type') == 1 else 'webhook utilisateur'}")
        print(f"Channel ID : {webhook_info.get('channel_id', 'None')}")
        print(f"Server ID  : {webhook_info.get('guild_id', 'None')}")

        print("\nUser information associated with the Webhook:")
        if 'user' in webhook_info and webhook_info['user']:
            user_info = webhook_info['user']
            print(f"ID : {user_info.get('id', 'None')}")
            print(f"Name : {user_info.get('username', 'None')}")
            print(f"DisplayName : {user_info.get('global_name', 'None')}")
            print(f"Number : {user_info.get('discriminator', 'None')}")
            print(f"Avatar : {user_info.get('avatar', 'None')}")
            print(f"Flags : {user_info.get('flags', 'None')} Publique: {user_info.get('public_flags', 'None')}")
            print(f"Color : {user_info.get('accent_color', 'None')}")
            print(f"Decoration : {user_info.get('avatar_decoration_data', 'None')}")
            print(f"Banner : {user_info.get('banner_color', 'None')}")
            print("")
        else:
            print("\nNo user information associated with the Webhook.")

    except requests.exceptions.RequestException as e:
        print_error(e)
        handle_error()

def handle_error():
    try:
        webhook_url = input("Webhook URL :").strip()
        info_webhook(webhook_url)
    except Exception as e:
        print_error(f"Error during URL input: {e}")

if __name__ == "__main__":
    clear()
    webhook_url = input("Enter Webhook URL: ").strip()
    info_webhook(webhook_url)
