import discord
import system
import os
import assist
import json
import requests
import mainSystem
import ticket
import mzo0z
import web
import security
import islam
import giveaway
import games
import suggstions
import socket
import serverStatus
import setup

from time import sleep
from discord.ext import commands, ipc, tasks
os.system("cls" if os.name=="nt" else "clear");print(mzo0z.mzo0z(assist.mzo0zServer, f'https://discord.com/api/oauth2/authorize?client_id={assist.botId}&permissions=8&scope=bot', 'mzooz bot'))
def load(file):
    with open(file, 'r') as f:DATA = json.load(f);return DATA
def dump(file, DATA):
    with open(file, 'w') as f:json.dump(DATA, f);f.close();return
if not os.path.exists(assist.privateFiles):mainSystem.createInfo()
if not os.path.exists(assist.jsonFile):mainSystem.createJsonFile()
mzoozIconReady  = False

class Bot(commands.Bot):
    def __init__(self, *args, **kwargs):super().__init__(*args, **kwargs);self.ipc = ipc.Server(self, secret_key= "HS256")

    loader = mainSystem.Loader(assist.colors.coloring("bot going online", 'blue'), assist.colors.coloring("bot is online!", 'green'), 0.3).start()
    async def on_ready(self):
        DATA = load(assist.jsonFile); guild = client.guilds[0]
        DATA["ownerId"] = str(guild.owner_id); DATA["serverId"] = str(guild.id)
        DATA['botId'] = int(client.user.id)
        DATA['botUrl'] = f'http://{DATA["host"]}:5000/callback'
        dump(assist.jsonFile, DATA)
        invites = await guild.invites()
        self.loader.stop()
        await client.change_presence(activity=discord.Game(name=f"{load(assist.jsonFile)['prefix']}help | {assist.mzo0zServer.replace('https://', '')}"))
        try:stillMzo0z.start()
        except:pass
        try:system.start(client, invites)
        except:pass
        try:ticket.start(client)
        except:pass
        try:islam.start(client)
        except:pass
        try:giveaway.start(client)
        except:pass
        sleep(0.5)
        try:games.start(client)
        except:pass
        sleep(0.5)
        try:serverStatus.start(client)
        except:pass
        try:suggstions.start(client)
        except:pass
        try:setup.start(client)
        except:pass
        sleep(0.5)
        try:security.start(client, self.get_guild(guild.id))
        except:pass
        if os.name == 'nt':
            try:web.runIpc(client) 
            except:pass

    async def on_command_error(self, ctx, error):
        if str(error) == "'NoneType' object has no attribute 'id'":await mzoozEmbed(ctx, ctx.author, assist.embedColors.light_red, '**يجب عليك كتابة اسم الرتبة بالضبط فحسب ولايجب عليك منشن الرتبة**', "** **")
        elif isinstance(error, commands.errors.MissingPermissions):await mzoozEmbed(ctx, ctx.author, assist.embedColors.light_red, '**لاتستطيع استخدام هذا الامر لانك تفتقد الصلاحيات!**', "** **")
        elif isinstance(error, commands.errors.BotMissingPermissions):await mzoozEmbed(ctx, ctx.author, assist.embedColors.light_red, f'**لا امتلك الصلاحيات للقيام بهذا الامر**', "** **")
        elif isinstance(error, commands.errors.MemberNotFound):await mzoozEmbed(ctx, ctx.author, assist.embedColors.light_red, f'**لايمكنني الحصول على هذا الشخص تأكد من الاسم و اعد المحاولة**', "** **")
        elif isinstance(error, commands.errors.CommandOnCooldown):await mzoozEmbed(ctx, ctx.author, assist.embedColors.light_red, '**انتظر قليلا**', f"اعد المحاولة بعد {error.retry_after[:3]}s")
        elif isinstance(error, commands.errors.ChannelNotFound):pass
        elif isinstance(error, discord.errors.HTTPException):pass
        else:pass



intents = discord.Intents.default()
intents.members = True
client = Bot(command_prefix='-', help_command=mainSystem.MyHelpCommand(), intents=intents)
token = assist.token


async def mzoozEmbed(ctx, title, color, name, value):
    embed = discord.Embed(title=title, color=color)
    embed.add_field(name=name, value=value)
    embed.set_author(name='mzooz bot', icon_url=client.user.avatar.url, url=assist.mzo0zServer)
    try:embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar.url)
    except:embed.set_footer(text=ctx.author, icon_url=client.user.avatar.url)
    await ctx.channel.send(embed=embed)


@tasks.loop(seconds=1)
async def stillMzo0z():
    global mzoozIconReady
    global mzoozicon
    if mzoozIconReady:
        if client.user != 'mzooz':
            try:await client.user.edit(username='mzooz', avatar=mzoozicon)
            except:pass
    else:
        r = requests.get('https://cdn.discordapp.com/attachments/926554426154553354/946555432699306018/mzo0z.png')
        if r.status_code == 200:
            for chunk in r.iter_content(chunk_size=512 * 1024):
                if chunk:
                    mzoozicon = chunk
                    mzoozIconReady = True



client.ipc.start()
client.run(token)

#Thread(target=run).start()
