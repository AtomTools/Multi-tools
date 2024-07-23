import os
import os.path
import discord
from discord.ext import commands

def clear():
    pass

def cleardmtitle():
    pass

def setTitle(title):
    pass

def main():
    pass

setTitle("Clear DM")
clear()
cleardmtitle()


token = input(f" Your Account Token: ")
print(f"Write \"!clear\" in one of your DMs to delete your messages")

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
            except:
                failed += 1
    print(f"\nRemoved {passed} messages with {failed} fails")
    input(f"\nPress ENTER to exit")
    main()

bot.run(token, bot=False)

if __name__ == "__main__":
    main()
