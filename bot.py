import os
from random import randint
import discord
from discord.ext import commands
from dotenv import load_dotenv
import requests

load_dotenv(".env")
CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
TOKEN = os.getenv('TOKEN')
GUILD = os.getenv('GUILD')

bot = commands.Bot(command_prefix='-', help_command=commands.DefaultHelpCommand(no_category='List of commands'))


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')


@bot.command(name='fyl', help='Bing Bong!')
async def on_message(ctx):
    await ctx.send('https://media.giphy.com/media/neAheaxUW7HuomL0On/giphy.gif')


@bot.command(name='reyna', help='Custom Reyna Message :)')
async def on_message(ctx):

    gifs = ['https://media.giphy.com/media/IzXiddo2twMmdmU8Lv/giphy.gif',
            'https://media.giphy.com/media/IzXiddo2twMmdmU8Lv/giphy.gif',
            'https://media.giphy.com/media/gjHkRHSuHqu99y9Yjt/giphy.gif',
            'https://media.giphy.com/media/KztT2c4u8mYYUiMKdJ/giphy.gif',
            'https://media.giphy.com/media/fSdPI1jp98tlg6xpZS/giphy.gif',
            'https://media.giphy.com/media/21Pi5sBUXvY62KrrHA/giphy.gif',
            'https://media.giphy.com/media/yvYEzDgh1s7XmXilw8/giphy.gif']

    embed = discord.Embed(title='Lidol Bean', description='<3', color=0x00ff00)
    embed.set_image(url=gifs[randint(0, len(gifs) - 1)])

    response_embed = embed

    await ctx.send(embed=response_embed)


@bot.command(name='anime', help='returns an anime streaming websites')
async def on_message(ctx):
    gogo_anime_url = 'https://www3.gogoanime.cm/'
    crunchy_roll_url = 'https://www.crunchyroll.com/en-gb'

    embed = discord.Embed(title='Anime Streaming Links', description='For the weebs', color=0x00ff00)
    embed.add_field(name='Crunchy Roll', value=crunchy_roll_url, inline=False)
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
    embed.add_field(name='Crunchy Roll', value=crunchy_roll_url, inline=False)
    embed.add_field(name='GoGo Anime', value=gogo_anime_url, inline=False)
    embed.add_field(name='Daily Dose of Internet', value=daily_dose_of_internet, inline=False)
    embed.add_field(name='Ordinary Sausage', value=ordinary_sausage, inline=False)
    embed.set_image(url=gifs[randint(0, len(gifs) - 1)])

    response_embed = embed

    await ctx.send(embed=response_embed)


@bot.command(name='song', help='returns a random song!')
async def on_message(ctx):
    base_spotify_url = 'https://open.spotify.com/track/'
    random_song_url = 'https://melody-find.herokuapp.com/mf/v1/song'
    res = requests.get(random_song_url)

    res = res.json()
    embed = discord.Embed(title='Random Song Generator', description='Returns a random song', color=0x00FFFF)

    embed.add_field(name='Song', value=res[0]['track']['name'], inline=False)
    embed.add_field(name='Spotify', value=base_spotify_url + res[0]['track']['id'], inline=False)
    embed.set_footer()

    for artist in res[0]['track']['artists']:
        print(artist['name'])
        embed.add_field(name='Artist', value=artist['name'], inline=False)

    await ctx.send(embed=embed)


bot.run(TOKEN)
