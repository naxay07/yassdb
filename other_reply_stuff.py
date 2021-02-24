import discord

def jojo_shocked():
    @client.event
    async def on_message(message):
        if message.author == client.user:
            print("bot author sent command: jojo shocked")
            return

        if message.content.startswith("loli jojo shocked"):
            await message.channel.send('https://media.discordapp.net/attachments/745707115569610845/813162309715230750/Screen_Shot_2021-02-22_at_00.36.16.png')