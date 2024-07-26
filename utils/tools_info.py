import webbrowser
from datetime import datetime
import json
import os

def clear_screen():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    pass

def ErrorModule(e):
    print(f"Error: {e}")

def Title(title):
    print(f"{title}")


try:
    with open('tools.json', 'r') as file:
        tool_info = json.load(file)
except Exception as e:
    ErrorModule(f"Error reading tools.json: {e}")
    tool_info = {}


try:
    clear_screen()
    print(f"""
Name : {tool_info.get('name', 'N/A')}
Coding : {tool_info.get('code', 'N/A')}
Language : {tool_info.get('language', 'N/A')}
Creator : {tool_info.get('creator', 'N/A')}
Discord : https://{tool_info.get('discord', 'N/A')}
GitHub : https://{tool_info.get('github', 'N/A')}""")

    input("\nPress Enter to return to the main menu...")
    clear_screen()

except Exception as e:
    ErrorModule(e)

if __name__ == "__main__":
    main()
