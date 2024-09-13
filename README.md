# JINGA Discord Bot

This is a Discord bot that automatically replaces Twitter and X links with vxtwitter links.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/kdot-mi/JINGA.git
    cd JINGA
    ```

2. Install the required packages:
    ```bash
    pip install discord
    ```

4. Create a file named `DISCORD_TOKEN.txt` in the `JINGA` directory and add your Discord bot token to this file.
   ```bash
   echo "YOUR_DISCORD_BOT_TOKEN" > JINGA/DISCORD_TOKEN.txt
   ```
   Visit the <a href='https://discord.com/developers/docs/reference'>**Discord Developer Portal**</a> for you Discord Bot Token.

## Usage

1. Run the bot:
    ```bash
    python app.py
    ```

## app.py

```python
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
```

## Features
- Automatically detects and replaces Twitter and X links with vxtwitter links.
- Deletes the original message containing the Twitter or X link.
- Sends a new message with the modified link.

## Requirements
- Python 3.8 or higher
- discord.py library

