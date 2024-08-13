import discord
from discord import app_commands
from discord.ext import commands

bot = commands.Bot(command_prefix="/", intents = discord.Intents.all())

@bot.event
async def on_ready():
    print("Bot está pronto para uso!")
    try:
        synced = await bot.tree.sync()
        print(f"Synced{len(synced)} commands(s)")
    except Exception as e:
        print(e) 
       
@bot.tree.command(name="ola")   
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message(f"hey{interaction.user.mention}! Comando slash requisitado pelo discord!", epheremal=True)
           
@bot.tree.command(name="say")
@app_commands.describe(thing_to_say= "O que quer que eu fale?")  
async def say(interaction: discord.Interaction, thing_to_say: str):
    await interaction.response.send_message(f"{interaction.user.name} said: '{thing_to_say}'")
    
bot.run('SEU TOKEN AQUI')

