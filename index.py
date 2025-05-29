import time
import discord
import my_token
import rolls
import cards

from discord.ext import commands
from discord import app_commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', case_insensitive=True, intents=intents)

print("Duality is alive!")
print("Started at " + time.strftime("%m/%d/%y %H:%M:%S"))

@bot.tree.command(name='card', description='Search for a domain card.')
@app_commands.describe(query = "The partial or complete name of the domain card")
async def cardquery(interaction: discord.Interaction, query:str=''):    
    username = str(interaction.user.display_name)
    print(time.strftime("%m/%d/%y %H:%M:%S") + " " + username + " searche the spell " + query)
    await interaction.response.send_message(cards.get_card_by_name(query))

@bot.tree.command(name="dd", description='Roll a Duality Dice.')
@app_commands.describe(modifier = "The modifier of your roll, like a trait or an experience")
async def dd(interaction: discord.Interaction, modifier: int = 0):
    username = str(interaction.user.display_name)
    r = rolls.dd(username, modifier)
    print(time.strftime("%m/%d/%y %H:%M:%S") + " " + r)    
    await interaction.response.send_message(r)

@bot.tree.command(name="rr", description='Roll a Reaction Roll.')
@app_commands.describe(modifier = "The modifier of your roll, like a trait or an experience")
async def rr(interaction: discord.Interaction, modifier: int = 0):
    username = str(interaction.user.display_name)
    r = rolls.rr(username, modifier)
    print(time.strftime("%m/%d/%y %H:%M:%S") + " " + r)    
    await interaction.response.send_message(r)

@bot.event
async def on_command_error(ctx, error):
    await ctx.send("Invalid Command")
    await ctx.send(str(error))

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    try:
        synced = await bot.tree.sync()
        print(f'Synced {len(synced)} command(s)')        
    except Exception as e:
        print(e)    
    await bot.change_presence(activity=discord.CustomActivity(name='Spotlighting'))

bot.run(my_token.TOKEN)

