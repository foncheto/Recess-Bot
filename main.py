import discord
from discord.ext import commands
import json

# Load the Discord API key from credentials.json
with open("credentials.json") as file:
    credentials = json.load(file)
    TOKEN = credentials["discord_api"]

from music_cog import music_cog
from help_cog import help_cog
from gpt_cog import gpt_cog
from image_cog import image_cog

intent = discord.Intents.all()

bot = commands.Bot(command_prefix="#", intents=intent)

bot.remove_command("help")


@bot.event
async def on_ready():
    await bot.add_cog(help_cog(bot))
    print("\nHelp cog loaded succesfully")
    await bot.add_cog(music_cog(bot))
    print("Music cog loaded succesfully")
    await bot.add_cog(gpt_cog(bot))
    print("GPT cog loaded succesfully")
    await bot.add_cog(image_cog(bot))
    print("Image cog loaded succesfully")
    await bot.change_presence(
        activity=discord.Game(name="Dale tu corte chuchetumare!!!")
    )
    print("------------------")
    print("Logged in as:")
    print(f"{bot.user.name} - Bot")
    print("Dale tu corte chuchetumare!!!")
    print("------------------")


bot.run(TOKEN)
