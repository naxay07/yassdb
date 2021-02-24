import discord
from discord.ext import commands
import bot_debug_logger, random
from jojolib import jojoReactions
from GawrGura_module import GawrGuraImages
bot = commands.Bot('.')

def consodalized_token_and_run():
    token_file = open("bot_token.txt", "r")
    token_old = token_file.readline()
    client.run(token_old)
    bot_debug_logger.start_debuglog()

prefix = "loli "
client = discord.Client()

@client.event
async def on_ready():
    print("logged in as {0.user}".format(client))
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="çöp kod"))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(prefix + "helo"):
        await message.channel.send('Loliler bunu kutsadı')

    # Jojo function:
    if message.content.startswith(prefix + "jojo"):
        m_content = message.content
        reply_content = jojoReactions.get(str(m_content))
        await message.channel.send(reply_content)

    # Gawr Gura function:
    if message.content.startswith(prefix + "a"):
        await message.channel.send('Gawr Gura\n' + random.choice(GawrGuraImages))

# You need to make a jojo library and then find a way to access stuff in it
# @client.event
# async def on_message(message):
#    if message.author == client.user:
#        print("congratulations, you have somehow got this code working")
#        return
#
#    if message.content.startswith(prefix + "jojo"):
#        m_content = message.content
#        reply_content = jojoReactions.get(str(m_content))
#        await message.channel.send(reply_content)


consodalized_token_and_run()