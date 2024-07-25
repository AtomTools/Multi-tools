def install_requirements():
    packages = [
        "whois",
        "discord.py==1.7.3",
        "emailrep",
        "requests",
        "phonenumbers",
        "pystyle",
        "holehe",
        "colorama"
    ]
    for package in packages:
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        except subprocess.CalledProcessError as e:
            print(f"Error installing package {package}: {e}")

import os
import sys
import time
import subprocess
from theme import set_theme, get_current_theme, themes
from pystyle import Colors, Colorate, Write


def animated_text(text, delay=0.05):
    for line in text.split('\n'):
        for char in line:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        sys.stdout.write('\n')
        sys.stdout.flush()
        time.sleep(delay)

def display_ascii_art():
    current_theme = get_current_theme()
    art = f"""{current_theme["primary"]}
 ▄▄▄· ▄▄▄▄▄      • ▌ ▄ ·.     • ▌ ▄ ·. ▄• ▄▌▄▄▌  ▄▄▄▄▄▪      ▄▄▄▄▄            ▄▄▌  .▄▄ · 
▐█ ▀█ •██  ▪     ·██ ▐███▪    ·██ ▐███▪█▪██▌██•  •██  ██     •██  ▪     ▪     ██•  ▐█ ▀. 
▄█▀▀█  ▐█.▪ ▄█▀▄ ▐█ ▌▐▌▐█·    ▐█ ▌▐▌▐█·█▌▐█▌██▪   ▐█.▪▐█·     ▐█.▪ ▄█▀▄  ▄█▀▄ ██▪  ▄▀▀▀█▄
▐█ ▪▐▌ ▐█▌·▐█▌.▐▌██ ██▌▐█▌    ██ ██▌▐█▌▐█▄█▌▐█▌▐▌ ▐█▌·▐█▌     ▐█▌·▐█▌.▐▌▐█▌.▐▌▐█▌▐▌▐█▄▪▐█
 ▀  ▀  ▀▀▀  ▀█▄▀▪▀▀  █▪▀▀▀    ▀▀  █▪▀▀▀ ▀▀▀ .▀▀▀  ▀▀▀ ▀▀▀     ▀▀▀  ▀█▄▀▪ ▀█▄▀▪.▀▀▀  ▀▀▀▀ 

Dev : Atom Tools
───────────────────── 
Version : 2.1
─────────────────────

{current_theme["reset"]}{current_theme["primary"]}1{current_theme["reset"]} Account Nuker               {current_theme["primary"]}11{current_theme["reset"]} Ip Information                  {current_theme["primary"]}21{current_theme["reset"]} Number Scrapper    
{current_theme["primary"]}2{current_theme["reset"]} Badge Changer               {current_theme["primary"]}12{current_theme["reset"]} Email Information               {current_theme["primary"]}22{current_theme["reset"]} Website Scrapper    
{current_theme["primary"]}3{current_theme["reset"]} Clear Dm                    {current_theme["primary"]}13{current_theme["reset"]} Number Information              {current_theme["primary"]}23{current_theme["reset"]} IBAN Generator      
{current_theme["primary"]}4{current_theme["reset"]} Group Spammer               {current_theme["primary"]}14{current_theme["reset"]} Get your Ip                     {current_theme["primary"]}24{current_theme["reset"]} CC Generator        
{current_theme["primary"]}5{current_theme["reset"]} Server Info                 {current_theme["primary"]}15{current_theme["reset"]} Roblox Id Information           {current_theme["primary"]}25{current_theme["reset"]} Obfuscator          
{current_theme["primary"]}6{current_theme["reset"]} Status Rotator              {current_theme["primary"]}16{current_theme["reset"]} Token Information               {current_theme["primary"]}26{current_theme["reset"]} Token Generator     
{current_theme["primary"]}7{current_theme["reset"]} Token Checker               {current_theme["primary"]}17{current_theme["reset"]} Roblox User Information         {current_theme["primary"]}27{current_theme["reset"]} Dos Voice           
{current_theme["primary"]}8{current_theme["reset"]} Token Mass Dm               {current_theme["primary"]}18{current_theme["reset"]} Username Tracker                {current_theme["primary"]}28{current_theme["reset"]} Theme Changer                           
{current_theme["primary"]}9{current_theme["reset"]} Webhook Info                {current_theme["primary"]}19{current_theme["reset"]} Nitro Generator                                          
{current_theme["primary"]}10{current_theme["reset"]} Webhook Spammer            {current_theme["primary"]}20{current_theme["reset"]} Tools Information                                        

{current_theme["reset"]}"""
    animated_text(art, delay=0.01)

def execute_script(script_name):
    script_path = os.path.join('utils', f'{script_name}')
    try:
        subprocess.run(['python', script_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"{get_current_theme()['primary']}Error executing script '{script_name}': {e}{get_current_theme()['reset']}")

def main():
    install_requirements()
    os.system('cls' if os.name == 'nt' else 'clear')

    current_theme = get_current_theme()

    warning_message = f"""
{current_theme["primary"]}
      ____               
     /___/\_     WARNING: The use of these tools can have significant
    _\   \/_/\__  risks and consequences. By using this software, you
  __\       \/_/\  agree that we are not responsible for any damage or
  \   __    __ \ \  issues that may arise from the use of these tools.
 __\  \_\   \_\ \ \   __  Please use responsibly and at your own risk.
/_/\\   __   __  \ \_/_/\          
\_\/_\__\/\__\/\__\/_\_\/          
   \_\/_/\       /_\_\/
      \_\/       \_\/
{current_theme["reset"]}
    """

    animated_text(warning_message, delay=0.01)

    input("\nPress Enter to continue...")

    os.system('cls' if os.name == 'nt' else 'clear')

    display_ascii_art()
    
    while True:
        current_theme = get_current_theme()
        prompt = f"""
{current_theme["primary"]}╭─── {current_theme["secondary"]}atom@user/Multi tools{current_theme["reset"]}
{current_theme["primary"]}│
{current_theme["primary"]}│
{current_theme["primary"]}╰─$ {current_theme["reset"]} """
        
        choice = input(prompt).strip()
        
        if choice == '1':
            execute_script('account_nuker.py')
        elif choice == '2':
            execute_script('badge_changer.py')
        elif choice == '3':
            execute_script('clear_dm.py')
        elif choice == '4':
            execute_script('group_spammer.py')
        elif choice == '5':
            execute_script('server_info.py')
        elif choice == '6':
            execute_script('status_rotator.py')
        elif choice == '7':
            execute_script('token_checker.py')
        elif choice == '8':
            execute_script('token_massdm.py')
        elif choice == '9':
            execute_script('webhook_info.py')
        elif choice == '10':
            execute_script('webhook_spammer.py')
        elif choice == '11':
            execute_script('ip_info.py')
        elif choice == '12':
            execute_script('email_info.py')
        elif choice == '13':
            execute_script('number_info.py')
        elif choice == '14':
            execute_script('get_ip.py')
        elif choice == '15':
            execute_script('roblox_id_info.py')
        elif choice == '16':
            execute_script('token_info.py')
        elif choice == '17':
            execute_script('roblox_user_info.py')
        elif choice == '18':
            execute_script('username_tracker.py')
        elif choice == '19':
            execute_script('nitro_generator.py')
        elif choice == '20':
            execute_script('tools_info.py')
        elif choice == '21':
            execute_script('number_scraper.py')
        elif choice == '22':
            execute_script('website_scraper.py')
        elif choice == '23':
            execute_script('iban_generator.py')
        elif choice == '24':
            execute_script('credit_card_scrapper.py')
        elif choice == '25':
            execute_script('obfuscator.py')
        elif choice == '26':
            execute_script('token_generator.py')
        elif choice == '27':
            execute_script('dos_voice.py')
        elif choice == '28':
            print("\nAvailable themes:")
            for i, theme_name in enumerate(themes.keys(), 1):
                print(f"{i}. {theme_name}")
            theme_choice = input("Choose a theme by number: ").strip()
            theme_names = list(themes.keys())
            try:
                theme_index = int(theme_choice) - 1
                if 0 <= theme_index < len(theme_names):
                    set_theme(theme_names[theme_index])
                    os.system('cls' if os.name == 'nt' else 'clear')
                    display_ascii_art() 
                else:
                    print(f"{get_current_theme()['primary']}Invalid choice. No theme changed.{get_current_theme()['reset']}")
            except ValueError:
                print(f"{get_current_theme()['primary']}Invalid input. Please enter a number.{get_current_theme()['reset']}")

if __name__ == "__main__":
    main()
