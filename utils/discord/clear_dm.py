import os
import discord
from discord.ext import commands

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    pass

def error_message(message):
    print(f"\033[91m{message}\033[0m")

clear()


token = input("Your Account Token: ").strip()
print("Write \"!clear\" in one of your DMs to delete your messages")

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", self_bot=True, intents=intents)
bot.remove_command("help")

@bot.command()
async def clear(ctx, limit: int=None):
    """Command to clear messages from a DM channel."""
    if not limit or limit <= 0:
        limit = 100 
    passed = 0
    failed = 0

    async for msg in ctx.message.channel.history(limit=limit):
        if msg.author.id == bot.user.id:
            try:
                await msg.delete()
                passed += 1
            except Exception as e:
                failed += 1
                error_message(f"Failed to delete message: {e}")

    print(f"\nRemoved {passed} messages with {failed} fails")
    input("\nPress ENTER to exit")
    main()

try:
    bot.run(token, bot=False)
except discord.LoginFailure:
    error_message("Invalid token provided. Please check your token and try again.")
except Exception as e:
    error_message(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
