import discord
import asyncio
import os
from pystyle import Colors

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_token():
    clear_screen()
    token = input(f"{Colors.red}Enter your Discord token: {Colors.reset}")
    if not token:
        raise ValueError(f"{Colors.red}You must provide a token.{Colors.reset}")
    return token

intents = discord.Intents.all()
client = discord.Client(intents=intents, self_bot=True)

async def sleep(ms):
    await asyncio.sleep(ms / 1000)

async def main():
    channel_id = input(f"{Colors.red}Enter the voice channel ID: {Colors.reset}")
    channel = client.get_channel(int(channel_id))
    if not channel:
        print(f"{Colors.red}No channel found{Colors.reset}")
        await sleep(2000)
        await main()
        return

    i = 0
    regions = ["japan", "hongkong", "russia", "india", "brazil", "sydney", "rotterdam", "singapore"]
    
    while True:
        print(f"{Colors.red}Changing Channel Region...{Colors.reset}")
        try:
            await channel.edit(rtc_region=regions[i])
        except Exception as e:
            print(f"{Colors.red}Error: {e}{Colors.reset}")
        i = (i + 1) % len(regions)
        await asyncio.sleep(1)

@client.event
async def on_ready():
    await main()

if __name__ == "__main__":
    token = get_token()
    client.run(token, bot=False)
