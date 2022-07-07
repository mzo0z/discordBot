from time import sleep
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
            scripts.serverStatusManagement:scripts.serverStatusManagementHtml,
        }
        for i in dta.keys():
            if not os.path.exists(i):
                f = open(i, 'wb')
                f.write(dta[i].encode('utf-8'))
                f.close()


        @app.route("/serverStatusManagement")
        async def serverStatusManagement():
            if not await discord.authorized:return redirect(url_for("login")) 
            data = load(assist.jsonFile)
            channels = await ipc_client.request('voiceChannels')
            active = True if data['serverStatus'][data['serverId']]['active'] == 1 else False
            return await render_template("serverStatusManagement.html", channels=channels, active=active)

        @app.route("/setServerStatus/<string:members>/<string:bots>/<string:allMembers>")
        async def setServerStatus(members, bots, allMembers):
            if not await discord.authorized:return redirect(url_for("login"))
            data = load(assist.jsonFile)
            channels = await ipc_client.request('voiceChannels')
            active = True if data['serverStatus'][data['serverId']]['active'] == 1 else False
            if members    != "0" and members    != "اختر القناة":data['serverStatus'][data['serverId']]['membersChannelId']    = int(channels[members])   ;dump(assist.jsonFile, data)
            if bots       != "0" and bots       != "اختر القناة":data['serverStatus'][data['serverId']]['botsChannelId']       = int(channels[bots])      ;dump(assist.jsonFile, data)
            if allMembers != "0" and allMembers != "اختر القناة":data['serverStatus'][data['serverId']]['allMembersChannelId'] = int(channels[allMembers]);dump(assist.jsonFile, data)
    
            return await render_template("serverStatusManagement.html", channels=channels, active=active)

        @app.route("/activeServerStatus/<string:onff>")
        async def activeServerStatus(onff):
            if not await discord.authorized:return redirect(url_for("login")) 

            data = load(assist.jsonFile)
            if onff == 'on':data['serverStatus'][data['serverId']]['active'] = 1;dump(assist.jsonFile, data)
            if onff == 'off':data['serverStatus'][data['serverId']]['active'] = 0;dump(assist.jsonFile, data)
            channels = await ipc_client.request('voiceChannels')
            active = True if data['serverStatus'][data['serverId']]['active'] == 1 else False
            return await render_template("serverStatusManagement.html", channels=channels, active=active)
        