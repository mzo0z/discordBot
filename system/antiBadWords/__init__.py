import asyncio
import assist
import json
import discord
from datetime import datetime
from discord.ext import commands

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
        def string(msg):
            new = ""
            for i in msg:new = new + i + ' '
            return new

        @client.command()
        @commands.has_permissions(administrator=True)
        async def show(ctx):await ctx.channel.send(string([i for i in load(assist.jsonFile)['badWords']]))

        @client.command()
        @commands.has_permissions(administrator=True)
        async def showList(ctx):await ctx.channel.send([i for i in load(assist.jsonFile)['badWords']])


        @client.command()
        @commands.has_permissions(administrator=True)
        async def purge(ctx):
            class view(discord.ui.View):
                @discord.ui.button(label='نعم', style=discord.ButtonStyle.red)
                async def yes(self, button: discord.Button, intercation: discord.Interaction):
                    data = load(assist.jsonFile)
                    data['badWords'] = []
                    dump(assist.jsonFile, data)
                    embed = discord.Embed(title="تم حذف جميع الكلمات من القائمة", color=assist.embedColors.green, timestamp=datetime.now())
                    embed.set_author(name='mzooz system bot', icon_url=client.user.avatar.url, url=assist.mzo0zServer)
                    try:embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar.url)
                    except:embed.set_footer(text=ctx.author)
                    try:await intercation.message.delete()
                    except:pass
                    await intercation.response.send_message(embed=embed)

                @discord.ui.button(label='لا', style=discord.ButtonStyle.green)
                async def no(self, button: discord.Button, intercation: discord.Interaction):
                    embed = discord.Embed(title="تم إلغاء العملية", color=assist.embedColors.red, timestamp=datetime.now())
                    embed.set_author(name='mzooz system bot', icon_url=client.user.avatar.url, url=assist.mzo0zServer)
                    try:embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar.url)
                    except:embed.set_footer(text=ctx.author)
                    try:await intercation.message.delete()
                    except:pass
                    await intercation.response.send_message(embed=embed)

            embed = discord.Embed(title="هل انت متأكد من انك تريد حذف جميع الكلمات من القائمة؟", color=assist.embedColors.green, timestamp=datetime.now())
            embed.set_author(name='mzooz system bot', icon_url=client.user.avatar.url, url=assist.mzo0zServer)
            try:embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar.url)
            except:embed.set_footer(text=ctx.author)
            await ctx.channel.send(embed=embed, view=view())


        @client.command()
        @commands.has_permissions(administrator=True)
        async def add(ctx):
            embed = discord.Embed(title="اكتب جميع الكلمات المراد حذفها عندما تكتب:", description='يعني اكتب كل السبات و اهم شي حط مسافه بين السبه والثانيه', color=assist.embedColors.blue, timestamp=datetime.now())
            embed.set_author(name='mzooz system bot', icon_url=client.user.avatar.url, url=assist.mzo0zServer)
            try:embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar.url)
            except:embed.set_footer(text=ctx.author)
            await ctx.channel.send(embed=embed)
            def getBads(m):return m.author == ctx.author and m.channel == ctx.channel

            class view(discord.ui.View):
                @discord.ui.button(label='نعم', style=discord.ButtonStyle.green)
                async def yes(self, button: discord.Button, intercation: discord.Interaction):
                    data = load(assist.jsonFile)
                    for i in msg.content.split(" "):
                        data['badWords'].append(i)
                    data['badWords'] = list(set(data['badWords']))
                    dump(assist.jsonFile, data)
                    embed = discord.Embed(title="تم إضافة الكلمات الى قائمة الكلمات البذيئة", color=assist.embedColors.green, timestamp=datetime.now())
                    embed.set_author(name='mzooz system bot', icon_url=client.user.avatar.url, url=assist.mzo0zServer)
                    try:embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar.url)
                    except:embed.set_footer(text=ctx.author)
                    try:await intercation.message.delete()
                    except:pass
                    await intercation.response.send_message(embed=embed)

                @discord.ui.button(label='لا', style=discord.ButtonStyle.red)
                async def no(self, button: discord.Button, intercation: discord.Interaction):
                    embed = discord.Embed(title="تم إلغاء العملية", color=assist.embedColors.red, timestamp=datetime.now())
                    embed.set_author(name='mzooz system bot', icon_url=client.user.avatar.url, url=assist.mzo0zServer)
                    try:embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar.url)
                    except:embed.set_footer(text=ctx.author)
                    try:await intercation.message.delete()
                    except:pass
                    await intercation.response.send_message(embed=embed)

            try:msg = await client.wait_for("message", check=getBads)
            except asyncio.TimeoutError:await ctx.channel.send(embed=discord.Embed(title='انتهى الوقت, لم تجب في الوقت', color=assist.embedColors.red, timestamp=datetime.datetime.now()).set_author(name='mzooz system bot', icon_url=client.user.avatar.url, url=assist.mzo0zServer)); return
            else:
                embed = discord.Embed(title="هل انت متأكد من انك تريد إضافة هذه الكلمات الى قائمة الكلمات البذيئة؟", description=msg.content.split(" "), color=assist.embedColors.blue, timestamp=datetime.now())
                embed.set_author(name='mzooz system bot', icon_url=client.user.avatar.url, url=assist.mzo0zServer)
                try:embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar.url)
                except:embed.set_footer(text=ctx.author)
                await ctx.channel.send(embed=embed, view=view())


repeat = {}
async def onMessage(ctx, client):
    DATA = load(assist.jsonFile)
    msg = ctx.content
    def string(word):
        str = ''
        for char in word:
            str = str + char + ' '
        return str
    msgs = []
    for i in msg.split(" "):
        answer2 = i.replace('أ', 'ا')
        answer2 = answer2.replace("ؤ", 'و')
        answer2 = answer2.replace("چ", 'ج')
        answer2 = answer2.replace("ژ", 'ز')
        answer2 = answer2.replace("ڤ", 'ق')
        answer2 = answer2.replace("گ", 'ك')
        answer2 = answer2.replace("ك", 'ق')
        answer2 = answer2.replace('ة', 'ه')
        answer2 = answer2.replace('ئ', 'ى')
        answer2 = answer2.replace('إ', 'ا')
        answer2 = answer2.replace('آ', 'ا')
        answer2 = answer2.replace('ّ', '')
        answer2 = answer2.replace('َ', '')
        answer2 = answer2.replace('ً', '')
        answer2 = answer2.replace('ُ', '')
        answer2 = answer2.replace('ٌ', '')
        answer2 = answer2.replace('ٍ', '')
        answer2 = answer2.replace('ِ', '')
        answer2 = answer2.replace('ْ', '')
        answer2 = answer2.replace('َ', '')
        answer2 = answer2.replace('َ', '')
        answer2 = answer2.replace('َ', '')
        answer2 = answer2.replace('َ', '')
        answer2 = answer2.replace('ّ', '')
        answer2 = answer2.replace('ً', '')
        answer2 = answer2.replace('ُ', '')
        answer2 = answer2.replace('ِ', '')
        answer2 = answer2.replace('ٍ', '')
        answer2 = answer2.replace('ْ', '')
        answer2 = answer2.replace('ٌ', '')
        answer2 = answer2.replace('ـ', '')
        answer2 = answer2.replace('ٰ', '')
        answer2 = answer2.replace('ٰ', '')
        answer2 = answer2.replace('ٓ', '')
        answer2 = answer2.replace('ال', '')
        msgs.append(answer2)

    for badWord in DATA["autoMod"][DATA["serverId"]]['antiBadWords']:
        answer = badWord.replace('أ', 'ا')
        answer = answer.replace("ؤ", 'و')
        answer = answer.replace("چ", 'ج')
        answer = answer.replace("ژ", 'ز')
        answer = answer.replace("ڤ", 'ق')
        answer = answer.replace("گ", 'ك')
        answer = answer.replace("ك", 'ق')
        answer = answer.replace('ة', 'ه')
        answer = answer.replace('ئ', 'ى')
        answer = answer.replace('إ', 'ا')
        answer = answer.replace('آ', 'ا')
        answer = answer.replace('ّ', '')
        answer = answer.replace('َ', '')
        answer = answer.replace('ً', '')
        answer = answer.replace('ُ', '')
        answer = answer.replace('ٌ', '')
        answer = answer.replace('ٍ', '')
        answer = answer.replace('ِ', '')
        answer = answer.replace('ْ', '')
        answer = answer.replace('َ', '')
        answer = answer.replace('َ', '')
        answer = answer.replace('َ', '')
        answer = answer.replace('َ', '')
        answer = answer.replace('ّ', '')
        answer = answer.replace('ً', '')
        answer = answer.replace('ُ', '')
        answer = answer.replace('ِ', '')
        answer = answer.replace('ٍ', '')
        answer = answer.replace('ْ', '')
        answer = answer.replace('ٌ', '')
        answer = answer.replace('ـ', '')
        answer = answer.replace('ٰ', '')
        answer = answer.replace('ٰ', '')
        answer = answer.replace('ٓ', '')
        answer = answer.replace('ال', '')
        if ctx.author != client.user:
            if answer in msgs:
                try:await ctx.delete()
                except:
                    try:await ctx.message.delete()
                    except:pass