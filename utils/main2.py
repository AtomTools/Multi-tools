import sys
import os
import time

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.theme import set_theme, get_current_theme, themes

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

                            Developers : red.(redwxll) x blue.(escopeta4020)
                            ────────────────────────────────────────────────────────────────────────────────────────── 
                            Version : 2.2
                            ──────────────────────────────────────────────────────────────────────────────────────────
                            {current_theme["primary"]}31{current_theme["reset"]} Ddos Ip                    {current_theme["primary"]}Prev{current_theme["reset"]} Previous Page
                            {current_theme["primary"]}32{current_theme["reset"]} Dos Voice                  {current_theme["primary"]}Exit{current_theme["reset"]} Exit Tool
                            {current_theme["primary"]}33{current_theme["reset"]} Proxy Scrappe
                            {current_theme["primary"]}34{current_theme["reset"]} Ip Genetator
                            {current_theme["primary"]}35{current_theme["reset"]} Site Phising
                            {current_theme["primary"]}36{current_theme["reset"]} Roblox Cookie Information
                            {current_theme["primary"]}37{current_theme["reset"]} Search In DataBase
                            {current_theme["primary"]}38{current_theme["reset"]} Token Decrypt
                            {current_theme["primary"]}39{current_theme["reset"]} Discord Mass Report

{current_theme["reset"]}"""
    animated_text(art, delay=0)

def main():
    clear()
    display_ascii_art()

if __name__ == "__main__":
    main()