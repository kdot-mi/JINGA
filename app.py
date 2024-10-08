import discord
from discord.ext import commands
import re
import os

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_message(message):
    # Don't process messages sent by the bot itself
    if message.author == bot.user:
        return

    # Check if the message contains a Twitter link
    twitter_link_pattern = r'https?://twitter\.com/(\S*)'
    x_link_pattern = r'https?://x\.com/(\S*)'
    if re.search(twitter_link_pattern, message.content) or re.search(x_link_pattern, message.content):
        # Replace 'twitter.com' or 'x.com' with 'vxtwitter.com'
        new_content = re.sub(twitter_link_pattern, r'https://vxtwitter.com/\1', message.content)
        new_content = re.sub(x_link_pattern, r'https://vxtwitter.com/\1', new_content)

        # Delete the original message
        await message.delete()

        # Send the new message
        await message.channel.send(f'**From:** {message.author.mention} {new_content}')

# Open the file and read the token
with open('JINGA\DISCORD_TOKEN.txt', 'r') as file:
    DISCORD_TOKEN = file.read().strip()

# Use the token
bot.run(DISCORD_TOKEN)