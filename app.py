import discord
import json
import random
import config
import requests
from discord.ext import commands

cclient = discord.Client()
client = commands.Bot(command_prefix=('/'))


@client.event
async def on_ready():
    print('ready as {0}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hi!')

    await client.process_commands(message)

@client.command(name='8ball',
                description="Answers a yes/no question.",
                brief="Answers from the beyond.",
                aliases=['eight_ball', 'eightball', '8-ball'],
                pass_context=True)
async def eightball(ctx, *arg):
    possible_responses = [
        'That is a resounding no',
        'It is not looking likely',
        'Too hard to tell',
        'It is quite possible',
        'Definitely',
    ]
    await ctx.send(' '.join(arg) + " " + random.choice(possible_responses))


@client.command(name='kd',
                description="Grabs Lifetime KD",
                brief="KD Grabber",
                aliases=['killdeath', 'kdr'],
                pass_context=True)
async def kdr(ctx, first:str, *, second:str):
    url = f'https://api.fortnitetracker.com/v1/profile/{first}/{second}/'
    kd = requests.get(url, headers = {'TRN-Api-Key' : config.trn}).json()
    if 'error' in kd:
        await ctx.send("Error")
    else:
        await ctx.send("Lifetime K/D: " + kd['lifeTimeStats'][11]['value'])


client.run(config.token)
