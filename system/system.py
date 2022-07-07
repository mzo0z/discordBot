import discord
import assist
import json
import datetime
import requests
import random
import io

from time        import sleep
from threading   import Thread
from dhooks      import Webhook
from discord.ext import commands
from . import antiBadWords
def load(file):
    with open(file, 'r') as f:
        DATA = json.load(f)
    return DATA

def dump(file, DATA):
    with open(file, 'w') as f:
        json.dump(DATA, f)
        f.close()
    return

jsonFile        = assist.jsonFile
giveawayMembers = []
logs            = []
ids             = {}
CLOSESERVER     = False
mzoozIconReady  = False
infoEmbed       = False
stopServer      = False

def addSafeChannel():
    DATA = load(assist.jsonFile)
    if 'memes' not in DATA:DATA['memes']=[];dump(assist.jsonFile, DATA)
    if 'commands' not in DATA:
        DATA['commands'] = {}
        DATA['commands']['kick'] = ['طرد']
        DATA['commands']['ban'] = ['بان', "باند"]
        DATA['commands']['unBan'] = ["فكباند"]
        DATA['commands']['clear'] = ["مسح", "امسح"]
        DATA['commands']['role'] = ["رتبة", "رول"]
        DATA['commands']['unRole'] = ["انرول", "ازالة_رتبة"]
        DATA['commands']['lock'] = ["قفل"]
        DATA['commands']['unLock'] = ["فتح"]
        DATA['commands']['mute'] = ["ميوت", "اسكات"]
        DATA['commands']['unMute'] = ["فكميوت", "سماح"]
        dump(assist.jsonFile, DATA)



    if "autoMod" not in DATA:
        DATA["autoMod"] = {}
        DATA["autoMod"][DATA["serverId"]] = {}
        DATA["autoMod"][DATA["serverId"]]['active'] = 0
        DATA["autoMod"][DATA["serverId"]]['autoResponse'] = {'سلام عليكم':"عليكم السلام", 'السلام عليكم':'عليكم السلام'}
        DATA["autoMod"][DATA["serverId"]]['antiBadWords'] = ['تنايجو', 'مكوة', 'منيوك', 'دعاره', 'نيكني', 'بنيج', 'زنا', 'تتمقحب', 'تنايكو', 'محنتني', 'تتمديث', 'سرسري', 'طيازها', 'زب', 'لزلز', 'دعار', 'گحبة', 'انيك', 'كحبه', 'مقود', 'گحاب', 'مقاويد', 'قحاب', 'ديود', 'مصه', 'شفشفيه', 'كىىىمك', 'عاهره', 'كت', 'مجارير', 'نسويه', 'شفشفنا', 'نيج', 'شراميط', 'قحايب', 'مقحوب', 'زبي', 'تنايكوا', 'قاي', 'دخله', 'طيازه', 'تمصه', 'منيوج', 'كسك', 'كسج', 'بلبوله', 'سنبول', 'قحيب', 'مكوه', 'كحايب', 'تمص', 'نياج', 'بزغب', 'قواده', 'بنيك', 'طيزي', 'يتمنيج', 'جرار', 'تتمنيج', 'تشفشفوا', 'يعور', 'زبك', 'اكته', 'بلبولك', 'زغب', 'الديوث', 'جرارين', 'تتمنيك', 'كواد', 'قضج', 'زغبته', 'طيوز', 'لحسه', 'كحبات', 'خنيث', 'طيزه', 'كسي', 'يتشفشفون', 'تنايك', 'كسوس', 'قواد', 'نايج', 'نيجوني', 'خرا', 'الكحبه', 'شيميل', 'خنيثه', 'ديوث', 'قحبات', 'عير', 'شرموطة', 'لبق', 'قحب', 'كسمك', 'نيجني', 'سمبول', 'عاهر', 'نسويات', 'نيجيني', 'زغبني', 'شمقضي', 'تشفشف', 'انيج', 'سكس', 'نيكيني', 'التمخنث', 'قي', 'اغتصب', 'شرموطات', 'كواويد', 'زبري', 'ذكوري', 'تتمخنث', 'تمنيك', 'بطيزي', 'قواويد', 'عيرك', 'عيري', 'تمحن', 'بلبولي', 'طياز', 'محنته', 'اة', 'شرموطا', 'مقحبه', 'مكوتها', 'تنايج', 'لزبيان', 'كحاب', 'تكوتا', 'مص', 'شرموط', 'تمديث', 'مكحب', 'كلزق', 'فحل', 'يتنايكون', 'يتنايج', 'تيز', 'زق', 'منيكه', 'زبه', 'آه', 'شفشفوا', 'نياك', 'اعرصك', 'تمقحب', 'مقحب', 'الجرار', 'سمبولي', 'محنه', 'نيك', 'قض', 'ابطيزي', 'جراره', 'مقه', 'الشرمطه', 'عهر', 'يتنايجون', 'عزبي', 'منايج', 'گحبه', 'مخانيث', 'قضك', 'شفشفو', 'يتنايك', 'شفشفته', 'تتشرمط', 'تشرمط', 'ذكور', 'زاغب', 'زوبري', 'منايك', 'نسوية', 'مماحين', 'زنوه', 'مزغوب', 'يتمنيك', 'تتمحن', 'شرموطه', 'قضوض', 'التمقحب', 'عواهر', 'نايك', 'كس', 'كحيب', 'معرص', 'قحبه', 'المحقبه', 'ممحون', 'ممحونه', 'مكاوي', 'تنايجوا', 'اه', 'شفشفه', 'يتمحن', 'سنبولي', 'عاهرات', 'بلبول', 'يمحن', 'نيكوني', 'تمقود', 'مخنوث', 'القحبه', 'مطيز', 'منيجه', 'مخنث', 'زاني', 'طيز', 'عيره', 'قحبة', 'مديثه', 'متمقحب', 'اعرص', 'تمنيج', 'التشرمط', 'زبر', 'منيوجه']
        DATA["autoMod"][DATA["serverId"]]['autoUrl'] = 0
        DATA["autoMod"][DATA["serverId"]]['antiSpam'] = 0
        dump(assist.jsonFile, DATA)

    if "welcome" not in DATA:
        DATA["logChannelId"] = 0
        DATA["line"] = {}
        DATA["line"][DATA["serverId"]] = {}
        DATA["line"][DATA["serverId"]]["url"] = 'https://cdn.discordapp.com/attachments/949076504342573066/966175309873434714/mzooz.gif'
        DATA["line"][DATA["serverId"]]["autoLine"] = {}
        DATA["line"][DATA["serverId"]]["autoLine"]['active'] = 0
        DATA["line"][DATA["serverId"]]["autoLine"]['channelsId'] = []

        DATA["welcome"] = {}
        DATA["welcome"][DATA["serverId"]] = {}
        DATA["welcome"]["invites_dict"] = {}
        DATA["welcome"][DATA["serverId"]]["welcomeChannelId"] = 0
        DATA["welcome"][DATA["serverId"]]["welcomeRole"] = {}
        DATA["welcome"][DATA["serverId"]]["welcomeRole"]["active"] = 0
        DATA["welcome"][DATA["serverId"]]["welcomeRole"]["roleId"] = []
        DATA["welcome"][DATA["serverId"]]["leaveChannelId"] = 0
        DATA["welcome"][DATA["serverId"]]["welcMsg"] = 'مرحبا بك يا [user] في [server] \nعدد الاعضاء في السيرفر: [membersCount] \nالداعي: [inviter] \nعدد الاشخاص من طرف [inviter]: [inviters]'
        DATA["welcome"][DATA["serverId"]]["leaveMsg"] = '[user] خرج من السيرفر \n عدد الاشخاص من طرف [inviter]: [inviters]'
        DATA["welcome"][DATA["serverId"]]["inviters"] = {}
        dump(assist.jsonFile, DATA)
    return 0

async def LINE(ctx):
    try:await ctx.message.delete()
    except:await ctx.delete()
    DATA = load(assist.jsonFile)
    await ctx.channel.send(DATA["line"][DATA["serverId"]]["url"])


async def onMessageUpdate(ctx, a, client):
    if ctx.author.bot:return
    try:logChannel = await client.fetch_channel(int(load(assist.jsonFile)["logChannelId"]))
    except:return
    msg = f"رسالة ارسلت بواسطة {ctx.author.mention} عدلت في {ctx.channel.mention}. :pencil2:"
    embed = discord.Embed(description=msg, color=assist.embedColors.blue, timestamp=datetime.datetime.now())
    embed.set_author(name='mzooz system bot', icon_url=client.user.avatar.url, url=assist.mzo0zServer)
    try:embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar.url)
    except:embed.set_footer(text=ctx.author)
    try:embed.add_field(name=f'الرسالة القديمة', value=str(ctx.content), inline=False)
    except:pass
    try:embed.add_field(name=f'الرسالة الحديثة', value=str(a.content), inline=False)
    except:pass
    try:await logChannel.send(embed=embed)
    except:pass


async def on_member_ban(guild, user, client):
    try:logChannel = await client.fetch_channel(int(load(assist.jsonFile)["logChannelId"]))
    except:return
    msg = f"تم حظر {user.mention} :hammer:"
    embed = discord.Embed(description=msg, color=assist.embedColors.blue, timestamp=datetime.datetime.now())
    embed.set_author(name='mzooz system bot', icon_url=client.user.avatar.url, url=assist.mzo0zServer)
    try:embed.set_footer(text=guild.name, icon_url=guild.icon.url)
    except:embed.set_footer(text=guild.name)
    await logChannel.send(embed=embed)



async def on_member_unban(guild, user, client):
    try:logChannel = await client.fetch_channel(int(load(assist.jsonFile)["logChannelId"]))
    except:return
    msg = f"تم فك حظر {user.mention} :airplane_arriving:"
    embed = discord.Embed(description=msg, color=assist.embedColors.blue, timestamp=datetime.datetime.now())
    embed.set_author(name='mzooz system bot', icon_url=client.user.avatar.url, url=assist.mzo0zServer)
    try:embed.set_footer(text=guild.name, icon_url=guild.icon.url)
    except:embed.set_footer(text=guild.name)
    await logChannel.send(embed=embed)



async def onMessageDelete(ctx, client):
    try:logChannel = await client.fetch_channel(int(load(assist.jsonFile)["logChannelId"]))
    except:return
    msg = f"رسالة أرسلت بواسطة {ctx.author.mention} حذفت في {ctx.channel.mention}. :wastebasket:"
    embed = discord.Embed(description=msg, color=assist.embedColors.blue, timestamp=datetime.datetime.now())
    embed.set_author(name='mzooz system bot', icon_url=client.user.avatar.url, url=assist.mzo0zServer)
    try:embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar.url)
    except:embed.set_footer(text=ctx.author, icon_url=ctx.author.default_avatar.url)
    try:embed.add_field(name=f'الرسالة', value=str(ctx.content), inline=False)
    except:embed.add_field(name=f'لايمكن عرض الرسالة', value=f'** **', inline=False)
    try:await logChannel.send(embed=embed)
    except:await logChannel.send(embed=discord.Embed(description=f"{msg}\nلايمكن عرض الرسالة", color=assist.embedColors.red, timestamp=datetime.datetime.now()).set_author(name='mzooz system bot', icon_url=client.user.avatar.url, url=assist.mzo0zServer))

async def on_guild_channel_delete(channel, client):
    try:logChannel = await client.fetch_channel(int(load(assist.jsonFile)["logChannelId"]))
    except:return
    msg = f"تم حذف روم: `{channel.name}`"
    embed = discord.Embed(title=msg, color=assist.embedColors.blue, timestamp=datetime.datetime.now())
    embed.set_author(name='mzooz system bot', icon_url=client.user.avatar.url, url=assist.mzo0zServer)
    try:embed.set_footer(text=channel.guild.name, icon_url=channel.guild.icon.url)
    except:embed.set_footer(text=channel.guild.name)
    await logChannel.send(embed=embed)

async def on_guild_channel_create(channel, client):
    try:logChannel = await client.fetch_channel(int(load(assist.jsonFile)["logChannelId"]))
    except:return
    msg = f"تم إنشاء روم: `{channel.name}`"
    embed = discord.Embed(title=msg, color=assist.embedColors.blue, timestamp=datetime.datetime.now())
    embed.set_author(name='mzooz system bot', icon_url=client.user.avatar.url, url=assist.mzo0zServer)
    try:embed.set_footer(text=channel.guild.name, icon_url=channel.guild.icon.url)
    except:embed.set_footer(text=channel.guild.name)
    await logChannel.send(embed=embed)

async def on_guild_channel_update(before, after, client):
    try:logChannel = await client.fetch_channel(int(load(assist.jsonFile)["logChannelId"]))
    except:return
    try:
        DATA = load(assist.jsonFile)
        if before.id == int(DATA["serverStatus"][DATA["serverId"]]['allMembersChannelId']):return
        if before.id == int(DATA["serverStatus"][DATA["serverId"]]['membersChannelId']):return
        if before.id == int(DATA["serverStatus"][DATA["serverId"]]['botsChannelId']):return
    except:pass


    beforeName = f"{before.name}"
    afterName = f"{after.name}"
    if str(before.type) == "text":
        beforeTopic = f"{before.topic}"
        afterTopic = f"{after.topic}"
        beforeNSFW = f"{before.nsfw}"
        afterNSFW = f"{after.nsfw}"
        beforeSlowmode = f"{before.slowmode_delay}"
        afterSlowmode = f"{after.slowmode_delay}"
    beforeCategory = f"{before.category}"
    afterCategory = f"{after.category}"
    beforeRoles = {}
    for role in before.overwrites:
        beforeRoles.update({role.name: {}})
        for permission in role.permissions:
            beforeRoles[role.name][permission[0]]=permission[1]
    
    afterRoles = {}
    for role in after.overwrites:
        afterRoles.update({role.name: {}})
        for permission in role.permissions:
            afterRoles[role.name][permission[0]]=permission[1]

    embed = discord.Embed(title=f"تم تحديث روم: `{before.name}`", color=assist.embedColors.blue, timestamp=datetime.datetime.now())
    embed.set_author(name='mzooz system bot', icon_url=client.user.avatar.url, url=assist.mzo0zServer)
    try:embed.set_footer(text=before.guild.name, icon_url=before.guild.icon.url)
    except:embed.set_footer(text=before.guild.name)
    embed.add_field(name=f'الأسم القديم', value=beforeName)
    embed.add_field(name=f'الأسم الجديد', value=afterName)
    embed.add_field(name=f'المجموعة القديمة', value=beforeCategory)
    embed.add_field(name=f'المجموعة الجديدة', value=afterCategory)
    if str(before.type) == "text":
        embed.add_field(name=f'الموضوع القديم', value=beforeTopic)
        embed.add_field(name=f'الموضوع الجديد', value=afterTopic)
        embed.add_field(name=f'nsfw القديم', value=beforeNSFW)
        embed.add_field(name=f'nsfw الجديد', value=afterNSFW)
        embed.add_field(name=f'السرعة القديمة', value=beforeSlowmode)
        embed.add_field(name=f'السرعة الجديدة', value=afterSlowmode)

    await logChannel.send(embed=embed)
    msg = ""

    for role in beforeRoles:
        msg += f"\nصلاحيات رتبة **{role}** القديمة:"
        for i in beforeRoles[role]:
            if beforeRoles[role][i] == True:
                msg += f"\n{i} ✅"
            if beforeRoles[role][i] == False:
                msg += f"\n{i} ❌"
    await logChannel.send(file=discord.File(io.BytesIO(msg.encode('utf-8')), filename=f"oldPermissions.txt"))
    msg = ""

    for role in afterRoles:
        msg += f"\nصلاحيات رتبة **{role}** الجديدة:"
        for i in afterRoles[role]:
            if afterRoles[role][i] == True:
                msg += f"\n{i} ✅"
            if afterRoles[role][i] == False:
                msg += f"\n{i} ❌"

    await logChannel.send(file=discord.File(io.BytesIO(msg.encode('utf-8')), filename=f"newPermissions.txt"))


async def on_member_update(before, after, client):
    try:logChannel = await client.fetch_channel(int(load(assist.jsonFile)["logChannelId"]))
    except:return
    beforeNickname = f"{before.nick}"
    afterNickname = f"{after.nick}"
    beforeRoles = f"{before.roles}"
    afterRoles = f"{after.roles}"

    if beforeNickname == afterNickname:
        if beforeRoles != afterRoles:
            embed = discord.Embed(description=f"تم تحديث رولات {before.mention}. :writing_hand:", color=assist.embedColors.blue, timestamp=datetime.datetime.now())
            embed.set_author(name='mzooz system bot', icon_url=client.user.avatar.url, url=assist.mzo0zServer)
            try:embed.set_footer(text=before.name, icon_url=before.avatar.url)
            except:embed.set_footer(text=before.name, icon_url=before.default_avatar.url)
            oldRoles = [i.name for i in before.roles]
            newRoles = [i.name for i in after.roles]
            for role in after.roles:
                if role.name not in oldRoles:
                    try:embed.add_field(name=f'{role.name} ✅', value="** **", inline=False)
                    except:pass

            for role in before.roles:
                if role.name not in newRoles:
                    try:embed.add_field(name=f'{role.name} ❌', value="** **", inline=False)
                    except:pass

            try:await logChannel.send(embed=embed)
            except:pass

    if beforeNickname != afterNickname:
        embed = discord.Embed(description=f"تم تحديث الاسم المستعار لـ {before.mention}. :writing_hand:", color=assist.embedColors.blue, timestamp=datetime.datetime.now())
        embed.set_author(name='mzooz system bot', icon_url=client.user.avatar.url, url=assist.mzo0zServer)
        try:embed.set_footer(text=before.name, icon_url=before.avatar.url)
        except:embed.set_footer(text=before.name, icon_url=before.default_avatar.url)
        try:embed.add_field(name=f'الاسم القديم', value=beforeNickname)
        except:pass
        try:embed.add_field(name=f'الاسم الجديد', value=afterNickname)
        except:pass
        try:await logChannel.send(embed=embed)
        except:pass

async def on_guild_role_create(role, client):
    try:logChannel = await client.fetch_channel(int(load(assist.jsonFile)["logChannelId"]))
    except:return
    embed = discord.Embed(description=f"تم انشاء رتبة {role.mention}. :writing_hand:", color=assist.embedColors.blue, timestamp=datetime.datetime.now())
    embed.set_author(name='mzooz system bot', icon_url=client.user.avatar.url, url=assist.mzo0zServer)
    try:embed.set_footer(text=role.guild.name, icon_url=role.guild.icon.url)
    except:embed.set_footer(text=role.guild.name)
    await logChannel.send(embed=embed)

async def on_guild_role_delete(role, client):
    try:logChannel = await client.fetch_channel(int(load(assist.jsonFile)["logChannelId"]))
    except:return
    embed = discord.Embed(description=f"تم حذف رتبة {role.name}. :writing_hand:", color=assist.embedColors.blue, timestamp=datetime.datetime.now())
    embed.set_author(name='mzooz system bot', icon_url=client.user.avatar.url, url=assist.mzo0zServer) 
    try:embed.set_footer(text=role.guild.name, icon_url=role.guild.icon.url)
    except:embed.set_footer(text=role.guild.name)
    await logChannel.send(embed=embed)

async def on_guild_role_update(before, after, client):
    try:logChannel = await client.fetch_channel(int(load(assist.jsonFile)["logChannelId"]))
    except:return
    embed = discord.Embed(description=f"تم تحديث رتبة {before.mention}. :writing_hand:", color=assist.embedColors.blue, timestamp=datetime.datetime.now())
    embed.set_author(name='mzooz system bot', icon_url=client.user.avatar.url, url=assist.mzo0zServer)
    try:embed.set_footer(text=before.guild.name, icon_url=before.guild.icon.url)
    except:embed.set_footer(text=before.guild.name)
    if before.name != after.name:
        embed.add_field(name=f'الاسم القديم', value=before.name)
        embed.add_field(name=f'الاسم الجديد', value=after.name)
    if before.colour != after.colour:
        embed.add_field(name=f'اللون القديم', value=before.colour)
        embed.add_field(name=f'اللون الجديد', value=after.colour)
    if before.hoist != after.hoist:
        embed.add_field(name=f'الترفيع القديم', value=before.hoist)
        embed.add_field(name=f'الترفيع الجديد', value=after.hoist)
    if before.mentionable != after.mentionable:
        embed.add_field(name=f'المنشن القديم', value=before.mentionable)
        embed.add_field(name=f'المنشن الجديد', value=after.mentionable)
    await logChannel.send(embed=embed)

    if before.permissions != after.permissions:
        msg = ""
        beforeRoles = {}
        beforeRoles.update({before.name: {}})
        for permission in before.permissions:beforeRoles[before.name][permission[0]]=permission[1]

        for role in beforeRoles:
            msg += f"\nصلاحيات رتبة **{role}** القديمة:"
            for i in beforeRoles[role]:
                if beforeRoles[role][i] == True:
                    msg += f"\n{i} ✅"
                if beforeRoles[role][i] == False:
                    msg += f"\n{i} ❌"
        await logChannel.send(file=discord.File(io.BytesIO(msg.encode('utf-8')), filename=f"oldPermissions.txt"))

        afterRoles = {}
        afterRoles.update({after.name: {}})
        for permission in after.permissions:afterRoles[after.name][permission[0]]=permission[1]
        msg = ""

        for role in afterRoles:
            msg += f"\nصلاحيات رتبة **{role}** الجديدة:"
            for i in afterRoles[role]:
                if afterRoles[role][i] == True:
                    msg += f"\n{i} ✅"
                if afterRoles[role][i] == False:
                    msg += f"\n{i} ❌"

        await logChannel.send(file=discord.File(io.BytesIO(msg.encode('utf-8')), filename=f"newPermissions.txt"))


repeat = {}
async def onMessage(ctx, client):
    DATA = load(assist.jsonFile)
    msg = ctx.content

    if ctx.channel.id in DATA["line"][DATA["serverId"]]["autoLine"]['channelsId']:
        if ctx.author != client.user:
            if DATA["line"][DATA["serverId"]]["autoLine"]['active'] == 1:
                await ctx.channel.send(DATA["line"][DATA["serverId"]]["url"])

    if DATA["autoMod"][DATA["serverId"]]['active'] == 1:
        for key in DATA["autoMod"][DATA["serverId"]]['autoResponse'].keys():
            if ctx.author != client.user:
                if msg.startswith(key):
                    await ctx.channel.send(DATA["autoMod"][DATA["serverId"]]['autoResponse'][key])

        await antiBadWords.onMessage(ctx, client)

    if DATA["autoMod"][DATA["serverId"]]['autoUrl'] ==1:
        if ctx.author != client.user:
            if msg.startswith("http") or msg.startswith("www.") or msg.startswith("discord.gg") :
                await ctx.delete()


    if DATA["autoMod"][DATA["serverId"]]['antiSpam'] == 1:
        if ctx.author != client.user:
            if ctx.author not in repeat:
                repeat.update({ctx.author:0})
            repeat.update({ctx.author:repeat[ctx.author]+1})
            def clearSpam():
                sleep(10)
                repeat.update({ctx.author:0})
            Thread(target=clearSpam).start()
            if repeat[ctx.author] >= 5:
                try:
                    await ctx.channel.purge(after=datetime.datetime.now() - datetime.timedelta(hours=1), check = lambda x: x.author.id == ctx.author.id, oldest_first=False) #purges the channel
                    roles = [str(i.name).lower() for i in ctx.guild.roles]
                    repeat.update({ctx.author:0})
                    if 'mute' not in roles:
                        await ctx.guild.create_role(name='mute')
                    if 'mute' not in [str(i.name).lower() for i in ctx.author.roles]:
                        await ctx.channel.set_permissions(discord.utils.get(ctx.guild.roles, name='mute'), send_messages = False)
                        role = discord.utils.get(ctx.guild.roles, name="mute")
                        await ctx.author.add_roles(role)
                        embed = discord.Embed(description=f'تم إسكات {ctx.author.mention} بسبب سبام الرسائل', color=assist.embedColors.green, timestamp=datetime.datetime.now())
                        embed.set_author(name='mzooz system bot', icon_url=client.user.avatar.url, url=assist.mzo0zServer)
                        try:embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar.url)
                        except:embed.set_footer(text=ctx.author)
                        await ctx.channel.send(embed=embed)
                except:pass



async def on_invite_create(invite):
    await set_invites(invite.guild)

async def on_invite_delete(invite):
    await set_invites(invite.guild)
guild_invites = ""
async def set_invites(guild):
    guild_invites = await guild.invites()

    data = load(assist.jsonFile)
    data["welcome"]["invites_dict"][data['serverId']] = []
    for invite in guild_invites:
        data["welcome"]["invites_dict"][data['serverId']].append(tuple((invite.code, invite.uses)))
        data["welcome"]["invites_dict"][data['serverId']] = list(set(data["welcome"]["invites_dict"][data['serverId']]))
    dump(assist.jsonFile, data)

async def onMemberJoin(member, client):
    if member.bot:return
    try:channel = await client.fetch_channel(int(load(assist.jsonFile)["logChannelId"]))
    except:return
    joinEmbed = discord.Embed(description=f'{member.mention} دخل السيرفر', color=assist.embedColors.ligh_green, timestamp = datetime.datetime.now())
    joinEmbed.set_author(name='mzooz system bot', icon_url=client.user.avatar.url, url=assist.mzo0zServer)
    try:joinEmbed.set_footer(text=f'{member.guild.name}', icon_url=member.guild.icon.url)
    except:joinEmbed.set_footer(text=f'{member.guild.name}')
    await channel.send(embed=joinEmbed)
    guild_invites = await member.guild.invites()
    for invite in guild_invites:
        for invite_dict in load(assist.jsonFile)["welcome"]["invites_dict"][str(member.guild.id)]:
            if invite_dict[0] == invite.code:
                if int(invite.uses) > invite_dict[1]:
                    inviter = invite.inviter
                    DATA = load(assist.jsonFile)
                    if inviter.mention not in DATA["welcome"][DATA["serverId"]]["inviters"]:
                        DATA["welcome"][DATA["serverId"]]["inviters"][inviter.mention] = 0
                        dump(assist.jsonFile, DATA)
                    DATA = load(assist.jsonFile)
                    DATA["welcome"][DATA["serverId"]]["inviters"][inviter.mention] = DATA["welcome"][DATA["serverId"]]["inviters"][inviter.mention]+1
                    dump(assist.jsonFile, DATA)

    DATA = load(assist.jsonFile)
    inviter = inviter.mention
    member_count = str(member.guild.member_count)
    welcMsg = load(assist.jsonFile)["welcome"][str(member.guild.id)]["welcMsg"]
    try:welcMsg = welcMsg.replace("[user]", member.mention)
    except:pass
    try:welcMsg = welcMsg.replace("[server]", member.guild.name)
    except:pass
    try:welcMsg = welcMsg.replace("[membersCount]", member_count)
    except:pass
    try:welcMsg = welcMsg.replace("[inviter]", inviter)
    except:pass
    try:welcMsg = welcMsg.replace("[inviters]", str(DATA["welcome"][DATA["serverId"]]["inviters"][inviter]))
    except:pass

    if DATA["welcome"][DATA["serverId"]]["welcomeRole"]["active"] == 1:
        for id in DATA["welcome"][DATA["serverId"]]["welcomeRole"]["roleId"]:
            try:await member.add_roles(discord.utils.get(member.guild.roles, id=int(id)))
            except:pass

    try:welcChannel = await client.fetch_channel(int(load(assist.jsonFile)["welcome"][load(assist.jsonFile)["serverId"]]["welcomeChannelId"]))
    except:return
    welc = discord.Embed(description=welcMsg, timestamp = datetime.datetime.now(), color=assist.embedColors.ligh_green)
    welc.set_author(name='mzooz system bot', icon_url=client.user.avatar.url, url=assist.mzo0zServer)
    try:welc.set_footer(text=f'{member}', icon_url=member.avatar.url)
    except:welc.set_footer(text=f'{member}', icon_url=member.default_avatar.url)
    await welcChannel.send(embed=welc)


async def onMemberRemove(member, client):
    if member.bot:return
    try:
        guild_invites = await member.guild.invites()
        DATA = load(assist.jsonFile)
        for invite in guild_invites:
            for invite_dict in load(assist.jsonFile)["welcome"]["invites_dict"][str(member.guild.id)]:
                if invite_dict[0] == invite.code:
                    if int(invite.uses) > invite_dict[1]:
                        try:inviter = invite.inviter
                        except:inviter = invite.code
                        DATA["welcome"][DATA["serverId"]]["inviters"][inviter.mention] = DATA["welcome"][DATA["serverId"]]["inviters"][inviter.mention]-1
                        dump(assist.jsonFile, DATA)

        try:inviter = inviter.mention
        except:inviter = ''
        member_count = str(member.guild.member_count)
    except:pass
    try:
        welcMsg = load(assist.jsonFile)["welcome"][str(member.guild.id)]["leaveMsg"]
        try:welcMsg = welcMsg.replace("[user]", member.mention)
        except:pass
        try:welcMsg = welcMsg.replace("[server]", member.guild.name)
        except:pass
        try:welcMsg = welcMsg.replace("[membersCount]", member_count)
        except:pass
        try:welcMsg = welcMsg.replace("[inviter]", inviter)
        except:pass
        try:welcMsg = welcMsg.replace("[inviters]", str(DATA["welcome"][DATA["serverId"]]["inviters"][inviter]))
        except:pass

        try:chanel = await client.fetch_channel(int(load(assist.jsonFile)["logChannelId"]))
        except:return
        leftEmbed = discord.Embed(description=f'{member} غادر السيرفر ', color=assist.embedColors.red)
        leftEmbed.set_author(name='mzooz system bot', icon_url=client.user.avatar.url, url=assist.mzo0zServer)
        leftEmbed.timestamp = datetime.datetime.now()
        leftEmbed.set_footer(text=f'{member.guild.name}', icon_url=client.user.avatar.url)
        await chanel.send(embed=leftEmbed)

        try:leaveChannel = await client.fetch_channel(int(load(assist.jsonFile)["welcome"][load(assist.jsonFile)["serverId"]]["leaveChannelId"]))
        except:return
        leave = discord.Embed(description=welcMsg, timestamp = datetime.datetime.now(), color=assist.embedColors.red)
        leave.set_author(name='mzooz system bot', icon_url=client.user.avatar.url, url=assist.mzo0zServer)
        try:leave.set_footer(text=f'{member}', icon_url=member.avatar.url)
        except:leave.set_footer(text=f'{member}', icon_url=member.default_avatar.url)
        await leaveChannel.send(embed=leave)
    except:pass

async def addEmbed(ctx, client):
    global publicEmbedToSend
    names = []
    fg = discord.Embed(title='رابط الـ webhook', description='يجب عليك وضع رابط webhook لكي اتمكن من ارسال الـ embed  الى سيرفرك', color=assist.embedColors.ligh_green, url=assist.mzo0zServer)
    fg.set_author(name='mzooz bot', icon_url=client.user.avatar.url)
    await ctx.channel.send(embed=fg)
    def webhookCheck(m):
        msg = m.content
        if msg:
            if m.author.id == ctx.author.id:
                if m.channel.id == ctx.channel.id:
                    return ' '
    r = await client.wait_for('message', check=webhookCheck)
    webhookUrl = r.content
    if webhookUrl.startswith('https://discord.com/api/webhooks'):
        code = requests.get(webhookUrl).status_code
        if int(code) != 200:
            embed = discord.Embed(title='حدث خطأ', description=f'هذا الرابط غير فعال {webhookUrl} تأكد من الرابط واعد المحاولة', color=assist.embedColors.red, url=assist.mzo0zServer)
            embed.set_author(name='mzooz bot', icon_url=client.user.avatar.url)
            try:
                embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar.url)
            except:
                embed.set_footer(text=ctx.author, icon_url='https://cdn.discordapp.com/attachments/926554426154553354/953808639473385552/r.png')
            await ctx.channel.send(embed=embed)
        elif int(code) == 200:
            publicEmbedToSend = discord.Embed(title='(العنوان)', description='ماهو عنوان الايمبيد الذي تريده (الوصف)', color=assist.embedColors.ligh_green, timestamp=datetime.datetime.now())
            publicEmbedToSend.set_author(name='mzooz bot', icon_url=client.user.avatar.url, url=assist.mzo0zServer)
            try:publicEmbedToSend.set_footer(text=ctx.author, icon_url=ctx.author.avatar.url)
            except:publicEmbedToSend.set_footer(text=ctx.author, icon_url=ctx.author.default_avatar_url)

            await ctx.channel.send(embed=publicEmbedToSend)
            def titleCheck(m):
                msg = m.content
                if msg:
                    if m.author.id == ctx.author.id:
                        if m.channel.id == ctx.channel.id:
                            return ' '
            r = await client.wait_for('message', check=titleCheck)
            title = r.content
            publicEmbedToSend = discord.Embed(title=title, description='ماهو وصف الايمبيد الذي تريده (الوصف)', color=assist.embedColors.ligh_green, url=assist.mzo0zServer)
            publicEmbedToSend.set_author(name='mzooz bot', icon_url=client.user.avatar.url)
            try:
                publicEmbedToSend.set_footer(text=ctx.author, icon_url=ctx.author.avatar.url)
            except:
                publicEmbedToSend.set_footer(text=ctx.author, icon_url='https://cdn.discordapp.com/attachments/926554426154553354/953808639473385552/r.png')
            await ctx.channel.send(embed=publicEmbedToSend)

            def descrCheck(m):
                msg = m.content
                if msg:
                    if m.author.id == ctx.author.id:
                        if m.channel.id == ctx.channel.id:
                            return ' '
            d = await client.wait_for('message', check=descrCheck)
            describtion = d.content
            publicEmbedToSend = discord.Embed(title=title, description=describtion, color=assist.embedColors.ligh_green, url=assist.mzo0zServer)
            try:
                publicEmbedToSend.set_footer(text=ctx.author, icon_url=ctx.author.avatar.url)
            except:
                publicEmbedToSend.set_footer(text=ctx.author, icon_url='https://cdn.discordapp.com/attachments/926554426154553354/953808639473385552/r.png')
            publicEmbedToSend.set_author(name='mzooz bot', icon_url=client.user.avatar.url)

            async def addLineCallBack(interaction):
                if interaction.user.id == ctx.author.id:
                    addLine.disabled = True
                    addPhoto.disabled = True
                    createIt.disabled = True
                    addThumb.disabled = True
                    canceleIt.disabled = True
                    global publicEmbedToSend
                    dd = discord.Embed(title=title, description=describtion, color=assist.embedColors.ligh_green, url=assist.mzo0zServer)
                    try:dd.set_footer(text=ctx.author, icon_url=ctx.author.avatar.url)
                    except:dd.set_footer(text=ctx.author, icon_url='https://cdn.discordapp.com/attachments/926554426154553354/953808639473385552/r.png')
                    dd.set_author(name='mzooz bot', icon_url=client.user.avatar.url)
                    dd.add_field(name='(الاسم)', value='ماهو الاسم الذي تريد وضعة (القيمة)')
                    await interaction.response.edit_message(embed=dd, view=embedView)

                    def fieldCheck(m):
                        msg = m.content
                        if msg:
                            if m.author.id == ctx.author.id:
                                if m.channel.id == ctx.channel.id:
                                    return ' '
                    d = await client.wait_for('message', check=fieldCheck)
                    fieldName = d.content
                    names.append(fieldName)
                    await d.delete()
                    dd = discord.Embed(title=title, description=describtion, color=assist.embedColors.ligh_green, url=assist.mzo0zServer)
                    try:
                        dd.set_footer(text=ctx.author, icon_url=ctx.author.avatar.url)
                    except:
                        dd.set_footer(text=ctx.author, icon_url='https://cdn.discordapp.com/attachments/926554426154553354/953808639473385552/r.png')
                    dd.set_author(name='mzooz bot', icon_url=client.user.avatar.url)
                    dd.add_field(name=fieldName, value='ماهي القيمةالتي تريد وضعها (القيمة)')
                    await interaction.message.edit(embed=dd)
                    def valueCheck(m):
                        msg = m.content
                        if msg:
                            if m.author.id == ctx.author.id:
                                if m.channel.id == ctx.channel.id:
                                    return ' '
                    d = await client.wait_for('message', check=valueCheck)
                    valueName = d.content
                    await d.delete()
                    publicEmbedToSend.add_field(name=fieldName, value=valueName, inline=False)
                    addLine.disabled = False
                    addPhoto.disabled = False
                    createIt.disabled = False
                    addThumb.disabled = False
                    canceleIt.disabled = False
                    await interaction.message.edit(embed=publicEmbedToSend, view=embedView)


            async def addPhotoCallBack(interaction):
                if interaction.user.id == ctx.author.id:
                    addLine.disabled = True
                    addPhoto.disabled = True
                    createIt.disabled = True
                    addThumb.disabled = True
                    canceleIt.disabled = True
                    global publicEmbedToSend
                    dd = discord.Embed(title=title, description=describtion, color=assist.embedColors.ligh_green, url=assist.mzo0zServer)
                    try:dd.set_footer(text=ctx.author, icon_url=ctx.author.avatar.url)
                    except:dd.set_footer(text=ctx.author, icon_url=ctx.author_default_avatar.url)
                    dd.set_author(name='mzooz bot', icon_url=client.user.avatar.url)
                    dd.add_field(name='ارسل رابط الصورة', value='** **')
                    await interaction.message.edit(embed=dd, view=embedView)
                    def photoCheck(m):
                        msg = m.content
                        if msg:
                            if m.author.id == ctx.author.id:
                                if m.channel.id == ctx.channel.id:
                                    return ' '
                    d = await client.wait_for('message', check=photoCheck)
                    photoUrl = d.content
                    await d.delete()
                    try:
                        code = requests.get(photoUrl).status_code
                    except:
                        code = 404
                    if code !=200:
                        embed = discord.Embed(title='حدث خطأ', description=f'هذا الرابط غير فعال {photoUrl} تأكد من الرابط واعد المحاولة', color=assist.embedColors.red, url=assist.mzo0zServer)
                        embed.set_author(name='mzooz bot', icon_url=client.user.avatar.url)
                        try:
                            embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar.url)
                        except:
                            embed.set_footer(text=ctx.author, icon_url='https://cdn.discordapp.com/attachments/926554426154553354/953808639473385552/r.png')
                        await ctx.channel.send(embed=embed, delete_after=3)
                    else:
                        publicEmbedToSend.set_image(url=photoUrl)
                        await interaction.message.edit(embed=publicEmbedToSend, view=embedView)
                    addLine.disabled = False
                    addPhoto.disabled = False
                    createIt.disabled = False
                    addThumb.disabled = False
                    canceleIt.disabled = False
                    await interaction.message.edit(embed=publicEmbedToSend, view=embedView)


            async def createItCallBack(interaction):
                if interaction.user.id == ctx.author.id:
                    global publicEmbedToSend
                    await interaction.message.delete()
                    Webhook(webhookUrl).send(username='mzooz bot', avatar_url=client.user.avatar.url, embed=publicEmbedToSend, content='@everyone')
                    embed = discord.Embed(title='نجحت', description=f'تم إرسال الـ webhook بنجاح', color=assist.embedColors.green, url=assist.mzo0zServer)
                    embed.set_author(name='mzooz bot', icon_url=client.user.avatar.url)
                    try:embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar.url)
                    except:embed.set_footer(text=ctx.author, icon_url=ctx.author_default_avatar.url)
                    await interaction.response.send_message(embed=embed)

            async def addThumbCallBack(interaction):
                if interaction.user.id == ctx.author.id:
                    addLine.disabled = True
                    addPhoto.disabled = True
                    createIt.disabled = True
                    addThumb.disabled = True
                    canceleIt.disabled = True
                    global publicEmbedToSend
                    global em
                    dd = discord.Embed(title=title, description=describtion, color=assist.embedColors.ligh_green)
                    try:dd.set_footer(text=ctx.author, icon_url=ctx.author.avatar.url)
                    except:dd.set_footer(text=ctx.author, icon_url=ctx.author_default_avatar.url)
                    dd.set_author(name='mzooz bot', icon_url=client.user.avatar.url, url=assist.mzo0zServer)
                    dd.add_field(name='ارسل رابط الثامنيل', value='** **')
                    await interaction.message.edit(embed=dd, view=embedView)
                    def photoCheck(m):
                        msg = m.content
                        if msg:
                            if m.author.id == ctx.author.id:
                                if m.channel.id == ctx.channel.id:
                                    return ' '
                    d = await client.wait_for('message', check=photoCheck)
                    photoUrl = d.content
                    await d.delete()
                    try:code = requests.get(photoUrl).status_code
                    except:code = 404
                    if code !=200:
                        embed = discord.Embed(title='حدث خطأ', description=f'هذا الرابط غير فعال {photoUrl} تأكد من الرابط واعد المحاولة', color=assist.embedColors.red)
                        embed.set_author(name='mzooz bot', icon_url=client.user.avatar.url, url=assist.mzo0zServer)
                        try:embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar.url)
                        except:embed.set_footer(text=ctx.author, icon_url=ctx.author_default_avatar.url)
                        await ctx.channel.send(embed=embed, delete_after=3)
                    else:
                        publicEmbedToSend.set_thumbnail(url=photoUrl)
                        await interaction.message.edit(embed=publicEmbedToSend, view=embedView)
                    addLine.disabled = False
                    addPhoto.disabled = False
                    createIt.disabled = False
                    addThumb.disabled = False
                    canceleIt.disabled = False
                    await interaction.message.edit(embed=publicEmbedToSend, view=embedView)

            async def canceleItCallBack(interaction):
                if interaction.user.id == ctx.author.id:
                    dd = discord.Embed(title='إلغاء', description='تم الغاء التيكت', color=assist.embedColors.red)
                    try:dd.set_footer(text=ctx.author, icon_url=ctx.author.avatar.url)
                    except:dd.set_footer(text=ctx.author, icon_url=assist.mzo0zServer)
                    dd.timestamp = datetime.datetime.now()
                    dd.set_author(name='mzooz bot', icon_url=client.user.avatar.url, url=assist.mzo0zServer)
                    await interaction.message.edit(embed=dd, view=None, delete_after=3)


            embedView = discord.ui.View()
            addLine = discord.ui.Button(style=discord.ButtonStyle.blurple, label='اضف سطر جديد', row=0)
            addLine.callback = addLineCallBack
            embedView.add_item(addLine)


            addPhoto = discord.ui.Button(style=discord.ButtonStyle.green, label='اضف صورة', row=0)
            addPhoto.callback = addPhotoCallBack
            embedView.add_item(addPhoto)


            createIt = discord.ui.Button(style=discord.ButtonStyle.blurple, label='إنشاء', row=1)
            createIt.callback = createItCallBack
            embedView.add_item(createIt)

            addThumb = discord.ui.Button(style=discord.ButtonStyle.green, label='اضف ثامنيل', row=1)
            addThumb.callback = addThumbCallBack
            embedView.add_item(addThumb)

            canceleIt = discord.ui.Button(style=discord.ButtonStyle.red, label='إلغاء', row=1)
            canceleIt.callback = canceleItCallBack
            embedView.add_item(canceleIt)

            await ctx.channel.send(embed=publicEmbedToSend, view=embedView)

async def png(ctx, client):
    if round(client.latency * 1000) <= 50:embed=discord.Embed(title="PING", description=f":ping_pong:  The ping is **{round(client.latency *1000)}**ms!", color=0x44ff44)
    elif round(client.latency * 1000) <= 100:embed=discord.Embed(title="PING", description=f":ping_pong:  The ping is **{round(client.latency *1000)}**ms!", color=0xffd000)
    elif round(client.latency * 1000) <= 200:embed=discord.Embed(title="PING", description=f":ping_pong:  The ping is **{round(client.latency *1000)}**ms!", color=0xff6600)
    else:embed=discord.Embed(title="PING", description=f":ping_pong:  The ping is **{round(client.latency *1000)}**ms!", color=0x990000, url=assist.mzo0zServer)
    try:embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar.url)
    except:embed.set_footer(text=ctx.author, icon_url=ctx.author.default_avatar.url)
    embed.set_author(icon_url=client.user.avatar.url, name = 'mzooz system bot', url=assist.mzo0zServer)
    await ctx.channel.send(embed=embed)

async def Roll(ctx, client):
    nums = [1, 2, 3, 4, 5, 6]
    roll = random.choice(nums)
    embed=discord.Embed(title=f"لقد حصلت على {roll}!", color=assist.embedColors.green, url=assist.mzo0zServer)
    try:embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar.url)
    except:embed.set_footer(text=ctx.author, icon_url=ctx.author.default_avatar.url)
    embed.set_author(icon_url=client.user.avatar.url, name = 'mzooz bot')
    await ctx.channel.send(embed=embed)

async def ROLES(ctx, client):
    embed=discord.Embed(title=f"{ctx.guild.name}", color=assist.embedColors.green)
    try:embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar.url)
    except:embed.set_footer(text=ctx.author, icon_url=ctx.author.default_avatar.url)
    embed.set_author(icon_url=client.user.avatar.url, name = 'mzooz system bot', url=assist.mzo0zServer)
    roles = ctx.guild.roles
    members = ctx.guild.members
    nums = 0
    maxF = 25
    sended = True
    for role in roles[::-1]:
        count = 0
        for member in members:
            if role in member.roles:
                count += 1
        if nums <= maxF:
            embed.add_field(name=f"{role}   {count}", value="** **", inline=False)
            nums +=1
            if nums >= maxF:
                maxF = maxF + 25
                await ctx.channel.send(embed=embed)
                embed=discord.Embed(description="** **", color=assist.embedColors.green)
                sended = False

    if sended:await ctx.channel.send(embed=embed)


async def ROOMS(ctx, client):
    guild = ctx.guild
    channels = [i for i in guild.channels]
    categorys = [channel for channel in channels if channel.type == discord.ChannelType.category]
    texts = [channel for channel in channels if channel.type == discord.ChannelType.text]
    voices = [channel for channel in channels if channel.type == discord.ChannelType.voice]
    embed = discord.Embed(title=f"{ctx.guild.name}", color=assist.embedColors.blurple, timestamp=datetime.datetime.now())
    try:embed.set_footer(text=f'{ctx.author}', icon_url=ctx.author.avatar.url)
    except:embed.set_footer(text=f'{ctx.author}', icon_url=ctx.author.default_avatar.url)
    embed.set_author(icon_url=client.user.avatar.url, name = 'mzooz system bot', url=assist.mzo0zServer)

    nums = 0
    maxF = 25
    sended = True
    for category in categorys:
        if nums <= maxF:
            embed.add_field(name=f"{category}  >مجموعة<", value="** **", inline=False)
            nums +=1
            if nums >= maxF:
                maxF = maxF + 25
                await ctx.channel.send(embed=embed)
                embed=discord.Embed(description="** **", color=assist.embedColors.blurple)
                sended = False

    for text in texts:
        if nums <= maxF:
            embed.add_field(name=f"{text}  >كتابي<", value="** **", inline=False)
            nums +=1
            if nums >= maxF:
                maxF = maxF + 25
                await ctx.channel.send(embed=embed)
                embed=discord.Embed(description="** **", color=assist.embedColors.blurple)
                sended = False

    for voice in voices:
        if nums <= maxF:
            embed.add_field(name=f"{voice}  >صوتي<", value="** **", inline=False)
            nums +=1
            if nums >= maxF:
                maxF = maxF + 25
                await ctx.channel.send(embed=embed)
                embed=discord.Embed(description="** **", color=assist.embedColors.blurple)
                sended = False

    if sended:await ctx.channel.send(embed=embed)


async def SERVER(ctx, client):
    prefix  = load(assist.jsonFile)["prefix"]
    guild   = client.get_guild(int(load(assist.jsonFile)["serverId"]))
    chns    = discord.Embed(title=f"{guild.name}", description='معلومات السيرفر', color=assist.embedColors.blurple, url=assist.mzo0zServer)
    created = guild.created_at
    year    = created.year
    month   = created.month
    day     = created.day
    created = f"{year}-{month}-{day}"
    members = guild.member_count
    id      = guild.id
    owend   = guild.owner
    chanels = len(guild.channels)
    voice   = len(guild.voice_channels)
    text    = len(guild.text_channels)
    verifi  = guild.verification_level.value
    roles   = len(guild.roles)
    try:
        chns.set_thumbnail(url=guild.icon.url)
    except:
        pass

    chns.add_field(name=f':date: انشأ في:', value=created, inline=True)
    chns.add_field(name=f':busts_in_silhouette: عدد الاعضاء:', value=f'{members}', inline=True)
    chns.add_field(name=f':id: اي دي السيرفر:', value=id, inline=True)
    chns.add_field(name=f':crown: مالك السيرفر:', value=owend.mention, inline=True)
    chns.add_field(name=f':speech_balloon: عدد الرومات: {chanels}', value=f"صوتي: {voice}\nكتابي: {text}", inline=True)
    chns.add_field(name=f':police_officer: مستوى الحماية:', value=verifi, inline=True)
    chns.add_field(name=f'عدد الرتب: {roles}', value=f'لإظهار جميع الرتب {prefix}roles', inline=True)
    await ctx.channel.send(embed=chns)

async def Avatar(ctx, client, user):
    if user == None:
        embed = discord.Embed(title=f'{ctx.author} avatar', color=assist.embedColors.blue, url=assist.mzo0zServer)
        embed.set_author(name='mzooz bot', icon_url=client.user.avatar.url)
        try:
            embed.set_image(url=ctx.author.avatar.url)
            embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar.url)
        except:
            embed.set_image(url='https://discord.com/assets/6f26ddd1bf59740c536d2274bb834a05.png')
            embed.set_footer(text=ctx.author, icon_url='https://discord.com/assets/6f26ddd1bf59740c536d2274bb834a05.png')
        await ctx.channel.send(embed=embed)

    else:
        try:
            embed = discord.Embed(title=f'{user} avatar', color=assist.embedColors.blue, url=assist.mzo0zServer)
            embed.set_author(name='mzooz bot', icon_url=client.user.avatar.url)
            try:
                embed.set_image(url=user.avatar.url)
            except:
                embed.set_image(url='https://discord.com/assets/6f26ddd1bf59740c536d2274bb834a05.png')

            try:
                embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar.url)
            except:
                embed.set_footer(text=ctx.author, icon_url='https://discord.com/assets/6f26ddd1bf59740c536d2274bb834a05.png')

            await ctx.channel.send(embed=embed)

        except commands.errors.MemberNotFound:
            embed = discord.Embed(title=f'{user} avatar', color=assist.embedColors.blue, url=assist.mzo0zServer)
            embed.add_field(name='**حدث خطأ**', value=f'**لايمكنني الحصول على افتار هذا الشخص {user} تأكد من الاسم و اعد المحاولة**')
            embed.set_author(name='mzooz bot', icon_url=client.user.avatar.url)
            try:
                avatar = ctx.author.avatar.url
            except:
                avatar = client.user.avatar.url
            embed.set_footer(text=ctx.author, icon_url=avatar)

            await ctx.channel.send(embed=embed)
            return

async def User(ctx, client, user):
    if user == None:
        embed = discord.Embed(title=f'معلومات {ctx.author}', color=assist.embedColors.dark_green, url=assist.mzo0zServer)
        author = ctx.author
        created = ctx.author.created_at
        year = created.year
        month = created.month
        day = created.day
        created = f'{year}-{month}-{day}'
        joinAt = ctx.author.joined_at
        year = joinAt.year
        month = joinAt.month
        day = joinAt.day
        joinAt = f'{year}-{month}-{day}'
        embed.add_field(name='تاريخ إنشاء الحساب:', value=created)
        embed.add_field(name='اي دي الحساب:', value=ctx.author.id, inline=False)
        embed.add_field(name='تاريخ دخول السيرفر:', value=joinAt)
        embed.set_author(name='mzooz bot', icon_url=client.user.avatar.url)

        try:
            embed.set_thumbnail(url=ctx.author.avatar.url)
            embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar.url)
        except:
            embed.set_footer(text=ctx.author, icon_url='https://discord.com/assets/6f26ddd1bf59740c536d2274bb834a05.png')

        await ctx.channel.send(embed=embed)
    else:
        embed = discord.Embed(title=f'معلومات {user}', color=assist.embedColors.dark_green, url=assist.mzo0zServer)
        created = user.created_at
        year = created.year
        month = created.month
        day = created.day
        created = f'{year}-{month}-{day}'
        joinAt = user.joined_at
        year = joinAt.year
        month = joinAt.month
        day = joinAt.day
        joinAt = f'{year}-{month}-{day}'
        embed.add_field(name='تاريخ إنشاء الحساب:', value=created)
        embed.add_field(name='اي دي الحساب:', value=user.id, inline=False)
        embed.add_field(name='تاريخ دخول السيرفر:', value=joinAt)
        embed.set_author(name='mzooz bot', icon_url=client.user.avatar.url)
        try:
            embed.set_thumbnail(url=user.avatar.url)
            embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar.url)
        except:
            embed.set_footer(text=ctx.author, icon_url='https://discord.com/assets/6f26ddd1bf59740c536d2274bb834a05.png')

        await ctx.channel.send(embed=embed)

async def Remove(ctx, client, user):
    if user != None:
        with open(assist.gamesjson, 'r') as f:
            game = json.load(f)
        try:
            del game[str(ctx.guild.id)][str(user)]
            with open(assist.gamesjson, 'w') as ff:
                json.dump(game, ff)
                ff.close()
            await ctx.channel.send(embed=discord.Embed(title=f'تمت بنجاح', color=assist.embedColors.green), delete_after=3)
        except:await ctx.channel.send(embed=discord.Embed(title=f'هذا الشخص ليس موجود في القائمة', color=assist.embedColors.red), delete_after=3)

async def mms(ctx, client):
    embed = discord.Embed(title='ميمز', color=assist.embedColors.blue)
    data = load(assist.jsonFile)
    urls = data['memes']
    imgs = [i for i in urls if i != '' and i != ' ']
    embed.set_image(url=random.choice(imgs))
    embed.set_author(name='mzooz bot', icon_url=client.user.avatar.url, url=assist.mzo0zServer)
    try:embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar.url)
    except:embed.set_footer(text=ctx.author, icon_url=ctx.author.default_avatar.url)
    await ctx.channel.send(embed=embed)

async def AddMeme(ctx, client, url):
    if url == None:await ctx.channel.send("يجب كتابة الرابط");return
    try:r = requests.get(url)
    except: await ctx.channel.send("الرابط غير صالح");return
    if r.status_code != 200:
        await ctx.channel.send("الرابط غير صالح");return
    else:
        embed = discord.Embed(title='ميمز', color=assist.embedColors.blue)
        data = load(jsonFile)
        data['memes'].append(url)
        data['memes']=list(set(data['memes']))
        dump(jsonFile, data)
        embed.set_image(url=url)
        embed.set_author(name='mzooz bot', icon_url=client.user.avatar.url, url=assist.mzo0zServer)
        try:embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar.url)
        except:embed.set_footer(text=ctx.author, icon_url=ctx.author.default_avatar.url)
        await ctx.channel.send(embed=embed)

async def TAX(ctx, client, income):
    if income == None:
        tx = discord.Embed(title=f'كيفية الاستخدام', description=f'اكتب {load(assist.jsonFile)["prefix"]}tax و اي رقم', color=assist.embedColors.dark_blue, url=assist.mzo0zServer)
        tx.set_author(name='mzooz bot', icon_url=client.user.avatar.url)
        await ctx.channel.send(embed=tx)
    else:
        tax = round(income * 5/100)
        to = int(income - tax)
        on = int(income + tax)

        def num(number):
            return ("{:,}".format(number))

        tx = discord.Embed(title=f'ضريبة : {num(income)}', color=assist.embedColors.dark_blue, url=assist.mzo0zServer)
        tx.add_field(name=f'كم سيسحب البوت:'                  , value =f'**`{num(tax)}`**', inline=False)
        tx.add_field(name=f'كم سيصل للشخص:'                   , value =f'**`{num(to)}`**', inline=False)
        tx.add_field(name=f'كم يجب التحويل ليصل المبلغ كامل:', value =f'**`{num(on)}`**', inline=False)
        tx.set_author(name='mzooz bot', icon_url=client.user.avatar.url)
        await ctx.channel.send(embed=tx)

async def Clear(ctx, client, limit):
    await ctx.channel.purge(limit=limit)
    embed = discord.Embed(title=ctx.guild, color=assist.embedColors.blue, description=f'تم حذف {limit} رسالة')
    embed.set_author(name='mzooz bot', icon_url=client.user.avatar.url, url=assist.mzo0zServer)
    try:embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar.url)
    except:embed.set_footer(text=ctx.author)
    embed.timestamp = datetime.datetime.now()
    await ctx.channel.send(embed=embed, delete_after=3)


async def ROLE(ctx, client, user, role):
    if user == None:await mzoozEmbed(ctx, 'role', assist.embedColors.red, f'اكتب اسم الشخص المراد اعطائه رتبة ثم اكتب اسم الرتبة', "** **", client)
    else:
        role = role.replace("<", "")
        role = role.replace(">", "")
        role = role.replace("@", "")
        role = role.replace("&", "")
        try:role=discord.utils.get(ctx.guild.roles, id=int(role))
        except:role = discord.utils.get(ctx.guild.roles, name=role)
        await user.add_roles(role)
        await mzoozEmbed(ctx, 'role', assist.embedColors.ligh_green, f'تم اضاقة {role} لـ {user} من قبل {ctx.author}', "** **", client)


async def UNRole(ctx, client, user, role):
    if user == None:await mzoozEmbed(ctx, 'unrole', assist.embedColors.red, f'اكتب اسم الشخص المراد ازالة منه رتبة ثم اكتب اسم الرتبة', "** **")
    else:
        role = role.replace("<", "")
        role = role.replace(">", "")
        role = role.replace("@", "")
        role = role.replace("&", "")
        try:role=discord.utils.get(ctx.guild.roles, id=int(role))
        except:role = discord.utils.get(ctx.guild.roles, name=role)
        await user.remove_roles(role)
        await mzoozEmbed(ctx, 'unrole', assist.embedColors.ligh_green, f'تم ازالة {role} من {user} من قبل {ctx.author}', "** **", client)

async def LOCK(ctx, client):
    await ctx.channel.set_permissions(discord.utils.get(ctx.guild.roles, id=int(load(jsonFile)["serverId"])), send_messages = False)
    await mzoozEmbed(ctx, 'lock', assist.embedColors.ligh_green, f'تم قفل الروم من قبل {ctx.author}', "** **", client)

async def BAN(ctx, client, user):
    if user == None:await mzoozEmbed(ctx, 'ban', assist.embedColors.red, f'اكتب اسم العضو المراد تبنيده', "** **", client)
    else:
        try:await user.ban();await mzoozEmbed(ctx, 'ban', assist.embedColors.ligh_green, f'تم تبنيد {user} من قبل {ctx.author}', "** **", client)
        except:await mzoozEmbed(ctx, 'ban', assist.embedColors.red, f'لا أستطيع تبنيد {user}', "** **", client)


async def UNban(ctx, client, user):
    if user == None:
        await mzoozEmbed(ctx, 'unban', assist.embedColors.red, f'اكتب اسم العضو المراد فك تبنيده', "** **", client)
    else:
        try:await ctx.guild.unban(user);await mzoozEmbed(ctx, 'unban', assist.embedColors.ligh_green, f'تم فك التبنيد من {user} من قبل {ctx.author}', "** **", client)
        except:await mzoozEmbed(ctx, 'ban', assist.embedColors.red, f'لا أستطيع فك تبنيد {user}', "** **", client)

async def MUTE(ctx, client, user):
    if user == None:await mzoozEmbed(ctx, 'mute', assist.embedColors.red, 'اكتب اسم العضو المراد تسكيته', "** **", client)
    else:
        roles = [str(i.name).lower() for i in ctx.guild.roles]
        if 'mute' not in roles:await ctx.guild.create_role(name='mute')
        if 'mute' not in [str(i.name).lower() for i in ctx.author.roles]:
            await user.add_roles(discord.utils.get(ctx.guild.roles, name="mute"))
        try:await ctx.channel.set_permissions(discord.utils.get(ctx.guild.roles, name='mute'), send_messages = False)
        except:pass
        await mzoozEmbed(ctx, 'mute', assist.embedColors.ligh_green, f'تم تسكيت {user} من قبل {ctx.author}', "** **", client)

async def UNMUTE(ctx, client, user):
    if user == None:await mzoozEmbed(ctx, 'mute', assist.embedColors.red, 'اكتب اسم العضو المراد السماح له بالكتابه', "** **", client)
    else:
        await user.remove_roles(discord.utils.get(ctx.guild.roles, name="mute"))
        await mzoozEmbed(ctx, 'mute', assist.embedColors.ligh_green, f'تم السماح لـ {user} بالكلام', "** **", client)

async def UNlock(ctx, client):
    await ctx.channel.set_permissions(discord.utils.get(ctx.guild.roles, id=int(load(jsonFile)["serverId"])), send_messages = True)
    await mzoozEmbed(ctx, 'unlock', assist.embedColors.ligh_green, f'تم فتح الروم من قبل {ctx.author}', "** **", client)

async def KICK(ctx, client, user):
    if user == None:await mzoozEmbed(ctx, 'kick', assist.embedColors.red, f'اكتب اسم العضو المراد طرده', "** **", client)
    else:
        try:await user.kick();await mzoozEmbed(ctx, 'kick', assist.embedColors.ligh_green, f'تم طرد {user} من قبل {ctx.author}', "** **", client)
        except:await mzoozEmbed(ctx, 'kick', assist.embedColors.red, f'لا أستطيع طرد {user}', "** **", client)

async def mzoozEmbed(ctx, title, color, name, value, client):
    embed = discord.Embed(title=title, color=color)
    embed.add_field(name=name, value=value)
    embed.set_author(name='mzooz bot', icon_url=client.user.avatar.url, url=assist.mzo0zServer)
    try:embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar.url)
    except:embed.set_footer(text=ctx.author, icon_url=ctx.author.default_avatar.url)
    await ctx.channel.send(embed=embed)
