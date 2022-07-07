from quart import Quart, render_template, request, redirect, url_for
from quart_discord import DiscordOAuth2Session
from discord.ext import ipc
from . import scripts
from threading import Thread
import threading
import assist
import json
import os
import asyncio

from . import ipcThings

from . import ticketWeb
from . import gamesWeb
from . import securityWeb
from . import systemWeb
from . import serverStatusWeb


def load(file):
    with open(file, 'r') as f:
        DATA = json.load(f)
    return DATA
def dump(file, DATA):
    with open(file, 'w') as f:
        json.dump(DATA, f)
        f.close()


class runIpc:
    def __init__(self, client):
        if not os.path.exists(scripts.privateFiles):os.mkdir(scripts.privateFiles)
        dta = {
            scripts.dashboard:scripts.dashboardHtml,
            scripts.index:scripts.indexHtml,
            scripts.bot:scripts.botHtml,
            scripts.server:scripts.serverHtml,
            scripts.islam:scripts.islamHtml
        }
        for i in dta.keys():
            if not os.path.exists(i):
                f = open(i, 'wb')
                f.write(dta[i].encode('utf-8'))
                f.close()

        app = Quart(__name__, template_folder=scripts.privateFiles)
        def running():
            app.run(debug=True, port=5000, host=load(assist.jsonFile)['host'])
        start(app, client)
        t = Thread(target=running)
        t.start()

class start:
    def __init__(self, app, client):
        ipc_client = ipc.Client(secret_key = "HS256")
        app.config["SECRET_KEY"] = "HS256"
        app.config["DISCORD_CLIENT_ID"]     = int(load(assist.jsonFile)['botId'])
        app.config["DISCORD_CLIENT_SECRET"] = load(assist.jsonFile)['secretKey']
        app.config["DISCORD_REDIRECT_URI"]  = load(assist.jsonFile)['botUrl']
        discord = DiscordOAuth2Session(app)
        ipcThings.start(client)
        def th():ticketWeb.start(app, ipc_client, discord)
        def gamesWb():gamesWeb.start(app, ipc_client, discord)
        def three():systemWeb.start(app, ipc_client, discord)
        def four():securityWeb.start(app, ipc_client, discord)
        def five():serverStatusWeb.start(app, ipc_client, discord)
        Thread(target=gamesWb).start()
        Thread(target=th).start()
        Thread(target=three).start()
        Thread(target=four).start()
        Thread(target=five).start()
            

        @app.errorhandler(404)
        async def not_found(e):
            return "حدث خطأ"


        @app.route("/")
        async def home():
            return await render_template("index.html", authorized = await discord.authorized)
        @app.route("/login")
        async def login():
            return await discord.create_session()

        @app.route("/callback")
        async def callback():
            try:
                await discord.callback()
            except Exception:
                pass

            return redirect(url_for("dashboard"))

        @app.route("/dashboard")
        async def dashboard():
            if not await discord.authorized:
                return redirect(url_for("login")) 

            guild_count = await ipc_client.request("get_guild_count")
            guild_ids = await ipc_client.request("get_guild_ids")

            user_guilds = await discord.fetch_guilds()

            guilds = []

            for guild in user_guilds:
                if guild.permissions.administrator:
                    guild.class_color = "green-border";guilds.append(guild) if guild.id in guild_ids else "red-border"

            guilds.sort(key = lambda x: x.class_color == "red-border")
            name = (await discord.fetch_user()).name
            return await render_template("dashboard.html", guild_count = guild_count, guilds = guilds, username=name)

        @app.route("/islam/<string:id>")
        async def islam(id):
            if not await discord.authorized:return redirect(url_for("login"))
            data = load(scripts.assist.jsonFile)
            channels = await ipc_client.request("textChannels")
            if id =="عدم تعيين":data['islamChannelId']=0;dump(assist.jsonFile, data)
            elif id != '0' and id !='اختر القناة':data['islamChannelId']=channels[id];dump(assist.jsonFile, data)
            await ipc_client.request("reloadIslam")
            return await render_template("islam.html", channels=channels)

        @app.route("/", methods=["POST", "GET"])
        @app.route("/bot/<string:cmd>", methods=["POST", "GET"])
        async def bot(cmd):
            if not await discord.authorized:return redirect(url_for("login"))
            global c
            WARNNING = ''
            DATA = load(assist.jsonFile)
            cmds = {
                "prefix":DATA['prefix'],
                "secret key":DATA['secretKey'],
                "host ip":DATA['host'],
                "support url":DATA['supportUrl'],
                "log channel id":DATA['logChannelId']
            }
            msgs = {
                "prefix":'ماهي البادئة الجديدة',
                "secret key":"ماهو المفتاح الجديد",
                "host ip":'ماهو الـ آي بي الجديد',
                "support url":'ماهو الرابط الجديد',
                "log channel id" : "ماهو الـ آي دي الجديد"
            }

            cds = {
                "prefix":'prefix',
                "secret key":'secretKey',
                "host ip":'host',
                "support url":'supportUrl',
                "log channel id": "logChannelId"
            }

            if str(request.method) == "POST":
                form = await request.form
                new = str(form['url'])
                nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
                if str(new[0]) in nums:WARNNING = f"""\n<script>alert("لايمكن استخدام ارقام");</script>\n"""
                if new != '0' and new != '' and new not in nums:
                    try:DATA[cds[c]]=int(new)
                    except:DATA[cds[c]]=new
                    dump(assist.jsonFile, DATA)
                    if cds[c] == 'prefix':await ipc_client.request("reload_prefix")
                    elif cds[c] == 'logChannelId':pass
                    else:WARNNING = f"""\n<script>alert("قم بإعادة تشغيل البوت");</script>\n"""

            try:cmds = cmds[cmd];msg=msgs[cmd];CMD=True
            except:cmds = cmds;msg='';CMD=False
            c = cmd

            return await render_template('bot.html', cmds=cmds, CMD=CMD, oldCmd=cmd, msg=msg) + WARNNING



        @app.route("/dashboard/<int:guild_id>")
        async def dashboard_server(guild_id):
            if not await discord.authorized:
                return redirect(url_for("login"))
            guild = await ipc_client.request("get_guild", guild_id = guild_id)
            if guild is None:
                return redirect(f'https://discord.com/oauth2/authorize?&client_id={app.config["DISCORD_CLIENT_ID"]}&scope=bot&permissions=8&guild_id={guild_id}&response_type=code&redirect_uri={app.config["DISCORD_REDIRECT_URI"]}')
            return await render_template("server.html")

        @app.route("/server")
        async def server():
            if not await discord.authorized:
                return redirect(url_for("login"))
            return await render_template("server.html")

        
