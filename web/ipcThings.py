import json
import assist
import discord
import islam
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
        async def textChannels(data):
            chnls = {}
            guild = client.guilds[0]
            for channel in guild.channels:
                if str(channel.type).lower() == 'text':
                    chnls.update({channel.name:channel.id})
            return chnls

        @client.ipc.route()
        async def voiceChannels(data):
            chnls = {}
            guild = client.guilds[0]
            for channel in guild.channels:
                if str(channel.type).lower() == 'voice':
                    chnls.update({channel.name:channel.id})
            return chnls


        @client.ipc.route()
        async def convertChannels(data):
            chnls = {}
            for channelId in data.channels:
                channel = await client.fetch_channel(channelId)
                if str(channel.type).lower() == 'text':
                    chnls.update({channel.name:channel.id})
            return chnls

        @client.ipc.route()
        async def reloadIslam(data):
            await islam.reload(client)

        @client.ipc.route()
        async def reload_prefix(data):
            prefix = load(assist.jsonFile)['prefix']
            client.command_prefix=prefix
            await client.change_presence(activity=discord.Game(name=f"{load(assist.jsonFile)['prefix']}help | {assist.mzo0zServer.replace('https://', '')}"))








