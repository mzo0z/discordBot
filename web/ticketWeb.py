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
            scripts.ticketManagment:scripts.ticketManagmentHtml,
            scripts.setCategory:scripts.setCategoryHtml,
            scripts.transcript:scripts.transcripthtml,
            scripts.moveTicket:scripts.moveTicketHtml,
            scripts.ticket:scripts.tickethtml
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


        @app.route("/ticketsManagment")
        async def ticketsManagment():
            if not await discord.authorized:
                return redirect(url_for("login")) 

            return await render_template("ticketManagment.html")

        @app.route("/tickets")
        async def tickets():
            if not await discord.authorized:
                return redirect(url_for("login")) 
            data = load(scripts.tickjson)

            guild_ids = await ipc_client.request("get_guild_ids")
            try:
                data[str(guild_ids[0])]
            except:
                data[str(guild_ids[0])] = {}
                data[str(guild_ids[0])]['tickets'] = {}
                data[str(guild_ids[0])]['category'] = 0
                dump(scripts.tickjson, data)

            return await render_template("ticket.html", tickets=data[str(guild_ids[0])]['tickets'])

        @app.route("/createCategory/<string:name>")
        async def createCategory(name):
            if not await discord.authorized:return redirect(url_for("login"))

            categorys = await ipc_client.request("getChannels")
            data = load(scripts.tickjson)
            guild_ids = await ipc_client.request("get_guild_ids")
            try:
                data[str(guild_ids[0])]
            except:
                data[str(guild_ids[0])] = {}
                data[str(guild_ids[0])]['tickets'] = {}
                data[str(guild_ids[0])]['category'] = 0
                dump(scripts.tickjson, data)

            if name == '0':
                return await render_template("setCategory.html", categorys=categorys.keys())
            if name == 'اختر المجموعة المراد تعيينها':
                return await render_template("setCategory.html", categorys=categorys.keys())

            if name == 'None':
                data = load(scripts.tickjson)
                guild_ids = await ipc_client.request("get_guild_ids")
                data[str(guild_ids[0])]['category'] = 0
                dump(scripts.tickjson, data)
                return await render_template("ticketManagment.html") + f"""\n<script>alert("تم جعل التيكت بدون مجموعة, سيتم فتح التيكت كـ روم عادي");</script>\n"""

            data = load(scripts.tickjson)
            guild_ids = await ipc_client.request("get_guild_ids")
            data[str(guild_ids[0])]['category'] = int(categorys[name])
            dump(scripts.tickjson, data)
            return await render_template("ticketManagment.html") + f"""\n<script>alert("تم تعيين {name} كـ المجموعة الرئيسية للتيكت, اي تيكت يتم إنشائه سيكون في هذه المجموعة");</script>\n"""

        @app.route("/moveTicket/<string:name>/<string:to>")
        async def moveTicket(name, to):
            if not await discord.authorized:return redirect(url_for("login")) 
            data = load(scripts.tickjson)
            guild_ids = await ipc_client.request("get_guild_ids")
            channels = await ipc_client.request("moveTicket")

            if name != '0' and to != '0':
                if name != 'اختر التيكت المراد نقله' and to != 'اختر القناة المراد نقله اليها':
                    return await render_template("ticketManagment.html") + await ipc_client.request("moveMsg", channelId=channels[to], ticket=data[str(guild_ids[0])]['tickets'][name], name=name, to=to)

            try:data[str(guild_ids[0])]
            except:data[str(guild_ids[0])] = {};data[str(guild_ids[0])]['tickets'] = {};data[str(guild_ids[0])]['category'] = 0;dump(scripts.tickjson, data);data = load(scripts.tickjson)

            return await render_template("moveTicket.html", tickets=data[str(guild_ids[0])]['tickets'], channels=channels.keys())

        @app.route("/transcripts")
        async def transcripts():
            if not await discord.authorized:
                return redirect(url_for("login")) 
            files = []
            for i in os.listdir(assist.scrpt):
                files.append(i)

            return await render_template("transcript.html", transcripts=files)

        @app.route('/openTranscript/<string:new>')
        async def openTranscript(new):
            if not await discord.authorized:
                return redirect(url_for("login"))
            return open(assist.scrpt + new, 'rb').read()

        @app.route("/delete/<string:name>")
        async def delete(name):
            data = load(scripts.tickjson)
            guild_ids = await ipc_client.request("get_guild_ids")
            if not await discord.authorized:return redirect(url_for("login")) 
            if name == 'اختر التيكت المراد حذفه':return await render_template("ticket.html", tickets=data[str(guild_ids[0])]['tickets'])
            await ipc_client.request('deleteMSG', ticket=data[str(guild_ids[0])]['tickets'][name])
            data = load(scripts.tickjson)
            return await render_template("ticket.html", tickets=data[str(guild_ids[0])]['tickets'])
