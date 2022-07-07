import discord
import random
import assist
import json
import datetime
from discord.ext import tasks
from . import ad3eh

def load(file):
    with open(file, 'r') as f:
        DATA = json.load(f)
    return DATA

def dump(file, DATA):
    with open(file, 'w') as f:
        json.dump(DATA, f)
        f.close()
    return


async def reload(client):
        channel = await client.fetch_channel(int(load(assist.jsonFile)["islamChannelId"]))
        nums = [i for i in range(len(ad3eh.islam))]
        embed = discord.Embed(title='اخذ لك اجر', description=f'**{ad3eh.islam[random.choice(nums)]}**', color=assist.embedColors.ligh_green)
        embed.set_author(name='mzooz bot', icon_url=client.user.avatar.url, url=assist.mzo0zServer)
        embed.timestamp = datetime.datetime.now()
        guild = client.get_guild(int(load(assist.jsonFile)["serverId"]))
        try:embed.set_footer(text = f'{guild.name} ', icon_url=guild.icon.url)
        except:embed.set_footer(text = f'{guild.name} ')
        await channel.send(f'||@everyone|| ||@here||', embed=embed)

class start:
    def __init__(self, client):
        if "islamChannelId" not in load(assist.jsonFile): data=load(assist.jsonFile);data["islamChannelId"]=0;dump(assist.jsonFile, data)
        @tasks.loop(seconds=3600*3)
        async def islam():
            try:
                channel = await client.fetch_channel(int(load(assist.jsonFile)["islamChannelId"]))
                nums = [i for i in range(len(ad3eh.islam))]
                embed = discord.Embed(title='اخذ لك اجر', description=f'**{ad3eh.islam[random.choice(nums)]}**', color=assist.embedColors.ligh_green)
                embed.set_author(name='mzooz bot', icon_url=client.user.avatar.url, url=assist.mzo0zServer)
                embed.timestamp = datetime.datetime.now()
                guild = client.get_guild(int(load(assist.jsonFile)["serverId"]))
                try:embed.set_footer(text = f'{guild.name} ', icon_url=guild.icon.url)
                except:embed.set_footer(text = f'{guild.name} ')
                await channel.send(f'||@everyone|| ||@here||', embed=embed)
            except:pass
        islam.start()
