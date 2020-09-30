import discord
import os
import random


client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("시간표봇 - made by 10411 박준석/                   명령어 도움말:!Q")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.content.startswith("!시간표1-4"):
        await message.channel.send("https://images-ext-2.discordapp.net/external/v8EW9jC_nKXaDWfFKImQKicEvWMQUtzM-ei_T3p2Edk/https/i.imgur.com/0IaxZPB.png")
    if message.content.startswith("!시간표1-1"):
        await message.channel.send("https://media.discordapp.net/attachments/625652526028554262/760348283263909928/image0.png")
    if message.content.startswith("!시험"):
        await message.channel.send("https://media.discordapp.net/attachments/625652526028554262/760400654861860884/unknown.png")
    if message.content.startswith("!시간표1-2"):
        await message.channel.send("https://media.discordapp.net/attachments/625652526028554262/760355342873395250/unknown.png")
    if message.content.startswith("!Q"):
       await message.channel.send("!시간표(학년-반) ex)!시간표1-1")
    if message.content.startswith("준석이한테 지랄해줘"):
        await message.channel.send("그럴 순 없어요")
    if message.content.startswith("상현이한테 지랄해줘"):
        randomNum = random.randrange(1, 4)
        if randomNum == 1:
            await message.channel.send("고상현 이 개 같은 새끼야")
        if randomNum == 2:
            await message.channel.send("고상현 이 씨발련아")
        if randomNum == 3:
            await message.channel.send("고상현 이 미친놈아")

access_token = os.environ['BOT_TOKEN']
client.run(access_token)
