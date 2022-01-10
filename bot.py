import datetime
import os
from random import randint
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv(".env")
CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
TOKEN = os.getenv('TOKEN')
GUILD = os.getenv('GUILD')

bot = commands.Bot(command_prefix='-')


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')


@bot.command(name='fyl', help='Bing Bong!')
async def on_message(ctx):
    await ctx.send('bing bong!')


@bot.command(name='anime', help='returns an anime streaming websites')
async def on_message(ctx):
    gogo_anime_url = 'https://www3.gogoanime.cm/'
    crunchy_roll_url = 'https://www.crunchyroll.com/en-gb'

    embed = discord.Embed(title='Anime Streaming Links', description='For the weebs', color=0x00ff00)
    embed.add_field(name='Crunchy Roll', value=crunchy_roll_url , inline=False)
    embed.add_field(name='GoGo Anime', value=gogo_anime_url, inline=False)
    embed.set_image(url='https://media.giphy.com/media/Q66ZEIpjEQddUOOKGW/giphy.gif')

    response_embed = embed

    await ctx.send(embed=response_embed)


@bot.command(name='watch', help='returns streaming websites')
async def on_message(ctx):
    daily_dose_of_internet = 'https://www.youtube.com/c/DailyDoseOfInternet/videos'
    ordinary_sausage = 'https://www.youtube.com/c/OrdinarySausage/videos'
    gogo_anime_url = 'https://www3.gogoanime.cm/'
    crunchy_roll_url = 'https://www.crunchyroll.com/en-gb'

    gifs = ['https://media.giphy.com/media/WoUynUguj7wEP7HN0T/giphy.gif',
            'https://media.giphy.com/media/S9i8jJxTvAKVHVMvvW/giphy.gif',
            'https://media.giphy.com/media/UCTaYoiR7pD2okgFK1/giphy.gif',
            'https://media.giphy.com/media/l0amJzVHIAfl7jMDos/giphy.gif',
            'https://media.giphy.com/media/qLkRR7Y5QRzL532sQx/giphy.gif',
            'https://media.giphy.com/media/DhstvI3zZ598Nb1rFf/giphy.gif',
            'https://media.giphy.com/media/l7fdqmHQ1jCg2HzQlx/giphy.gif']

    embed = discord.Embed(title='Useful Links!', description='list of watch links!', color=0x00ff00)
    embed.add_field(name='Crunchy Roll', value=crunchy_roll_url , inline=False)
    embed.add_field(name='GoGo Anime', value=gogo_anime_url, inline=False)
    embed.add_field(name='Daily Dose of Internet', value=daily_dose_of_internet, inline=False)
    embed.add_field(name='Ordinary Sausage', value=ordinary_sausage, inline=False)
    embed.set_image(url=gifs[randint(0, len(gifs) - 1)])

    response_embed = embed

    await ctx.send(embed=response_embed)


@bot.command(name='embed', help='embed objec')
async def on_message(ctx):
    embed = discord.Embed(title='Test Title', description='test embed', color=0x00ff00)
    embed.add_field(name='testField', value='this is a tedst value', inline=False)
    await ctx.send(embed=embed)


bot.run(TOKEN)