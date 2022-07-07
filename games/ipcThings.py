import json
import assist
import discord

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
        async def convertToChannelName(data):
            names = []
            for id in data.ids:
                try:
                    channel = await client.fetch_channel(id)
                    names.append(channel.name)
                except:pass
            return names

    