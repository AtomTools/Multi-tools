import os
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from deep_translator import GoogleTranslator

def clear():
    print("\033c", end="")

def continue_prompt():
    input("\nPress Enter to continue...")

def only_windows():
    print("This option is only available on Windows.")
    continue_prompt()
    clear()

def only_linux():
    print("This option is only available on Linux.")
    continue_prompt()
    clear()

def error_choice():
    print("Invalid choice. Please select a valid option.")
    continue_prompt()
    clear()

def error_module(e):
    print(f"Error importing module: {e}")
    continue_prompt()
    clear()

def error(e):
    print(f"An error occurred: {e}")
    continue_prompt()
    clear()

def text_translated(text):
    try:
        translated_text = GoogleTranslator(source='auto', target='en').translate(text)
    except Exception as e:
        print(f"Translation error: {e}")
        translated_text = text
    return translated_text

def tiktok_search(driver, username):
    try:
        link = f"https://www.tiktok.com/@{username}"
        driver.get(link)
        driver.implicitly_wait(10)
        time.sleep(2)
        if "This account cannot be found" in text_translated(driver.execute_script("return document.documentElement.innerText")):
            return False
        else:
            return link
    except Exception as e:
        return f"Error: {e}"

def instagram_search(driver, username):
    try:
        link = f"https://instagram.com/{username}"
        driver.get(link)
        driver.implicitly_wait(10)
        time.sleep(2)
        if "This page is unfortunately not available" in text_translated(driver.execute_script("return document.documentElement.innerText")):
            return False
        else:
            return link
    except Exception as e:
        return f"Error: {e}"

def giters_search(driver, username):
    try:
        link = f"https://giters.com/{username}"
        driver.get(link)
        driver.implicitly_wait(10)
        time.sleep(2)
        if "This page could not be found" in text_translated(driver.execute_script("return document.documentElement.innerText")):
            return False
        elif username in driver.execute_script("return document.documentElement.innerText"):
            return link
        else:
            return False
    except Exception as e:
        return f"Error: {e}"

def github_search(driver, username):
    try:
        link = f"https://github.com/{username}"
        driver.get(link)
        driver.implicitly_wait(10)
        time.sleep(2)
        if "Find code, projects, and people on GitHub" in text_translated(driver.execute_script("return document.documentElement.innerText")):
            return False
        else:
            return link
    except Exception as e:
        return f"Error: {e}"

def paypal_search(driver, username):
    try:
        link = f"https://www.paypal.com/paypalme/{username}"
        driver.get(link)
        driver.implicitly_wait(10)
        time.sleep(2)
        if "We cannot find this profile" in text_translated(driver.execute_script("return document.documentElement.innerText")):
            return False
        elif "We were not able to process your request. Please try again later" in text_translated(driver.execute_script("return document.documentElement.innerText")):
            return "Error: Rate Limit"
        else:
            return link
    except Exception as e:
        return f"Error: {e}"

def telegram_search(driver, username):
    try:
        link = f"https://t.me/{username}"
        driver.get(link)
        driver.implicitly_wait(10)
        time.sleep(2)
        if "If you have Telegram, you can contact" in text_translated(driver.execute_script("return document.documentElement.innerText")):
            return False
        elif "a new era of messaging" in text_translated(driver.execute_script("return document.documentElement.innerText")):
            return False
        else:
            return link
    except Exception as e:
        return f"Error: {e}"

def snapchat_search(driver, username):
    try:
        link = f"https://www.snapchat.com/add/{username}"
        driver.get(link)
        driver.implicitly_wait(10)
        time.sleep(2)
        if "This content could not be found" in text_translated(driver.execute_script("return document.documentElement.innerText")):
            return False
        else:
            return link
    except Exception as e:
        return f"Error: {e}"

def linktree_search(driver, username):
    try:
        link = f"https://linktr.ee/{username}"
        driver.get(link)
        driver.implicitly_wait(10)
        time.sleep(2)
        if "The page you’re looking for doesn’t exist" in text_translated(driver.execute_script("return document.documentElement.innerText")):
            return False
        else:
            return link
    except Exception as e:
        return f"Error: {e}"

def roblox_search(driver, username):
    try:
        link = f"https://www.roblox.com/search/users?keyword={username}"
        driver.get(link)
        driver.implicitly_wait(10)
        time.sleep(2)
        if "No results available for" in text_translated(driver.execute_script("return document.documentElement.innerText")):
            return False
        else:
            return link
    except Exception as e:
        return f"Error: {e}"

def streamlabs_search(driver, username):
    try:
        link = f"https://streamlabs.com/{username}/tip"
        driver.get(link)
        driver.implicitly_wait(10)
        time.sleep(2)
        if "UNAUTHORIZED" in text_translated(driver.execute_script("return document.documentElement.innerText")):
            return False
        elif "401" in text_translated(driver.execute_script("return document.documentElement.innerText")):
            return False
        else:
            return link
    except Exception as e:
        return f"Error: {e}"

def pinterest_search(driver, username):
    try:
        link = f"https://www.pinterest.com/{username}"
        driver.get(link)
        driver.implicitly_wait(10)
        time.sleep(2)
        if "Sorry, we couldn’t find any Pins for" in text_translated(driver.execute_script("return document.documentElement.innerText")):
            return False
        else:
            return link
    except Exception as e:
        return f"Error: {e}"

def reddit_search(driver, username):
    try:
        link = f"https://www.reddit.com/user/{username}"
        driver.get(link)
        driver.implicitly_wait(10)
        time.sleep(2)
        if "Sorry, nobody on Reddit goes by that name" in text_translated(driver.execute_script("return document.documentElement.innerText")):
            return False
        else:
            return link
    except Exception as e:
        return f"Error: {e}"

def twitter_search(driver, username):
    try:
        link = f"https://twitter.com/{username}"
        driver.get(link)
        driver.implicitly_wait(10)
        time.sleep(2)
        if "This account doesn’t exist" in text_translated(driver.execute_script("return document.documentElement.innerText")):
            return False
        else:
            return link
    except Exception as e:
        return f"Error: {e}"

def main():
    try:
        clear()
        username = input("\nUsername: ")

        print("""
[01] -> Chrome (Linux)
[02] -> Chrome (Windows)
[03] -> Firefox (Windows)
[04] -> Edge (Windows)
        """)
        browser = input("Browser: ")

        if browser in ['1', '01']:
            if sys.platform.startswith("win"):
                only_windows()
            try:
                navigator = "Chrome Linux"
                print(f"Starting {navigator}..")
                chrome_driver_path = os.path.abspath("./Driver/chromedriverlinux")
                chrome_options = webdriver.ChromeOptions()
                chrome_options.add_argument(f"webdriver.chrome.driver={chrome_driver_path}")
                driver = webdriver.Chrome(options=chrome_options)
                print(f"{navigator} Ready!")
            except Exception as e:
                print(f"{navigator} not installed or driver not up to date.")
                continue_prompt()
                clear()
                
        elif browser in ['2', '02']:
            if sys.platform.startswith("linux"):
                only_linux()
            try:
                navigator = "Chrome"
                print(f"Starting {navigator}..")
                driver = webdriver.Chrome()
                print(f"{navigator} Ready!")
            except Exception as e:
                print(f"{navigator} not installed or driver not up to date.")
                continue_prompt()
                clear()

        elif browser in ['3', '03']:
            if sys.platform.startswith("linux"):
                only_linux()
            try:
                navigator = "Firefox"
                print(f"Starting {navigator}..")
                driver = webdriver.Firefox()
                print(f"{navigator} Ready!")
            except Exception as e:
                print(f"{navigator} not installed or driver not up to date.")
                continue_prompt()
                clear()

        elif browser in ['4', '04']:
            if sys.platform.startswith("linux"):
                only_linux()
            try:
                navigator = "Edge"
                print(f"Starting {navigator}..")
                driver = webdriver.Edge()
                print(f"{navigator} Ready!")
            except Exception as e:
                print(f"{navigator} not installed or driver not up to date.")
                continue_prompt()
                clear()
        else:
            error_choice()

        driver.set_window_size(900, 600)

        results = {
            "Tiktok": tiktok_search(driver, username),
            "Instagram": instagram_search(driver, username),
            "Snapchat": snapchat_search(driver, username),
            "Giters": giters_search(driver, username),
            "Github": github_search(driver, username),
            "Paypal": paypal_search(driver, username),
            "Telegram": telegram_search(driver, username),
            "Linktree": linktree_search(driver, username),
            "Roblox": roblox_search(driver, username),
            "Streamlabs": streamlabs_search(driver, username),
            "Pinterest": pinterest_search(driver, username),
            "Reddit": reddit_search(driver, username),
            "Twitter": twitter_search(driver, username)
        }

        print(f"""
The username "{username}" was found:

    Tiktok     : {results.get('Tiktok')}
    Instagram  : {results.get('Instagram')}
    Snapchat   : {results.get('Snapchat')}
    Giters     : {results.get('Giters')}
    Github     : {results.get('Github')}
    Paypal     : {results.get('Paypal')}
    Telegram   : {results.get('Telegram')}
    Linktree   : {results.get('Linktree')}
    Roblox     : {results.get('Roblox')}
    Streamlabs : {results.get('Streamlabs')}
    Pinterest  : {results.get('Pinterest')}
    Reddit     : {results.get('Reddit')}
    Twitter    : {results.get('Twitter')}
        """)

        driver.quit()

        continue_prompt()
    except Exception as e:
        error(e)

if __name__ == "__main__":
    main()
