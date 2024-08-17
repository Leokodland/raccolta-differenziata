import discord
from discord.ext import commands
from rifiuti import waste
intents = discord.Intents.default()
intents.message_content = True
 
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Hai fatto l\'accesso come {bot.user}')
 
@bot.command()
async def riciclare(ctx):
    await ctx.send(f'La raccolta differenziata consiste nel suddividere i rifiuti domestici in base al tipo di rifiuto svolgendo una prima scrematura che permette poi di riciclare correttamente i materiali riciclabili (carta, vetro, plastica, acciaio e rifiuti organici).')
@bot.command()
async def scelta(ctx):
    await ctx.send(waste())
bot.run("token")
