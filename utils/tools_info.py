import webbrowser
from datetime import datetime
import json
import os
from pystyle import Colors

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_error(message):
    print(f"{Colors.red}Error: {message}{Colors.reset}")

def print_title(title):
    print(f"{Colors.red}{title}{Colors.reset}")

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
        print(f"""
{Colors.red}Name : {tool_info.get('name', 'N/A')}
Coding : {tool_info.get('code', 'N/A')}
Language : {tool_info.get('language', 'N/A')}
Creator : {tool_info.get('creator', 'N/A')}
Discord : https://{tool_info.get('discord', 'N/A')}
GitHub : https://{tool_info.get('github', 'N/A')}{Colors.reset}""")

        input(f"{Colors.red}\nPress Enter to return to the main menu...{Colors.reset}")
        clear_screen()
    except Exception as e:
        print_error(e)

def main():
    tools_file_path = os.path.join('utils', 'tools.json')
    tool_info = read_tool_info(tools_file_path)
    display_tool_info(tool_info)

if __name__ == "__main__":
    main()
