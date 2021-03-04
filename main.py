import discord
from discord.ext import commands
import bot_debug_logger, random, time
from jojolib import jojoReactions
from pyfiglet import Figlet

def consodalized_token_and_run():
    token_file = open("bot_token.txt", "r")
    token_old = token_file.readline()
    bot_debug_logger.start_debuglog()
    bot.run(token_old)

bot = commands.Bot(command_prefix=commands.when_mentioned_or("loli "))

# this event prints console logged in status and
# changes rich presence of bot to 'watching trash code'
@bot.event
async def on_ready():
    print("logged in as {0.user}".format(bot))
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="çöp kod"))

# this is my futile attempt to get bot error-management
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Cannot found command. Try using `help` to (not) figure out commands!")
    if isinstance(error, commands.errors.MissingRequiredArgument):
        await ctx.send("*you forgot to pass an argument*\nhttps://tenor.com/view/jojo-fans-jojo-oh-you-watch-jojos-bizzare-adventure-too-kiss-couple-gif-16394548")


# heart-warming greeting function
@bot.command(name="helo")
async def helo_function(ctx):
    await ctx.channel.send("Loliler bunu kutsadı")

# ping! pong!
@bot.command()
async def ping(ctx):
    before = time.monotonic()
    ping_message = await ctx.channel.send("Pong! I'm here!")
    ping = (time.monotonic() - before) * 1000
    await ping_message.edit(content=f"Pong! `{int(ping)}ms`")

# amogus command
@bot.command(name="amogus")
async def amogus_function(ctx):
    amogus_file = open("amogus_reactions.txt", "r")
    amogus_lines = random.choice(list(amogus_file))
    await ctx.channel.send(amogus_lines)
    amogus_file.close()

# Gawr Gura function that is there for absolutely no apparent reason
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
        niceDickBro = ["https://media.discordapp.net/attachments/813152141567983676/814204377987285012/a8G91OQ_700bwp.png", "https://media.discordapp.net/attachments/813152141567983676/814205125170167808/nice_dick_bro_tomboy.jpg", "https://i.imgur.com/Cx3KeTk.jpg", "https://i.redd.it/uywhmuty8pk61.png"]
        await ctx.channel.send(obligoryBananaMessage + random.choice(niceDickBro))

# fucking ducking jojo function that consumed shit out of my time
@bot.command(name="jojo")
async def jojo(ctx, arg):
    try:
        reply_content = jojoReactions[str(arg)]
        await ctx.channel.send(reply_content)
    except KeyError:
        await ctx.channel.send("```Cannot found command or dev fucked up something```")

# This command allows users to use (not fully featured) figlet in Discord
@bot.command(name='figlet')
async def bot_figlet(ctx, *, arg):
    f = Figlet(font='big')
    figletizedMessage = f.renderText(arg)
    await ctx.channel.send(f"```{figletizedMessage}```")

consodalized_token_and_run()