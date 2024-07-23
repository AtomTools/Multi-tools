import requests
from pystyle import Colors, Colorate

def clear():
    pass

def housechangertitle():
    pass

def setTitle(title):
    pass

def main():
    pass

clear()
housechangertitle()
setTitle("HypeSquad Changer")

print( "Which house do you want to be part of:\n\n01 Bravery\n02 Brilliance\n03 Balance\n\n")
print()
house = input("Enter your House choice : ")
token = str(input("\nEnter the token : "))


validityTest = requests.get('https://discordapp.com/api/v6/users/@me', headers={'Authorization': token, 'Content-Type': 'application/json'})
if validityTest.status_code != 200:
    print("\nInvalid token")
    input("\nPress ENTER to exit...")
    main()
else:
    headers = {'Authorization': token, 'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'}
    if house == "1": payload = {'house_id': 1}
    elif house == "2": payload = {'house_id': 2}
    elif house == "3": payload = {'house_id': 3}
    else:
        print("Invalid Choice")
        input("\nPress ENTER to exit...")
        main()
    r = requests.post('https://discordapp.com/api/v6/hypesquad/online', headers=headers, json=payload, timeout=10)
    if r.status_code == 204:
        print(" \nHypesquad House changed")
        input("\nPress ENTER to exit...")
        main()
    else:
        print(" \nAn error occurred, please retry")
        input("\nPress ENTER to exit")


if __name__ == "__main__":
    main()