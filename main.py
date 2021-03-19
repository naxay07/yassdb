import discord
from discord.ext import commands
import bot_debug_logger, random, time, os
from jojolib import jojoReactions
from pyfiglet import Figlet
from dotenv import load_dotenv
import praw

load_dotenv()

def consodalized_token_and_run():
    discord_token = os.getenv('bot_token')
    bot_debug_logger.start_debuglog()
    bot.run(discord_token)

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
            await ctx.send("*you forgot to pass an argument*")


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
@bot.command(name="amogus", brief="random amogus shitpost", description="Random amogus shitposts and copypastas from \"database\".")
async def amogus_function(ctx):
    amogus_file = open("amogus_reactions.txt", "r")
    amogus_lines = random.choice(list(amogus_file))
    await ctx.channel.send(amogus_lines)
    amogus_file.close()

# Gawr Gura function that is there for absolutely no apparent reason
@bot.command(brief="Gawr Gura", description="Random Gawr Gura images", name="a")
async def GawrGura_function(ctx):
    # using a text file instead of 
    GawrGura_file = open("GawrGura_images.txt", "r")
    GawrGura_lines = random.choice(list(GawrGura_file))
    embed=discord.Embed(title="Gawr Gura", url="https://www.youtube.com/channel/UCoSrY_IQQVpmIRZ9Xf-y93g", description="Shark Vtuber!", color=0x5d81c7)
    embed.set_footer(text="bottom gear")
    embed.set_image(url=GawrGura_lines)
    await ctx.channel.send(embed=embed)
    # the command you see under this line deprecated in favor of embed aestetics
    # await ctx.channel.send('Gawr Gura\n' + GawrGura_lines)
    GawrGura_file.close()

# where banana
@bot.command(name="banana")
async def banana(ctx):
    bananaSizeRandom = random.randint(0, 55)
    obligoryBananaMessage = f"{ctx.message.author.mention}, your gel banana is {str(bananaSizeRandom)} burger king to mcdonalds\n"
    if bananaSizeRandom <= 10:
        await ctx.channel.send(obligoryBananaMessage + "https://media.discordapp.net/attachments/813152141567983676/814203998545379398/9e4.png")
    else:
        niceDickBro = ["https://media.discordapp.net/attachments/813152141567983676/814204377987285012/a8G91OQ_700bwp.png", "https://media.discordapp.net/attachments/813152141567983676/814205125170167808/nice_dick_bro_tomboy.jpg", "https://i.imgur.com/Cx3KeTk.jpg", "https://i.redd.it/uywhmuty8pk61.png"]
        await ctx.channel.send(obligoryBananaMessage + random.choice(niceDickBro))

# fucking ducking jojo function that consumed shit out of my time
@bot.command(name="jojo")
async def jojo(ctx, arg):
    try:
        reply_content = jojoReactions[arg]
        await ctx.channel.send(reply_content)
    except KeyError:
        await ctx.channel.send("```Cannot found command or dev fucked up something```")

# This command allows users to use (not fully featured) figlet in Discord
@bot.command(name='figlet')
async def bot_figlet(ctx, *, arg):
    # This loop cancels the command if it sees a weird character in the arg
    isViable = True
    for word in arg:
        for char in word:
            if ord(char) > 122:
                isViable = False
    
    if isViable:
        # run the pyfiglet and send output as message
        f = Figlet(font='big')
        figletizedMessage = f.renderText(" ".join(arg))
        await ctx.channel.send(f"```{figletizedMessage}```")
    else:
        await ctx.channel.send("Don't know that letter sir.")

@bot.command()
async def owo(ctx, *, arg):
    basa_gelecek = ["OwO ", "<3 ", "UwU ", "uwu ", "(つ°ヮ°)つ ", "ohayo! ", "(≧∇≦) "]
    sona_geleck = [" 0.0", " :3", " (◡ ‿ ◡ ✿)", " (灬╹ω╹灬)", " (≧◡≦)"]

    cevrilmis = ""
    for harf in arg:
        if harf.lower() in "lr":
            cevrilmis = cevrilmis + "w"
        else:
            cevrilmis = cevrilmis + harf
    cevrilmis = random.choice(basa_gelecek) + cevrilmis + random.choice(sona_geleck)
    await ctx.channel.send(cevrilmis)

# WIP/Reddit: Grabbing a random post from a specified subreddit and sending it as embed
@bot.command()
async def reddit(ctx):
# command name is a placeholder
    async with ctx.channel.typing():
        reddit = praw.Reddit(client_id=os.getenv('reddit_id'),
                             client_secret=os.getenv('reddit_secret'),
                             user_agent='legaln\'t lolibot discord bot by u/naxaypu')
        subreddit = reddit.subreddit("ProgrammerHumor")
        submission = subreddit.random()
        print('just before embed')
        embed = discord.Embed(title=f'{subreddit.title}', description=f'{submission.title}')
        print('embed initialization ok')
        embed.set_image(url=f'{submission.url}')
        embed.set_footer(text=f'Posted by u/{submission.author} on r/{subreddit.display_name}')
    await ctx.channel.send(embed= embed)

@bot.command()
async def wholesomeyuri(ctx):
    async with ctx.channel.typing():
        reddit = praw.Reddit(client_id=os.getenv('reddit_id'),
                             client_secret=os.getenv('reddit_secret'),
                             user_agent='legaln\'t lolibot discord bot by u/naxaypu')
        subreddit = reddit.subreddit('wholesomeyuri')
        for posts in subreddit.hot(limit=20):
            randomPostNumber = random.randint(0,20)
            for i,posts in enumerate()
        submission = subreddit
        print('wholesomeyuri just before embed')
        wholesomeyuri_embed = discord.Embed(title=f'{subreddit.title}', description=f'{submission.title}')
        # wholesomeyuri_embed.set_image(url=f'{submission.url}')
        # wholesomeyuri_embed.set_footer(text=f'Posted by u/{submission.author} on r/{subreddit.display_name}')
        print("embed initialization done")
    await ctx.channel.send(embed=wholesomeyuri_embed)

# TODO:
# I will add rich presence to the server client when I learn
# multithreading. Have nice day

consodalized_token_and_run()