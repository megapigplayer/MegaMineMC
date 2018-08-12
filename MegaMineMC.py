import discord
import asyncio
from discord.ext import commands
from discord.ext.commands import Bot
import time
import random
import os
import time


Client = commands.Bot(command_prefix = "!")
Client.remove_command("help")
owner = ["Insert-Owner-ID"]

@Client.event
async def on_ready():
    print("Bot Is ready!")
    await Client.change_status(game=discord.Game(name="!help | MegaMineBot"))
	
@Client.command(pass_context=True, no_pm=True)
async def servericon(ctx):
    """Guild Icon"""
    await Client.reply("{}".format(ctx.message.server.icon_url))

@Client.command(pass_context=True, no_pm=True)
async def membericon(ctx, member: discord.Member):
    """User Avatar"""
    await Client.reply("{}".format(member.avatar_url))

@Client.command()
async def say(output):
    await Client.say(output)

@Client.command()
async def ip():
    await Client.say("""
__The Games Server Ip:__
**COMING SOON!**
__The City/SMP Server Ip:__
**COMING SOON!**
**for joim to the city server see- #city-announcements **
""")


@Client.command()
async def serverinfo():
        embed = discord.Embed(title="Bot Information", description="""
__hello! im MegaMineBot!__

```Welcome to the server: MegaMineMC!```
**here you can play with players minecraft!
and every week we play all server in map or special game!
like big uhc or cool mini game and more!
you can join too the smp server!- MegaMine City!
by ask the owner MegaPig and write your name in #minecraft-names !
have fun here! for more info ask the support rank!**
`XbotByMegaPigX`
""", color=0xe88af4)
        await Client.say(embed=embed)

@Client.command()
async def help():
        embed = discord.Embed(title="Command List", description="""
__**MegaMineBot Commands list**__
`!help` - **this page.**
`!serverinfo` **- the info of the server.**
`!servericon` **- the server icon.**
`!membericon @TAG` **- the avatar of the member you write.**
`!ip` - **the games server ip and the city.**
`!say (what you want)` **- the bot say what you want.**
""", color=0xe88af4)
        await Client.say(embed=embed)
	
@Client.command(pass_context = True)
async def freeze(ctx, member: discord.Member):
     if ctx.message.author.server_permissions.view_audit_log or ctx.message.author.id == '194151340090327041':
        role = discord.utils.get(member.server.roles, name='FREEZE')
        await Client.add_roles(member, role)
        embed=discord.Embed(title="User Is Been Freeze!", description="**{0}** was been freeze by **{1}**!".format(member, ctx.message.author), color=0xff00f6)
        await Client.say(embed=embed)
     else:
        embed=discord.Embed(title="You cant freeze this user!", description="You don't have permission to use this command.", color=0xff00f6)
        await Client.say(embed=embed)
	
@Client.command(pass_context = True)
async def unfreeze(ctx, member: discord.Member):
     if ctx.message.author.server_permissions.view_audit_log or ctx.message.author.id == '194151340090327041':
        role = discord.utils.get(member.server.roles, name='FREEZE')
        await Client.remove_roles(member, role)
        embed=discord.Embed(title="User Is Been UnFreeze!", description="**{0}** was been unfreeze by **{1}**!".format(member, ctx.message.author), color=0xff00f6)
        await Client.say(embed=embed)
     else:
        embed=discord.Embed(title="You cant unfreeze this user!", description="You don't have permission to use this command.", color=0xff00f6)
        await Client.say(embed=embed)
	
	
Client.run(os.getenv("TOKEN"))
