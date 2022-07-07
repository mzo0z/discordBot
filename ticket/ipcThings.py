import json
import assist
import discord
from . import scripts
from . import Ticket

def load(file):
    with open(file, 'r') as f:
        DATA = json.load(f)
    return DATA
def dump(file, DATA):
    with open(file, 'w') as f:
        json.dump(DATA, f)
        f.close()
    return
class start:
    def __init__(self, client):
        @client.event
        async def on_ipc_error(endpoint, error):
            print(endpoint, "raised", error)

        @client.ipc.route()
        async def get_guild_count(data):
            return len(client.guilds) # returns the len of the guilds to the client

        @client.ipc.route()
        async def get_guild_ids(data):
            final = []
            for guild in client.guilds:
                final.append(guild.id)
            return final # returns the guild ids to the client

        @client.ipc.route()
        async def get_guild(data):
            guild = client.get_guild(data.guild_id)
            if guild is None: return None

            guild_data = {
                "name": guild.name,
                "id": guild.id,
                "prefix" : load(assist.jsonFile)['prefix']
            }

            return guild_data

        @client.ipc.route()
        async def deleteMSG(data):
            await Ticket.afterDelete(client=client, ticket=data.ticket, guildId=client.guilds[0].id)
            return load(scripts.jsonFile)[str(client.guilds[0].id)]["tickets"]

        @client.ipc.route()
        async def getChannels(data):
            chnls = {}
            guild = client.guilds[0]
            for channel in guild.channels:
                if str(channel.type).lower() == 'category':
                    chnls.update({channel.name:channel.id})
            return chnls

        @client.ipc.route()
        async def moveMsg(data):
            try:
                await Ticket.autoTicket(client=client, title=data.ticket["title"], description=data.ticket["description"], author=data.ticket["author"], avatar=data.ticket["avatar"], thumbnail=data.ticket["thumbnail"], feilds=data.ticket["feilds"], allows=data.ticket["allow"], photo=data.ticket["photo"], channel=int(data.channelId), button=data.ticket["button"], cid=data.ticket["custom_id"], guildId=client.guilds[0].id, oldChannel=int(data.ticket["channelId"]), msg=data.ticket["msg"])
                return f"""\n<script>alert("تم نقل التيكت: {data.name[:data.name.find("_")].replace('[SPACE]', " ")} الى روم: {data.to}");</script>\n"""
            except:
                return f'\n<script>alert("حدث خطأ اثناء نقل التيكت");</script>\n'

        @client.ipc.route()
        async def moveTicket(data):
            chnls = {}
            guild = client.guilds[0]
            for channel in guild.channels:
                if str(channel.type).lower() == 'text':
                    chnls.update({channel.name:channel.id})
            return chnls

    