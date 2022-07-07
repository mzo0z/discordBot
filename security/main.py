import discord
import datetime
import assist
import json
import os
import io
from discord.ext import tasks
from . import safeSystem

def load(file):
    with open(file, 'r') as f:
        DATA = json.load(f)
    return DATA

def dump(file, DATA):
    with open(file, 'w') as f:
        json.dump(DATA, f)
        f.close()
    return

logs = []
ids = {}

class start:
    def __init__(self, client, guild):
        if not os.path.exists(assist.safejson):dump(assist.safejson, {});gg = load(assist.safejson);gg[str(guild.id)]={};gg[str(guild.id)]["trustedIds"] = [];gg[str(guild.id)]["users"]={};gg[str(guild.id)]["activeRole"]={};gg[str(guild.id)]["activeRole"]["roleId"]=0;gg[str(guild.id)]["activeRole"]["active"]=0;gg[str(guild.id)]["trustedIds"].append(client.user.id);gg[str(guild.id)]["trustedIds"].append(guild.owner.id);dump(assist.safejson, gg)
        try:self.safing.start(client, guild)
        except:pass
        try:self.checking.start(client, guild, load(assist.jsonFile)["logChannelId"])
        except:pass
        try:self.rstrt.start()
        except:pass
        @client.listen('on_member_join')
        async def securityOnMemberJoin(member):await safeSystem.onMemberJoin(member, client, load(assist.jsonFile)["logChannelId"])


    @tasks.loop(seconds=0.1)
    async def safing(self, client, guild):
        async for Log in guild.audit_logs(limit=1):
            if Log not in logs:
                logs.append(Log)
                await self.check_log(guild, Log, client)

    @tasks.loop(seconds=0.1)
    async def checking(self, client, guild, logChannelId):
        if load(assist.safejson)[str(guild.id)]["activeRole"]["active"] == 1:
            try:
                users = load(assist.safejson)
                for userid in users[str(guild.id)]["users"]:
                    if users[str(guild.id)]["users"][str(userid)] >= 3:
                        member = await client.fetch_user(int(userid))
                        kickEmbed = discord.Embed(title=f':warning:تم طردك من السيرفر:warning:', description=f'لانك في السيرفر لثلاثة ايام ولم تفعل نفسك', color=assist.embedColors.red)
                        kickEmbed.set_author(name='mzooz security bot', icon_url=client.user.avatar.url, url=assist.mzo0zServer)
                        kickEmbed.timestamp = datetime.datetime.now()
                        kickEmbed.set_footer(text=f'{guild.name}', icon_url=client.user.avatar.url)
                        await member.send(embed=kickEmbed)

                        try:
                            channel = await client.fetch_channel(int(logChannelId))
                            joinEmbed = discord.Embed(title=f'mzooz security', description=f'تم طرد {member} لانه في السيرفر لثلاثة ايام ولم يفعل نفسه', color=assist.embedColors.red)
                            joinEmbed.set_author(name='mzooz bot', icon_url=client.user.avatar.url, url=assist.mzo0zServer)
                            joinEmbed.timestamp = datetime.datetime.now()
                            joinEmbed.set_footer(text=f'{guild.name}', icon_url=client.user.avatar.url)
                            for user in guild.members:
                                if user == member:await user.kick()
                            await channel.send(embed=joinEmbed)
                            del users[str(guild.id)]["users"][str(userid)]
                            dump(assist.safejson, users)
                        except:
                            joinEmbed = discord.Embed(title=f'mzooz security', description=f'لااستطيع طرد هذا الشخص {member}, لماذا اريد طرده؟ لأنه في السيرفر لثلاثة ايام ولم يفعل نفسه!', color=assist.embedColors.red)
                            joinEmbed.set_author(name='mzooz bot', icon_url=client.user.avatar.url, url=assist.mzo0zServer)
                            joinEmbed.timestamp = datetime.datetime.now()
                            joinEmbed.set_footer(text=f'{guild.name}', icon_url=client.user.avatar.url)
                            channel = await client.fetch_channel(int(logChannelId))
                            users[str(guild.id)]["users"][str(userid)] = 0
                            dump(assist.safejson, users)
                            await channel.send(embed=joinEmbed)


                    if datetime.datetime.now().hour == 00 and datetime.datetime.now().minute == 00:
                        user = await client.fetch_user(userid)
                        for member in guild.members:
                            if member == user:
                                if discord.utils.get(guild.roles, id=int(load(assist.safejson)[str(guild.id)]["activeRole"]["roleId"])) not in member.roles:
                                    users = load(assist.safejson)
                                    users[str(guild.id)]["users"][str(userid)] = users[str(guild.id)]["users"][str(userid)]+1
                                    dump(assist.safejson, users)
            except:pass

    @tasks.loop(seconds=3600)
    async def rstrt(self):
        for id in ids.keys():
            ids.update({id:1})

    async def check_log(self, guild, log, client):
        action = log.action
        trustedIds = load(assist.safejson)[str(guild.id)]["trustedIds"]
        if action == discord.AuditLogAction.channel_delete:
            if log.user.bot and log.user.id not in trustedIds:await guild.kick(await client.fetch_user(int(log.user.id)), reason='محاولة تهكير السيرفر')

            await self.security(guild, log, client)
            try:channel = await client.fetch_channel(int(load(assist.jsonFile)["logChannelId"]))
            except:return
            await channel.send(file=discord.File(io.BytesIO(safeSystem.createLog(log, guild, log.changes.before.type).encode('utf-8')), filename=f"deleted_channel.log"))

        elif action == discord.AuditLogAction.channel_create:
            if log.user.bot and log.user.id not in trustedIds:await guild.kick(await client.fetch_user(int(log.user.id)), reason='محاولة تهكير السيرفر')
            await self.security(guild, log, client)
            try:channel = await client.fetch_channel(int(load(assist.jsonFile)["logChannelId"]))
            except:return
            await channel.send(file=discord.File(io.BytesIO(safeSystem.createLog(log, guild, log.changes.after.type).encode('utf-8')), filename=f"created_channel.log"))

        elif action == discord.AuditLogAction.kick:
            if log.user.bot and log.user.id not in trustedIds:await guild.kick(await client.fetch_user(int(log.user.id)), reason='محاولة تهكير السيرفر')
            await self.security(guild, log, client)
            try:channel = await client.fetch_channel(int(load(assist.jsonFile)["logChannelId"]))
            except:return
            user = log.user.mention
            target = log.target.mention
            reason = log.reason
            embed = discord.Embed(description=f"{user} طرد {target} بسبب: **{reason}**", color=assist.embedColors.red, timestamp=datetime.datetime.now())
            embed.set_author(name='mzooz security bot', icon_url=client.user.avatar.url, url=assist.mzo0zServer)
            try:embed.set_footer(text=f'{guild.name}', icon_url=guild.icon.url)
            except:embed.set_footer(text=f'{guild.name}')
            await channel.send(embed=embed)

        elif action == discord.AuditLogAction.ban:
            if log.user.bot and log.user.id not in trustedIds:await guild.kick(await client.fetch_user(int(log.user.id)), reason='محاولة تهكير السيرفر')
            await self.security(guild, log, client)

        elif action == discord.AuditLogAction.webhook_delete:
            if log.user.bot and log.user.id not in trustedIds:await guild.kick(await client.fetch_user(int(log.user.id)), reason='محاولة تهكير السيرفر')
            await self.security(guild, log, client)
            try:channel = await client.fetch_channel(int(load(assist.jsonFile)["logChannelId"]))
            except:return
            user = log.user.mention
            target = log.changes.before.name
            msg = f"{user} حذف {target} (ويب هوك في <#{log.changes.before.channel.id}>)"
            embed = discord.Embed(description=msg, color=assist.embedColors.red, timestamp=datetime.datetime.now())
            embed.set_author(name='mzooz security bot', icon_url=client.user.avatar.url, url=assist.mzo0zServer)
            try:embed.set_footer(text=f'{guild.name}', icon_url=guild.icon.url)
            except:embed.set_footer(text=f'{guild.name}')
            await channel.send(embed=embed)

        elif action == discord.AuditLogAction.role_delete:
            if log.user.bot and log.user.id not in trustedIds:await guild.kick(await client.fetch_user(int(log.user.id)), reason='محاولة تهكير السيرفر')
            await self.security(guild, log, client)
            try:channel = await client.fetch_channel(int(load(assist.jsonFile)["logChannelId"]))
            except:return
            await channel.send(file=discord.File(io.BytesIO(safeSystem.createLog(log, guild, log.changes.before).encode('utf-8')), filename=f"deleted_role.log"))

        elif action == discord.AuditLogAction.role_create:
            if log.user.bot and log.user.id not in trustedIds:await guild.kick(await client.fetch_user(int(log.user.id)), reason='محاولة تهكير السيرفر')
            await self.security(guild, log, client)

        elif action == discord.AuditLogAction.bot_add:
            if log.user.bot and log.user.id not in trustedIds:await guild.kick(await client.fetch_user(int(log.user.id)), reason='محاولة تهكير السيرفر')
            await self.security(guild, log, client)

        elif action == discord.AuditLogAction.role_update:
            if log.user.bot and log.user.id not in trustedIds:await guild.kick(await client.fetch_user(int(log.user.id)), reason='محاولة تهكير السيرفر')
            await self.security(guild, log, client)
        return 0

    async def security(self, guild, log, client):
        DATA = load(assist.safejson)
        if log.user.id not in DATA[str(guild.id)]["trustedIds"]:
            if log.user.bot:
                botToKick = await client.fetch_user(int(log.user.id))
                await guild.kick(botToKick, reason='محاولة تهكير السيرفر')
            try:channel = await client.fetch_channel(int(load(assist.jsonFile)["logChannelId"]))
            except:return
            if log.action == discord.AuditLogAction.bot_add:
                isBot = log.target.bot
                botId = log.target.id
                user = log.user.mention
                userId = log.user.id
                if isBot:
                    botToKick = await client.fetch_user(int(botId))
                    await guild.kick(botToKick, reason='محاولة تهكير السيرفر')
                    userToKick = await client.fetch_user(int(userId))
                    try:await guild.kick(userToKick, reason='محاولة تهكير السيرفر عن طريق بوت');cantKick=False # if the user had kicked then the system bot will send message says that the user has been kicked
                    except:cantKick=True # if not then we will send error message
                    if cantKick:
                        msg = f"لايمكنني طرد {user}, السبب وراء محاولة طردة: **يحاول تهكير السيرفر**"
                        embed = discord.Embed(description=msg, color=assist.embedColors.red, timestamp=datetime.datetime.now())
                        embed.set_author(name='mzooz security bot', icon_url=client.user.avatar.url, url=assist.mzo0zServer)
                        try:embed.set_footer(text=f'{guild.name}', icon_url=guild.icon.url)
                        except:embed.set_footer(text=f'{guild.name}')
                        await channel.send(embed=embed)

            if log.user.id not in ids.keys():ids.update({log.user.id:1})
            try:
                ids.update({log.user.id:ids[log.user.id]+1})
                mzo0z = await client.fetch_user(int(load(assist.jsonFile)["ownerId"]))
                infoEmbed  = discord.Embed(title=f'**security**', color=assist.embedColors.ligh_green)
                infoButton = discord.ui.View()
                infoEmbed.set_author(icon_url=client.user.avatar.url, name = 'mzooz security bot', url=assist.mzo0zServer)
                infoEmbed.add_field(name=f"you don't have permission ,\nask @{mzo0z} to allow you to edit server or you will kicked!", value=f'<@{int(load(assist.jsonFile)["ownerId"])}>', inline=True)
                infoEmbed.add_field(name=f"لاتملك صلاحية تعديل السيرفر,\nاطلب من @{mzo0z} ان يسمح لك بتعديل السيرفر او سيتم طردك!", value=f'<@{int(load(assist.jsonFile)["ownerId"])}>', inline=True)

                dissupport  = discord.ui.Button(label='support - الدعم الفني', url=str(load(assist.jsonFile)["supportUrl"]))
                infoButton.add_item(item=dissupport)

                userToKick = await client.fetch_user(log.user.id)
                await userToKick.send(f'<@{log.user.id}>', embed=infoEmbed, view=infoButton)
            except:pass

            if ids[log.user.id] == 3:
                try:
                    userToKick = await client.fetch_user(log.user.id)
                    mzo0z = await client.fetch_user(int(load(assist.jsonFile)["ownerId"]))
                    infoEmbed  = discord.Embed(title=f'**security**', color=assist.embedColors.ligh_green)
                    infoButton = discord.ui.View()
                    infoEmbed.set_author(icon_url=client.user.avatar.url, name = 'mzooz security bot', url=assist.mzo0zServer)
                    infoEmbed.add_field(name=f"you have been kicked from the server because you edit something without leaders permission!", value=f'<@{int(load(assist.jsonFile)["ownerId"])}>', inline=True)
                    infoEmbed.add_field(name=f"تم طردك من السيرفر لأنك اجريت تعديلا دون اذن الليدرز!", value=f'<@{int(load(assist.jsonFile)["ownerId"])}>', inline=True)

                    dissupport  = discord.ui.Button(label='support - الدعم الفني', url=str(load(assist.jsonFile)["supportUrl"]))
                    infoButton.add_item(item=dissupport)

                    await userToKick.send(f'<@{log.user.id}>', embed=infoEmbed, view=infoButton)
                    await guild.kick(userToKick, reason='تخطى عدد السماح بتعديل السيرفر بدون اذن')
                    ids.pop(log.user.id)
                except:pass
        return 0






