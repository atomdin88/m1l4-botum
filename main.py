import discord
from discord.ext import commands


from fonksiyonlar import *



intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba {bot.user}! Ben bir botum!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)



@bot.command()                          #bota komut ekliyoruz.
async def para(ctx):  #ctx i unutma     #discordda botumuzu nasıl çağıracağız. ismini girin.
    await ctx.send(yazi_tura())         #çalıştırılacak fonksiyon parantez içine bak.



@bot.command()
async def sifre(ctx, sifre_uzunlugu = 15):
    await ctx.send(gen_pass(sifre_uzunlugu))

@bot.command()
async def emoji(ctx):
    await ctx.send(emoji_olusturucu())


bot.run("token yaz.")
