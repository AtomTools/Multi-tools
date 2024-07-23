import requests
import time
import threading

def clear():
    print("\033c", end="")

def setTitle(title):
    print(f"\033]0;{title}\007")


def main():
    print("Returning to main menu...")

def webhookspam():
    setTitle("WebHook Spammer")
    clear()
    webhook = input(f"WebHook Link: ")
    try:
        requests.post(webhook, json={'content': ""})
    except:
        print(f"Your WebHook is invalid !")
        time.sleep(2)
        clear()
        main()
    print(f"\nEnter the message to spam ")
    message = input(f"Message: ")
    print(f"\nAmount of messages to send ")
    amount = int(input(f"Amount: "))
    
    def spam():
        try:
            requests.post(webhook, json={'content': message})
        except Exception as e:
            print(f"Error: {e}")

    for x in range(amount):
        threading.Thread(target=spam).start()
        time.sleep(0.1)  
    
    clear()
    print(f"Webhook has been correctly spammed")
    input(f"\nPress ENTER to exit")
    main()

webhookspam()

if __name__ == "__main__":
    main()