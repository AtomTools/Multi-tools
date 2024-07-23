import requests
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def setTitle(title):
    print(f"{title}")

def main():
    clear()
    print("Atom Tools")

    while True:
        server_lookup()
        input("\nPress ENTER to return to the main menu")
        clear()

def server_lookup():
    setTitle("Server Lookup")
    clear()
    print("""You can find: \n\n""")
    print("""Invite Link           Inviter Username      Guild Banner        Guild Splash\n""")
    print("""Channel Name          Inviter ID            Guild Description    Guild Features\n""")
    print("""Channel ID            Guild Name            Custom Invite Link\n""")
    print("""Expiration Date       Guild ID              Verification Level\n\n\n\n""")
    invitelink = input("Insert end part of link of discord server link: ").strip()
    clear()

    try:
        if "discord.gg" in invitelink:
            code = invitelink.split('/')[-1]
        else:
            code = invitelink
        
        res = requests.get(f"https://discord.com/api/v9/invites/{code}")

        if res.status_code == 200:
            res_json = res.json()

            print(f"\nInvitation Information:")
            print(f" Invite Link: https://discord.gg/{res_json['code']}")
            print(f" Channel: {res_json['channel']['name']} ({res_json['channel']['id']})")
            print(f" Expiration Date: {res_json['expires_at']}\n")

            print(f"Inviter Information:")
            print(f" Username: {res_json['inviter']['username']}#{res_json['inviter']['discriminator']}")
            print(f" User ID: {res_json['inviter']['id']}\n")

            print(f"Server Information:")
            print(f" Name: {res_json['guild']['name']}")
            print(f" Server ID: {res_json['guild']['id']}")
            print(f" Banner: {res_json['guild']['banner']}")
            print(f" Description: {res_json['guild']['description']}")
            print(f" Custom Invite Link: {res_json['guild']['vanity_url_code']}")
            print(f" Verification Level: {res_json['guild']['verification_level']}")
            print(f" Splash: {res_json['guild']['splash']}")
            print(f" Features: {res_json['guild']['features']}")
        else:
            print(f"An error occurred while sending request (Status Code: {res.status_code})")
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
