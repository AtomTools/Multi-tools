import requests
import os
from pystyle import Colors

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_title(title):
    print(f"{Colors.blue}{'=' * 60}\n{title}\n{'=' * 60}{Colors.reset}")

def print_error(message):
    print(f"{Colors.red}Error: {message}{Colors.reset}")

def print_info(message):
    print(f"{Colors.green}{message}{Colors.reset}")

def print_header(header):
    """Prints a header with cyan color."""
    print(f"{Colors.cyan}{header}{Colors.reset}")

def server_lookup():
    clear()
    print_header("Discord Server Lookup")
    print("""You can find: \n\n""")
    print("""Invite Link           Inviter Username      Guild Banner        Guild Splash\n""")
    print("""Channel Name          Inviter ID            Guild Description    Guild Features\n""")
    print("""Channel ID            Guild Name            Custom Invite Link\n""")
    print("""Expiration Date       Guild ID              Verification Level\n\n\n\n""")
    
    invitelink = input(f"{Colors.yellow}Insert end part of link of discord server link: {Colors.reset}").strip()
    clear()

    try:
        if "discord.gg" in invitelink:
            code = invitelink.split('/')[-1]
        else:
            code = invitelink
        
        res = requests.get(f"https://discord.com/api/v9/invites/{code}")

        if res.status_code == 200:
            res_json = res.json()

            print_header("Invitation Information:")
            print_info(f"Invite Link: https://discord.gg/{res_json['code']}")
            print_info(f"Channel: {res_json['channel']['name']} ({res_json['channel']['id']})")
            print_info(f"Expiration Date: {res_json['expires_at']}\n")

            print_header("Inviter Information:")
            print_info(f"Username: {res_json['inviter']['username']}#{res_json['inviter']['discriminator']}")
            print_info(f"User ID: {res_json['inviter']['id']}\n")

            print_header("Server Information:")
            print_info(f"Name: {res_json['guild']['name']}")
            print_info(f"Server ID: {res_json['guild']['id']}")
            print_info(f"Banner: {res_json['guild']['banner']}")
            print_info(f"Description: {res_json['guild']['description']}")
            print_info(f"Custom Invite Link: {res_json['guild']['vanity_url_code']}")
            print_info(f"Verification Level: {res_json['guild']['verification_level']}")
            print_info(f"Splash: {res_json['guild']['splash']}")
            print_info(f"Features: {', '.join(res_json['guild']['features'])}")
        else:
            print_error(f"An error occurred while sending request (Status Code: {res.status_code})")
        
    except Exception as e:
        print_error(f"Error: {e}")

def main():
    clear()
    print_header("Atom Tools")

    while True:
        server_lookup()
        input(f"{Colors.yellow}\nPress ENTER to return to the main menu{Colors.reset}")
        clear()

if __name__ == "__main__":
    main()
