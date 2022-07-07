import discord
import datetime
import assist
import random
import emoji
import json

from time import sleep
from dhooks import Webhook
from typing import Union
from . import gamesAssist


def load(file):
    with open(file, 'r') as f:DATA = json.load(f);return DATA
def dump(file, DATA):
    with open(file, 'w') as f:json.dump(DATA, f);f.close();return


async def start(ctx, client):
    await ctx.message.delete()
 
    TICKET = load(assist.tickjson)


    outstorybool          = False #outstory
    outstoryleader        = '' #outstory
    players               = [] #outstory
    playersN              = []
    playersName           = {} #outStory
    gamesjson = assist.gamesjson

    outstorymodes = {
        '1': 'دول',
        '2': 'حيوانات',
        '5': 'مشاهير يوتيوب',
        '6': 'اكلات',
        '7': 'مشروبات'}  # outstory

    emojis = gamesAssist.emojis

    MODES = {
        '1': gamesAssist.countrys,
        '2': gamesAssist.animals,
        '3': gamesAssist.devices,
        '4': gamesAssist.people,
        '5': gamesAssist.youtubers,
        '6': gamesAssist.food,
        '7': gamesAssist.drinks,
        '8': gamesAssist.things
    }

    DATA     = load(assist.gamesjson)
    SERVER   = load(assist.jsonFile)
    TICKET   = load(assist.tickjson)
    everyone = int(SERVER["serverId"])
    if outstorybool == False:
        webhooksNames = await ctx.channel.webhooks()
        webhooks = []
        for webhook in webhooksNames:
            if webhook.name == 'mzooz':
                outstoryUrlWebhook = webhook.url
            webhooks.append(webhook.name)

        if 'mzooz' not in webhooks:
            await ctx.channel.create_webhook(name="mzooz")
            webhooksNames = await ctx.channel.webhooks()
            for webhook in webhooksNames:
                if webhook.name == 'mzooz':
                    outstoryUrlWebhook = webhook.url
                    webhooks.append(webhook.name)

        invite = await ctx.channel.create_invite(max_age = 12 * 3600)

        class fastReturn(discord.ui.View):
            @discord.ui.button(style=discord.ButtonStyle.green, label='انتقال سريع', row=0, url=str(invite))
            async def BACK(self, button: discord.ui.Button, interaction: discord.Interaction):
                pass

        global thestoryis
        outstorybool = True
        outstoryleader = ctx.author.id

        adm = str(await client.fetch_user(outstoryleader))

        if adm in  DATA[str(ctx.guild.id)]:
            Added = discord.Embed(title='**برا السالفة - out story**',description=f"لايمكنك بدأ لعبة وانت تلعب لعبة اخرى", color=assist.embedColors.red)
            Added.set_author(name='mzooz bot', icon_url=client.user.avatar.url, url=assist.mzo0zServer)
            Added.timestamp = datetime.datetime.now()
            try:
                icon_url=ctx.author.avatar.url
            except:
                icon_url=client.user.avatar.url
            Added.set_footer(text = f'{ctx.author} ', icon_url=icon_url)
            done = await ctx.channel.send(embed=Added, delete_after=3)
            return 0
        players.append(f'<@!{outstoryleader}>')
        mentionPlayers = discord.Embed(title='**برا السالفة - out story**', description=f"<@{outstoryleader}> منشن جميع اللاعبين الذين سيلعبون لإضافتهم", color=assist.embedColors.yellow)
        mentionPlayers.set_author(name='mzooz bot', icon_url=client.user.avatar.url, url=assist.mzo0zServer)

        msg = await ctx.channel.send(embed=mentionPlayers)
        outPlayers = []
        def playersToPlayOutStory(m):
            player = m.content
            if player:
                if m.channel.id == ctx.channel.id:
                    if m.author.id != outstoryleader:
                        pass
                    elif m.author.id == outstoryleader:
                        player = player.split(' ')
                        if len(player) < 2:
                            lowPlayers = discord.Embed(title='**برا السالفة - out story**', description=f'```يجب ان يكون عدد اللاعبين 3 على الاقل, قم بمنشن اللاعبين من جديد```', color=assist.embedColors.red, url=' https://discord.gg/7gzWBSCbY6')
                            lowPlayers.set_author(name='mzooz bot', icon_url=client.user.avatar.url)
                            Webhook(outstoryUrlWebhook).send(username='mzooz',avatar_url=client.user.avatar.url, embed=lowPlayers)
                        else:
                            for p in player:
                                if p == ' ':
                                    pass
                                elif p == '':
                                    pass
                                else:
                                    outPlayers.append(p)
                            return ' '

        jh = await client.wait_for("message", check=playersToPlayOutStory)
        await jh.delete()
        DATA[str(ctx.guild.id)][adm] = {}
        DATA[str(ctx.guild.id)][adm]["leader"] = outstoryleader
        DATA[str(ctx.guild.id)][adm]["allow"] = []
        with open(gamesjson, 'w') as f:
            json.dump(DATA, f)
            f.close()

        for p in outPlayers:
            playerid = p.replace('@', '')
            playerid = playerid.replace('<', '')
            playerid = playerid.replace('>', '')
            playerid = playerid.replace('!', '')
            if p == "":
                pass
            else:
                try:
                    if len(players) < 12:
                        user = await client.fetch_user(playerid)
                        Added = discord.Embed(title='**برا السالفة - out story**',description=f"تم اضافتك للعبة من قبل <@{outstoryleader}>", color=assist.embedColors.green)
                        Added.set_author(name='mzooz bot', icon_url=client.user.avatar.url, url=assist.mzo0zServer)
                        Added.timestamp = datetime.datetime.now()
                        Added.set_footer(text = f'{ctx.guild.name} ', icon_url=client.user.avatar.url)

                        done = await user.send(embed=Added, view=fastReturn())

                        if done:
                            if p in players:
                                alreadyAdded = discord.Embed(title='**برا السالفة - out story**',description=f"هذا اللاعب {p} مضاف بالفعل!", color=assist.embedColors.red)
                                alreadyAdded.timestamp = datetime.datetime.now()
                                alreadyAdded.set_footer(text = f'{ctx.guild.name} ', icon_url=client.user.avatar.url)
                                alreadyAdded.set_author(name='mzooz bot', icon_url=client.user.avatar.url, url=assist.mzo0zServer)
                                await msg.edit(embed=alreadyAdded)
                            if p not in players:
                                players.append(p)
                                playersN.append(str(user))
                                playersName.update({str(p):user})
                                DATA[str(ctx.guild.id)][adm]["allow"].append(p)
                                with open(gamesjson, 'w') as f:
                                    json.dump(DATA, f)
                                    f.close()

                                doneAdd = discord.Embed(title='**برا السالفة - out story**',description=f"تم إضافة {p}", color=assist.embedColors.green)
                                doneAdd.timestamp = datetime.datetime.now()
                                doneAdd.set_footer(text = f'{ctx.guild.name} ', icon_url=client.user.avatar.url)
                                doneAdd.set_author(name='mzooz bot', icon_url=client.user.avatar.url, url=assist.mzo0zServer)
                                await msg.edit(embed=doneAdd)


                    else:
                        fullPlayers = discord.Embed(title='**برا السالفة - out story**',description="لا أستطيع اضافة المزيد من اللاعبين!", color=assist.embedColors.red)
                        fullPlayers.timestamp = datetime.datetime.now()
                        fullPlayers.set_footer(text = f'{ctx.guild.name} ', icon_url=client.user.avatar.url)
                        fullPlayers.set_author(name='mzooz bot', icon_url=client.user.avatar.url, url=assist.mzo0zServer)
                        await msg.edit(embed=fullPlayers)
                except:
                    cantAdd = discord.Embed(title='**برا السالفة - out story**',description=f"لا استطيع إضافة هذا اللاعب {p} لانه غير موجود او بوت, تأكد من الاسم.", color=assist.embedColors.red)
                    cantAdd.timestamp = datetime.datetime.now()
                    cantAdd.set_footer(text = f'{ctx.guild.name} ', icon_url=client.user.avatar.url)
                    cantAdd.set_author(name='mzooz bot', icon_url=client.user.avatar.url, url=assist.mzo0zServer)
                    await msg.edit(embed=cantAdd)


        await msg.delete()
        num = datetime.datetime.now().microsecond
        num = str(num)[:3] + str(ctx.author.id)[:3]
        chName = f'out story-{adm}'
        channel = await ctx.guild.create_text_channel(chName)

        webhooksNames = await channel.webhooks()
        webhooks = []
        for webhook in webhooksNames:
            if webhook.name == 'mzooz':
                outstoryUrlWebhook = webhook.url
            webhooks.append(webhook.name)

        if 'mzooz' not in webhooks:
            await channel.create_webhook(name="mzooz")
            webhooksNames = await channel.webhooks()
            for webhook in webhooksNames:
                if webhook.name == 'mzooz':
                    outstoryUrlWebhook = webhook.url
                    webhooks.append(webhook.name)

        await channel.set_permissions(ctx.author, read_messages=True)
        await channel.set_permissions(discord.utils.get(ctx.guild.roles, id=int(everyone)), read_messages=False)
        for i in DATA[str(ctx.guild.id)][adm]["allow"]:
            o = i.replace('!', '')
            o = o.replace('@', '')
            o = o.replace('<', '')
            o = o.replace('>', '')
            usr = await client.fetch_user(o)
            await channel.set_permissions(usr, read_messages=True)

        TICKET[str(ctx.guild.id)][channel.id] = {}
        TICKET[str(ctx.guild.id)][channel.id]["msg"] = channel.id
        TICKET[str(ctx.guild.id)][channel.id]["leader"] = adm
        with open(assist.tickjson, 'w') as f:
            json.dump(TICKET, f)
            f.close()

        ich = await channel.create_invite(max_age = 60 * 5)
        bdt = discord.Embed(title='**برا السالفة - out story**',description=f"اللعبة بدأت في هذا الروم", color=assist.embedColors.red)
        bdt.timestamp = datetime.datetime.now()
        bdt.set_footer(text = f'{ctx.guild.name} ', icon_url=client.user.avatar.url)
        bdt.set_author(name='mzooz bot', icon_url=client.user.avatar.url, url=assist.mzo0zServer)

        class fastGo(discord.ui.View):
            @discord.ui.button(style=discord.ButtonStyle.green, label='انتقال سريع', row=0, url=str(ich))
            async def BACK(self, button: discord.ui.Button, interaction: discord.Interaction):
                pass
        await ctx.channel.send(embed=bdt, view=fastGo(), delete_after=5)



        class outstoryoptions(discord.ui.Select):
            def __init__(self):
                options=[
                    discord.SelectOption(label="دول", value='1'),
                    discord.SelectOption(label="حيوانات", value='2'),
                    discord.SelectOption(label="مشاهير يوتيوب", value='5'),
                    discord.SelectOption(label="اكلات", value='6'),
                    discord.SelectOption(label="مشروبات", value='7'),
                    ]
                super().__init__(placeholder="اختار المود",max_values=1,min_values=1,options=options)
            async def callback(self, interaction: discord.Interaction):
                global outstorychoose
                if interaction.user.id != outstoryleader:
                    pass
                else:
                    outstorychoose = self.values[0]
                    mode = discord.Embed(title='**برا السالفة - out story**',description=f"**المود الي اخترته: {outstorymodes[self.values[0]]}**", color=assist.embedColors.blue)
                    mode.set_author(name='mzooz bot', icon_url=client.user.avatar.url, url=assist.mzo0zServer)
                    await interaction.response.send_message(embed=mode)
                    await channel.set_permissions(discord.utils.get(ctx.guild.roles, id=everyone), send_messages = True)

        class outstoryview(discord.ui.View):
            def __init__(self):
                super().__init__()
                self.add_item(outstoryoptions())
        try:
            await channel.purge(limit=100)
        except:
            pass
        await channel.set_permissions(discord.utils.get(ctx.guild.roles, id=everyone), send_messages = False)
        chooseMode = discord.Embed(title='**برا السالفة - out story**',description=f'<@{outstoryleader}> اختار المود:', color=assist.embedColors.teal)
        chooseMode.set_author(name='mzooz bot', icon_url=client.user.avatar.url, url=assist.mzo0zServer)
        await channel.send(stringl(players) , embed=chooseMode, view=outstoryview())
        sleep(3)


        outPlayers = []
        await channel.purge(limit=100)
        outStoryLobby = discord.Embed(title='**برا السالفة - out story**',description=f'<@{outstoryleader}> ماذا تريد ان تفعل؟', color=0x00ff00)
        outStoryLobby.set_author(name='mzooz bot', icon_url=client.user.avatar.url, url=assist.mzo0zServer)

        errorPlayers = discord.Embed(title='عدد اللاعبين', description="**لبدأ اللعبة يجب ان يكون عدد اللاعبين 3 على الاقل.**", color=assist.embedColors.red)
        errorPlayers.set_author(name='mzooz bot', icon_url=client.user.avatar.url, url=assist.mzo0zServer)

        class outStoryViewLobby(discord.ui.View):
            @discord.ui.button(style=discord.ButtonStyle.green, label='بدء جولة جديدة', row=0)
            async def outstoryStartGameCallBack(self, button: discord.ui.Button, interaction: discord.Interaction):
                if interaction.user.id == outstoryleader:
                    if interaction.channel == channel:
                        if len(players) < 3:
                            await interaction.response.send_message(embed = errorPlayers, view=outStoryViewLobby())
                        else:
                            await startOutStroeyGame()

            @discord.ui.button(style=discord.ButtonStyle.blurple, label='إضافة لاعبين', row=0)
            async def outstoryAddPlayersCallBack(self, button: discord.ui.Button, interaction: discord.Interaction):
                if interaction.user.id == outstoryleader:
                    if interaction.channel == channel:
                        await channel.set_permissions(discord.utils.get(ctx.guild.roles, id=everyone), send_messages = True)
                        await outstoryAddPlayers()

            @discord.ui.button(style=discord.ButtonStyle.red, label='حذف لاعبين', row=0)
            async def outstoryDelPlayersCallBack(self, button: discord.ui.Button, interaction: discord.Interaction):
                if interaction.user.id == outstoryleader:
                    if interaction.channel == channel:
                        await channel.set_permissions(discord.utils.get(ctx.guild.roles, id=everyone), send_messages = True)
                        await outStoryDelPlayers()

            @discord.ui.button(style=discord.ButtonStyle.green, label='تغيير المود', row=1)
            async def outstoryChangeModeCallBack(self, button: discord.ui.Button, interaction: discord.Interaction):
                if interaction.user.id == outstoryleader:
                    if interaction.channel == channel:
                        await channel.purge(limit=100)
                        await outStoryChangeMode()

            @discord.ui.button(style=discord.ButtonStyle.blurple, label='إظهار اللاعبين', row=1)
            async def outstoryShowPlayersCallBack(self, button: discord.ui.Button, interaction: discord.Interaction):
                if interaction.user.id == outstoryleader:
                    if interaction.channel == channel:
                        await interaction.response.send_message(stringl(players))

            @discord.ui.button(style=discord.ButtonStyle.red, label='إنهاء اللعبة', row=1, custom_id=channel.id)
            async def outstoryEndGameCallBack(self, button: discord.ui.Button, interaction: discord.Interaction):
                if interaction.user.id == outstoryleader:
                    if interaction.channel == channel:
                        return 0 


        outstoryRole = discord.utils.get(ctx.guild.roles, id=everyone)
        await channel.set_permissions(outstoryRole, send_messages = False)
        await channel.send(embed=outStoryLobby, view=outStoryViewLobby())

    async def startOutStroeyGame():
        global unRepeatOutStory
        global outStoryRoundsToPlay
        global outstorychoose
        global alreadyVoted
        global outstoryCountPlayers
        outstoryCountPlayers = 0
        alreadyVoted = []
        await channel.set_permissions(discord.utils.get(ctx.guild.roles, id=everyone), send_messages = False)
        unRepeatOutStory = []
        await channel.purge(limit=100)
        if len(players) <= 2:
            await channel.send("**لبدأ اللعبة يجب ان يكون عدد اللاعبين 3 على الاقل.**", view=outStoryViewLobby())
        else:
            global outthestory
            global thestoryis
            global outstoryemoji
            global voteoutstoryplayers
            global outstoryPlayersPoints
            global outPlayers
            gameStarted = discord.Embed(title='برا السالفة - out story', description="`بدأت اللعبة على جميع اللاعبين ان يتفقدوا المحادثة الخاصة`", color=assist.embedColors.dark_blue).set_author(name='mzooz games bot', icon_url=client.user.avatar.url, url=assist.mzo0zServer)
            await channel.send(embed=gameStarted)
            try:
                m = await channel.send(f"الاسألة بعد `5`s")
                for i in range(5, 0 , -1):
                    await m.edit(content=f"الاسألة بعد `{i}`s")
                    sleep(0.5)
                await m.delete()
            except:
                pass
            for mode in MODES[str(outstorychoose)]:
                unRepeatOutStory.append(mode)
            if len(unRepeatOutStory) == 3:
                unRepeatOutStory = []
                for mode in MODES[str(outstorychoose)]:
                    unRepeatOutStory.append(mode)
            thestoryis = random.choice(unRepeatOutStory)
            unRepeatOutStory.remove(thestoryis)
            out = random.choice(players)
            pid = out.replace('@', '')
            pid = pid.replace('<', '')
            pid = pid.replace('>', '')
            pid = pid.replace('!', '')
            user = await client.fetch_user(pid)
            await user.send(f"**انت خارج السالفة يجب ان تعرف ماهي السالفة**")
            outthestory = out
            for i in players:
                if i == out:
                    pass
                else:
                    oid  = i.replace('@', '')
                    oid  = oid.replace('<', '')
                    oid  = oid.replace('>', '')
                    oid  = oid.replace('!', '')
                    user = await client.fetch_user(oid)
                    await user.send(f"**انت داخل السالفة والتي `{thestoryis}`**")

            if outthestory:
                for i in players:
                    try:
                        whoAsk = random.choice(players)
                        if whoAsk == i:
                            await channel.send(f'{random.choice(players)} اسأل ==> {i}')
                        else:
                            await channel.send(f'{whoAsk} اسأل ==> {i}')
                        timer = await channel.send('**بدأ المؤقت!**')
                        for i in range(25, 0, -1):
                            try:
                                await timer.edit(content=f"**المؤقت:** `{i}`")
                            except:
                                pass
                        try:
                            await timer.edit(content='**إنتهى الوقت!**')
                        except:
                            pass
                    except:
                        pass

                for i in players:
                    try:
                        await channel.send(f"{i} اسأل اي شخص  تريده")
                        timer = await channel.send('**بدأ المؤقت!**')
                        for i in range(25, 0, -1):
                            await timer.edit(content=f"**المؤقت:** `{i}`")
                        await timer.edit(content='**إنتهى الوقت!**')
                    except:
                        pass
                if True:
                    outstoryPlayersPoints = {}
                    voteoutstoryplayers = {}
                    embed = discord.Embed(title='**التصويت**', description='صوّت على الشخص الذي تتوقع انه خارج السالفة,\nملاحظة لايمكنك تغيير تصويتك', color=0x00ff00, url='https://discord.gg/7gzWBSCbY6')
                    reactions = []
                    outstoryemoji = random.choice(emojis)
                    outstoryemoji = emoji.emojize(outstoryemoji)
                    doneAddPlayer = list(voteoutstoryplayers.values())
                    plrs = []
                    for i in players:
                        plrs.append(i)
                    timesToS = len(plrs)
                    for ranemo in range(timesToS):
                        for i in plrs:
                            if i not in doneAddPlayer:
                                if emojis[ranemo] != outstoryemoji:
                                    if i == outthestory:
                                        voteoutstoryplayers.update({emoji.emojize(outstoryemoji): outthestory})
                                        outstoryPlayersPoints.update({outthestory: 0})
                                        reactions.append(emoji.emojize(outstoryemoji))
                                    else:
                                        if emojis[ranemo] not in reactions:
                                            voteoutstoryplayers.update({emoji.emojize(emojis[ranemo]): i})
                                            outstoryPlayersPoints.update({i: 0})
                                            reactions.append(emojis[ranemo])
                                        else:
                                            voteoutstoryplayers.update({emoji.emojize(emojis[ranemo+1]): i})
                                            outstoryPlayersPoints.update({i: 0})
                                            reactions.append(emoji.emojize(emojis[ranemo+1]))
                                    plrs.remove(i)

                    sortvoteplayers = list(voteoutstoryplayers.keys())
                    for i in sortvoteplayers:
                        getUserIdOUTSTORY = voteoutstoryplayers[i].replace('@', '')
                        getUserIdOUTSTORY = getUserIdOUTSTORY.replace('<', '')
                        getUserIdOUTSTORY = getUserIdOUTSTORY.replace('>', '')
                        getUserIdOUTSTORY = getUserIdOUTSTORY.replace('!', '')
                        user = await client.fetch_user(getUserIdOUTSTORY)
                        embed.add_field(name=f'{i}  ==>  {user}', value='================', inline=False)
                        embed.set_author(icon_url=client.user.avatar.url, name = 'mzooz games bot')

                    mes = await channel.send(embed=embed)
                    for i in sortvoteplayers:
                        try:
                            await mes.add_reaction(emoji.emojize(i))
                        except discord.errors.NotFound:
                            pass
                        except Exception as e:
                            raise e
                    outPlayers = []
                    def check(r: discord.Reaction, u: Union[discord.Member, discord.User]):
                        global outPlayers
                        global outstoryCountPlayers
                        global alreadyVoted
                        global outstoryPlayersPoints
                        player = f"<@!{u.id}>"
                        if u.id != client.user.id:
                            if player in players:
                                if player in alreadyVoted:
                                    pass
                                else:
                                    alreadyVoted.append(player)
                                    if outstoryCountPlayers < len(players):
                                        outstoryCountPlayers +=1
                                        if str(r.emoji) == outstoryemoji:
                                            usrToPoint = voteoutstoryplayers[outstoryemoji]
                                            point = outstoryPlayersPoints[usrToPoint]
                                            outstoryPlayersPoints.update({usrToPoint: int(point)+1})
                                        else:
                                            rea = str(r.emoji)
                                            usrToPoint = voteoutstoryplayers[rea]
                                            point = outstoryPlayersPoints[usrToPoint]
                                            outstoryPlayersPoints.update({usrToPoint: int(point)+1})

                                    if outstoryCountPlayers == len(players):
                                        return ' '



                reaction, userrr = await client.wait_for(event = 'reaction_add', check = check)
                embed = discord.Embed(title='**النتائج**', color=0x00ff00)

                def restartcote():
                    global voteoutstoryplayers
                    global outstoryPlayersPoints
                    global outstoryCountPlayers
                    global alreadyVoted
                    alreadyVoted = []
                    outstoryCountPlayers = 0
                    voteoutstoryplayers = {}
                    outstoryPlayersPoints = {}

                for i in outstoryPlayersPoints:
                    playerid = i.replace('@', '')
                    playerid = playerid.replace('<', '')
                    playerid = playerid.replace('>', '')
                    playerid = playerid.replace('!', '')
                    user = await client.fetch_user(playerid)
                    embed.add_field(name=f'**{user}**', value=outstoryPlayersPoints[i], inline=False)
                higherPoint = max(outstoryPlayersPoints, key=outstoryPlayersPoints.get)
                embed.add_field(name=f'**السالفة**', value=f"`{thestoryis}`", inline=True)
                embed.set_author(icon_url=client.user.avatar.url, name = 'mzooz games bot', url=assist.mzo0zServer)
                if higherPoint == outthestory:
                    embed.add_field(name=f'**انكشف**', value=f"{outthestory}", inline=True)
                else:
                    embed.add_field(name=f'**لم ينكشف**', value=f"{outthestory}", inline=True)
                restartcote()
                await reaction.message.edit(embed=embed, view=outStoryViewLobby())


    async def outstoryAddPlayers():
        try:
            if len(players) < 12:
                addPlayer = discord.Embed(title='**برا السالفة - out story**',description=f"<@{outstoryleader}> منشن اللاعبين المراد إضافتهم", color=assist.embedColors.yellow)
                addPlayer.set_author(name='mzooz bot', icon_url=client.user.avatar.url, url=assist.mzo0zServer)
                ff = await channel.send(embed=addPlayer)

                outPlayers = []
                def playersToPlayOutStory(m):
                    player = m.content
                    if player:
                        if m.channel == channel:
                            if m.author.id != outstoryleader:
                                pass
                            elif m.author.id == outstoryleader:
                                player = player.split(' ')
                                for p in player:
                                    if p == ' ':
                                        pass
                                    elif p == '':
                                        pass
                                    else:
                                        outPlayers.append(p)
                                return ' '

                await client.wait_for("message", check=playersToPlayOutStory)
                for playerToAddInOutStory in outPlayers:
                    outStoryPlayerIdToAdd = playerToAddInOutStory.replace('@', '')
                    outStoryPlayerIdToAdd = outStoryPlayerIdToAdd.replace('<', '')
                    outStoryPlayerIdToAdd = outStoryPlayerIdToAdd.replace('>', '')
                    outStoryPlayerIdToAdd = outStoryPlayerIdToAdd.replace('!', '')
                    if playerToAddInOutStory == "":
                        pass
                    else:
                        user = await client.fetch_user(outStoryPlayerIdToAdd)

                        Added = discord.Embed(title='**برا السالفة - out story**',description=f"تم اضافتك للعبة من قبل <@{outstoryleader}>", color=assist.embedColors.green)
                        Added.set_author(name='mzooz bot', icon_url=client.user.avatar.url, url=assist.mzo0zServer)
                        Added.timestamp = datetime.datetime.now()
                        Added.set_footer(text = f'{ctx.guild.name} ', icon_url=client.user.avatar.url)
                        done = await user.send(embed=Added, view=fastReturn())
                        if done:
                            if playerToAddInOutStory in players:
                                alreadyAdded = discord.Embed(title='**برا السالفة - out story**',description=f"هذا اللاعب {playerToAddInOutStory} مضاف بالفعل!", color=assist.embedColors.red)
                                alreadyAdded.set_author(name='mzooz bot', icon_url=client.user.avatar.url, url=assist.mzo0zServer)
                                alreadyAdded.timestamp = datetime.datetime.now()
                                alreadyAdded.set_footer(text = f'{ctx.guild.name} ', icon_url=client.user.avatar.url)
                                await ff.edit(embed=alreadyAdded)
                            elif playerToAddInOutStory not in players:
                                players.append(playerToAddInOutStory)
                                playersN.append(str(user))
                                playersName.update({str(playerToAddInOutStory):user})
                                await channel.set_permissions(user, read_messages = True)
                                doneAdd = discord.Embed(title='**برا السالفة - out story**',description=f"تم إضافة {playerToAddInOutStory}", color=assist.embedColors.green)
                                doneAdd.set_author(name='mzooz bot', icon_url=client.user.avatar.url)
                                doneAdd.timestamp = datetime.datetime.now()
                                doneAdd.set_footer(text = f'{ctx.guild.name} ', icon_url=client.user.avatar.url)
                                await ff.edit(embed=doneAdd)
            else:
                fullPlayers = discord.Embed(title='**برا السالفة - out story**',description="لا أستطيع اضافة المزيد من اللاعبين!", color=assist.embedColors.red)
                fullPlayers.set_author(name='mzooz bot', icon_url=client.user.avatar.url, url=assist.mzo0zServer)
                fullPlayers.timestamp = datetime.datetime.now()
                fullPlayers.set_footer(text = f'{ctx.guild.name} ', icon_url=client.user.avatar.url)
                await ff.edit(embed=fullPlayers)
        except:
            cantAdd = discord.Embed(title='**برا السالفة - out story**',description=f"لا استطيع إضافة هذا اللاعب {playerToAddInOutStory} لانه غير موجود او بوت, تأكد من الاسم.", color=assist.embedColors.red)
            cantAdd.set_author(name='mzooz bot', icon_url=client.user.avatar.url, url=assist.mzo0zServer)
            await ff.edit(embed=cantAdd)
        mode = discord.Embed(title='**برا السالفة - out story**',description=f"**ماذا تريد ان تفعل؟ <@{outstoryleader}>**", color=assist.embedColors.purple)
        mode.set_author(name='mzooz bot', icon_url=client.user.avatar.url, url=assist.mzo0zServer)
        sleep(1.5)
        await ff.edit(embed=mode, view=outStoryViewLobby())
        

    async def outStoryDelPlayers():
        await channel.purge(limit=1000)
        delPlayer = discord.Embed(title='**برا السالفة - out story**',description=f"<@{outstoryleader}> منشن اللاعبين المراد طردهم", color=assist.embedColors.yellow)
        delPlayer.set_author(name='mzooz bot', icon_url=client.user.avatar.url, url=assist.mzo0zServer)
        ff = await channel.send(embed=delPlayer)
        outPlayers = []
        def playersToPlayOutStory(m):
            player = m.content
            if player:
                if m.channel == channel:
                    if m.author.id != outstoryleader:
                        pass
                    elif m.author.id == outstoryleader:
                        player = player.split(' ')
                        for p in player:
                            if p == ' ':
                                pass
                            elif p == '':
                                pass
                            else:
                                outPlayers.append(p)
                        return ' '

        await client.wait_for("message", check=playersToPlayOutStory)

        for playerToDelFromOutStory in outPlayers:
            if playerToDelFromOutStory in players:
                players.remove(playerToDelFromOutStory)

                ouStoryPlayerIdToDel = playerToDelFromOutStory.replace('@', '')
                ouStoryPlayerIdToDel = ouStoryPlayerIdToDel.replace('<', '')
                ouStoryPlayerIdToDel = ouStoryPlayerIdToDel.replace('>', '')
                ouStoryPlayerIdToDel = ouStoryPlayerIdToDel.replace('!', '')
                user = await client.fetch_user(ouStoryPlayerIdToDel)
                playersN.remove(str(user))
                await channel.set_permissions(user, read_messages=False)
                doneDel = discord.Embed(title='**برا السالفة - out story**',description=f"تم حذف {playerToDelFromOutStory}!", color=assist.embedColors.blurple)
                doneDel.set_author(name='mzooz bot', icon_url=client.user.avatar.url, url=assist.mzo0zServer)
                await ff.edit(embed=doneDel)
            else:
                notHere = discord.Embed(title='**برا السالفة - out story**',description=f"هذا اللاعب غير موجود {playerToDelFromOutStory}", color=assist.embedColors.red)
                notHere.set_author(name='mzooz bot', icon_url=client.user.avatar.url, url=assist.mzo0zServer)
                await ff.edit(embed=notHere)


        await channel.set_permissions(discord.utils.get(ctx.guild.roles, id=everyone), send_messages=False)
        await ff.edit(embed=showPlayers())
        mode = discord.Embed(title='**برا السالفة - out story**',description=f"**ماذا تريد ان تفعل؟ <@{outstoryleader}>**", color=assist.embedColors.purple)
        mode.set_author(name='mzooz bot', icon_url=client.user.avatar.url, url=assist.mzo0zServer)
        sleep(1.5)
        await ff.edit(embed=mode, view=outStoryViewLobby())


    def showPlayers():
        playersAre = discord.Embed(title='**برا السالفة - out story**',description='هؤلاء هم اللاعبين:', color=assist.embedColors.dark_purple)
        playersAre.set_author(name='mzooz bot', icon_url=client.user.avatar.url, url=assist.mzo0zServer)
        playersAre.add_field(name=stringl(playersN), value="** **", inline=True)
        return playersAre

    async def outStoryChangeMode():
        class outstoryoptions(discord.ui.Select):
            def __init__(self):
                options=[
                    discord.SelectOption(label="دول", value='1'),
                    discord.SelectOption(label="حيوانات", value='2'),
                    discord.SelectOption(label="مشاهير يوتيوب", value='5'),
                    discord.SelectOption(label="اكلات", value='6'),
                    discord.SelectOption(label="مشروبات", value='7'),
                    ]
                super().__init__(placeholder="اختار المود",max_values=1,min_values=1,options=options)

            async def callback(self, interaction: discord.Interaction):
                global outstorychoose
                if interaction.user.id != outstoryleader:
                    pass
                else:
                    outstorychoose = self.values[0]
                    mode = discord.Embed(title='**برا السالفة - out story**',description=f"**المود الذي اخترته: {outstorymodes[self.values[0]]}\n<@{outstoryleader}> ماذا تريد ان تفعل؟**", color=assist.embedColors.purple)
                    mode.set_author(name='mzooz bot', icon_url=client.user.avatar.url, url=assist.mzo0zServer)
                    await channel.purge(limit=100)
                    await interaction.response.send_message(embed=mode, view=outStoryViewLobby())
                    await channel.set_permissions(discord.utils.get(ctx.guild.roles, id=everyone), send_messages = True)

        class outstoryview(discord.ui.View):
            def __init__(self):
                super().__init__()
                self.add_item(outstoryoptions())
        try:
            await channel.purge(limit=100)
        except:
            pass


        chooseMode = discord.Embed(title='**برا السالفة - out story**',description=f'<@{outstoryleader}> اختار المود:', color=assist.embedColors.teal)
        chooseMode.set_author(name='mzooz bot', icon_url=client.user.avatar.url, url=assist.mzo0zServer)
        await channel.send(embed=chooseMode, view=outstoryview())
        sleep(1.5)



def stringl(tup):
    str = ''
    for item in tup:
        str = str + item + '\n'
    return str