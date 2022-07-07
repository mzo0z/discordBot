import assist
import json
import os

#from . import outstory as outstoryGame # under coding
#from . import describe as describeGame # under coding
from . import asking as askingGame
from . import findme as findmeGame
from . import flags as flagsGame
from . import reversing as reversingGame
from . import sorting as sortingGame
from . import xoGame as xoGame

def load(file):
    with open(file, 'r') as f:return json.load(f)

def dump(file, DATA):
    with open(file, 'w') as f:json.dump(DATA, f);f.close();return

class start:
    def __init__(self, client):
        if not os.path.exists(assist.gamesjson):
            dump(assist.gamesjson, {})
            data = load(assist.gamesjson)
            data[str(load(assist.jsonFile)["serverId"])] = {}
            data["games"] = {}
            data["games"]['category'] = 0
            data["games"]["gamesChannels"] = []
            dump(assist.gamesjson, data)


        @client.command()
        async def xo(ctx, *, names=None):
            if ctx.channel.id in load(assist.gamesjson)["games"]["gamesChannels"]:  await xoGame.start(ctx, client, names);return
            if ctx.channel.category.id == load(assist.gamesjson)["games"]["category"]:await xoGame.start(ctx, client, names);return

        @client.command(aliases=['q', 'ask', 'س', 'سؤال'])
        async def question(ctx):
            if ctx.channel.id in load(assist.gamesjson)["games"]["gamesChannels"]:  await askingGame.play(ctx, client);return
            if ctx.channel.category.id == load(assist.gamesjson)["games"]["category"]:await askingGame.play(ctx, client);return

        @client.command(aliases=['كلمة', 'w'])
        async def word(ctx):
            if ctx.channel.id in load(assist.gamesjson)["games"]["gamesChannels"]:  await findmeGame.start(ctx, client);return
            if ctx.channel.category.id == load(assist.gamesjson)["games"]["category"]:await findmeGame.start(ctx, client);return

        @client.command(aliases=['r', 'ع', "عكس", "اعكس"])
        async def reverse(ctx):
            if ctx.channel.id in load(assist.gamesjson)["games"]["gamesChannels"]:  await reversingGame.start(ctx, client);return
            if ctx.channel.category.id == load(assist.gamesjson)["games"]["category"]:await reversingGame.start(ctx, client);return

        @client.command(aliases=['f', 'اعلام', 'علم'])
        async def flag(ctx):
            if ctx.channel.id in load(assist.gamesjson)["games"]["gamesChannels"]:  await flagsGame.start(ctx, client);return
            if ctx.channel.category.id == load(assist.gamesjson)["games"]["category"]:await flagsGame.start(ctx, client);return

        @client.command(aliases=['رتب'])
        async def sort(ctx):
            if ctx.channel.id in load(assist.gamesjson)["games"]["gamesChannels"]:  await sortingGame.start(ctx, client);return
            if ctx.channel.category.id == load(assist.gamesjson)["games"]["category"]:await sortingGame.start(ctx, client);return
