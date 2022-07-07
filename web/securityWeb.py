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
            scripts.securityManagment:scripts.securityManagmentHtml,
        }
        for i in dta.keys():
            if not os.path.exists(i):
                f = open(i, 'wb')
                f.write(dta[i].encode('utf-8'))
                f.close()

        DATA = load(assist.jsonFile)
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
            DATA["autoMod"][DATA["serverId"]]['autoResponse'] = {'سلام عليكم':"عليكم السلام", 'السلام عليكم':'عليكم السلام'}
            DATA["autoMod"][DATA["serverId"]]['antiBadWords'] = ['fuck']
            DATA["autoMod"][DATA["serverId"]]['autoUrl'] = 0
            DATA["autoMod"][DATA["serverId"]]['antiSpam'] = 0

            DATA["welcome"] = {}
            DATA["welcome"][DATA["serverId"]] = {}
            DATA["welcome"]["invites_dict"] = {}
            DATA["welcome"][DATA["serverId"]]["welcomeChannelId"] = 0
            DATA["welcome"][DATA["serverId"]]["welcomeRole"] = {}
            DATA["welcome"][DATA["serverId"]]["welcomeRole"]["active"] = 0
            DATA["welcome"][DATA["serverId"]]["welcomeRole"]["roleId"] = 0
            DATA["welcome"][DATA["serverId"]]["leaveChannelId"] = 0
            DATA["welcome"][DATA["serverId"]]["welcMsg"] = 'مرحبا بك يا [user] في [server] \nعدد الاعضاء في السيرفر: [membersCount] \nالداعي: [inviter] \nعدد الاشخاص من طرف [inviter]: [inviters]'
            DATA["welcome"][DATA["serverId"]]["leaveMsg"] = '[user] خرج من السيرفر \n عدد الاشخاص من طرف [inviter]: [inviters]'
            DATA["welcome"][DATA["serverId"]]["inviters"] = {}
            dump(assist.jsonFile, DATA)



        @app.route("/securityManagment/<string:active>/<string:onff>/<string:roleName>/<string:logChannel>/<string:some>")
        async def securityManagment(active, onff, roleName, logChannel, some):
            if not await discord.authorized:return redirect(url_for("login"))
            roles = await ipc_client.request('getRoles')
            channels = await ipc_client.request('textChannels')
            members = await ipc_client.request('getMembers')
            ALL = await ipc_client.request('getMembers')
            trustedMembers = await ipc_client.request('trustedMembers', safe=load(assist.safejson)[load(assist.jsonFile)['serverId']]['trustedIds'])
            trust = False
            msg = ''
            if active == "all":
                data = load(assist.safejson)
                trustedMember       = onff.replace('trustMember:', '')
                unTrustedMember     = roleName.replace('unTrustMember:', '')
                roleName            = logChannel.replace('activeRole:', '')
                logChannel          = some.replace('logChannel:', '')
                if roleName        != 'اختر الرتبة' and roleName != '0' :data[load(assist.jsonFile)['serverId']]['activeRole']['roleId']=roles[roleName];dump(assist.safejson, data); msg = msg + f"""\n<script>alert("تم جعل {roleName} كـ رتبة التفعيل, اي شخص لايملك هذه الرتبة لـ ثلاثة ايام سيتم طرده ");</script>\n"""
                sleep(0.5)
                if trustedMember   != 'اختر العضو': data[load(assist.jsonFile)['serverId']]['trustedIds'].append(ALL[trustedMember])  ;data[load(assist.jsonFile)['serverId']]['trustedIds']=list(set(data[load(assist.jsonFile)['serverId']]['trustedIds']));dump(assist.safejson, data); msg = msg + f"""\n<script>alert("تم الوثوق بـ {trustedMember}, البوت لن يقوم بفعل اي شيء له!");</script>\n"""
                sleep(0.5)
                if unTrustedMember != 'اختر العضو': data[load(assist.jsonFile)['serverId']]['trustedIds'].remove(trustedMembers[unTrustedMember]);data[load(assist.jsonFile)['serverId']]['trustedIds']=list(set(data[load(assist.jsonFile)['serverId']]['trustedIds']));dump(assist.safejson, data); msg = msg + f"""\n<script>alert("تم إزالة {unTrustedMember} من قائمة الموثوقين!");</script>\n"""
                sleep(0.5)
                if logChannel      != '0' and logChannel != 'اختر القناة':d = load(assist.jsonFile);d['logChannelId'] = channels[logChannel];dump(assist.jsonFile, d); msg = msg + f"""\n<script>alert("تم جعل {logChannel} كـ قناة الـ log");</script>\n""" 


            elif active == "logChannel":
                if some != '0' and some != 'اختر القناة':d = load(assist.jsonFile);d['logChannelId'] = channels[some];dump(assist.jsonFile, d); msg = msg + f"""\n<script>alert("تم جعل {some} كـ قناة الـ log");</script>\n""" 

            elif active == "roleAndLog":
                data = load(assist.safejson)
                roleName = roleName.replace('activeRole:', '')
                logChannel = logChannel.replace('logChannel:', '')
                if roleName != 'اختر الرتبة' and roleName != '0' and roleName :data[load(assist.jsonFile)['serverId']]['activeRole']['roleId']=roles[roleName];dump(assist.safejson, data); msg = msg + f"""\n<script>alert("تم جعل {roleName} كـ رتبة التفعيل, اي شخص لايملك هذه الرتبة لـ ثلاثة ايام سيتم طرده ");</script>\n"""
                if logChannel != '0' and logChannel != 'اختر القناة':d = load(assist.jsonFile);d['logChannelId'] = channels[logChannel];dump(assist.jsonFile, d); msg = msg + f"""\n<script>alert("تم جعل {logChannel} كـ قناة الـ log");</script>\n""" 
            
            elif active == 'activeRole':
                data = load(assist.safejson)
                if onff == 'on':data[load(assist.jsonFile)['serverId']]['activeRole']['active']=1;dump(assist.safejson, data)
                elif onff == 'off':data[load(assist.jsonFile)['serverId']]['activeRole']['active']=0;dump(assist.safejson, data)

            elif active == 'trustAndLog':
                data = load(assist.safejson)
                trustedMember   = roleName.replace('trustedMember:', '')
                unTrustedMember = logChannel.replace('unTrustedMember:', '')
                logChannel      = some.replace('logChannel:', '')
                if trustedMember   != 'اختر العضو': data[load(assist.jsonFile)['serverId']]['trustedIds'].append(ALL[trustedMember])  ;data[load(assist.jsonFile)['serverId']]['trustedIds']=list(set(data[load(assist.jsonFile)['serverId']]['trustedIds']));dump(assist.safejson, data); msg = msg + f"""\n<script>alert("تم الوثوق بـ {trustedMember}, البوت لن يقوم بفعل اي شيء له!");</script>\n"""
                if unTrustedMember != 'اختر العضو': data[load(assist.jsonFile)['serverId']]['trustedIds'].remove(trustedMembers[unTrustedMember]);data[load(assist.jsonFile)['serverId']]['trustedIds']=list(set(data[load(assist.jsonFile)['serverId']]['trustedIds']));dump(assist.safejson, data); msg = msg + f"""\n<script>alert("تم إزالة {unTrustedMember} من قائمة الموثوقين!");</script>\n"""
                if logChannel != '0' and logChannel != 'اختر القناة':d = load(assist.jsonFile);d['logChannelId'] = channels[logChannel];dump(assist.jsonFile, d); msg = msg + f"""\n<script>alert("تم جعل {logChannel} كـ قناة الـ log");</script>\n""" 

            elif active == "trust" :
                if onff == "on" and roleName =="0" and logChannel == "0":trust = True

            memberss = []
            for mmbr in ALL.keys():
                if ALL[mmbr] not in load(assist.safejson)[load(assist.jsonFile)['serverId']]['trustedIds']:memberss.append(mmbr)

            data = True if load(assist.safejson)[load(assist.jsonFile)['serverId']]['activeRole']['active']==1  else False
            return await render_template("securityManagment.html", trusted=data, roles=roles, channels=channels, members=memberss, trust=trust, trustedMembers=trustedMembers) + msg
        
