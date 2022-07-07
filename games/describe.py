import discord
import datetime, assist, random
import json
from time import sleep
from dhooks import Webhook
from . import gamesAssist

async def start(ctx, client):
    gamesjson = assist.gamesjson
    with open(gamesjson, 'r') as (ff):
        DATA = json.load(ff)
    with open(assist.jsonFile, 'r') as (ff):
        SERVER = json.load(ff)
    describePlayers = []
    describePlayersN = []
    describeleader = ''
    describebool = False
    MZO0Z = int(SERVER['ownerId'])
    everyone = int(SERVER['serverId'])
    describemodes = {'1':'دول', 
     '2':'حيوانات', 
     '3':'اجهزة', 
     '4':'اشخاص'}
    MODES = {'1':gamesAssist.countrys, 
     '2':gamesAssist.animals, 
     '3':gamesAssist.devices, 
     '4':gamesAssist.people, 
     '5':gamesAssist.youtubers, 
     '6':gamesAssist.food, 
     '7':gamesAssist.drinks, 
     '8':gamesAssist.things}

    with open(gamesjson, 'r') as (gg):
        DATA = json.load(gg)

    with open(assist.jsonFile, 'r') as (ff):
        SERVER = json.load(ff)

    with open(assist.tickjson, 'r') as (f):
        TICKET = json.load(f)


    await ctx.message.delete()
    if describebool == False:
        describeleader = ctx.author.id
        webhooksNames = await ctx.channel.webhooks()
        webhooks = []
        for webhook in webhooksNames:
            if webhook.name == 'mzooz':
                describeUrlWebhook = webhook.url
            webhooks.append(webhook.name)
        else:
            if 'mzooz' not in webhooks:
                await ctx.channel.create_webhook(name='mzooz')
                webhooksNames = await ctx.channel.webhooks()
                for webhook in webhooksNames:
                    if webhook.name == 'mzooz':
                        describeUrlWebhook = webhook.url
                        webhooks.append(webhook.name)

            invite = await ctx.channel.create_invite(max_age=43200)

            class fastReturn(discord.ui.View):

                @discord.ui.button(style=(discord.ButtonStyle.green), label='انتقال سريع', row=0, url=(str(invite)))
                async def BACK(self, button: discord.ui.Button, interaction: discord.Interaction):
                    pass

            adm = str(await client.fetch_user(describeleader))
            if str(ctx.guild.id) not in DATA:
                DATA[str(ctx.guild.id)] = {}
                with open(gamesjson, 'w') as (f):
                    json.dump(DATA, f)
                    f.close()
            if adm in DATA[str(ctx.guild.id)]:
                Added = discord.Embed(title='**اوصف - describe**', description='لايمكنك بدأ لعبة وانت تلعب لعبة اخرى', color=(assist.embedColors.red) )
                Added.set_author(name='mzooz bot', icon_url=(client.user.avatar.url))
                Added.timestamp = datetime.datetime.now()
                try:
                    icon_url = ctx.author.avatar.url
                except:
                    icon_url = client.user.avatar.url
                else:
                    Added.set_footer(text=f"{ctx.author} ", icon_url=icon_url, url=assist.mzo0zServer)
                    done = await ctx.channel.send(embed=Added, delete_after=3)
                    return 0
            mentionPlayers = discord.Embed(title='**اوصف - describe**', description=f"<@{describeleader}> منشن جميع اللاعبين الذين سيلعبون لإضافتهم", color=(assist.embedColors.yellow))
            mentionPlayers.set_author(name='mzooz bot', icon_url=(client.user.avatar.url), url=assist.mzo0zServer)
            msg = await ctx.channel.send(embed=mentionPlayers)
            desPlayers = []

            def playersToPlayDescribe(m):
                player = m.content
                if player:
                    if m.channel.id == ctx.channel.id:
                        if m.author.id != describeleader:
                            pass
                        elif m.author.id == describeleader:
                            player = player.split(' ')
                            if len(player) < 2:
                                lowPlayers = discord.Embed(title='**اوصف - describe**', description='```يجب ان يكون عدد اللاعبين 2 على الاقل, قم بمنشن اللاعبين من جديد```', color=(assist.embedColors.red))
                                lowPlayers.set_author(name='mzooz bot', icon_url=(client.user.avatar.url), url=assist.mzo0zServer)
                                Webhook(describeUrlWebhook).send(username='mzooz', avatar_url=(client.user.avatar.url), embed=lowPlayers)
                            else:
                                for p in player:
                                    if p == ' ':
                                        pass
                                    elif p == '':
                                        pass
                                    else:
                                        desPlayers.append(p)
                                else:
                                    return ' '

            jh = await client.wait_for('message', check=playersToPlayDescribe)
            await jh.delete()
            DATA[str(ctx.guild.id)][adm] = {}
            DATA[str(ctx.guild.id)][adm]['leader'] = describeleader
            DATA[str(ctx.guild.id)][adm]['allow'] = []
            with open(gamesjson, 'w') as (f):
                json.dump(DATA, f)
                f.close()

        for desplayer in desPlayers:
            desPlayerId = desplayer.replace('@', '')
            desPlayerId = desPlayerId.replace('<', '')
            desPlayerId = desPlayerId.replace('>', '')
            desPlayerId = desPlayerId.replace('!', '')
            try:
                if len(describePlayers) < 12:
                    user = await client.fetch_user(desPlayerId)
                    Added = discord.Embed(title='**اوصف - describe**', description=f"تم اضافتك للعبة من قبل  <@{describeleader}>", color=(assist.embedColors.green))
                    Added.set_author(name='mzooz bot', icon_url=(client.user.avatar.url), url=assist.mzo0zServer)
                    Added.timestamp = datetime.datetime.now()
                    Added.set_footer(text=f"{ctx.guild.name} ", icon_url=(client.user.avatar.url))
                    done = await user.send(embed=Added, view=(fastReturn()))
                    if done:
                        if desplayer in describePlayers:
                            alreadyAdded = discord.Embed(title='**اوصف - describe**', description=f"هذا اللاعب {desplayer} مضاف بالفعل!", color=(assist.embedColors.red))
                            alreadyAdded.set_author(name='mzooz bot', icon_url=(client.user.avatar.url), url=assist.mzo0zServer)
                            alreadyAdded.timestamp = datetime.datetime.now()
                            alreadyAdded.set_footer(text=f"{ctx.guild.name} ", icon_url=(client.user.avatar.url))
                            await msg.edit(embed=alreadyAdded)
                        if desplayer not in describePlayers:
                            describePlayers.append(desplayer)
                            describePlayersN.append(str(user))
                            DATA[str(ctx.guild.id)][adm]['allow'].append(desplayer)
                            with open(gamesjson, 'w') as (f):
                                json.dump(DATA, f)
                                f.close()
                            doneAdd = discord.Embed(title='**اوصف - describe**', description=f"تم إضافة {desplayer}", color=(assist.embedColors.green))
                            doneAdd.timestamp = datetime.datetime.now()
                            doneAdd.set_footer(text=f"{ctx.guild.name} ", icon_url=(client.user.avatar.url))
                            doneAdd.set_author(name='mzooz bot', icon_url=(client.user.avatar.url), url=assist.mzo0zServer)
                            await msg.edit(embed=doneAdd)
                else:
                    fullPlayers = discord.Embed(title='**اوصف - describe**', description='لا أستطيع اضافة المزيد من اللاعبين!', color=(assist.embedColors.red))
                    fullPlayers.timestamp = datetime.datetime.now()
                    fullPlayers.set_footer(text=f"{ctx.guild.name} ", icon_url=(client.user.avatar.url))
                    fullPlayers.set_author(name='mzooz bot', icon_url=(client.user.avatar.url), url=assist.mzo0zServer)
                    await msg.edit(embed=fullPlayers)
            except:
                cantAdd = discord.Embed(title='**اوصف - describe**', description=f"لا استطيع إضافة هذا اللاعب {desplayer} لانه غير موجود او بوت, تأكد من الاسم.", color=(assist.embedColors.red))
                cantAdd.timestamp = datetime.datetime.now()
                cantAdd.set_footer(text=f"{ctx.guild.name} ", icon_url=(client.user.avatar.url))
                cantAdd.set_author(name='mzooz bot', icon_url=(client.user.avatar.url), url=assist.mzo0zServer)
                await msg.edit(embed=cantAdd)

        else:
            await msg.delete()
            num = datetime.datetime.now().microsecond
            num = str(num)[:3] + str(ctx.author.id)[:3]
            chName = f"describe-{ctx.author}"
            channel = await ctx.guild.create_text_channel(chName)
            webhooksNames = await channel.webhooks()
            webhooks = []
            for webhook in webhooksNames:
                if webhook.name == 'mzooz':
                    describeUrlWebhook = webhook.url
                webhooks.append(webhook.name)
            else:
                if 'mzooz' not in webhooks:
                    await channel.create_webhook(name='mzooz')
                    webhooksNames = await channel.webhooks()
                    for webhook in webhooksNames:
                        if webhook.name == 'mzooz':
                            describeUrlWebhook = webhook.url
                            webhooks.append(webhook.name)

            await channel.set_permissions(ctx.author, read_messages=True, send_messages=False)
            await channel.set_permissions(discord.utils.get((ctx.guild.roles), id=(int(everyone))), read_messages=False)

        for i in DATA[str(ctx.guild.id)][adm]['allow']:
            o = i.replace('!', '')
            o = o.replace('@', '')
            o = o.replace('<', '')
            o = o.replace('>', '')
            usr = await client.fetch_user(o)
            await channel.set_permissions(usr, read_messages=True, send_messages=False)
        else:
            describeChannel = channel.id
            TICKET[str(ctx.guild.id)][channel.id] = {}
            TICKET[str(ctx.guild.id)][channel.id]['msg'] = channel.id
            TICKET[str(ctx.guild.id)][channel.id]['leader'] = adm
            with open(assist.tickjson, 'w') as (f):
                json.dump(TICKET, f)
                f.close()
            ich = await channel.create_invite(max_age=300)
            bdt = discord.Embed(title='**اوصف - describe**', description='اللعبة بدأت في هذا الروم', color=(assist.embedColors.red))
            bdt.timestamp = datetime.datetime.now()
            bdt.set_footer(text=f"{ctx.guild.name} ", icon_url=(client.user.avatar.url))
            bdt.set_author(name='mzooz bot', icon_url=(client.user.avatar.url), url=assist.mzo0zServer)

            class fastGo(discord.ui.View):
                @discord.ui.button(style=(discord.ButtonStyle.green), label='انتقال سريع', row=0, url=(str(ich)))
                async def BACK(self, button: discord.ui.Button, interaction: discord.Interaction):
                    pass

            await ctx.channel.send(embed=bdt, view=(fastGo()), delete_after=5)

            class describeOptions(discord.ui.Select):
                def __init__(self):
                    options = [
                     discord.SelectOption(label='دول', value='1'),
                     discord.SelectOption(label='حيوانات', value='2'),
                     discord.SelectOption(label='اجهزة', value='3'),
                     discord.SelectOption(label='اشخاص', value='4')]
                    super().__init__(placeholder='اختار المود', max_values=1, min_values=1, options=options)

                async def callback(self, interaction):
                    global describechoose
                    if interaction.user.id != describeleader:
                        pass
                    else:
                        describechoose = self.values[0]
                        modew = discord.Embed(title='**اوصف - describe**', description=f"**المود الي اخترته: {describemodes[self.values[0]]} ماذا تريد ان تفعل؟**", color=(assist.embedColors.blue))
                        modew.set_author(name='mzooz bot', icon_url=(client.user.avatar.url), url=assist.mzo0zServer)
                        await interaction.response.send_message(embed=modew)


            class describeView(discord.ui.View):
                def __init__(self):
                    super().__init__()
                    self.add_item(describeOptions())

            chooseMode = discord.Embed(title='**اوصف - describe**', description=f"<@{describeleader}> اختار المود:", color=assist.embedColors.teal)
            chooseMode.set_author(name='mzooz bot', icon_url=client.user.avatar.url, url=assist.mzo0zServer)
            await channel.send(stringl(describePlayers), embed=chooseMode, view=describeView())
            sleep(3)
            desPlayers = []
            await channel.purge(limit=100)
            invite = await channel.create_invite(max_age=43200)
            class fastReturn(discord.ui.View):
                @discord.ui.button(style=(discord.ButtonStyle.green), label='انتقال سريع', row=0, url=(str(invite)))
                async def BACK(self, button: discord.ui.Button, interaction: discord.Interaction):
                    pass
            describeLobby = discord.Embed(title='**اوصف - describe**', description=f"<@{describeleader}> ماذا تريد ان تفعل؟", color=0x00ff00)
            describeLobby.set_author(name='mzooz bot', icon_url=(client.user.avatar.url), url=assist.mzo0zServer)
            errorPlayers = discord.Embed(title='عدد اللاعبين', description='**لبدأ اللعبة يجب ان يكون عدد اللاعبين 2 على الاقل.**', color=(assist.embedColors.red))
            errorPlayers.set_author(name='mzooz bot', icon_url=(client.user.avatar.url), url=assist.mzo0zServer)
            class DescribeView(discord.ui.View):
                @discord.ui.button(style=(discord.ButtonStyle.green), label='بدء جولة جديدة', row=0)
                async def describeStartGameCallBack(self, button, interaction):
                    if interaction.user.id == describeleader:
                        if interaction.channel.id == describeChannel:
                            await startDescribeGame()

                @discord.ui.button(style=(discord.ButtonStyle.blurple), label='إضافة لاعبين', row=0)
                async def outstoryAddPlayersCallBack(self, button, interaction):
                    if interaction.user.id == describeleader:
                        if interaction.channel.id == describeChannel:
                            await channel.set_permissions(ctx.author, read_messages=True, send_messages=True)
                            await addPlayersToDescribe()

                @discord.ui.button(style=(discord.ButtonStyle.red), label='حذف لاعبين', row=0)
                async def outstoryDelPlayersCallBack(self, button, interaction):
                    if interaction.user.id == describeleader:
                        if interaction.channel.id == describeChannel:
                            await channel.set_permissions(ctx.author, read_messages=True, send_messages=True)
                            await describeDelPlayers()

                @discord.ui.button(style=(discord.ButtonStyle.green), label='تغيير المود', row=1)
                async def outstoryChangeModeCallBack(self, button, interaction):
                    if interaction.user.id == describeleader:
                        if interaction.channel.id == describeChannel:
                            await describeChangeMode()

                @discord.ui.button(style=(discord.ButtonStyle.blurple), label='إظهار اللاعبين', row=1)
                async def outstoryShowPlayersCallBack(self, button, interaction):
                    if interaction.user.id == describeleader:
                        if interaction.channel.id == describeChannel:
                            await channel.send(embed=(showPlayers()))

                @discord.ui.button(style=(discord.ButtonStyle.red), label='إنهاء اللعبة', row=1, custom_id=(channel.id))
                async def outstoryEndGameCallBack(self, button, interaction):
                    if interaction.user.id == describeleader or interaction.user.id == MZO0Z:
                        if interaction.channel.id == describeChannel:
                            await channel.purge(limit=100)
                            await endDescribeGame()

        await channel.send(embed=describeLobby, view=DescribeView())


    async def addPlayersToDescribe():
        try:
            if len(describePlayers) < 12:
                addPlayer = discord.Embed(title='**اوصف - describe**', description=f"<@{describeleader}> منشن اللاعبين المراد إضافتهم", color=(assist.embedColors.yellow))
                addPlayer.set_author(name='mzooz bot', icon_url=(client.user.avatar.url), url=assist.mzo0zServer)
                await channel.send(embed=addPlayer)
                desPlayers = []

                def playersToPlayDescribe(m):
                    player = m.content
                    if player:
                        if m.channel.id == describeChannel:
                            if m.author.id != describeleader:
                                pass
                            elif m.author.id == describeleader:
                                player = player.split(' ')
                                for p in player:
                                    if p == ' ':
                                        pass
                                    elif p == '':
                                        pass
                                    else:
                                        desPlayers.append(p)
                                else:
                                    return ' '

                await client.wait_for('message', check=playersToPlayDescribe)
                for playerToAddInDescribe in desPlayers:
                    describePlayerIdToAdd = playerToAddInDescribe.replace('@', '')
                    describePlayerIdToAdd = describePlayerIdToAdd.replace('<', '')
                    describePlayerIdToAdd = describePlayerIdToAdd.replace('>', '')
                    describePlayerIdToAdd = describePlayerIdToAdd.replace('!', '')
                    if playerToAddInDescribe == '':
                        pass
                    else:
                        user = await client.fetch_user(describePlayerIdToAdd)
                        Added = discord.Embed(title='**اوصف - describe**', description=f"تم اضافتك للعبة من قبل <@{describeleader}>", color=(assist.embedColors.green))
                        Added.timestamp = datetime.datetime.now()
                        Added.set_footer(text=f"{ctx.guild.name} ", icon_url=(client.user.avatar.url))
                        Added.set_author(name='mzooz bot', icon_url=(client.user.avatar.url), url=assist.mzo0zServer)
                        done = await user.send(embed=Added, view=(fastReturn()))

                if done:
                    if playerToAddInDescribe in describePlayers:
                        alreadyAdded = discord.Embed(title='**اوصف - describe**', description=f"هذا اللاعب {playerToAddInDescribe} مضاف بالفعل!", color=(assist.embedColors.red))
                        alreadyAdded.set_author(name='mzooz bot', icon_url=(client.user.avatar.url), url=assist.mzo0zServer)
                        alreadyAdded.timestamp = datetime.datetime.now()
                        alreadyAdded.set_footer(text=f"{ctx.guild.name} ", icon_url=(client.user.avatar.url))
                        await channel.send(embed=alreadyAdded)
                    if playerToAddInDescribe not in describePlayers:
                        describePlayers.append(playerToAddInDescribe)
                        describePlayersN.append(str(user))
                        doneAdd = discord.Embed(title='**اوصف - describe**', description=f"تم إضافة {playerToAddInDescribe}", color=(assist.embedColors.green))
                        doneAdd.timestamp = datetime.datetime.now()
                        doneAdd.set_footer(text=f"{ctx.guild.name} ", icon_url=(client.user.avatar.url))
                        doneAdd.set_author(name='mzooz bot', icon_url=(client.user.avatar.url), url=assist.mzo0zServer)
                        await channel.purge(limit=100)
                        await channel.send(embed=doneAdd, view=(DescribeView()))
            else:
                fullPlayers = discord.Embed(title='**اوصف - describe**', description='لا أستطيع اضافة المزيد من اللاعبين!', color=(assist.embedColors.red))
                fullPlayers.timestamp = datetime.datetime.now()
                fullPlayers.set_footer(text=f"{ctx.guild.name} ", icon_url=(client.user.avatar.url))
                fullPlayers.set_author(name='mzooz bot', icon_url=(client.user.avatar.url), url=assist.mzo0zServer)
                await channel.send(embed=fullPlayers)
        except:
            cantAdd = discord.Embed(title='**اوصف - describe**', description=f"لا استطيع إضافة هذا اللاعب {playerToAddInDescribe} لانه غير موجود او بوت, تأكد من الاسم.", color=(assist.embedColors.red))
            cantAdd.set_author(name='mzooz bot', icon_url=(client.user.avatar.url), url=assist.mzo0zServer)
            await channel.send(embed=cantAdd)
        await channel.set_permissions(ctx.author, read_messages=True, send_messages=False)

    async def describeDelPlayers():
        delPlayer = discord.Embed(title='**اوصف - describe**', description=f"<@{describeleader}> منشن اللاعبين المراد طردهم", color=(assist.embedColors.yellow))
        delPlayer.set_author(name='mzooz bot', icon_url=(client.user.avatar.url), url=assist.mzo0zServer)
        await channel.send(embed=delPlayer)
        desPlayers = []

        def playersToPlayDescribe(m):
            player = m.content
            if player:
                if m.channel.id == describeChannel:
                    if m.author.id != describeleader:
                        pass
                    elif m.author.id == describeleader:
                        player = player.split(' ')
                        for p in player:
                            if p == ' ':
                                pass
                            elif p == '':
                                pass
                            else:
                                desPlayers.append(p)
                        else:
                            return ' '

        await client.wait_for('message', check=playersToPlayDescribe)
        for playerToDelFromDescribe in desPlayers:
            if playerToDelFromDescribe in describePlayers:
                describePlayers.remove(playerToDelFromDescribe)
                describePlayerIdToDel = playerToDelFromDescribe.replace('@', '')
                describePlayerIdToDel = describePlayerIdToDel.replace('<', '')
                describePlayerIdToDel = describePlayerIdToDel.replace('>', '')
                describePlayerIdToDel = describePlayerIdToDel.replace('!', '')
                user = await client.fetch_user(describePlayerIdToDel)
                describePlayersN.remove(str(user))
                doneDel = discord.Embed(title='**اوصف - describe**', description=f"تم حذف {playerToDelFromDescribe}!", color=(assist.embedColors.blurple))
                doneDel.set_author(name='mzooz bot', icon_url=(client.user.avatar.url), url=assist.mzo0zServer)
                await channel.set_permissions(user, read_messages=True)
                await channel.send(embed=doneDel)
            else:
                notHere = discord.Embed(title='**اوصف - describe**', description=f"هذا اللاعب غير موجود {playerToDelFromDescribe}", color=(assist.embedColors.red))
                notHere.set_author(name='mzooz bot', icon_url=(client.user.avatar.url), url=assist.mzo0zServer)
                await channel.send(embed=notHere)
        await channel.set_permissions(ctx.author, read_messages=True, send_messages=False)
        await channel.purge(limit=100)
        await channel.send(embed=(showPlayers()), view=(DescribeView()))

    def showPlayers():
        playersAre = discord.Embed(title='**اوصف - describe**', description='هؤلاء هم اللاعبين:', color=(assist.embedColors.dark_purple))
        playersAre.set_author(name='mzooz bot', icon_url=(client.user.avatar.url), url=assist.mzo0zServer)
        playersAre.add_field(name=(stringl(describePlayersN)), value='** **', inline=True)
        return playersAre

    async def describeChangeMode():
        await channel.purge(limit=100)

        class newDescribeOptions(discord.ui.Select):

            def __init__(self):
                options = [
                    discord.SelectOption(label='دول', value='1'),
                    discord.SelectOption(label='حيوانات', value='2'),
                    discord.SelectOption(label='اجهزة', value='3'),
                    discord.SelectOption(label='اشخاص', value='4')]
                super().__init__(placeholder='اختار المود', max_values=1, min_values=1, options=options)


            async def callback(self, interaction):
                global describechoose
                if interaction.user.id != describeleader:
                    pass
                else:
                    describechoose = self.values[0]
                    mode = discord.Embed(title='**اوصف - describe**', description=f"**المود الي اخترته: {describemodes[self.values[0]]}\n<@{describeleader}> ماذا تريد ان تفعل؟**", color=(assist.embedColors.purple))
                    mode.set_author(name='mzooz bot', icon_url=(client.user.avatar.url), url=assist.mzo0zServer)
                    await channel.purge(limit=100)
                    await interaction.response.send_message(embed=mode, view=(DescribeView()))

        class newDescribeView(discord.ui.View):

            def __init__(self):
                super().__init__()
                self.add_item(newDescribeOptions())

        try:
            await channel.purge(limit=100)
        except:
            pass
        else:
            chooseMode = discord.Embed(title='**اوصف - describe**', description=f"<@{describeleader}> اختار المود:", color=(assist.embedColors.teal))
            chooseMode.set_author(name='mzooz bot', icon_url=(client.user.avatar.url), url=assist.mzo0zServer)
            await channel.send(embed=chooseMode, view=(newDescribeView()))

    async def startDescribeGame():
        unRepeat = []
        if len(describePlayers) < 2:
            await channel.purge(limit=100)
            await channel.send(embed=errorPlayers, view=(DescribeView()))
        else:
            await channel.purge(limit=100)
            for mode in MODES[str(describechoose)]:
                unRepeat.append(mode)
            else:
                if len(unRepeat) == 3:
                    for mode in MODES[str(describechoose)]:
                        unRepeat.append(mode)

                describeIs = random.choice(unRepeat)
                unRepeat.remove(describeIs)
                describerIs = random.choice(describePlayers)
                pdid = describerIs.replace('@', '')
                pdid = pdid.replace('<', '')
                pdid = pdid.replace('>', '')
                pdid = pdid.replace('!', '')
                user = await client.fetch_user(pdid)
                describePlayer = discord.Embed(title='**اوصف - describe**', description=f"اوصف لهم **{describeIs}** بدون لاتذكر الاسم", color=(assist.embedColors.blue))
                describePlayer.set_author(name='mzooz bot', icon_url=(client.user.avatar.url), url=assist.mzo0zServer)
                describeWith = discord.Embed(title='**اوصف - describe**', description=f"الوصف عند **{describerIs}**", color=(assist.embedColors.blue))
                describeWith.set_author(name='mzooz bot', icon_url=(client.user.avatar.url), url=assist.mzo0zServer)

            await user.send(embed=describePlayer, view=(fastReturn()))
            await channel.send(embed=describeWith, view=(DescribeView()))

    async def endDescribeGame():
        global describebool
        if channel.id == describeChannel:
            if ctx.author.id == describeleader:
                describebool = False
                return 0


def stringl(tup):
    str = ''
    for item in tup:
        str = str + item + '\n'
    else:
        return str


def restartdescribe():
    global describeGameStarted
    global describePlayers
    global describePlayersN
    global describebool
    global describechoose
    global describeleader
    global unRepeat
    describePlayersN = []
    unRepeat = []
    describeGameStarted = False
    describebool = False
    describeleader = ''
    describePlayers = []
    describechoose = ''
    return ' '
