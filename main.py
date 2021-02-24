import discord
from discord.ext import commands
import bot_debug_logger, random
from jojolib import jojoReactions
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

    # Heart-warming greeting function
    if message.content.startswith(prefix + "helo"):
        await message.channel.send('Loliler bunu kutsadı')

    # Jojo function:
    if message.content.startswith(prefix + "jojo"):
        m_content = message.content
        reply_content = jojoReactions.get(str(m_content))
        await message.channel.send(reply_content)

    # Gawr Gura function:
    if message.content == prefix + "a":
        GawrGura_file = open("GawrGura_images.txt", "r")
        GawrGura_lines = random.choice(list(GawrGura_file))
        await message.channel.send('Gawr Gura\n' + GawrGura_lines)
        GawrGura_file.close()

    # banana function
    if message.content.startswith(prefix + "how long banana"):
        bananaSizeRandom = random.randint(0, 55)
        obligoryBananaMessage = "Your gel banana is, " + str(bananaSizeRandom) + " burger king to mcdonalds\n"
        if bananaSizeRandom <= 10:
            await message.channel.send(obligoryBananaMessage + "https://media.discordapp.net/attachments/813152141567983676/814203998545379398/9e4.png")
        else:
            niceDickBro = ["https://media.discordapp.net/attachments/813152141567983676/814204377987285012/a8G91OQ_700bwp.png", "https://media.discordapp.net/attachments/813152141567983676/814205125170167808/nice_dick_bro_tomboy.jpg"]
            await message.channel.send(obligoryBananaMessage + random.choice(niceDickBro))
    
    # amogus function
    if message.content.startswith(prefix + "amogus"):
        amogus_file = open("amogus_reactions.txt", "r")
        amogus_lines = random.choice(list(amogus_file))
        await message.channel.send(amogus_lines)
        amogus_file.close()

consodalized_token_and_run()