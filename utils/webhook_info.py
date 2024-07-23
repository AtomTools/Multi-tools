import requests

def main():
    print("Atom Tools")

def info_webhook(webhook_url):
    headers = {
        'Content-Type': 'application/json',
    }

    try:
        response = requests.get(webhook_url, headers=headers)
        response.raise_for_status() 
        webhook_info = response.json()
        print("\nInformation Webhook:")

        print(f"ID      : {webhook_info['id']}")
        print(f"Token   : {webhook_info['token']}")
        print(f"Name    : {webhook_info['name']}")
        print(f"Avatar  : {webhook_info['avatar']}")
        print(f"Type    : {'bot' if webhook_info['type'] == 1 else 'webhook utilisateur'}")
        print(f"Channel ID : {webhook_info['channel_id']}")
        print(f"Server ID  : {webhook_info['guild_id']}")

        print("\nUser information associated with the Webhook:")
        if 'user' in webhook_info and webhook_info['user']:
            user_info = webhook_info['user']
            print(f"ID          : {user_info['id']}")
            print(f"Name        : {user_info['username']}")
            print(f"DisplayName : {user_info['global_name']}")
            print(f"Number      : {user_info['discriminator']}")
            print(f"Avatar      : {user_info['avatar']}")
            print(f"Flags       : {user_info['flags']} Publique: {user_info['public_flags']}")
            print(f"Color       : {user_info['accent_color']}")
            print(f"Decoration  : {user_info['avatar_decoration_data']}")
            print(f"Banner      : {user_info['banner_color']}")
            print("")
        else:
            print("\nNo user information associated with the Webhook.")

    except requests.exceptions.RequestException as e:
        Error(e)

def Error(e):
    print(f"[ERROR] {e}")

    try:
        webhook_url = input("\nWebhook URL -> ")
        info_webhook(webhook_url)

    except Exception as e:
        Error(e)

if __name__ == "__main__":
    main()