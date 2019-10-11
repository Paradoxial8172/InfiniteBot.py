import discord
from discord.ext import commands, tasks
from itertools import cycle
import os
import datetime

bot = commands.Bot(command_prefix = '=') 
status = cycle(['with Discord API', '=help for list of commands', 'with fire...'])

@bot.event
async def on_ready():
    change_status.start()
    print('You are logged in as InfiniteBot.py')

bot.remove_command('help')

@tasks.loop(seconds=30)
async def change_status():
    await bot.change_presence(activity=discord.Game(next(status)))
#==================================================cogs
@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'cogs.{extension}')

@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')
#==================================================cogs
@bot.command()
async def ping(ctx):
    embed = discord.Embed(
    title = (f'Pong! {round(bot.latency * 1000)}ms.'),
    colour = discord.Colour.green()
    )
    await ctx.send(embed=embed)
#===================================================
@bot.event
async def on_message(message):
    if message.content.startswith('prefix'):
        channel = message.channel
        await channel.send('My prefix is "="')

    await bot.process_commands(message)

#=======================================================
bot.run('######################################')
