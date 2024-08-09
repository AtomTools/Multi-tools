import requests
import threading
import os
from pystyle import Colors

DEFAULT_REPORT_REASON = "Inappropriate content"

def clear():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def report_message(token, guild_id, channel_id, message_id, reason):
    """Send a single report request."""
    url = 'https://discord.com/api/v8/report'
    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US',
        'User-Agent': 'Discord/21295 CFNetwork/1128.0.1 Darwin/19.6.0',
        'Content-Type': 'application/json',
        'Authorization': f'Bot {token}' 
    }
    payload = {
        'channel_id': channel_id,
        'message_id': message_id,
        'guild_id': guild_id,
        'reason': reason
    }

    response = requests.post(url, json=payload, headers=headers)
    
    status = response.status_code
    response_message = response.json().get('message', 'Unknown error')

    if status == 201:
        print(f"Report successfully sent for message ID {message_id}!")
    elif status in (401, 403):
        print(f"Authorization Error: {response_message}")
    else:
        print(f"Error: {response_message} | Status Code: {status}")

def mass_report(token, guild_id, channel_id, message_id, reason):
    """Create multiple threads to send report requests."""
    for _ in range(500):
        threading.Thread(target=report_message, args=(token, guild_id, channel_id, message_id, reason)).start()

if __name__ == "__main__":
    clear()
    token = input(f"{Colors.red}Enter your Discord token: ")
    guild_id = input(f"{Colors.red}Enter the server ID: ")
    channel_id = input(f"{Colors.red}Enter the channel ID: ")
    message_id = input(f"{Colors.red}Enter the message ID: ")
    
    reason = input(f"{Colors.red}Enter the report reason (default: {DEFAULT_REPORT_REASON}): ").strip()
    if not reason:
        reason = DEFAULT_REPORT_REASON

    mass_report(token, guild_id, channel_id, message_id, reason)
