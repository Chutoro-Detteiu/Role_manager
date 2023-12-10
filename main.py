#Role Manager Ver.1.1α
version = '1.1α'

import discord 
import argparse
from discord import app_commands
from discord.ext import commands
import traceback


TOKEN_dev  = 'hogehoge1234567890'
TOKEN_prod = 'hogehoge1234567890'

Intents = discord.Intents.default()
Intents.members = True
client = discord.Client(activity=discord.Game('Ver.'+version),intents=Intents)
tree   = app_commands.CommandTree(client)


parser = argparse.ArgumentParser()
parser.add_argument('-p','--production',  action='store_true', default=False , help='Use when running in PRODUCTION ENVIRONMENT')
args   = parser.parse_args()

if args.production:
    TOKEN    = TOKEN_prod
else:
    TOKEN    = TOKEN_dev


print('Please wait, now launching...')

@client.event
async def on_ready():
    await tree.sync()
    print('Role Management System Ver.' + version)
    print('When you want to operate me, type the command in the Discord message...')

@tree.command(name="add",description="ロール付与")
@commands.has_permissions(administrator=True)
async def add(interaction: discord.Interaction, name:discord.Member, role:discord.Role):
    try:
        await name.add_roles(role)
        await interaction.response.send_message("Done")
    except:
        await interaction.response.send_message(traceback.format_exc())


@tree.command(name="remove",description="ロール削除")
@commands.has_permissions(administrator=True)
async def remove(interaction: discord.Interaction, name:discord.Member, role:discord.Role):
    try:
        await name.remove_roles(role)
        await interaction.response.send_message("Done")
    except:
        await interaction.response.send_message(traceback.format_exc())

client.run(TOKEN)
