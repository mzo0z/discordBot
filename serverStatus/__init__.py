import assist
import json

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
        DATA = load(assist.jsonFile)
        if "serverStatus" not in DATA:
            DATA["serverStatus"] = {}
            DATA['serverStatus'][DATA["serverId"]] = {}
            DATA["serverStatus"][DATA["serverId"]]['active'] = 0
            DATA["serverStatus"][DATA["serverId"]]['allMembersChannelId'] = 0
            DATA["serverStatus"][DATA["serverId"]]['membersChannelId'] = 0
            DATA["serverStatus"][DATA["serverId"]]['botsChannelId'] = 0
            dump(assist.jsonFile, DATA)


        @client.listen('on_member_join')
        async def on_member_join(member):
            if DATA["serverStatus"][DATA["serverId"]]['active'] == 1:
                guild = member.guild
                allMembers = guild.member_count
                members = 0
                bots = 0
                for i in guild.members:
                    if not i.bot:members += 1
                for i in guild.members:
                    if i.bot:bots += 1
                try:allMembersChannel = await guild.fetch_channel(int(DATA["serverStatus"][DATA["serverId"]]['allMembersChannelId']))
                except:pass
                try:membersChannel = await guild.fetch_channel(int(DATA["serverStatus"][DATA["serverId"]]['membersChannelId']))
                except:pass
                try:botsChannel = await guild.fetch_channel(int(DATA["serverStatus"][DATA["serverId"]]['botsChannelId']))
                except:pass
                try:
                    if str(allMembersChannel.name) != str(allMembers):await allMembersChannel.edit(name=f"عدد الاعضاء في السيرفر: {allMembers}")
                except:pass
                try:
                    if str(membersChannel.name) != str(members):await membersChannel.edit(name=f"عدد الاعضاء في السيرفر: {members}")
                except:pass
                try:
                    if str(botsChannel.name) != str(bots):await botsChannel.edit(name=f"عدد البوتات في السيرفر: {bots}")
                except:pass

        @client.listen('on_member_remove')
        async def on_member_remove(member):
            if DATA["serverStatus"][DATA["serverId"]]['active'] == 1:
                guild = member.guild
                allMembers = guild.member_count
                members = 0
                bots = 0
                for i in guild.members:
                    if not i.bot:members += 1

                for i in guild.members:
                    if i.bot:bots += 1

                try:allMembersChannel = await guild.fetch_channel(int(DATA["serverStatus"][DATA["serverId"]]['allMembersChannelId']))
                except:pass
                try:membersChannel = await guild.fetch_channel(int(DATA["serverStatus"][DATA["serverId"]]['membersChannelId']))
                except:pass
                try:botsChannel = await guild.fetch_channel(int(DATA["serverStatus"][DATA["serverId"]]['botsChannelId']))
                except:pass
                try:
                    if str(allMembersChannel.name) != str(allMembers):await allMembersChannel.edit(name=f"عدد الاعضاء في السيرفر: {allMembers}")
                except:pass
                try:
                    if str(membersChannel.name) != str(members):await membersChannel.edit(name=f"عدد الاعضاء في السيرفر: {members}")
                except:pass
                try:
                    if str(botsChannel.name) != str(bots):await botsChannel.edit(name=f"عدد البوتات في السيرفر: {bots}")
                except:pass