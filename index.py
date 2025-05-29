
import json
import sys
import re
import time
import discord
import my_token
import rolls

from discord.ext import commands
from discord import app_commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', case_insensitive=True, intents=intents)

print("Duality is alive!")
print("Started at " + time.strftime("%m/%d/%y %H:%M:%S"))

@bot.command(name='spell', help="!spell <quoted spell name>")
async def spellquery2(ctx, *, query:str=''):    
    username = str(ctx.author.display_name)
    print(time.strftime("%m/%d/%y %H:%M:%S") + " " + username + " searche the spell " + query)

@bot.tree.command(name='spell', description='Search for a spell.')
@app_commands.describe(query = "The partial or complete name of the spell")
async def spellquery(interaction: discord.Interaction, query:str=''):    
    username = str(interaction.user.display_name)
    print(time.strftime("%m/%d/%y %H:%M:%S") + " " + username + " searche the spell " + query)

@bot.tree.command(name="roll", description='Roll traditional dice expressions.')
@app_commands.describe(diceexpression = "The dice expression, like 1d20+6", reason = "The reason for the roll")
async def roll(interaction: discord.Interaction, diceexpression: str, reason:str=''):
    username = str(interaction.user.display_name)
    print(time.strftime("%m/%d/%y %H:%M:%S") + " " + username + " rolled a dice expression " + diceexpression +  " for " + reason)    
    #await interaction.response.send_message(armdice.roll(username, diceexpression, reason))

@bot.command(name='roll', help="!roll <diceexpression> [reason] - Rolls a dice expression, like 3d6. Optional reason for the roll.")
async def roll2(ctx, diceexpression: str, reason:str=''):
    username = str(ctx.author.display_name)
    print(time.strftime("%m/%d/%y %H:%M:%S") + " " + username + " rolled a dice expression: " + diceexpression + " for " + reason)    
    #await ctx.send(armdice.roll(username, diceexpression, reason))

@bot.tree.command(name="dd", description='Roll a Duality Dice.')
@app_commands.describe(modifier = "The modifier of your dice, like a trait or an experience")
async def dd(interaction: discord.Interaction, modifier: int = 0):
    username = str(interaction.user.display_name)
    r = rolls.dd(username, modifier)
    print(time.strftime("%m/%d/%y %H:%M:%S") + " " + r)    
    await interaction.response.send_message(r)

@bot.command(name='dd', help="!dd [modifier] - Rolls a Duality Dice, like a trait or an experience")
async def dd2(ctx, modifier: int = 0):
    username = str(ctx.author.display_name)
    r = rolls.dd(username, modifier)
    print(time.strftime("%m/%d/%y %H:%M:%S") + " " + r)    
    await ctx.send(r)

@bot.event
async def on_command_error(ctx, error):
    await ctx.send("Invalid Command - type !help for more information")
    await ctx.send(str(error))

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    try:
        synced = await bot.tree.sync()
        print(f'Synced {len(synced)} command(s)')
    except Exception as e:
        print(e)
    await bot.change_presence(activity=discord.CustomActivity(name='Distilling Vis'))

bot.run(my_token.TOKEN)

