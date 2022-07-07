from pydoc import describe
import assist
import datetime
import discord
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


async def onMemberJoin(member, client, logChannelId):
    at = member.created_at
    year = at.year
    month = at.month
    day = at.day
    now = datetime.datetime.now()
    mday = now.day
    d = mday-3
    if d <= 0:
        d = 30 + d
    lst = []
    nday = int(day)+1

    while nday > d:
        lst.append(d)
        d+=1

    try:
        if year == now.year and month == now.month and day in lst:
            kickEmbed = discord.Embed(title=f':warning:تم طردك من السيرفر:warning:', description=f'لان حسابك وهمي و جديد', color=assist.embedColors.red)
            kickEmbed.set_author(name='mzooz security bot', icon_url=client.user.avatar.url, url=assist.mzo0zServer)
            kickEmbed.timestamp = datetime.datetime.now()
            kickEmbed.set_footer(text=f'{member.guild.name}', icon_url=client.user.avatar.url)
            await member.send(embed=kickEmbed)
            await member.kick(reason='حساب وهمي')
        else:
            users = load(assist.safejson)
            users[str(member.guild.id)]["users"][member.id] = 0
            dump(assist.safejson, users)
    except:pass

def createLog(log, guild, type=None):
    if log.action == discord.AuditLogAction.channel_delete:
        if str(type).lower() == 'text':
            msg = ""
            beforeNSFW = f"{log.changes.before.nsfw}"
            beforeSlowmode = f"{log.changes.before.slowmode_delay}"

            beforeRoles = {}
            for role in log.changes.before.overwrites:
                role = discord.utils.get(guild.roles, id=role[0].id)
                beforeRoles.update({role.name: {}})
                for permission in role.permissions:beforeRoles[role.name][permission[0]]=permission[1]
            
            msg = msg + f"""channel name:{log.changes.before.name}\ntype: {log.changes.before.type}\nNSFW : {beforeNSFW}\nslowmode: {beforeSlowmode}\nصلاحيات الرتب:"""

            for role in beforeRoles:
                msg += f"\n\n\n==============={role}==============="
                for i in beforeRoles[role]:
                    if beforeRoles[role][i] == True:msg += f"\n{i} ✅"
                    if beforeRoles[role][i] == False:msg += f"\n{i} ❌"
            return msg

        if str(type).lower() == 'voice':
            msg = ""
            beforeRoles = {}
            for role in log.changes.before.overwrites:
                role = discord.utils.get(guild.roles, id=role[0].id)
                beforeRoles.update({role.name: {}})
                for permission in role.permissions:beforeRoles[role.name][permission[0]]=permission[1]
            
            msg = msg + f"""channel name:{log.changes.before.name}\ntype: {log.changes.before.type}\nbitrate : {log.changes.before.bitrate}\nuser_limit: {log.changes.before.user_limit}\n\nصلاحيات الرتب:"""

            for role in beforeRoles:
                msg += f"\n\n\n==============={role}==============="
                for i in beforeRoles[role]:
                    if beforeRoles[role][i] == True:
                        msg += f"\n{i} ✅"
                    if beforeRoles[role][i] == False:
                        msg += f"\n{i} ❌"
            return msg

    if log.action == discord.AuditLogAction.channel_create:
        if str(type).lower() == 'text':
            msg = ""
            NSFW = f"{log.changes.after.nsfw}"
            Slowmode = f"{log.changes.after.slowmode_delay}"

            Roles = {}
            for role in log.changes.after.overwrites:
                role = discord.utils.get(guild.roles, id=role[0].id)
                Roles.update({role.name: {}})
                for permission in role.permissions:Roles[role.name][permission[0]]=permission[1]
            
            msg = msg + f"""channel name:{log.changes.after.name}\ntype: {log.changes.after.type}\nNSFW : {NSFW}\nslowmode: {Slowmode}\nصلاحيات الرتب:"""

            for role in Roles:
                msg += f"\n\n\n==============={role}==============="
                for i in Roles[role]:
                    if Roles[role][i] == True:
                        msg += f"\n{i} ✅"
                    if Roles[role][i] == False:
                        msg += f"\n{i} ❌"
            return msg

        if str(type).lower() == 'voice':
            msg = ""
            Roles = {}
            for role in log.changes.after.overwrites:
                role = discord.utils.get(guild.roles, id=role[0].id)
                Roles.update({role.name: {}})
                for permission in role.permissions:Roles[role.name][permission[0]]=permission[1]
            
            msg = msg + f"""channel name:{log.changes.after.name}\ntype: {log.changes.after.type}\nbitrate : {log.changes.after.bitrate}\nuser_limit: {log.changes.after.user_limit}\n\nصلاحيات الرتب:"""

            for role in Roles:
                msg += f"\n\n\n==============={role}==============="
                for i in Roles[role]:
                    if Roles[role][i] == True:
                        msg += f"\n{i} ✅"
                    if Roles[role][i] == False:
                        msg += f"\n{i} ❌"
            return msg

    if log.action == discord.AuditLogAction.role_delete:
        perms = {}
        name = f"{log.changes.before.name}"
        color = f"{log.changes.before.color}"
        hoist = f"{log.changes.before.hoist}"
        mentionable = f"{log.changes.before.mentionable}"

        perms.update({log.changes.before.name: {}})
        for permission in log.changes.before.permissions:perms[log.changes.before.name][permission[0]]=permission[1]
        msg = f"""اسم الرتبة: {name}\nلون الرتبة:{color}\nموجودة في قائمة الرتب:{hoist}\nقابلة للمنشن:{mentionable}\nصلاحيات الرتبة:"""
        msg += f"\n==============={log.changes.before.name}==============="
        for i in perms[log.changes.before.name]:
            if perms[log.changes.before.name][i] == True:msg += f"\n{i} ✅"
            if perms[log.changes.before.name][i] == False:msg += f"\n{i} ❌"
        return msg

    if log.action == discord.AuditLogAction.role_create:
        perms = {}
        name = f"{log.changes.after.name}"
        color = f"{log.changes.after.color}"
        hoist = f"{log.changes.after.hoist}"
        mentionable = f"{log.changes.after.mentionable}"

        perms.update({log.changes.after.name: {}})
        for permission in log.changes.after.permissions:perms[log.changes.after.name][permission[0]]=permission[1]
        msg = f"""اسم الرتبة: {name}\nلون الرتبة:{color}\nموجودة في قائمة الرتب:{hoist}\nقابلة للمنشن:{mentionable}\nصلاحيات الرتبة:"""
        msg += f"\n==============={log.changes.after.name}==============="
        for i in perms[log.changes.after.name]:
            if perms[log.changes.after.name][i] == True:msg += f"\n{i} ✅"
            if perms[log.changes.after.name][i] == False:msg += f"\n{i} ❌"
        return msg

