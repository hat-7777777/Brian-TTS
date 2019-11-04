import discord, requests, random, os
from discord.ext import commands
from playsound import playsound

#NOTE PLAYSOUND MODULE DOES NOT WORK ON RASPBIAN. If you want to run this on a Raspberry Pi, you'll have to replace playsound. Use PyGame or pydub (from pydub import AudioSegment\n from pydub.playback import play)

client = commands.Bot(command_prefix="!brian")

@client.event
async def on_ready():
    print("Brian is now active")
    await client.change_presence(activity=discord.Game("!briantts <message>"))

@client.command()
async def tts(ctx, *, payload):
    await ctx.send(f'Playing message: "{payload}" :arrow_forward:')
    print(f"incoming message: {payload}")
    req = requests.get("https://api.streamelements.com/kappa/v2/speech?voice=Brian&text=" + str(payload))
    print("getting audio from", req.url)

    print("creating file")
    r1 = random.randint(1,1000000)
    randfile = str(r1)+".mp3"

    print(f"writing audio to {randfile}")
    with open(randfile, "wb") as my_file:
        my_file.write(req.content)

    print("playing audio")
    playsound(randfile)

    print(f"removing file {randfile}")
    os.remove(randfile)

client.run("NjQwNjkxMDY2NDgzNTA3MjAx.Xb9hjQ.Dhgzz_q0YA4oRo4wX4fidxgzF4Q")