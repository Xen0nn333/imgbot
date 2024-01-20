import discord
from discord.ext import commands
import os
import random
print(os.listdir('images'))

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def mem(ctx):
    with open('images/Trollface.png', 'rb') as f:
        picture = discord.File(f)
        
    await ctx.send(file=picture)

@bot.command()
async def mymem(ctx):
    with open('images/Mymem.jpg', 'rb') as f:
        picture = discord.File(f)
#Отправляет созданный мною мем
    await ctx.send(file=picture)

@bot.command()
async def randmem(ctx):
    img_name = random.choice(os.listdir('images'))
    with open(f'images/{img_name}', 'rb') as f:
        picture = discord.File(f)
 
    await ctx.send(file=picture)

bot.run("token")
