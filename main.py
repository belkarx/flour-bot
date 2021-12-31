import os

import discord
from discord.utils import get
from discord.ext import commands
from mcstatus import MinecraftServer


TOKEN = os.getenv('DISCORD_BOT_TOKEN')

client = commands.Bot(command_prefix="$")

@client.event
async def on_ready():
    guild = client.guilds[0]

    global rice_channel
    global sexy_emoji
    rice_channel = get(guild.channels, name="rices").id
    sexy_emoji = get(client.emojis, name='100sexy')

    print(f"we have logged on as {client.user}")

@client.event
async def on_message(msg):
    if msg.author == client.user:
        return
    
    #adds sexy emoji reaction to all images in #rices
    if (msg.channel.id == rice_channel and msg.attachments):
        await msg.add_reaction(emoji=sexy_emoji)

    if msg.content.startswith("$"):
        cmd = msg.content
        if cmd.startswith("$status"):
            try:
                status = MinecraftServer.lookup(cmd[8:]).status()
                await msg.channel.send(f"The server has {status.players.online} players and replied in {status.latency} ms")
            except:
                await msg.channel.send("invalid address or argument. Usage: $status [mc server name[:port]]")

                    #changes command arg to leetspeak
        if msg.content.startswith("$leet"):
            await msg.channel.send(msg.content[5:].replace("A","4").replace("a","@").replace("B","8").replace("b","6").replace("C", "[").replace("E", "3").replace("g", "9").replace("I", "|").replace("J", "]").replace("O", "0").replace("T","7").replace("l", "1").replace("S", "$").replace("s", "5").replace("t", "+").replace("Z", "2"))

client.run(TOKEN)
