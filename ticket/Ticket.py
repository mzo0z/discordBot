from time import sleep
import discord
import datetime
import assist
import json
import requests
from . import scripts

embedToSend = None
em = None
roles = []

def load(file):
    with open(file, 'r') as f:
        DATA = json.load(f)
    return DATA
def dump(file, DATA):
    with open(file, 'w') as f:
        json.dump(DATA, f)
        f.close()
    return

async def create(ctx, client):
    names = []
    global roles
    roles = []
    global embedToSend
    global em
    FEILDS = {}
    global thumbnailUrl
    global photoUrl
    thumbnailUrl = None
    photoUrl = None
    await ctx.message.delete()
    with open(scripts.jsonFile, 'r') as ff:
        TICKET = json.load(ff)

    if str(ctx.guild.id) not in TICKET:
        TICKET[str(ctx.guild.id)] = {}
        TICKET[str(ctx.guild.id)]["tickets"] = {}
        TICKET[str(ctx.guild.id)]["category"] = 0
        dump(scripts.jsonFile, TICKET)

    embedToSend = discord.Embed(title='(العنوان)', description='ماهو عنوان التيكت الذي تريده (الوصف)', color=assist.embedColors.ligh_green)
    embedToSend.set_author(name='mzooz ticket bot', icon_url=client.user.avatar.url, url=assist.mzo0zServer)
    try:embedToSend.set_footer(text=ctx.author, icon_url=ctx.author.avatar.url)
    except:embedToSend.set_footer(text=ctx.author, icon_url=ctx.author.default_avatar.url)

    em = await ctx.channel.send(embed=embedToSend)
    def titleCheck(m):return m.author == ctx.author and m.channel == ctx.channel
    r = await client.wait_for('message', check=titleCheck)
    title = r.content
    await r.delete()
    embedToSend = discord.Embed(title=title, description='ماهو وصف التيكت الذي تريده (الوصف)', color=assist.embedColors.ligh_green)
    embedToSend.set_author(name='mzooz ticket bot', icon_url=client.user.avatar.url, url=assist.mzo0zServer)
    try:embedToSend.set_footer(text=ctx.author, icon_url=ctx.author.avatar.url)
    except:embedToSend.set_footer(text=ctx.author, icon_url=ctx.author.default_avatar.url)

    em = await em.edit(embed=embedToSend)

    def descrCheck(m):return m.author == ctx.author and m.channel == ctx.channel
    d = await client.wait_for('message', check=descrCheck)
    describtion = d.content
    DESCRIPTION = describtion
    await d.delete()
    embedToSend = discord.Embed(title=title, description=describtion, color=assist.embedColors.ligh_green)
    try:embedToSend.set_footer(text=ctx.author, icon_url=ctx.author.avatar.url)
    except:embedToSend.set_footer(text=ctx.author, icon_url=ctx.author.default_avatar.url)
    embedToSend.set_author(name='mzooz ticket bot', icon_url=client.user.avatar.url, url=assist.mzo0zServer)

    async def addButtonCallBack(interaction):
        if interaction.user.id == ctx.author.id:
            addLine.disabled = True
            addRoles.disabled = True
            addPhoto.disabled = True
            createIt.disabled = True
            addThumb.disabled = True
            canceleIt.disabled = True
            addButton.disabled = True
            global embedToSend
            global em
            dd = discord.Embed(title=title, description=describtion, color=assist.embedColors.ligh_green)
            try:dd.set_footer(text=ctx.author, icon_url=ctx.author.avatar.url)
            except:dd.set_footer(text=ctx.author, icon_url=ctx.author.default_avatar.url)
            dd.set_author(name='mzooz ticket bot', icon_url=client.user.avatar.url, url=assist.mzo0zServer)
            dd.add_field(name='مااسم الزر الذي تريد إضافته', value='ملاحظة: لن تستطيع رؤية الزر الا بعد إنشاء التيكت')
            await interaction.response.edit_message(embed=dd, view=embedView)

            def nameCheck(m):return m.author == ctx.author and m.channel == ctx.channel
            d = await client.wait_for('message', check=nameCheck)
            buttonName = d.content
            names.append(str(buttonName).replace(" ", "[SPACE]"))
            await d.delete()
            addLine.disabled = False
            addRoles.disabled = False
            addPhoto.disabled = False
            createIt.disabled = False
            addThumb.disabled = False
            canceleIt.disabled = False
            addButton.disabled = False
            
            await interaction.message.edit(embed=embedToSend, view=embedView)

    async def addLineCallBack(interaction):
        if interaction.user.id == ctx.author.id:
            addLine.disabled = True
            addRoles.disabled = True
            addPhoto.disabled = True
            createIt.disabled = True
            addThumb.disabled = True
            canceleIt.disabled = True
            addButton.disabled = True
            global embedToSend
            global em
            dd = discord.Embed(title=title, description=describtion, color=assist.embedColors.ligh_green)
            try:dd.set_footer(text=ctx.author, icon_url=ctx.author.avatar.url)
            except:dd.set_footer(text=ctx.author, icon_url=ctx.author.default_avatar.url)
            dd.set_author(name='mzooz ticket bot', icon_url=client.user.avatar.url, url=assist.mzo0zServer)
            dd.add_field(name='(الاسم)', value='ماهو وصف التيكت الذي تريده (الوصف)')
            await interaction.response.edit_message(embed=dd, view=embedView)

            def fieldCheck(m):return m.author == ctx.author and m.channel == ctx.channel
            d = await client.wait_for('message', check=fieldCheck)
            fieldName = d.content
            await d.delete()
            dd = discord.Embed(title=title, description=describtion, color=assist.embedColors.ligh_green)
            try:dd.set_footer(text=ctx.author, icon_url=ctx.author.avatar.url)
            except:dd.set_footer(text=ctx.author, icon_url=ctx.author.default_avatar.url)
            dd.set_author(name='mzooz ticket bot', icon_url=client.user.avatar.url, url=assist.mzo0zServer)
            dd.add_field(name=fieldName, value='ماهو وصف التيكت الذي تريده (الوصف)')
            await interaction.message.edit(embed=dd)
            def valueCheck(m):return m.author == ctx.author and m.channel == ctx.channel
            d = await client.wait_for('message', check=valueCheck)
            valueName = d.content
            await d.delete()
            embedToSend.add_field(name=fieldName, value=valueName, inline=False)
            addLine.disabled = False
            addRoles.disabled = False
            addPhoto.disabled = False
            createIt.disabled = False
            addThumb.disabled = False
            canceleIt.disabled = False
            addButton.disabled = False
            FEILDS.update({fieldName:valueName})
            await interaction.message.edit(embed=embedToSend, view=embedView)

    async def addRolesCallBack(interaction):
        if interaction.user.id == ctx.author.id:
            addLine.disabled = True
            addRoles.disabled = True
            addPhoto.disabled = True
            createIt.disabled = True
            addThumb.disabled = True
            canceleIt.disabled = True
            addButton.disabled = True

            global embedToSend
            global em

            dd = discord.Embed(title=title, description=describtion, color=assist.embedColors.ligh_green)
            try:dd.set_footer(text=ctx.author, icon_url=ctx.author.avatar.url)
            except:dd.set_footer(text=ctx.author, icon_url=ctx.author.default_avatar.url)
            dd.set_author(name='mzooz ticket bot', icon_url=client.user.avatar.url, url=assist.mzo0zServer)
            dd.add_field(name='**:small_red_triangle:منشن جميع الرتب المسموح لها بالرد في هذا التيكت:small_red_triangle: **', value='** **')
            await interaction.message.edit(embed=dd, view=embedView)

            def ju(m):return m.author == ctx.author and m.channel == ctx.channel
            d = await client.wait_for('message', check=ju)
            ju = d.content
            await d.delete()
            for i in ju.split(' '):
                h = i.replace('!', '')
                h = h.replace('@', '')
                h = h.replace('<', '')
                h = h.replace('>', '')
                h = h.replace('&', '')
                roles.append(h)

            embed = discord.Embed(title='نجحت', description=f'\n{roles}تم السماح لهذه الرتب بالرد في هذا التيكت', color=assist.embedColors.green)
            embed.set_author(name='mzooz ticket bot', icon_url=client.user.avatar.url, url=assist.mzo0zServer)
            try:embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar.url)
            except:embed.set_footer(text=ctx.author, icon_url=ctx.author.default_avatar.url)
            addLine.disabled = False
            addRoles.disabled = False
            addPhoto.disabled = False
            createIt.disabled = False
            addThumb.disabled = False
            canceleIt.disabled = False
            addButton.disabled = False
            await interaction.message.edit(embed=dd, view=embedView)
            await ctx.channel.send(embed=embed, delete_after=3)

    async def addPhotoCallBack(interaction):
        if interaction.user.id == ctx.author.id:
            addLine.disabled = True
            addRoles.disabled = True
            addPhoto.disabled = True
            createIt.disabled = True
            addThumb.disabled = True
            canceleIt.disabled = True
            addButton.disabled = True
            global embedToSend
            global em
            global photoUrl
            dd = discord.Embed(title=title, description=describtion, color=assist.embedColors.ligh_green)
            try:dd.set_footer(text=ctx.author, icon_url=ctx.author.avatar.url)
            except:dd.set_footer(text=ctx.author, icon_url=ctx.author.default_avatar.url)
            dd.set_author(name='mzooz ticket bot', icon_url=client.user.avatar.url, url=assist.mzo0zServer)
            dd.add_field(name='ارسل رابط الصورة', value='** **')
            await interaction.message.edit(embed=dd, view=embedView)
            def photoCheck(m):return m.author == ctx.author and m.channel == ctx.channel
            d = await client.wait_for('message', check=photoCheck)
            photoUrl = d.content
            await d.delete()
            try:code = requests.get(photoUrl).status_code
            except:code = 404
            if code !=200:
                embed = discord.Embed(description=f'هذا الرابط غير فعال {photoUrl} تأكد من الرابط واعد المحاولة', color=assist.embedColors.red)
                embed.set_author(name='mzooz ticket bot', icon_url=client.user.avatar.url, url=assist.mzo0zServer)
                try:embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar.url)
                except:embed.set_footer(text=ctx.author, icon_url=ctx.author.default_avatar.url)
                photoUrl = None
                await ctx.channel.send(embed=embed, delete_after=3)
            else:
                embedToSend.set_image(url=photoUrl)
                await interaction.message.edit(embed=embedToSend, view=embedView)

            addLine.disabled = False
            addRoles.disabled = False
            addPhoto.disabled = False
            createIt.disabled = False
            addThumb.disabled = False
            canceleIt.disabled = False
            addButton.disabled = False
            await interaction.message.edit(embed=embedToSend, view=embedView)

    async def createItCallBack(interaction):
        if interaction.user.id == ctx.author.id:
            global embedToSend
            global em
            global photoUrl
            global thumbnailUrl
            embedToSend.timestamp = datetime.datetime.now()
            view = discord.ui.View()
            btns = []
            if len(names) == 0:
                num = datetime.datetime.now().microsecond
                num = str(num)[:3] + str(interaction.user.id)[:3]
                chName = f'{title}_{num}'
                op = discord.ui.Button(style=discord.ButtonStyle.blurple, label=title.replace('[SPACE]', ' '), custom_id=chName)
                view.add_item(op)
                btns.append(chName)
            else:
                for i in names:
                    num = datetime.datetime.now().microsecond
                    num = str(num)[:3] + str(interaction.user.id)[:3]
                    chName = f'{i}_{num}'
                    op = discord.ui.Button(style=discord.ButtonStyle.blurple, label=i.replace('[SPACE]', ' '), custom_id=chName)
                    view.add_item(op)
                    btns.append(chName)

            bt = await ctx.channel.send(embed=embedToSend, view=view)
            
            for i in btns:
                if len(names) == 0:
                    TICKET[str(ctx.guild.id)]['tickets'][str(i)] = {}
                    TICKET[str(ctx.guild.id)]['tickets'][str(i)]["msg"] = str(bt)
                    TICKET[str(ctx.guild.id)]['tickets'][str(i)]["allow"] = roles
                    TICKET[str(ctx.guild.id)]['tickets'][str(i)]["title"] = title
                    TICKET[str(ctx.guild.id)]['tickets'][str(i)]["description"] = DESCRIPTION
                    TICKET[str(ctx.guild.id)]['tickets'][str(i)]["author"] = str(ctx.author)
                    try:TICKET[str(ctx.guild.id)]['tickets'][str(i)]["avatar"] = str(ctx.author.avatar.url)
                    except:TICKET[str(ctx.guild.id)]['tickets'][str(i)]["avatar"] = str(ctx.author.default_avatar.url)
                    TICKET[str(ctx.guild.id)]['tickets'][str(i)]["thumbnail"] = thumbnailUrl
                    TICKET[str(ctx.guild.id)]['tickets'][str(i)]["photo"] = photoUrl
                    TICKET[str(ctx.guild.id)]['tickets'][str(i)]["feilds"] = FEILDS
                    TICKET[str(ctx.guild.id)]['tickets'][str(i)]["custom_id"] = i
                    TICKET[str(ctx.guild.id)]['tickets'][str(i)]["button"] = i[:i.find("_")]
                    TICKET[str(ctx.guild.id)]['tickets'][str(i)]["channelId"] = bt.channel.id
                    TICKET[str(ctx.guild.id)]['tickets'][str(i)]["messageId"] = bt.id
                    TICKET[str(ctx.guild.id)]['tickets'][str(i)]["guildId"] = ctx.guild.id
                else:
                    TICKET[str(ctx.guild.id)]['tickets'][str(i)] = {}
                    TICKET[str(ctx.guild.id)]['tickets'][str(i)]["msg"] = str(bt)
                    TICKET[str(ctx.guild.id)]['tickets'][str(i)]["allow"] = roles
                    TICKET[str(ctx.guild.id)]['tickets'][str(i)]["title"] = title
                    TICKET[str(ctx.guild.id)]['tickets'][str(i)]["description"] = DESCRIPTION
                    TICKET[str(ctx.guild.id)]['tickets'][str(i)]["author"] = str(ctx.author)
                    try:TICKET[str(ctx.guild.id)]['tickets'][str(i)]["avatar"] = str(ctx.author.avatar.url)
                    except:TICKET[str(ctx.guild.id)]['tickets'][str(i)]["avatar"] = str(ctx.author.default_avatar.url)
                    TICKET[str(ctx.guild.id)]['tickets'][str(i)]["thumbnail"] = thumbnailUrl
                    TICKET[str(ctx.guild.id)]['tickets'][str(i)]["photo"] = photoUrl
                    TICKET[str(ctx.guild.id)]['tickets'][str(i)]["feilds"] = FEILDS
                    TICKET[str(ctx.guild.id)]['tickets'][str(i)]["custom_id"] = i
                    TICKET[str(ctx.guild.id)]['tickets'][str(i)]["button"] = i[:i.find("_")]
                    TICKET[str(ctx.guild.id)]['tickets'][str(i)]["channelId"] = bt.channel.id
                    TICKET[str(ctx.guild.id)]['tickets'][str(i)]["messageId"] = bt.id
                    TICKET[str(ctx.guild.id)]['tickets'][str(i)]["guildId"] = ctx.guild.id
                        

            with open(scripts.jsonFile, 'w') as f:
                json.dump(TICKET, f)
                f.close()

            embed = discord.Embed(title='نجحت', description=f'تم إنشاء التيكت بنجاح', color=assist.embedColors.green)
            embed.set_author(name='mzooz ticket bot', icon_url=client.user.avatar.url, url=assist.mzo0zServer)
            try:embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar.url)
            except:embed.set_footer(text=ctx.author, icon_url=ctx.author.default_avatar.url)
            await em.delete()
            await ctx.channel.send(embed=embed, delete_after=2)


    async def addThumbCallBack(interaction):
        if interaction.user.id == ctx.author.id:
            addLine.disabled = True
            addRoles.disabled = True
            addPhoto.disabled = True
            createIt.disabled = True
            addThumb.disabled = True
            canceleIt.disabled = True
            addButton.disabled = True
            global embedToSend
            global em
            global thumbnailUrl
            dd = discord.Embed(title=title, description=describtion, color=assist.embedColors.ligh_green)
            try:dd.set_footer(text=ctx.author, icon_url=ctx.author.avatar.url)
            except:dd.set_footer(text=ctx.author)
            dd.set_author(name='mzooz ticket bot', icon_url=client.user.avatar.url, url=assist.mzo0zServer)
            dd.add_field(name='ارسل رابط الثامنيل', value='** **')
            await interaction.message.edit(embed=dd, view=embedView)
            def photoCheck(m):return m.author == ctx.author and m.channel == interaction.message.channel
            d = await client.wait_for('message', check=photoCheck)
            thumbnailUrl = d.content
            await d.delete()
            try:code = requests.get(thumbnailUrl).status_code
            except:code = 404
            if code !=200:
                embed = discord.Embed(description=f'هذا الرابط غير فعال {thumbnailUrl} تأكد من الرابط واعد المحاولة', color=assist.embedColors.red)
                embed.set_author(name='mzooz ticket bot', icon_url=client.user.avatar.url, url=assist.mzo0zServer)
                try:embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar.url)
                except:embed.set_footer(text=ctx.author, icon_url=ctx.author.default_avatar.url)
                await ctx.channel.send(embed=embed, delete_after=3)
            else:
                embedToSend.set_thumbnail(url=thumbnailUrl)
                await interaction.message.edit(embed=embedToSend, view=embedView)
            addLine.disabled = False
            addRoles.disabled = False
            addPhoto.disabled = False
            createIt.disabled = False
            addThumb.disabled = False
            canceleIt.disabled = False
            addButton.disabled = False
            await interaction.message.edit(embed=embedToSend, view=embedView)


    async def canceleItCallBack(interaction):
        if interaction.user.id == ctx.author.id:
            global em
            dd = discord.Embed(title='إلغاء', description='تم الغاء التيكت', color=assist.embedColors.red)
            try:dd.set_footer(text=ctx.author, icon_url=ctx.author.avatar.url)
            except:dd.set_footer(text=ctx.author, icon_url=ctx.author.default_avatar.url)
            dd.timestamp = datetime.datetime.now()
            dd.set_author(name='mzooz ticket bot', icon_url=client.user.avatar.url)
            await interaction.message.edit(embed=dd, view=None, delete_after=3)

    embedView = discord.ui.View()
    addLine = discord.ui.Button(style=discord.ButtonStyle.blurple, label='اضف سطر جديد', row=0)
    addLine.callback = addLineCallBack
    embedView.add_item(addLine)

    addRoles = discord.ui.Button(style=discord.ButtonStyle.blurple, label='اضافة رتب لهم الصلاحية برؤية القناة', row=0)
    addRoles.callback = addRolesCallBack
    embedView.add_item(addRoles)


    addPhoto = discord.ui.Button(style=discord.ButtonStyle.green, label='اضف صورة', row=0)
    addPhoto.callback = addPhotoCallBack
    embedView.add_item(addPhoto)


    createIt = discord.ui.Button(style=discord.ButtonStyle.blurple, label='إنشاء', row=1)
    createIt.callback = createItCallBack
    embedView.add_item(createIt)

    addThumb = discord.ui.Button(style=discord.ButtonStyle.blurple, label='اضف ثامنيل', row=1)
    addThumb.callback = addThumbCallBack
    embedView.add_item(addThumb)

    addButton = discord.ui.Button(style=discord.ButtonStyle.green, label='اضف زر', row=1)
    addButton.callback = addButtonCallBack
    embedView.add_item(addButton)


    canceleIt = discord.ui.Button(style=discord.ButtonStyle.red, label='إلغاء', row=1)
    canceleIt.callback = canceleItCallBack
    embedView.add_item(canceleIt)

    em = await em.edit(embed=embedToSend, view=embedView)





async def afterDelete(client, ticket, guildId):
    embed = discord.Embed(title=ticket["title"], description=ticket["description"], timestamp=datetime.datetime.now(), color=assist.embedColors.ligh_green)
    embed.set_author(name='mzooz ticket bot', url=assist.mzo0zServer, icon_url=client.user.avatar.url)
    try:embed.set_footer(text=ticket['author'], icon_url=ticket["avatar"])
    except:embed.set_footer(text=ticket["author"])
    if ticket['photo'] != None:
        try:embed.set_image(url=ticket['photo'])
        except:pass
    if ticket['thumbnail'] != None:
        try:embed.set_thumbnail(url=ticket['thumbnail'])
        except:pass

    try:
        for feild in ticket['feilds'].keys():
            try:embed.add_field(name=feild, value=ticket['feilds'][feild], inline=False)
            except:pass
    except:pass


    TICKET = load(scripts.jsonFile)
    oldView = discord.ui.View()
    oldChannel = await client.fetch_channel(int(ticket['channelId']))
    buttons = {}
    oldCids = []
    for oldCid in TICKET[str(guildId)]['tickets']:
        if ticket['msg'] == TICKET[str(guildId)]['tickets'][oldCid]['msg']:
            buttons.update({TICKET[str(guildId)]['tickets'][oldCid]['button']:oldCid})
            oldCids.append(oldCid)

    for oldButton in buttons.keys():
        if oldButton != ticket['button']:
            opp = discord.ui.Button(style=discord.ButtonStyle.blurple, label=str(oldButton).replace('[SPACE]', ' '), custom_id=buttons[oldButton])
            oldView.add_item(opp)

    oldMSG = await oldChannel.fetch_message(int(ticket["messageId"]))
    try:await oldMSG.edit(embed=embed, view=oldView)
    except:await oldMSG.edit(embed=embed)
    del TICKET[str(guildId)]['tickets'][ticket['custom_id']]
    dump(scripts.jsonFile, TICKET)



async def autoTicket(client, title='** **', description="** **", author=None, avatar=None, thumbnail="", feilds=None, allows=None, photo="", channel=None, button=None, cid=None, guildId=0, oldChannel=0, msg=None):
    embed = discord.Embed(title=title, description=description, timestamp=datetime.datetime.now(), color=assist.embedColors.ligh_green)
    embed.set_author(name='mzooz ticket bot', url=assist.mzo0zServer, icon_url=client.user.avatar.url)
    try:embed.set_footer(text=author, icon_url=avatar)
    except:embed.set_footer(text=author)
    if photo != None:
        try:embed.set_image(url=photo)
        except:pass
    if thumbnail != None:
        try:embed.set_thumbnail(url=thumbnail)
        except:pass

    try:
        for feild in feilds.keys():
            try:embed.add_field(name=feild, value=feilds[feild], inline=False)
            except:pass
    except:pass


    TICKET = load(scripts.jsonFile)
    view = discord.ui.View()
    oldView = discord.ui.View()
    channel = await client.fetch_channel(int(channel))
    oldChannel = await client.fetch_channel(int(oldChannel))

    buttons = {}
    oldCids = []
    for oldCid in TICKET[str(guildId)]['tickets']:
        if msg == TICKET[str(guildId)]['tickets'][oldCid]['msg']:
            buttons.update({TICKET[str(guildId)]['tickets'][oldCid]['button']:oldCid})
            oldCids.append(oldCid)

    for oldButton in buttons.keys():
        if oldButton != button:
            opp = discord.ui.Button(style=discord.ButtonStyle.blurple, label=str(oldButton).replace('[SPACE]', ' '), custom_id=buttons[oldButton])
            oldView.add_item(opp)

    oldMSG = await oldChannel.fetch_message(int(TICKET[str(guildId)]['tickets'][cid]["messageId"]))
    try:oldMsg = await oldMSG.edit(embed=embed, view=oldView)
    except:oldMsg = await oldMSG.edit(embed=embed)
    del TICKET[str(guildId)]['tickets'][cid]
    dump(scripts.jsonFile, TICKET)

    for oldCid in oldCids:
        for _oldCid in TICKET[str(guildId)]['tickets']:
            if _oldCid == oldCid:
                TICKET[str(guildId)]['tickets'][_oldCid]['msg'] = str(oldMsg)

    dump(scripts.jsonFile, TICKET)

    TICKET = load(scripts.jsonFile)
    op = discord.ui.Button(style=discord.ButtonStyle.blurple, label=str(button).replace('[SPACE]', ' '), custom_id=cid)
    view.add_item(op)

    bt = await channel.send(embed=embed, view=view)
    TICKET[str(guildId)]['tickets'][cid] = {}
    TICKET[str(guildId)]['tickets'][cid]["msg"] = str(bt)
    TICKET[str(guildId)]['tickets'][cid]["allow"] = roles
    TICKET[str(guildId)]['tickets'][cid]["title"] = title
    TICKET[str(guildId)]['tickets'][cid]["description"] = description
    TICKET[str(guildId)]['tickets'][cid]["author"] = str(author)
    TICKET[str(guildId)]['tickets'][cid]["thumbnail"] = thumbnailUrl
    TICKET[str(guildId)]['tickets'][cid]["photo"] = photoUrl
    TICKET[str(guildId)]['tickets'][cid]["feilds"] = feilds
    TICKET[str(guildId)]['tickets'][cid]["custom_id"] = cid
    TICKET[str(guildId)]['tickets'][cid]["button"] = cid[:cid.find("_")]
    TICKET[str(guildId)]['tickets'][cid]["channelId"] = bt.channel.id
    TICKET[str(guildId)]['tickets'][cid]["messageId"] = bt.id
    try:   TICKET[str(guildId)]['tickets'][cid]["avatar"] = avatar
    except:TICKET[str(guildId)]['tickets'][cid]["avatar"] = None

    dump(scripts.jsonFile, TICKET)


async def opn(ctx, client, cid):
    view = discord.ui.View()
    with open(scripts.jsonFile, 'r') as f:
        TICKET = json.load(f)

    everyone = load(assist.jsonFile)['serverId']
    num = datetime.datetime.now().microsecond
    num = str(num) + str(ctx.user.id)[:3]
    chName = f'ticket-{num}'
    cat = None
    if TICKET[str(ctx.guild.id)]["category"] != 0:cat = client.get_channel(TICKET[str(ctx.guild.id)]["category"])
    try: channel = await cat.create_text_channel(chName)
    except:channel = await ctx.guild.create_text_channel(chName)
    await channel.set_permissions(ctx.user, read_messages=True)
    await channel.set_permissions(discord.utils.get(ctx.guild.roles, id=int(everyone)), read_messages=False)
    for i in TICKET[str(ctx.guild.id)]["tickets"][cid]["allow"]:
        try:await channel.set_permissions(discord.utils.get(ctx.guild.roles, id=int(i)), read_messages=True)
        except:
            try:
                usr = await client.fetch_user(int(i))
                await channel.set_permissions(usr, read_messages=True)
            except:pass

    op = discord.ui.Button(style=discord.ButtonStyle.red, label='إغلاق التيكت', row=0, custom_id=chName)
    view.add_item(op)
    TICKET[str(ctx.guild.id)][chName] = {}
    TICKET[str(ctx.guild.id)][chName]["closeTicket"] = channel.id
    with open(scripts.jsonFile, 'w') as f:
        json.dump(TICKET, f)
        f.close()

    embed = discord.Embed(title=f'إغلاق التيكت', color=assist.embedColors.red)
    embed.set_author(name='mzooz bot', icon_url=client.user.avatar.url, url=assist.mzo0zServer)
    embed.timestamp = datetime.datetime.now()
    try:embed.set_footer(text=ctx.user, icon_url=ctx.user.avatar.url)
    except:embed.set_footer(text=ctx.user)
    
    await ctx.channel.send(channel.mention, delete_after=5)
    await channel.send(f'{ctx.user.mention} فتح تيكت\n@everyone',embed=embed, view=view)


