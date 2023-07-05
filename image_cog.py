import discord
from discord.ext import commands
import json
import openai

with open("credentials.json") as file:
    credentials = json.load(file)
    TOKEN = credentials["openai_api"]

openai.api_key = TOKEN


class image_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="image", help="Generates a realistic image from a prompt.")
    async def generate_image(self, ctx, *args):
        query = " ".join(args)
        response = openai.Image.create(
            prompt=f"Generate a realistic image of {query}", n=1, size="1024x1024"
        )
        await ctx.send(response["data"][0]["url"])
