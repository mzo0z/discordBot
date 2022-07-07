import assist
import json
import os

from . import scripts
from quart import render_template, redirect, url_for

def load(file):
    with open(file, 'r') as f:
        DATA = json.load(f)
    return DATA
def dump(file, DATA):
    with open(file, 'w') as f:
        json.dump(DATA, f)
        f.close()

class start:
    def __init__(self, app, ipc_client, discord):
        dta = {
            scripts.gamesManagment:scripts.gamesManagmentHtml,
            scripts.setGamesCategory:scripts.setGamesCategoryHtml,
            scripts.setGamesChannel:scripts.setGamesChannelHtml
        }
        for i in dta.keys():
            if not os.path.exists(i):
                f = open(i, 'wb')
                f.write(dta[i].encode('utf-8'))
                f.close()

        data = load(scripts.tickjson)
        try:
            data[str(load(assist.jsonFile)['serverId'])]
        except:
            data[str(load(assist.jsonFile)['serverId'])] = {}
            data[str(load(assist.jsonFile)['serverId'])]['tickets'] = {}
            data[str(load(assist.jsonFile)['serverId'])]['category'] = 0
            dump(scripts.tickjson, data)


        @app.route("/gamesManagment")
        async def gamesManagment():
            if not await discord.authorized:
                return redirect(url_for("login")) 
            return await render_template("gamesManagment.html")
        
        @app.route("/setGamesCategory/<string:name>")
        async def setGamesCategory(name):
            if not await discord.authorized:return redirect(url_for("login"))

            categorys = await ipc_client.request("getChannels")
            data = load(assist.gamesjson)

            if name == '0':return await render_template("setGamesCategory.html", categorys=categorys.keys())
            if name == 'اختر المجموعة المراد تعيينها':return await render_template("setGamesCategory.html", categorys=categorys.keys())
            if name == 'None':
                data = load(assist.gamesjson)
                data['games']['category'] = 0
                dump(assist.gamesjson, data)
                return await render_template("gamesManagment.html") + f"""\n<script>alert("تم جعل الالعاب يمكن تشغليهم في القنوات المحدده فقط");</script>\n"""

            data = load(assist.gamesjson)
            data['games']['category'] = int(categorys[name])
            dump(assist.gamesjson, data)
            return await render_template("gamesManagment.html") + f"""\n<script>alert("تم جعل {name} كـ المجموعة الرئيسية للالعاب, اي قناة في هذه المجموعة يمكن اللعب بها");</script>\n"""


        @app.route("/setGamesChannel/<string:what>/<string:id>")
        async def setGamesChannel(what, id):
            if not await discord.authorized:return redirect(url_for("login")) 

            channel = await ipc_client.request("textChannels")
            data = load(assist.gamesjson)
            if what == "add":
                if id != 'اختر القناة':
                    data['games']['gamesChannels'].append(channel[id])
                    data['games']['gamesChannels'] = list(set(data['games']['gamesChannels']))
                    dump(assist.gamesjson, data)
                    data = load(assist.gamesjson)
                    dta = [i for i in channel.keys() if int(channel[i]) not in data['games']['gamesChannels']]
                    chnls = await ipc_client.request("convertToChannelName", ids=data['games']['gamesChannels'])
                    return await render_template("setGamesChannel.html", channels=dta, addedChannels=chnls) + f"""\n<script>alert("تم إضافة {id} لقنوات الالعاب");</script>\n"""

            if what == "delete":
                if id != 'اختر القناة':
                    data = load(assist.gamesjson)
                    data['games']['gamesChannels'].remove(int(channel[id]))
                    data['games']['gamesChannels'] = list(set(data['games']['gamesChannels']))
                    dump(assist.gamesjson, data)
                    data = load(assist.gamesjson)
                    dta = [i for i in channel.keys() if int(channel[i]) not in data['games']['gamesChannels']]
                    chnls = await ipc_client.request("convertToChannelName", ids=data['games']['gamesChannels'])
                    return await render_template("setGamesChannel.html", channels=dta, addedChannels=chnls) + f"""\n<script>alert("تم إزالة {id} من قنوات الالعاب");</script>\n"""

            data = load(assist.gamesjson)
            dta = [i for i in channel.keys() if int(channel[i]) not in data['games']['gamesChannels']]
            chnls = await ipc_client.request("convertToChannelName", ids=data['games']['gamesChannels'])
            return await render_template("setGamesChannel.html", channels=dta, addedChannels=chnls)

