import discord
import json, random
from discord.ext.commands import Bot

cclient = discord.Client()
client = Bot(command_prefix=('/'))

@client.event
async def on_ready():
    print('ready as {0}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hi!')


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


client.run('NTc0OTgwNTIyNTAyMjU4NzAw.XNBSkg.J6z9RMuGsuAtWgnr0npyiisHPRY')
