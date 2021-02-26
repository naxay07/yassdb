import discord
from discord.ext import commands
import bot_debug_logger, random
from jojolib import jojoReactions

def consodalized_token_and_run():
    token_file = open("bot_token.txt", "r")
    token_old = token_file.readline()
    bot_debug_logger.start_debuglog()
    bot.run(token_old)

bot = commands.Bot(command_prefix="loli ")

@bot.event
async def on_ready():
    print("logged in as {0.user}".format(bot))
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="çöp kod"))

# heart-warming greeting function
@bot.command(name="helo")
async def helo_function(ctx):
    await ctx.channel.send("Loliler bunu kutsadı")

# ping! pong!
@bot.command(name="ping")
async def ping_function(ctx):
    await ctx.channel.send("Pong! I'm here!")

# amogus command
@bot.command(name="amogus")
async def amogus_function(ctx):
    amogus_file = open("amogus_reactions.txt", "r")
    amogus_lines = random.choice(list(amogus_file))
    await ctx.channel.send(amogus_lines)
    amogus_file.close()

# Gawr Gura funtion that is there for absolutely no apparent reason
@bot.command(name="a")
async def GawrGura_function(ctx):
    GawrGura_file = open("GawrGura_images.txt", "r")
    GawrGura_lines = random.choice(list(GawrGura_file))
    await ctx.channel.send('Gawr Gura\n' + GawrGura_lines)
    GawrGura_file.close()

# where banana
@bot.command(name="banana")
async def banana(ctx):
    bananaSizeRandom = random.randint(0, 55)
    obligoryBananaMessage = "Your gel banana is, " + str(bananaSizeRandom) + " burger king to mcdonalds\n"
    if bananaSizeRandom <= 10:
        await ctx.channel.send(obligoryBananaMessage + "https://media.discordapp.net/attachments/813152141567983676/814203998545379398/9e4.png")
    else:
        niceDickBro = ["https://media.discordapp.net/attachments/813152141567983676/814204377987285012/a8G91OQ_700bwp.png", "https://media.discordapp.net/attachments/813152141567983676/814205125170167808/nice_dick_bro_tomboy.jpg"]
        await ctx.channel.send(obligoryBananaMessage + random.choice(niceDickBro))

@bot.command(name="jojo")
async def jojo(ctx, arg):
    try:
        reply_content = jojoReactions[str(arg)]
        await ctx.channel.send(reply_content)
    except KeyError:
        await ctx.channel.send("```Cannot found command or dev fucked up something```")

consodalized_token_and_run()