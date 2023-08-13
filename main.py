#Role Manager for Discord Ver.1.0
version = 1.0

import discord 
import argparse
from discord import app_commands
from discord import commands
import traceback


TOKEN_dev  = 'hogehoge1234567890'
TOKEN_prod = 'hogehoge1234567890'

guildid_dev  = 1234567890
guildid_prod = 1234567890

Intents = discord.Intents.default()
Intents.members = True
client  = discord.Client(activity='Ver.'+str(version),intents=discord.Intents.all())
tree    = app_commands.CommandTree(client)

parser = argparse.ArgumentParser()
parser.add_argument('-p','--production',  action='store_true', default=False , help='Use when running in PRODUCTION ENVIRONMENT')
args   = parser.parse_args()

if args.production:
    TOKEN    = TOKEN_prod
    guild_id = guildid_prod
else:
    TOKEN    = TOKEN_dev
    guild_id = guildid_dev
    

print('Please wait, now launching...')

@client.event
async def on_ready():
    await tree.sync()
    print('Role Management System for MRR Ver.1.0')
    print('When you want to operate me, type the command in the Discord message...')


@tree.command(name="add",description="ロール付与")
@commands.has_permmisons(administrator=True)
async def add(interaction: discord.Interaction, name:str, role:str):
    try:
        guild     = client.get_guild(guild_id)
        memberid  = int(name.replace('<@', '').replace('>',''))
        roleid    = int(role.replace('<@&', '').replace('>',''))
        print(name,memberid,role,roleid)
        role_data = guild.get_role(roleid)
        member    = guild.get_member(memberid)
        await member.add_roles(role_data)
        await interaction.response.send_message("Done")
    except:
        await interaction.response.send_message(traceback.format_exc())


@tree.command(name="remove",description="ロール削除")
@commands.has_permmisons(administrator=True)
async def remove(interaction: discord.Interaction, name:str, role:str):
    try:
        guild     = client.get_guild(guild_id)
        memberid  = int(name.replace('<@', '').replace('>',''))
        roleid    = int(role.replace('<@&', '').replace('>',''))
        print(name,memberid,role,roleid)
        role_data = guild.get_role(roleid)
        member    = guild.get_member(memberid)
        await member.remove_roles(role_data)
        await interaction.response.send_message("Done")
    except:
        await interaction.response.send_message(traceback.format_exc())




client.run(TOKEN)
