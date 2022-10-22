import responses
import os
from random import randint
import discord
from dotenv import load_dotenv
from discord.ext import commands
import requests
import wavelink

load_dotenv(".env")
CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
TOKEN = os.getenv('TOKEN')
GUILD = os.getenv('GUILD')

intents = discord.Intents.default()
intents.message_content = True
# client = discord.Client(intents=intents)
client = commands.Bot(command_prefix="!", intents=intents)


class CustomPlayer(wavelink.Player):

    def __init__(self):
        super().__init__()
        self.queue = wavelink.Queue()


async def send_message(message, user_message, is_private):
    try:
        response = responses.handle_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)


def run_discord_bot():
    @client.event
    async def on_ready():
        client.loop.create_task(connect_nodes())
        print(f'{client.user.name} is ready!')

    async def connect_nodes():
        await client.wait_until_ready()
        await wavelink.NodePool.create_node(
            bot=client,
            host='127.0.0.1',
            port=2333,
            password='youshallnotpass'
        )

    @client.event
    async def on_wavelink_node_ready(node: wavelink.Node):
        print(f'Node: {node.identifier} is ready!')

    @client.event
    async def on_wavelink_track_end(player: CustomPlayer, track: wavelink.Track, reason):
        if not player.queue.is_empty:
            next_track = player.queue.get()
            await player.play(next_track)

            @client.command()
            async def connect(ctx):
                voice_client = ctx.voice_client
                try:
                    channel = ctx.author.voice.channel
                except AttributeError:
                    return await ctx.send('Join a voice channel')

                if not voice_client:
                    await ctx.author.voice.channel.connect(cls=CustomPlayer())
                else:
                    await ctx.send('The bot is already in a voice channel')

    @client.command()
    async def coin(ctx):
        if randint(1,2) == 1:
            return await ctx.message.channel.send('Heads')
        await ctx.message.channel.send('Tails')

    @client.command()
    async def roll(ctx):
        response = randint(1,6)
        await ctx.message.channel.send(response)

    @client.command()
    async def connect(ctx):
        voice_client = ctx.voice_client
        try:
            channel = ctx.author.voice.channel
        except AttributeError:
            return await ctx.send('Join a voice channel')

        if not voice_client:
            await ctx.author.voice.channel.connect(cls=CustomPlayer())
        else:
            await ctx.send('The bot is already in a voice channel')

    @client.command()
    async def disconnect(ctx):
        voice_client = ctx.voice_client

        if voice_client:
            await voice_client.disconnect()
        else:
            await ctx.send('The bot is not connected to a channel')

    @client.command()
    async def play(ctx, *, search: wavelink.YouTubeTrack):

        voice_client = ctx.voice_client

        if not voice_client:
            custom_player = CustomPlayer()
            voice_client: CustomPlayer = await ctx.author.voice.channel.connect(cls=custom_player)

        if voice_client.is_playing():

            voice_client.queue.put(item=search)

            await ctx.send(embed=discord.Embed(
                title=search.title,
                url=search.uri,
                description=f"Queued {search.title} in {voice_client.channel}"
            ))
        else:
            print(search)
            await voice_client.play(search)

            await ctx.send(embed=discord.Embed(
                title=voice_client.source.title,
                url=voice_client.source.uri,
                description=f"Playing {voice_client.source.title} in {voice_client.channel}"
            ))

    client.run(TOKEN)
