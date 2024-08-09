import webbrowser
from datetime import datetime
import json
import os
import sys
from pystyle import Colors

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.theme import set_theme, get_current_theme, themes

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_error(message):
    print(f"""{Colors.red}Error: {message}{Colors.reset}""")

def print_title(title):
    print(f"""{current_theme["primary"]}{title}{current_theme["reset"]}""")

def read_tool_info(file_path):
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except Exception as e:
        print_error(f"Error reading {file_path}: {e}")
        return {}

def display_tool_info(tool_info):
    try:
        clear_screen()
        current_theme = get_current_theme()
        print(f"""
{current_theme["primary"]}Name :{current_theme["reset"]} {current_theme["secondary"]}{tool_info.get('name', 'N/A')}{current_theme["reset"]}
{current_theme["primary"]}Coding :{current_theme["reset"]} {current_theme["secondary"]}{tool_info.get('code', 'N/A')}{current_theme["reset"]}
{current_theme["primary"]}Language :{current_theme["reset"]} {current_theme["secondary"]}{tool_info.get('language', 'N/A')}{current_theme["reset"]}
{current_theme["primary"]}Creator :{current_theme["reset"]} {current_theme["secondary"]}{tool_info.get('creator', 'N/A')}{current_theme["reset"]}
{current_theme["primary"]}Discord :{current_theme["reset"]} {current_theme["secondary"]}https://{tool_info.get('discord', 'N/A')}{current_theme["reset"]}
{current_theme["primary"]}GitHub :{current_theme["reset"]} {current_theme["secondary"]}https://{tool_info.get('github', 'N/A')}{current_theme["reset"]}""")

        input(f"""{current_theme["primary"]}\nPress Enter to return to the main menu...{current_theme["reset"]}""")
        clear_screen()
    except Exception as e:
        print_error(e)

def main():
    tools_file_path = os.path.join('utils', 'tools.json')
    tool_info = read_tool_info(tools_file_path)
    display_tool_info(tool_info)

if __name__ == "__main__":
    main()
