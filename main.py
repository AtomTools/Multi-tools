import os
import subprocess
from colorama import init, Fore, Style

import os
import subprocess
from colorama import init, Fore, Style


os.system('cls' if os.name == 'nt' else 'clear')

init(autoreset=True)

os.system('cls' if os.name == 'nt' else 'clear')

init(autoreset=True)

def display_ascii_art():
    art = f""" {Fore.RED}

                             ▄▄▄· ▄▄▄▄▄      • ▌ ▄ ·.     • ▌ ▄ ·. ▄• ▄▌▄▄▌  ▄▄▄▄▄▪      ▄▄▄▄▄            ▄▄▌  .▄▄ · 
                             █ ▀█ •██  ▪     ·██ ▐███▪    ·██ ▐███▪█▪██▌██•  •██  ██     •██  ▪     ▪     ██•  ▐█ ▀. 
                            ▄█▀▀█  ▐█.▪ ▄█▀▄ ▐█ ▌▐▌▐█·    ▐█ ▌▐▌▐█·█▌▐█▌██▪   ▐█.▪▐█·     ▐█.▪ ▄█▀▄  ▄█▀▄ ██▪  ▄▀▀▀█▄
                            ▐█ ▪▐▌ ▐█▌·▐█▌.▐▌██ ██▌▐█▌    ██ ██▌▐█▌▐█▄█▌▐█▌▐▌ ▐█▌·▐█▌     ▐█▌·▐█▌.▐▌▐█▌.▐▌▐█▌▐▌▐█▄▪▐█
                             ▀  ▀  ▀▀▀  ▀█▄▀▪▀▀  █▪▀▀▀    ▀▀  █▪▀▀▀ ▀▀▀ .▀▀▀  ▀▀▀ ▀▀▀     ▀▀▀  ▀█▄▀▪ ▀█▄▀▪.▀▀▀  ▀▀▀▀             
                         ╒═════════════════════════════════════════════════════════════════════════════════════════════════════╕                                              
                         │  1 - Account Nuker               │ 11 - Ip Information                  │ 21 - Number Scrapper      │                                           
                         │  2 - Badge Changer               │ 12 - Email Information               │ 22 - Website Scrapper     │                                                        
                         │  3 - Clear Dm                    │ 13 - Number Information              │ 23 - IBAN Generator       │                                       
                         │  4 - Group Spammer               │ 14 - Get your Ip                     │ 24 - CC Generator         │                                      
                         │  5 - Server Info                 │ 15 - Roblox Id Information           │ 25 - Obfuscator           │                                       
                         │  6 - Status Rotator              │ 16 - Token Information               │ 26 - Token Generator      │      
                         │  7 - Token Checker               │ 17 - Roblox User Inforamtion         │ 27 - Dos Voice            │        
                         │  8 - Token Mass Dm               │ 18 - Username Tracker                │                           │     
                         │  9 - Webhook Info                │ 19 - Nitro Generator                 │                           │      
                         │  10 - Webhook Spammer            │ 20 - Tools Information               │                           │    
                         ╘═════════════════════════════════════════════════════════════════════════════════════════════════════╛
"""
    print(art)

def execute_script(script_name):
    script_path = os.path.join('utils', f'{script_name}')
    try:
        subprocess.run(['python', script_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error executing script '{script_name}': {e}")

def main():
    display_ascii_art()
    while True:
        choice = input(Fore.RED + "Choose an option:  " + Style.RESET_ALL)

        if choice == '1':
            execute_script('account_nuker.py')
        elif choice == '2':
            execute_script('badge_changer.py')
        elif choice == '3':
            execute_script('clear_dm.py')
        elif choice == '4':
            execute_script('groupe_spammer.py')
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
            execute_script('scrapper_number.py')
        elif choice == '22':
            execute_script('website_scraper.py')
        elif choice == '23':
            execute_script('iban_scrapper.py')
        elif choice == '24':
            execute_script('credit_card_scrapper.py')
        elif choice == '25':
            execute_script('obfuscator.py')
        elif choice == '26':
            execute_script('token_generator.py')
        elif choice == '27':
            execute_script('dos_voice.py')
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
