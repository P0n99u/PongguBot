import discord
import ScrapEventBroad
import os

TOKEN= os.environ["BOT_TOKEN"]

client = discord.Client()
    
@client.event
async def on_ready():
    a=discord.Game("!help |금요일 10시 요정 ")
    await client.change_presence(status=discord.Status.online,activity=a)
    print(client.user.name)
    print(client.user.id)

@client.event
async def on_message(message):
    if message.author == client.user:
        return None
    if message.content.startswith("!help"):
        await message.channel.send("!금요일")
    if message.content.startswith("!금요일"):
        s=ScrapEventBroad.GetSundayInfo()
        await message.channel.send(s)
    if message.content.startswith("!로또"):
       s=Lotto.Get_Lotto()
       await message.channel.send(s)
client.run(TOKEN)
