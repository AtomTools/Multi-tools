import requests
import time

def clear():
    pass

def autologintitle():
    pass

def setTitle(title):
    pass

def main():
    pass

def autologin():
    from selenium import webdriver
    setTitle("Auto Login")
    clear()
    autologintitle()
    print("Enter the token of the account you want to connect to")
    entertoken = input("Token: ")
    validityTest = requests.get('https://discordapp.com/api/v6/users/@me', headers={'Authorization': entertoken, 'Content-Type': 'application/json'})
    if validityTest.status_code != 200:
        print("\nInvalid token")
        input("Press ENTER to exit")
        main()
    try:
        options = webdriver.ChromeOptions()
        options.add_argument("--disable-blink-features=AutomationControlled")
        driver = webdriver.Chrome(options=options)
        driver.maximize_window()
        driver.get('https://discord.com/login')
        js = 'function login(token) {setInterval(() => {document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`}, 50);setTimeout(() => {location.reload();}, 500);}'
        time.sleep(3)
        driver.execute_script(js + f'login("{entertoken}")')
        time.sleep(10)
        if driver.current_url == 'https://discord.com/login':
            clear()
            autologintitle()
            print("""Connection Failed""")
            driver.close()
        else:
            clear()
            autologintitle()
            print("""Connection Established""")
        input("""Press ENTER to exit""")
        main()
    except Exception as e:
        print(f"A problem occurred: {e}")
        time.sleep(2)
        clear()
        main()

autologin()

if __name__ == "__main__":
    main()