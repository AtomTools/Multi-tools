import requests
import time
import threading
from pystyle import Colors

def clear():
    print("\033c", end="")

def setTitle(title):
    print(f"\033]0;{title}\007")


def main():
    pass

def webhookspam():
    clear()
    webhook = input(f"{Colors.red}WebHook Link: ")
    try:
        requests.post(webhook, json={'content': ""})
    except:
        print(f"Your WebHook is invalid !")
        time.sleep(2)
        clear()
    message = input(f"\n{Colors.red}Enter the message to spam ")
    amount = int(input(f"\n{Colors.red}Amount of messages to send "))
    
    def spam():
        try:
            requests.post(webhook, json={'content': message})
        except Exception as e:
            print(f"Error: {e}")

    for x in range(amount):
        threading.Thread(target=spam).start()
        time.sleep(0.1)  
    
    
    print(f"Webhook has been correctly spammed")
    input(f"\nPress ENTER to exit")
    clear()

webhookspam()

if __name__ == "__main__":
    main()