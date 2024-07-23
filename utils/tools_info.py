import webbrowser
from datetime import datetime
import json


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
    print(f"""
Name : {tool_info.get('name_tool', 'N/A')}
Version : {tool_info.get('version', 'N/A')}
Coding : {tool_info.get('code', 'N/A')}
Language : {tool_info.get('language', 'N/A')}
Author : {tool_info.get('author', 'N/A')}
Platform : {tool_info.get('platform', 'N/A')}
Discord : https://{tool_info.get('discord', 'N/A')}
GitHub : https://{tool_info.get('github', 'N/A')}""")

    input("\nPress Enter to return to the main menu...")

except Exception as e:
    ErrorModule(e)

if __name__ == "__main__":
    main()
