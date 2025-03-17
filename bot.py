import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
load_dotenv()

print("Lancement du bot...")
bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
  print("Bot connecté")

  try:
    synced = await bot.tree.sync()
    print(f"Commandes synchronisées: {len(synced)}")
  except Exception as e:
    print(f"Erreur lors de la synchronisation des commandes: {e}")

@bot.event
async def on_message(message: discord.Message):
  if message.author.bot:
    return

  if message.content.lower() == 'bonjour':
    channel = message.channel
    author = message.author
    await author.send("Bonjour !")
  if message.content.lower() == 'bienvenue':
    welcome_channel = bot.get_channel(1351214503123226726)
    await welcome_channel.send("Salut !")

@bot.tree.command(name="embed", description="test embed")
async def embed(interaction: discord.Interaction):
  embed = discord.Embed(
    title="Test", 
    description="Ceci est un test", 
    color=discord.Color.blue()
  )
  embed.add_field(name="Field 1", value="Value 1")
  embed.add_field(name="Field 2", value="Value 2")
  embed.set_footer(text="Footer")

  await interaction.response.send_message(embed=embed)

@bot.tree.command(name="warn", description="avertir un utilisateur")
async def warn(interaction: discord.Interaction, member: discord.Member):
  await interaction.response.send_message(f"{member.mention} a été averti !")
  await member.send("tu as été averti !")

@bot.tree.command(name="ban", description="ban un utilisateur")
async def ban(interaction: discord.Interaction, member: discord.Member):
  await interaction.response.send_message(f"{member.mention} a été ban !")
  await member.ban(reason="Tu as été ban car ...")
  await member.send("tu as été ban !")

@bot.tree.command(name="test", description="Commande de test")
async def test(interaction: discord.Interaction):
  await interaction.response.send_message("Test réussi")

bot.run(os.getenv("DISCORD_TOKEN"))