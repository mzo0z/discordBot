from time import sleep
import assist
import json
import os

from . import scripts
from quart import render_template, redirect, url_for, request

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
            scripts.systemManagment:scripts.systemManagmentHtml,
            scripts.cmdsManagment:scripts.cmdsManagmentHtml,
            scripts.wlcbyeManagment:scripts.wlcbyeManagmentHtml,
            scripts.addAntiWord:scripts.addAntiWordHtml,
            scripts.robotManagment:scripts.robotManagmentHtml,
            scripts.addAutoResponse:scripts.addAutoResponseHtml,
            scripts.setSuggstions:scripts.setSuggstionsHtml,
            scripts.setLine:scripts.setLineHtml,
        }
        for i in dta.keys():
            if not os.path.exists(i):
                f = open(i, 'wb')
                f.write(dta[i].encode('utf-8'))
                f.close()

        DATA = load(assist.jsonFile)

        if 'commands' not in DATA:
            DATA['commands'] = {}
            DATA['commands']['kick'] = []
            DATA['commands']['ban'] = []
            DATA['commands']['unBan'] = []
            DATA['commands']['clear'] = []
            DATA['commands']['role'] = []
            DATA['commands']['unRole'] = []
            DATA['commands']['lock'] = []
            DATA['commands']['unLock'] = []
            DATA['commands']['mute'] = []
            DATA['commands']['unMute'] = []
            dump(assist.jsonFile, DATA)

        if "welcome" not in DATA:
            DATA["logChannelId"] = 0
            DATA["line"] = {}
            DATA["line"][DATA["serverId"]] = {}
            DATA["line"][DATA["serverId"]]["active"] = 0
            DATA["line"][DATA["serverId"]]["url"] = 'https://cdn.discordapp.com/attachments/949076504342573066/966175309873434714/mzooz.gif'
            DATA["line"][DATA["serverId"]]["autoLine"] = {}
            DATA["line"][DATA["serverId"]]["autoLine"]['active'] = 0
            DATA["line"][DATA["serverId"]]["autoLine"]['channelsId'] = []


            DATA["autoMod"] = {}
            DATA["autoMod"][DATA["serverId"]] = {}
            DATA["autoMod"][DATA["serverId"]]['active'] = 0
            DATA["autoMod"][DATA["serverId"]]['autoResponse'] = {'???????? ??????????':"?????????? ????????????", '???????????? ??????????':'?????????? ????????????'}
            DATA["autoMod"][DATA["serverId"]]['antiBadWords'] = ['????????????', '????????', '??????????', '??????????', '??????????', '????????', '??????', '????????????', '????????????', '????????????', '????????????', '??????????', '????????????', '????', '????????', '????????', '????????', '????????', '????????', '????????', '????????', '????????????', '????????', '????????', '??????', '????????????', '????????????', '??????????', '????', '????????????', '??????????', '????????????', '??????', '????????????', '??????????', '??????????', '??????', '??????????????', '??????', '????????', '??????????', '????????', '??????????', '??????', '??????', '????????????', '??????????', '????????', '????????', '??????????', '??????', '????????', '????????', '??????????', '????????', '????????', '????????????', '????????', '????????????', '??????????????', '????????', '??????', '????????', '????????????', '??????', '????????????', '????????????', '????????????', '????????', '??????', '??????????', '????????', '????????', '??????????', '????????', '????????', '??????', '????????????????', '??????????', '????????', '????????', '????????', '????????????', '??????', '????????????', '??????????', '??????????', '????????', '??????????', '??????', '????????????', '??????', '??????', '????????', '??????????', '??????????', '????????', '????????????', '????????????', '??????????', '??????????', '??????????', '????????', '??????', '????????????', '??????????????', '????', '??????????', '??????????????', '????????????', '????????', '??????????', '????????????', '??????????', '??????????', '????????????', '????????', '????????', '????????', '????????????', '????????', '??????????', '????', '????????????', '??????????', '????????????', '??????????', '????????????', '????????', '??????????', '????', '??????????', '??????????', '????????', '????????', '??????', '????????????????', '????????????', '??????', '????', '??????????', '??????', '????', '????????????', '????????', '??????????', '??????????', '????????', '????????????', '????????????', '????????', '??????', '????', '????????????', '??????????', '??????', '??????????????', '??????', '????????????????', '????????', '??????????', '????????', '????????????', '??????', '??????????', '????????????', '????????????', '????????????', '??????????', '????????', '????????', '??????????', '??????????', '??????????', '????????????', '????????', '??????????', '????????????', '??????????', '????????????', '????????', '??????????????', '??????????', '????????', '????', '????????', '????????', '????????', '??????????????', '??????????', '????????????', '??????????', '??????????????', '????', '??????????', '??????????', '????????????', '????????????', '??????????', '????????', '????????????', '??????????', '??????????', '????????????', '????????', '??????????', '????????', '????????', '??????', '????????', '????????', '??????????', '????????????', '????????', '??????????', '??????????????', '??????', '????????????']
            DATA["autoMod"][DATA["serverId"]]['autoUrl'] = 0
            DATA["autoMod"][DATA["serverId"]]['antiSpam'] = 0

            DATA["welcome"] = {}
            DATA["welcome"][DATA["serverId"]] = {}
            DATA["welcome"]["invites_dict"] = {}
            DATA["welcome"][DATA["serverId"]]["welcomeChannelId"] = 0
            DATA["welcome"][DATA["serverId"]]["welcomeRole"] = {}
            DATA["welcome"][DATA["serverId"]]["welcomeRole"]["active"] = 0
            DATA["welcome"][DATA["serverId"]]["welcomeRole"]["roleId"] = []
            DATA["welcome"][DATA["serverId"]]["leaveChannelId"] = 0
            DATA["welcome"][DATA["serverId"]]["welcMsg"] = '?????????? ???? ???? [user] ???? [server] \n?????? ?????????????? ???? ??????????????: [membersCount] \n????????????: [inviter] \n?????? ?????????????? ???? ?????? [inviter]: [inviters]'
            DATA["welcome"][DATA["serverId"]]["leaveMsg"] = '[user] ?????? ???? ?????????????? \n ?????? ?????????????? ???? ?????? [inviter]: [inviters]'
            DATA["welcome"][DATA["serverId"]]["inviters"] = {}
            dump(assist.jsonFile, DATA)




        @app.route('/systemManagment')
        async def systemManagment():
            if not await discord.authorized:return redirect(url_for("login"))
            return await render_template('systemManagment.html')

        @app.route("/", methods=["GET", "POST"])
        @app.route('/cmdsManagment/<string:cmd>/<string:rem>', methods=['POST', 'GET'])
        async def cmdsManagment(cmd, rem):
            if not await discord.authorized:return redirect(url_for("login"))
            global c
            WARNNING = ''
            DATA = load(assist.jsonFile)
            cmds = {
                'kick': DATA['commands']['kick'],
                'ban': DATA['commands']['ban'],
                'unBan': DATA['commands']['unBan'],
                'clear': DATA['commands']['clear'],
                'role': DATA['commands']['role'],
                'unRole': DATA['commands']['unRole'],
                'lock': DATA['commands']['lock'],
                'unLock': DATA['commands']['unLock'],
                'mute': DATA['commands']['mute'],
                'unMute': DATA['commands']['unMute'],
            }
            if str(request.method) == "POST":
                form = await request.form
                u = form['url']
                if u != '':
                    if u.startswith(load(assist.jsonFile)['prefix']):u=u[1:]
                    lst = [o for i in cmds.values() for o in i]
                    if u in lst:WARNNING = f"""\n<script>alert("?????????????? ?????????? ?????? ???????????? ????????????");</script>\n"""
                    else:
                        DATA['commands'][cmd].append(u)
                        DATA['commands'][cmd] = list(set(DATA['commands'][cmd]))
                        dump(assist.jsonFile, DATA)
                        

            if rem != '0' and rem !='???????? ????????????':DATA['commands'][c].remove(rem);dump(assist.jsonFile, DATA)
            try:cmds = cmds[cmd];CMD=True
            except:cmds = cmds;CMD=False
            c = cmd

            return await render_template('cmdsManagment.html', cmds=cmds, CMD=CMD, oldCmd=cmd) + WARNNING



        @app.route("/", methods=["GET", "POST"])
        @app.route("/autoRoles/<string:onff>", methods=['POST', 'GET'])
        async def autoRoles(onff):
            if not await discord.authorized:return redirect(url_for("login"))
            chanels = await ipc_client.request("textChannels")
            roles = await ipc_client.request("getRoles")
            DATA = load(assist.jsonFile)

            if onff == 'on':DATA["welcome"][DATA["serverId"]]["welcomeRole"]["active"]=1;dump(assist.jsonFile, DATA)
            if onff == 'off':DATA["welcome"][DATA["serverId"]]["welcomeRole"]["active"]=0;dump(assist.jsonFile, DATA)

            if str(request.method) == "POST":
                form = await request.form
                msg=form['subject']
                if msg != '':DATA["welcome"][DATA["serverId"]]["welcMsg"]=msg;dump(assist.jsonFile, DATA)


            actv = True if DATA["welcome"][DATA["serverId"]]["welcomeRole"]["active"] == 1 else False


            onRoles = await ipc_client.request("convertRoles", roles=DATA["welcome"][DATA["serverId"]]["welcomeRole"]["roleId"])
            rls = [rl for rl in roles.keys() if roles[rl] not in DATA["welcome"][DATA["serverId"]]["welcomeRole"]["roleId"]]

            return await render_template('wlcbyeManagment.html', channels=chanels, message=DATA["welcome"][DATA["serverId"]]["welcMsg"], activeRole=actv, roles=rls, onRoles=onRoles)


        @app.route("/", methods=["GET", "POST"])
        @app.route('/wlcbyeManagment/<string:welc>/<string:leave>/<string:addRole>/<string:remRole>', methods=['POST', 'GET'])
        async def wlcbyeManagment(welc, leave, addRole, remRole):
            if not await discord.authorized:return redirect(url_for("login"))
            chanels = await ipc_client.request("textChannels")
            roles = await ipc_client.request("getRoles")
            DATA = load(assist.jsonFile)

            if str(request.method) == "POST":
                form = await request.form
                msg=form['subject']
                if msg != '':DATA["welcome"][DATA["serverId"]]["welcMsg"]=msg;dump(assist.jsonFile, DATA)

            if welc    != '0' and welc   != '???????? ????????????' and welc  != '=??????????????=':DATA["welcome"][DATA["serverId"]]["welcomeChannelId"]=chanels[welc];dump(assist.jsonFile, DATA)
            if leave   != '0' and leave  != '???????? ????????????' and leave != "=??????????????=":DATA["welcome"][DATA["serverId"]]["leaveChannelId"]=chanels[leave];dump(assist.jsonFile, DATA)
            if addRole != '0' and addRole!= '???????? ????????????':DATA["welcome"][DATA["serverId"]]["welcomeRole"]["roleId"].append(roles[addRole]);DATA["welcome"][DATA["serverId"]]["welcomeRole"]["roleId"]=list(set(DATA["welcome"][DATA["serverId"]]["welcomeRole"]["roleId"]));dump(assist.jsonFile, DATA)
            if remRole != '0' and remRole!= '?????? ????????????' :DATA["welcome"][DATA["serverId"]]["welcomeRole"]["roleId"].remove(roles[remRole]);DATA["welcome"][DATA["serverId"]]["welcomeRole"]["roleId"]=list(set(DATA["welcome"][DATA["serverId"]]["welcomeRole"]["roleId"]));dump(assist.jsonFile, DATA)
            if welc  == '??????????????':DATA["welcome"][DATA["serverId"]]["welcomeChannelId"]=0;dump(assist.jsonFile, DATA)
            if leave == '??????????????':DATA["welcome"][DATA["serverId"]]["leaveChannelId"]=0;dump(assist.jsonFile, DATA)
            actv = True if DATA["welcome"][DATA["serverId"]]["welcomeRole"]["active"] == 1 else False
            onRoles = await ipc_client.request("convertRoles", roles=DATA["welcome"][DATA["serverId"]]["welcomeRole"]["roleId"])
            rls = [rl for rl in roles.keys() if roles[rl] not in DATA["welcome"][DATA["serverId"]]["welcomeRole"]["roleId"]]

            return await render_template('wlcbyeManagment.html', channels=chanels, message=DATA["welcome"][DATA["serverId"]]["welcMsg"], activeRole=actv, roles=rls, onRoles=onRoles)

        @app.route('/addAntiWord/<string:word>/<string:wordToDel>')
        async def addAntiWord(word, wordToDel):
            if not await discord.authorized:return redirect(url_for("login"))
            DATA = load(assist.jsonFile)
            word = word.replace("`", '/')
            if word != '0' and word != 'word':DATA["autoMod"][DATA["serverId"]]['antiBadWords'].append(word);DATA["autoMod"][DATA["serverId"]]['antiBadWords']=list(set(DATA["autoMod"][DATA["serverId"]]['antiBadWords']));dump(assist.jsonFile, DATA)
            if wordToDel != '0' and wordToDel != '???????? ???????????? ???????????? ???????????? ??????':DATA["autoMod"][DATA["serverId"]]['antiBadWords'].remove(wordToDel);dump(assist.jsonFile, DATA)
            words = load(assist.jsonFile)['autoMod'][DATA['serverId']]['antiBadWords']
            return await render_template('addAntiWord.html', words=words)


        @app.route('/antiSpam/<string:onff>')
        async def antiSpam(onff):
            if not await discord.authorized:return redirect(url_for("login"))
            DATA = load(assist.jsonFile)
            msg = ''
            if onff   == 'on' :DATA["autoMod"][DATA["serverId"]]['antiSpam'] = 1
            elif onff == 'off':DATA["autoMod"][DATA["serverId"]]['antiSpam'] = 0
            dump(assist.jsonFile, DATA)
            activeAuto = True if load(assist.jsonFile)['autoMod'][DATA["serverId"]]['active'] == 1 else False
            antiUrls   = True if load(assist.jsonFile)['autoMod'][DATA["serverId"]]['autoUrl'] == 1 else False
            antiSpam   = True if load(assist.jsonFile)['autoMod'][DATA["serverId"]]['antiSpam'] == 1 else False
            return await render_template('robotManagment.html', activeAuto=activeAuto, antiUrls=antiUrls, antiSpam=antiSpam) + msg

        @app.route('/addAntiBad/<string:word>/<string:response>')
        async def addAntiBad(word, response):
            if not await discord.authorized:return redirect(url_for("login"))
            DATA = load(assist.jsonFile)
            DATA["autoMod"][DATA["serverId"]]['autoResponse'].update({word:response})
            dump(assist.jsonFile, DATA)
            return await render_template('addAutoResponse.html')

        @app.route('/addAutoResponse')
        async def addAutoResponse():
            if not await discord.authorized:return redirect(url_for("login"))
            return await render_template('addAutoResponse.html')

        @app.route('/antiUrls/<string:onff>')
        async def antiUrls(onff):
            if not await discord.authorized:return redirect(url_for("login"))
            DATA = load(assist.jsonFile)
            msg = ''
            if onff   == 'on' :DATA["autoMod"][DATA["serverId"]]['autoUrl'] = 1
            elif onff == 'off':DATA["autoMod"][DATA["serverId"]]['autoUrl'] = 0
            dump(assist.jsonFile, DATA)
            activeAuto = True if load(assist.jsonFile)['autoMod'][DATA["serverId"]]['active'] == 1 else False
            antiUrls   = True if load(assist.jsonFile)['autoMod'][DATA["serverId"]]['autoUrl'] == 1 else False
            antiSpam   = True if load(assist.jsonFile)['autoMod'][DATA["serverId"]]['antiSpam'] == 1 else False
            return await render_template('robotManagment.html', activeAuto=activeAuto, antiUrls=antiUrls, antiSpam=antiSpam) + msg

        @app.route('/robotAutoActive/<string:onff>')
        async def robotAutoActive(onff):
            if not await discord.authorized:return redirect(url_for("login"))
            DATA = load(assist.jsonFile)
            msg = ''
            if onff   == 'on' :DATA["autoMod"][DATA["serverId"]]['active'] = 1; msg = msg + f"""\n<script>alert("???? ?????????? ???????? ?????????????? ??????????????????");</script>\n"""
            elif onff == 'off':DATA["autoMod"][DATA["serverId"]]['active'] = 0; msg = msg + f"""\n<script>alert("???? ?????????? ???????? ?????????????? ??????????????????");</script>\n"""
            dump(assist.jsonFile, DATA)
            activeAuto = True if load(assist.jsonFile)['autoMod'][DATA["serverId"]]['active'] == 1 else False
            antiUrls = True if load(assist.jsonFile)['autoMod'][DATA["serverId"]]['autoUrl'] == 1 else False
            antiSpam = True if load(assist.jsonFile)['autoMod'][DATA["serverId"]]['antiSpam'] == 1 else False
            return await render_template('robotManagment.html', activeAuto=activeAuto, antiUrls=antiUrls, antiSpam=antiSpam) + msg

        @app.route('/robotManagment')
        async def robotManagment():
            if not await discord.authorized:return redirect(url_for("login"))
            msg = ''
            DATA = load(assist.jsonFile)
            activeAuto = True if load(assist.jsonFile)['autoMod'][DATA["serverId"]]['active'] == 1 else False
            antiUrls = True if load(assist.jsonFile)['autoMod'][DATA["serverId"]]['autoUrl'] == 1 else False
            antiSpam = True if load(assist.jsonFile)['autoMod'][DATA["serverId"]]['antiSpam'] == 1 else False
            return await render_template('robotManagment.html', activeAuto=activeAuto, antiUrls=antiUrls, antiSpam=antiSpam) + msg

        @app.route('/suggestionsManagment/<string:setChannel>/<string:unSetChannel>')
        async def suggestionsManagment(setChannel, unSetChannel):
            if not await discord.authorized:return redirect(url_for("login"))
            DATA = load(assist.jsonFile)
            msg = ''
            channels = await ipc_client.request("textChannels")
            if   setChannel   != '0' and setChannel  != '???????? ????????????':DATA["suggestions"][DATA["serverId"]]["suggestionsChannelId"].append(channels[setChannel]);DATA["suggestions"][DATA["serverId"]]["suggestionsChannelId"] = list(set(DATA["suggestions"][DATA["serverId"]]["suggestionsChannelId"]));dump(assist.jsonFile, DATA); msg = msg + f"""\n<script>alert("???? ?????????? {setChannel} ?????? ?????????? ?????????? ????????????????????");</script>\n"""
            elif unSetChannel != '0' and unSetChannel!= '???????? ????????????':DATA["suggestions"][DATA["serverId"]]["suggestionsChannelId"].remove(channels[unSetChannel]);dump(assist.jsonFile, DATA); msg = msg + f"""\n<script>alert("???? ?????????? {unSetChannel} ???? ?????????? ?????????? ????????????????????");</script>\n"""
            activeSuggstions = True if load(assist.jsonFile)['suggestions'][load(assist.jsonFile)['serverId']]['active'] == 1 else False
            onChannels = await ipc_client.request("convertChannels", channels=load(assist.jsonFile)['suggestions'][load(assist.jsonFile)['serverId']]['suggestionsChannelId'])
            channels = [channel for channel in channels.keys() if channel not in onChannels]
            return await render_template('setSuggstions.html', channels=channels, onChannels=onChannels, activeSuggstions=activeSuggstions) + msg

        @app.route('/activeSuggstions/<string:onff>')
        async def activeSuggstions(onff):
            DATA = load(assist.jsonFile)
            msg = ''
            if onff == 'on':DATA["suggestions"][DATA["serverId"]]["active"] = 1 ; msg = msg + f"""\n<script>alert("???? ?????????? ???????? ???????????????????? ");</script>\n"""
            elif onff == 'off':DATA["suggestions"][DATA["serverId"]]["active"] = 0; msg = msg + f"""\n<script>alert("???? ?????????? ???????? ????????????????????");</script>\n"""
            dump(assist.jsonFile, DATA)
            activeSuggstions = True if load(assist.jsonFile)['suggestions'][load(assist.jsonFile)['serverId']]['active'] == 1 else False
            channels = await ipc_client.request("textChannels")
            onChannels = await ipc_client.request("convertChannels", channels=load(assist.jsonFile)['suggestions'][load(assist.jsonFile)['serverId']]['suggestionsChannelId'])
            channels = [channel for channel in channels.keys() if channel not in onChannels]
            return await render_template('setSuggstions.html', channels=channels, onChannels=onChannels, activeSuggstions=activeSuggstions) + msg


        @app.route('/activeAutoLine/<string:Bool>')
        async def activeAutoLine(Bool):
            if not await discord.authorized:return redirect(url_for("login"))
            DATA = load(assist.jsonFile)
            msg = ''
            if Bool == 'on':DATA["line"][DATA["serverId"]]["autoLine"]['active'] = 1 ; msg = msg + f"""\n<script>alert("???? ?????????? ???????? ???????? ????????????????");</script>\n"""
            elif Bool == 'off':DATA["line"][DATA["serverId"]]["autoLine"]['active'] = 0; msg = msg + f"""\n<script>alert("???? ?????????? ???????? ???????? ????????????????");</script>\n"""
            dump(assist.jsonFile, DATA)
            channels = await ipc_client.request("textChannels")
            activeAutoLine = True if load(assist.jsonFile)['line'][load(assist.jsonFile)['serverId']]['autoLine']['active'] == 1 else False
            onChannels = await ipc_client.request("convertChannels", channels=load(assist.jsonFile)['line'][load(assist.jsonFile)['serverId']]['autoLine']['channelsId'])
            return await render_template('setLine.html', channels=channels, onChannels=onChannels, lineUrl=load(assist.jsonFile)["line"][DATA["serverId"]]["url"], activeAutoLine=activeAutoLine) + msg

        @app.route('/setLine/<string:setChannelId>/<string:unSetChannelId>/<string:gif>')
        async def setLine(setChannelId, unSetChannelId, gif):
            if not await discord.authorized:return redirect(url_for("login"))
            msg = ''
            channels = await ipc_client.request("textChannels")
            activeAutoLine = True if load(assist.jsonFile)['line'][load(assist.jsonFile)['serverId']]['autoLine']['active'] == 1 else False
            DATA = load(assist.jsonFile)
            if setChannelId   !='0' and setChannelId   != '???????? ????????????':DATA["line"][DATA["serverId"]]["autoLine"]['channelsId'].append(channels[setChannelId])  ;DATA["line"][DATA["serverId"]]["autoLine"]['channelsId']=list(set(DATA["line"][DATA["serverId"]]["autoLine"]['channelsId']));dump(assist.jsonFile, DATA)
            if unSetChannelId !='0' and unSetChannelId != '???????? ????????????':DATA["line"][DATA["serverId"]]["autoLine"]['channelsId'].remove(channels[unSetChannelId]);DATA["line"][DATA["serverId"]]["autoLine"]['channelsId']=list(set(DATA["line"][DATA["serverId"]]["autoLine"]['channelsId']));dump(assist.jsonFile, DATA)
            if gif != '0' and gif != '???????? ????????????':DATA["line"][DATA["serverId"]]["url"] = gif.replace('`', '/');dump(assist.jsonFile, DATA)
            onChannels = await ipc_client.request("convertChannels", channels=load(assist.jsonFile)['line'][load(assist.jsonFile)['serverId']]['autoLine']['channelsId'])
            channels = [channel for channel in channels.keys() if channel not in onChannels]
            return await render_template('setLine.html', channels=channels, onChannels=onChannels, lineUrl=load(assist.jsonFile)["line"][DATA["serverId"]]["url"], activeAutoLine=activeAutoLine) + msg

