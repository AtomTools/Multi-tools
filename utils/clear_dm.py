import os
import discord
from discord.ext import commands
from pystyle import Colors

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def cleardmtitle():
    print(f"{Colors.red}Clear DM Tool{Colors.reset}")

def setTitle(title):
    os.system(f"title {title}")

def main():
    pass

setTitle("Clear DM")
clear()
cleardmtitle()

token = input(f"{Colors.red}Your Account Token: {Colors.reset}")
print(f"{Colors.red}Write \"!clear\" in one of your DMs to delete your messages{Colors.reset}")

global bot
bot = commands.Bot(command_prefix="!", self_bot=True)
bot.remove_command("help")

@bot.command()
async def clear(ctx, limit: int=None):
    passed = 0
    failed = 0
    async for msg in ctx.message.channel.history(limit=limit):
        if msg.author.id == bot.user.id:
            try:
                await msg.delete()
                passed += 1
            except Exception as e:
                failed += 1
                print(f"{Colors.red}Failed to delete message: {e}{Colors.reset}")
    
    print(f"{Colors.red}\nRemoved {passed} messages with {failed} fails{Colors.reset}")
    input(f"{Colors.red}\nPress ENTER to exit{Colors.reset}")
    main()

bot.run(token, bot=False)

if __name__ == "__main__":
    main()
