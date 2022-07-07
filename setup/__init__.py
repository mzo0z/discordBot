import asyncio
from requests import delete
import discord
import assist
import json
import islam


from datetime import datetime
from ticket import Ticket
from discord.ext import commands


def load(file):
    with open(file, 'r') as f:
        DATA = json.load(f)
    return DATA
def dump(file, DATA):
    with open(file, 'w') as f:
        json.dump(DATA, f)
        f.close()


class start:
    def __init__(self, client):
        @client.command(aliases=['setup', 'SETUP', 'Setup', 'SetUp'])
        @commands.is_owner()
        async def setUp(ctx):
            try:await ctx.delete()
            except:await ctx.message.delete()
            global canceled
            canceled = False

            channels = {channel.id: channel.name for channel in ctx.guild.channels if channel.type == discord.ChannelType.text}
            categorys = {category.id: category.name for category in ctx.guild.channels if category.type == discord.ChannelType.category}
            roles = {role.id: role.name for role in ctx.guild.roles[::-1] if role.id != ctx.guild.id}
            gamesChannels = {ctx.guild.get_channel(i).id: ctx.guild.get_channel(i).name for i in load(assist.gamesjson)['games']['gamesChannels']}

            securityoptions = {"activeSystem": "نظام التفعيل","manageTrusted": "إدارة الموثوقين"}
            channels.update({0:">لاتعيين<"})
            categorys.update({0:">لاتعيين<"})
            setUpOptions = ['تعيين خط',"الاقتراحات","ترحيب-توديع","الرقابة","اوامر خاصة"]
            gamesoptions = {'cate': 'تعيين مجموعة للالعاب',"channel": "أضف قناة للالعاب","remChannel": "أزل قناة من قنوات الالعاب",}
            ticketoptions = {"cate": "تعيين مجموعة","move": "نقل تيكت","rem": "حذف تيكت"}
            manageOptions = {"islam":"ادارة نظام الاجر","ticket" : "ادارة التيكت","bot" : "ادارة البوت","system" : "ادارة السيستم","games" : "ادارة الالعاب", "security" : "ادارة الحماية","status" : "ادارة نظام بيانات السيرفر"}
            botoptions = ["prefix","secret key","host ip","support url","log channel"]


            #new update:
            #add function to get categorys and role
            # add getId = "url" for youtube video 
            # add functions like getChannels and setChannel

            async def getChannels(embed):
                if int(len(channels)) >= 25:
                    text = """بسبب وجود العديد من القنوات في السيرفر, لايمكن إنشاء قائمة للقنوات, من فضلك قم بنشن القناة\nاذا لاتريد اختيار قناة اكتب 0"""
                    options = [discord.SelectOption(label=0, value=0)]
                    hide = True
                else:
                    text="اختر القناة"
                    options = [discord.SelectOption(label=channels[id], value=id) for id in channels]
                    hide = False
                embed.description=text
                return embed, options, text, hide


            async def setChannel(interaction, channelType):
                def word(m):return m.author == ctx.author and m.channel == ctx.channel
                word = await client.wait_for('message', check=word)
                await word.delete()
                word = word.content
                try:
                    try:
                        if int(word)==0:id=0
                    except:
                        id = int(word[2:-1])
                        await client.fetch_channel(id)
                except:
                    embed.description="لم تمنشن القناة بشكل صحيح"
                    embed.color=assist.embedColors.red
                    await interaction.message.edit(embed=embed, view=None)
                    return

                data = load(assist.jsonFile)
                embed = discord.Embed(color=assist.embedColors.green, timestamp=datetime.now())
                embed.set_author(name='mzooz bot', icon_url=client.user.avatar.url, url=assist.mzo0zServer)
                try:embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar.url)
                except:embed.set_footer(text=ctx.author, icon_url=ctx.author.default.avatar.url)
                if channelType =='islam':
                    data['islamChannelId']=id;dump(assist.jsonFile, data)
                    if id !=0:embed.description=f"تم تعيين <#{id}> قناة الاجر";await islam.reload(client)
                    else:embed.description=f"تم إالغاء نظام الاجر"
    

                if channelType =='ticket':pass
                if channelType =='bot':pass
                if channelType =='games':pass
                if channelType =='security':pass
                

                await interaction.message.edit(embed=embed, view=None)


            class islamOptions(discord.ui.Select):
                def __init__(self, options, text, hide):
                    super().__init__(placeholder=text, max_values=1, min_values=1, options=options, disabled=hide)

                async def callback(self, interaction):
                    if interaction.user.id == ctx.author.id:
                        id = int(self.values[0])
                        data = load(assist.jsonFile)
                        data['islamChannelId']=id;dump(assist.jsonFile, data)
                        embed = discord.Embed(color=assist.embedColors.green, timestamp=datetime.now())
                        embed.set_author(name='mzooz bot', icon_url=client.user.avatar.url, url=assist.mzo0zServer)
                        try:embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar.url)
                        except:embed.set_footer(text=ctx.author, icon_url=ctx.author.default.avatar.url)
                        if id !=0:embed.description=f"تم تعيين <#{id}> قناة الاجر";await islam.reload(client)
                        else:embed.description=f"تم إالغاء نظام الاجر"
                        await interaction.response.edit_message(embed=embed, view=None)

            class islamView(discord.ui.View):
                def __init__(self, options, text, hide, *, timeout = 180):
                    super().__init__(timeout=timeout)
                    self.add_item(islamOptions(options, text, hide))
                    self.add_item(cancele())

            class cateOptions(discord.ui.Select):
                def __init__(self):
                    options = [discord.SelectOption(label=categorys[id], value=id) for id in categorys]
                    super().__init__(placeholder='اختر المجموعة المراد تعيينها', max_values=1, min_values=1, options=options)

                async def callback(self, interaction):
                    if interaction.user.id == ctx.author.id:
                        id = int(self.values[0])
                        data = load(assist.tickjson)
                        data[str(ctx.guild.id)]['category']=id;dump(assist.tickjson, data)
                        embed = discord.Embed(color=assist.embedColors.green, timestamp=datetime.now())
                        embed.set_author(name='mzooz bot', icon_url=client.user.avatar.url, url=assist.mzo0zServer)
                        try:embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar.url)
                        except:embed.set_footer(text=ctx.author, icon_url=ctx.author.default.avatar.url)
                        if id != 0: embed.description=f"تم تعيين {categorys[id]} المجموعة الرئيسية للتيكت"
                        else:embed.description=f"تم إالغاء مجموعة التيكت"
                        await interaction.response.edit_message(embed=embed, view=None)

            class cateView(discord.ui.View):
                def __init__(self, *, timeout = 180):
                    super().__init__(timeout=timeout)
                    self.add_item(cateOptions())
                    self.add_item(cancele())


            class moveToOptions(discord.ui.Select):
                def __init__(self, ticket):
                    self.ticket = ticket
                    options = [discord.SelectOption(label=channels[id], value=id) for id in channels if id != 0]
                    super().__init__(placeholder='اختر القناة المراد نقله إليها', max_values=1, min_values=1, options=options)

                async def callback(self, interaction):
                    if interaction.user.id == ctx.author.id:
                        id = int(self.values[0])
                        notDone = False
                        embed = discord.Embed(color=assist.embedColors.green, timestamp=datetime.now())
                        embed.set_author(name='mzooz bot', icon_url=client.user.avatar.url, url=assist.mzo0zServer)
                        try:embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar.url)
                        except:embed.set_footer(text=ctx.author, icon_url=ctx.author.default.avatar.url)
                        data = load(assist.tickjson)
                        ticket = data[str(ctx.guild.id)]['tickets'][self.ticket]
                        try:await Ticket.autoTicket(client=client, title=ticket["title"], description=ticket["description"], author=ticket["author"], avatar=ticket["avatar"], thumbnail=ticket["thumbnail"], feilds=ticket["feilds"], allows=ticket["allow"], photo=ticket["photo"], channel=int(id), button=ticket["button"], cid=ticket["custom_id"], guildId=ctx.guild.id, oldChannel=int(ticket["channelId"]), msg=ticket["msg"]);notDone=False
                        except:notDone=True
                        if notDone:embed.description=f"حدث خطأ اثناء نقل التيكت إلى <#{id}>"
                        else:
                            msg = self.ticket[:self.ticket.find("_")].replace("[SPACE]", ' ')
                            embed.description=f"تم نقل {msg} الى <#{id}>"
                        await interaction.response.edit_message(embed=embed, view=None)

            class moveToView(discord.ui.View):
                def __init__(self, ticket, *, timeout = 60*60):
                    super().__init__(timeout=timeout)
                    self.add_item(moveToOptions(ticket))
                    self.add_item(cancele())


            class moveOptions(discord.ui.Select):
                def __init__(self):
                    data = load(assist.tickjson)
                    tickets=data[str(ctx.guild.id)]['tickets']
                    options = [discord.SelectOption(label=ticket[:ticket.find("_")].replace("[SPACE]", ' '), value=ticket) for ticket in tickets]
                    super().__init__(placeholder='اختر التيكت المراد نقلة', max_values=1, min_values=1, options=options)

                async def callback(self, interaction):
                    if interaction.user.id == ctx.author.id:
                        id = self.values[0]
                        embed = discord.Embed(color=assist.embedColors.green, timestamp=datetime.now())
                        embed.set_author(name='mzooz bot', icon_url=client.user.avatar.url, url=assist.mzo0zServer)
                        try:embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar.url)
                        except:embed.set_footer(text=ctx.author, icon_url=ctx.author.default.avatar.url)
                        embed.description=f"اختر القناة المراد نقله إليها"
                        await interaction.response.edit_message(embed=embed, view=moveToView(id))

            class moveView(discord.ui.View):
                def __init__(self, *, timeout = 60*60):
                    super().__init__(timeout=timeout)
                    self.add_item(moveOptions())
                    self.add_item(cancele())

            class remOptions(discord.ui.Select):
                def __init__(self):
                    data = load(assist.tickjson)
                    tickets=data[str(ctx.guild.id)]['tickets']
                    placeholder="اختر التيكت المراد حذفة";disable=False
                    if tickets == {}:placeholder="لايوجد تيكت";disable=True;options = [discord.SelectOption(label=placeholder, value=placeholder)]
                    if tickets!={}:options = [discord.SelectOption(label=ticket[:ticket.find("_")].replace("[SPACE]", ' '), value=ticket) for ticket in tickets]
                    self.dis = disable
                    super().__init__(placeholder=placeholder, max_values=1, min_values=1, options=options, disabled=disable)

                async def callback(self, interaction):
                    if interaction.user.id == ctx.author.id:
                        id = self.values[0]
                        embed = discord.Embed(color=assist.embedColors.green, timestamp=datetime.now())
                        embed.set_author(name='mzooz bot', icon_url=client.user.avatar.url, url=assist.mzo0zServer)
                        try:embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar.url)
                        except:embed.set_footer(text=ctx.author, icon_url=ctx.author.default.avatar.url)
                        embed.description=f"لايوجد تيكت"
                        if self.dis:
                            data = load(assist.tickjson)
                            deleted = False
                            try:await Ticket.afterDelete(client=client, ticket=data[str(ctx.guild.id)]['tickets'][id], guildId=ctx.guild.id);deleted=False
                            except:deleted=True
                            msg = id[:id.find("_")].replace("[SPACE]", ' ')
                            if deleted:embed.description=f"حدث خطأ اثناء حذف {msg}"
                            else:embed.description=f"تم حذف {msg} بنجاح"
                        await interaction.response.edit_message(embed=embed, view=None)

            class remView(discord.ui.View):
                def __init__(self, *, timeout = 60*60):
                    super().__init__(timeout=timeout)
                    self.add_item(remOptions())
                    self.add_item(cancele())

            class cancele(discord.ui.Button):
                def __init__(self):
                    super().__init__(style=discord.ButtonStyle.red, label='إلغاء')

                async def callback(self, interaction: discord.Interaction):
                    if interaction.user.id == ctx.author.id:
                        global canceled
                        canceled = True
                        embed = discord.Embed(color=assist.embedColors.red, timestamp=datetime.now())
                        embed.set_author(name='mzooz bot', icon_url=client.user.avatar.url, url=assist.mzo0zServer)
                        try:embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar.url)
                        except:embed.set_footer(text=ctx.author, icon_url=ctx.author.default.avatar.url)
                        embed.description=f"تم إلغاء العملية"
                        await interaction.response.edit_message(embed=embed, view=None)


            class ticketOptions(discord.ui.Select):
                def __init__(self):
                    options = [discord.SelectOption(label=ticketoptions[id], value=id) for id in ticketoptions]
                    super().__init__(placeholder='اختر', max_values=1, min_values=1, options=options)

                async def callback(self, interaction):
                    if interaction.user.id == ctx.author.id:
                        id = self.values[0]
                        embed = discord.Embed(color=assist.embedColors.green, timestamp=datetime.now())
                        embed.set_author(name='mzooz bot', icon_url=client.user.avatar.url, url=assist.mzo0zServer)
                        try:embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar.url)
                        except:embed.set_footer(text=ctx.author, icon_url=ctx.author.default.avatar.url)
                        if id == 'cate':
                            embed.description=f"اختر المجموعة"
                            await interaction.response.edit_message(embed=embed, view=cateView())
                        elif id == 'move':
                            if load(assist.tickjson)[str(ctx.guild.id)]['tickets'] != {}:embed.description=f"اختر التيكت المراد نقلة";await interaction.response.edit_message(embed=embed, view=moveView())
                            else:embed.description=f"لايوجد تيكت";embed.color=assist.embedColors.red;await interaction.response.edit_message(embed=embed, view=None)
                        elif id == 'rem':
                            if load(assist.tickjson)[str(ctx.guild.id)]['tickets'] != {}:embed.description=f"اختر التيكت المراد حذفة";await interaction.response.edit_message(embed=embed, view=remView())
                            else:embed.description=f"لايوجد تيكت";embed.color=assist.embedColors.red;await interaction.response.edit_message(embed=embed, view=None)

            class ticketView(discord.ui.View):
                def __init__(self, *, timeout = 180):
                    super().__init__(timeout=timeout)
                    self.add_item(ticketOptions())
                    self.add_item(cancele())

            class logOptions(discord.ui.Select):
                def __init__(self):
                    options = [discord.SelectOption(label=channels[id], value=id) for id in channels if id != 0]
                    super().__init__(placeholder='اختر القناة', max_values=1, min_values=1, options=options)

                async def callback(self, interaction):
                    if interaction.user.id == ctx.author.id:
                        id = int(self.values[0])
                        embed = discord.Embed(color=assist.embedColors.green, timestamp=datetime.now())
                        embed.set_author(name='mzooz bot', icon_url=client.user.avatar.url, url=assist.mzo0zServer)
                        try:embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar.url)
                        except:embed.set_footer(text=ctx.author, icon_url=ctx.author.default.avatar.url)
                        embed.description=f"تم تعيين  {channels[id]} كـ قناة اللوق"
                        data = load(assist.jsonFile)
                        data['logChannelId']=int(id)
                        dump(assist.jsonFile, data)
                        await interaction.response.edit_message(embed=embed, view=None)

            class logView(discord.ui.View):
                def __init__(self, *, timeout = 60*60):
                    super().__init__(timeout=timeout)
                    self.add_item(logOptions())
                    self.add_item(cancele())


            class botOptions(discord.ui.Select):
                def __init__(self, d=False, placeholder="اختر"):
                    options = [discord.SelectOption(label=id, value=id) for id in botoptions]
                    super().__init__(placeholder=placeholder, max_values=1, min_values=1, options=options, disabled=d)

                async def callback(self, interaction):
                    if interaction.user.id == ctx.author.id:
                        id = self.values[0]
                        embed = discord.Embed(color=assist.embedColors.green, timestamp=datetime.now())
                        embed.set_author(name='mzooz bot', icon_url=client.user.avatar.url, url=assist.mzo0zServer)
                        try:embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar.url)
                        except:embed.set_footer(text=ctx.author, icon_url=ctx.author.default.avatar.url)
                        global canceled
                        if id == 'prefix':
                            embed.description=f"ماهي البادئة الجديدة"
                            await interaction.response.edit_message(embed=embed, view=botView(d=True, placeholder='ماهي البادئة الجديدة'))
                            def newPrefix(m):return m.author == ctx.author and m.channel == interaction.channel
                            newP = await client.wait_for('message', check=newPrefix)
                            await newP.delete()
                            newP = newP.content
                            if canceled:return
                            nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
                            if newP[0] in nums:embed.description=f'لايمكن استحدام ارقام!';embed.color=assist.embedColors.red;await interaction.message.edit(embed=embed, view=None);return
                            data = load(assist.jsonFile)
                            data['prefix']=newP
                            dump(assist.jsonFile, data)
                            prefix = load(assist.jsonFile)['prefix']
                            client.command_prefix=prefix
                            await client.change_presence(activity=discord.Game(name=f"{load(assist.jsonFile)['prefix']}help | {assist.mzo0zServer.replace('https://', '')}"))
                            embed.description=f'تم تعيين `{newP}` كـ البادئة الجديدة'
                            await interaction.message.edit(embed=embed, view=None)

                        if id == 'secret key':
                            embed.description="ماهو المفتاح السري الجديد"
                            await interaction.response.edit_message(embed=embed, view=botView(d=True, placeholder="ماهو المفتاح السري الجديد"))
                            def newPrefix(m):return m.author == ctx.author and m.channel == interaction.channel
                            newP = await client.wait_for('message', check=newPrefix)
                            await newP.delete()
                            newP = newP.content
                            if canceled:return
                            data = load(assist.jsonFile)
                            data['secretKey']=newP
                            dump(assist.jsonFile, data)
                            embed.description=f'تم تعيين `{newP}` كـ المفتاح السري الجديد, من فضلك قم بإعادة تشغيل البوت'
                            await interaction.message.edit(embed=embed, view=None)
                        if id == 'host ip':
                            embed.description="ماهو الـ آي بي الجديد"
                            await interaction.response.edit_message(embed=embed, view=botView(d=True, placeholder="ماهو الـ آي بي الجديد"))
                            def newPrefix(m):return m.author == ctx.author and m.channel == interaction.channel
                            newP = await client.wait_for('message', check=newPrefix)
                            await newP.delete()
                            newP = newP.content
                            if canceled:return
                            data = load(assist.jsonFile)
                            data['host']=newP
                            dump(assist.jsonFile, data)
                            embed.description=f'تم تعيين `{newP}` كـ الآي بي الجديد, من فضلك قم بإعادة تشغيل البوت'
                            await interaction.message.edit(embed=embed, view=None)
                        if id == 'support url':
                            embed.description="ماهو رابط الدعم الفني الجديد"
                            await interaction.response.edit_message(embed=embed, view=botView(d=True, placeholder="ماهو رابط الدعم الفني الجديد"))
                            def newPrefix(m):return m.author == ctx.author and m.channel == interaction.channel
                            newP = await client.wait_for('message', check=newPrefix)
                            await newP.delete()
                            newP = newP.content
                            if canceled:return
                            data = load(assist.jsonFile)
                            data['supportUrl']=newP
                            dump(assist.jsonFile, data)
                            embed.description=f'تم تعيين `{newP}` كـ رابط الدعم الفني الجديد'
                            await interaction.message.edit(embed=embed, view=None)
                        if id == 'log channel':
                            embed.description="اختر قناة اللوق الجديدة"
                            await interaction.response.edit_message(embed=embed, view=logView())



            class botView(discord.ui.View):
                def __init__(self, d=False, placeholder='اختر', *, timeout = 180):
                    super().__init__(timeout=timeout)
                    self.add_item(botOptions(d=d, placeholder=placeholder))
                    self.add_item(cancele())


            class setCateGamesOptions(discord.ui.Select):
                def __init__(self):
                    options = [discord.SelectOption(label=categorys[id], value=id) for id in categorys]
                    super().__init__(placeholder='اختر المجموعة', max_values=1, min_values=1, options=options)

                async def callback(self, interaction):
                    if interaction.user.id == ctx.author.id:
                        id = int(self.values[0])
                        embed = discord.Embed(color=assist.embedColors.green, timestamp=datetime.now())
                        embed.set_author(name='mzooz bot', icon_url=client.user.avatar.url, url=assist.mzo0zServer)
                        try:embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar.url)
                        except:embed.set_footer(text=ctx.author, icon_url=ctx.author.default.avatar.url)
                        data = load(assist.gamesjson)
                        if id!=0:data['games']['category']=int(id);dump(assist.gamesjson, data);embed.description=f"تم تعيين `{categorys[id]}` كـ المجموعة الجديدة"
                        if id==0:data['games']['category']=0;dump(assist.gamesjson, data);embed.description=f"تم إلغاء مجموعة الالعاب";embed.color=assist.embedColors.red
                        await interaction.response.edit_message(embed=embed, view=None)

            class setCateGamesView(discord.ui.View):
                def __init__(self, *, timeout = 60*60):
                    super().__init__(timeout=timeout)
                    self.add_item(setCateGamesOptions())
                    self.add_item(cancele())


            class addGamesOptions(discord.ui.Select):
                def __init__(self):
                    options = [discord.SelectOption(label=channels[id], value=id) for id in channels]
                    super().__init__(placeholder='اختر القناة', max_values=1, min_values=1, options=options)

                async def callback(self, interaction):
                    if interaction.user.id == ctx.author.id:
                        id = int(self.values[0])
                        embed = discord.Embed(color=assist.embedColors.green, timestamp=datetime.now())
                        embed.set_author(name='mzooz bot', icon_url=client.user.avatar.url, url=assist.mzo0zServer)
                        try:embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar.url)
                        except:embed.set_footer(text=ctx.author, icon_url=ctx.author.default.avatar.url)
                        data = load(assist.gamesjson)
                        data['games']['gamesChannels'].append(id)
                        data['games']['gamesChannels'] = list(set(data['games']['gamesChannels']))
                        dump(assist.gamesjson, data)
                        embed.description=f'تم إضافة `{channels[id]}` الى قنوات الالعاب'
                        await interaction.response.edit_message(embed=embed, view=None)

            class addGamesView(discord.ui.View):
                def __init__(self, *, timeout = 60*60):
                    super().__init__(timeout=timeout)
                    self.add_item(addGamesOptions())
                    self.add_item(cancele())

            class remGamesOptions(discord.ui.Select):
                def __init__(self):
                    
                    options = [discord.SelectOption(label=gamesChannels[id], value=id) for id in gamesChannels]
                    super().__init__(placeholder='اختر القناة', max_values=1, min_values=1, options=options)

                async def callback(self, interaction):
                    if interaction.user.id == ctx.author.id:
                        id = int(self.values[0])
                        embed = discord.Embed(color=assist.embedColors.green, timestamp=datetime.now())
                        embed.set_author(name='mzooz bot', icon_url=client.user.avatar.url, url=assist.mzo0zServer)
                        try:embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar.url)
                        except:embed.set_footer(text=ctx.author, icon_url=ctx.author.default.avatar.url)
                        data = load(assist.gamesjson)
                        data['games']['gamesChannels'].remove(id)
                        data['games']['gamesChannels'] = list(set(data['games']['gamesChannels']))
                        dump(assist.gamesjson, data)
                        embed.description=f'تم إزالة `{gamesChannels[id]}` من قنوات الالعاب'
                        await interaction.response.edit_message(embed=embed, view=None)

            class remGamesView(discord.ui.View):
                def __init__(self, *, timeout = 60*60):
                    super().__init__(timeout=timeout)
                    self.add_item(remGamesOptions())
                    self.add_item(cancele())

            class gamesOptions(discord.ui.Select):
                def __init__(self):
                    options = [discord.SelectOption(label=gamesoptions[id], value=id) for id in gamesoptions]
                    super().__init__(placeholder='اختر', max_values=1, min_values=1, options=options)

                async def callback(self, interaction):
                    if interaction.user.id == ctx.author.id:
                        id = self.values[0]
                        embed = discord.Embed(color=assist.embedColors.green, timestamp=datetime.now())
                        embed.set_author(name='mzooz bot', icon_url=client.user.avatar.url, url=assist.mzo0zServer)
                        try:embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar.url)
                        except:embed.set_footer(text=ctx.author, icon_url=ctx.author.default.avatar.url)
                        if id == 'cate':
                            embed.description=f"اختر المجموعة المراد تعيينها للالعاب"
                            await interaction.response.edit_message(embed=embed, view=setCateGamesView())
                        if id == 'channel':
                            embed.description=f"اختر القناة المراد إضافتها لقنوات الالعاب"
                            await interaction.response.edit_message(embed=embed, view=addGamesView())
                        if id == 'remChannel':
                            if gamesChannels != {}:embed.description="اختر القناة المراد إزالتها من قنوات الالعاب";await interaction.response.edit_message(embed=embed, view=remGamesView())
                            else:embed.description=f"لاتوجد قناة للالعاب";embed.color=assist.embedColors.red;await interaction.response.edit_message(embed=embed, view=None)

            class gamesView(discord.ui.View):
                def __init__(self, *, timeout = 60*60):
                    super().__init__(timeout=timeout)
                    self.add_item(gamesOptions())
                    self.add_item(cancele())

            class securityOptions(discord.ui.Select):
                def __init__(self):
                    options = [discord.SelectOption(label=securityoptions[id], value=id) for id in securityoptions]
                    super().__init__(placeholder='اختر', max_values=1, min_values=1, options=options)

                async def callback(self, interaction):
                    if interaction.user.id == ctx.author.id:
                        id = self.values[0]
                        embed = discord.Embed(color=assist.embedColors.green, timestamp=datetime.now())
                        embed.set_author(name='mzooz bot', icon_url=client.user.avatar.url, url=assist.mzo0zServer)
                        try:embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar.url)
                        except:embed.set_footer(text=ctx.author, icon_url=ctx.author.default.avatar.url)
                        if id == 'activeSystem':
                            if load(assist.safejson)[str(ctx.guild.id)]['activeRole']['active'] == 0:
                                embed.description=f"يجب تفعيل النظام"
                                await interaction.response.edit_message(embed=embed, view=activeSystemView())
                            else:
                                if int(len(roles)) >= 25:
                                    embed.description="بسبب وجود الكثير من الرتب في السيرفر, لايمكن إنشاء قائمة للرتب, من فضلك قم بنشن رتبة التفعيل"
                                    await interaction.response.edit_message(embed=embed, view=activeSystemView())
                                    def hi(m):return m.author == ctx.author and m.channel == ctx.channel
                                    role = await client.wait_for('message', check=hi)
                                    await role.delete()
                                    global canceled
                                    if canceled:return
                                    try:
                                        role=discord.utils.get(ctx.guild.roles, id=int(role.content[3:-1]))
                                        data = load(assist.safejson)
                                        data[str(ctx.guild.id)]['activeRole']['roleId']=int(role.id)
                                        dump(assist.safejson, data)
                                        embed.description=f"تم جعل {role.mention} رتبة التفعيل, اي شخص لايملك هذه الرتبة لثلاثة ايام سيتم طرده"
                                        await interaction.message.edit(embed=embed, view=None)
                                    except:
                                        embed.description=f"يجب ان تقوم بمنشن الرتبة ويجب ان تكون رتبة واحدة فقط"
                                        embed.color=assist.embedColors.red
                                        await interaction.message.edit(embed=embed, view=None)

                                else:embed.description="اختر الرتبة";await interaction.response.edit_message(embed=embed, view=activeSystemView())


            class securityView(discord.ui.View):
                def __init__(self, *, timeout = 60*60):
                    super().__init__(timeout=timeout)
                    self.add_item(securityOptions())
                    self.add_item(cancele())

            class activeSystemOptions(discord.ui.Select):
                def __init__(self):
                    if load(assist.safejson)[str(ctx.guild.id)]['activeRole']['active']==0:
                        d=True
                        placeholder='النظام معطل'
                        options = [discord.SelectOption(label=0000, value=0000)]
                    else:
                        placeholder='اختر رتبة التفعيل'
                        if int(len(roles))>=25:options = [discord.SelectOption(label=0000, value=0000)];d=True
                        else:options = [discord.SelectOption(label=roles[id], value=id) for id in roles];d=False
                    super().__init__(placeholder=placeholder, max_values=1, min_values=1, options=options, disabled=d)

                async def callback(self, interaction):
                    if interaction.user.id == ctx.author.id:
                        id = self.values[0]
                        embed = discord.Embed(color=assist.embedColors.green, timestamp=datetime.now())
                        embed.set_author(name='mzooz bot', icon_url=client.user.avatar.url, url=assist.mzo0zServer)
                        try:embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar.url)
                        except:embed.set_footer(text=ctx.author, icon_url=ctx.author.default.avatar.url)
                        role = discord.utils.get(ctx.guild.roles, id=int(id))
                        data = load(assist.safejson)
                        data[str(ctx.guild.id)]['activeRole']['roleId']=int(role.id)
                        dump(assist.safejson, data)

                        embed.description=f"تم جعل {role.mention} رتبة التفعيل, اي شخص لايملك هذه الرتبة لثلاثة ايام سيتم طرده"
                        await interaction.message.edit(embed=embed, view=None)

            class activeSystemView(discord.ui.View):
                def __init__(self, *, timeout = 60*60):
                    super().__init__(timeout=timeout)
                    self.add_item(activeSystemOptions())
                    self.add_item(cancele())
                    self.add_item(activeOrNo())

            class activeOrNo(discord.ui.Button):
                def __init__(self):
                    data = load(assist.safejson)
                    if data[str(ctx.guild.id)]['activeRole']['active'] == 0:
                        label = "غير مفعل"
                        color = discord.ButtonStyle.red
                    else:
                        label = "مفعل"
                        color = discord.ButtonStyle.green
                    super().__init__(style=color, label=label)

                async def callback(self, interaction: discord.Interaction):
                    if interaction.user.id == ctx.author.id:
                        data = load(assist.safejson)
                        embed = discord.Embed(color=assist.embedColors.green, timestamp=datetime.now())
                        embed.set_author(name='mzooz bot', icon_url=client.user.avatar.url, url=assist.mzo0zServer)
                        try:embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar.url)
                        except:embed.set_footer(text=ctx.author, icon_url=ctx.author.default.avatar.url)
                        if data[str(ctx.guild.id)]['activeRole']['active'] == 0:
                            data[str(ctx.guild.id)]['activeRole']['active']=1
                            embed.description=f"تم تفعيل النظام\nاختر رتبة التفعيل"
                            if int(len(roles)) >= 25:
                                embed.description="بسبب وجود الكثير من الرتب في السيرفر, لايمكن إنشاء قائمة للرتب, من فضلك قم بنشن رتبة التفعيل"
                        else:data[str(ctx.guild.id)]['activeRole']['active']=0;embed.description=f"تم تعطيل النظام"
                        dump(assist.safejson, data)
                        await interaction.response.edit_message(embed=embed, view=activeSystemView())


            class managementOptions(discord.ui.Select):
                def __init__(self):
                    options = [discord.SelectOption(label=manageOptions[id], value=id) for id in manageOptions]
                    super().__init__(placeholder='اختر النظام المراد إدارته', max_values=1, min_values=1, options=options)

                async def callback(self, interaction):
                    if interaction.user.id == ctx.author.id:
                        id = self.values[0]
                        embed = discord.Embed(color=assist.embedColors.green, timestamp=datetime.now())
                        embed.set_author(name='mzooz bot', icon_url=client.user.avatar.url, url=assist.mzo0zServer)
                        try:embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar.url)
                        except:embed.set_footer(text=ctx.author, icon_url=ctx.author.default.avatar.url)


                        if id =='islam':
                            embed, options, text, hide = await getChannels(embed)
                            await interaction.response.edit_message(embed=embed, view=islamView(options, text, hide))
                            if hide:await setChannel(interaction, id)

                        if id =='ticket':
                            embed.title=f"إدارة التيكت"
                            await interaction.response.edit_message(embed=embed, view=ticketView())
                        if id =='bot':
                            embed.title=f"إدارة البوت"
                            await interaction.response.edit_message(embed=embed, view=botView())
                        if id =='games':
                            embed.title=f"إدارة الألعاب"
                            await interaction.response.edit_message(embed=embed, view=gamesView())
                        if id =='security':
                            embed.title=f"إدارة الحماية"
                            await interaction.response.edit_message(embed=embed, view=securityView())



            class managementView(discord.ui.View):
                def __init__(self, *, timeout = 180):
                    super().__init__(timeout=timeout)
                    self.add_item(managementOptions())
                    self.add_item(cancele())

            await ctx.channel.send(view=managementView())


