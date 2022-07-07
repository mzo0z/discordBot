import discord
import random
import assist
import datetime
from . import gamesAssist
async def play(ctx, client):
    askingmodes = {
        '1' : 'askscience',
        '2' : 'asksport',
        '3' : 'askcountrys',
        '4' : 'askmedical',
        '5' : 'askcivilization',
        '6' : 'asklang',
        '7' : 'askpublicinfo'} #asking

    mds = ['1', '2', '3', '4', '5', '6', '7']
    askingchoose = random.choice(mds)
    askingleader = ctx.author.id
    quizs = [i for i in gamesAssist.askingQ[askingmodes[askingchoose]]]
    quesId = random.choice(quizs)
    askingQuestion = quesId
    askingAnswer   = gamesAssist.askingQ[askingmodes[askingchoose]][quesId]["answer"]
    askingHint     = gamesAssist.askingQ[askingmodes[askingchoose]][quesId]["hint"]
    askingHint = askingHint.split('\n')
    try:askingHint.remove('')
    except:pass
    questions = {}
    for ask in askingHint:questions.update({ask[0]:ask[2:]})
    view = discord.ui.View()
    style = discord.ButtonStyle.green
    async def ch1(c):
        global askingstoptimer
        global resultTrue
        global resultFalse
        if c.user.id == askingleader:
            if questions['1'] == askingAnswer:
                ansr = '**:white_check_mark: اجابة صحيحة!**'
                ebd = discord.Embed(title=ansr, description=f'السؤال كان: {askingQuestion}', color=assist.embedColors.green, timestamp = datetime.datetime.now())
                ebd.add_field(name=f"اجابتك كانت: {questions['1']}", value=f'** **')
                try:ebd.set_footer(text=ctx.author, icon_url=ctx.author.avatar.url)
                except:ebd.set_footer(text=ctx.author, icon_url=ctx.author.default_avatar.url)
                ebd.set_author(icon_url=client.user.avatar.url, name='mzooz games bot', url=assist.mzo0zServer)
                choice1.disabled = True
                choice2.disabled = True
                choice3.disabled = True
                await ms.edit(embed=ebd, view=view)
            else:
                ansr = '**:x: اجابة خاطئة!**'
                ebd = discord.Embed(title=ansr, description=f'السؤال كان: {askingQuestion}', color=assist.embedColors.green, timestamp = datetime.datetime.now())
                ebd.add_field(name=f"اجابتك كانت: {questions['1']}", value=f'الاجابة الصحيحة هي: **{askingAnswer}**')
                try:ebd.set_footer(text=ctx.author, icon_url=ctx.author.avatar.url)
                except:ebd.set_footer(text=ctx.author, icon_url=ctx.author.default_avatar.url)
                ebd.set_author(icon_url=client.user.avatar.url, name='mzooz games bot', url=assist.mzo0zServer)
                choice1.disabled = True
                choice2.disabled = True
                choice3.disabled = True
                await ms.edit(embed=ebd, view=view)
    async def ch2(c):
        global askingalreadyclicked
        global askingstoptimer
        global resultTrue
        global resultFalse
        if c.user.id == askingleader:
            if questions['2'] == askingAnswer:
                ansr = '**:white_check_mark: اجابة صحيحة!**'
                ebd = discord.Embed(title=ansr, description=f'السؤال كان: {askingQuestion}', color=assist.embedColors.green, timestamp = datetime.datetime.now())
                ebd.add_field(name=f"اجابتك كانت: {questions['2']}", value=f'** **')
                try:ebd.set_footer(text=ctx.author, icon_url=ctx.author.avatar.url)
                except:ebd.set_footer(text=ctx.author, icon_url=ctx.author.default_avatar.url)
                ebd.set_author(icon_url=client.user.avatar.url, name='mzooz games bot', url=assist.mzo0zServer)
                choice1.disabled = True
                choice2.disabled = True
                choice3.disabled = True
                await ms.edit(embed=ebd, view=view)
            else:
                ansr = '**:x: اجابة خاطئة!**'
                ebd = discord.Embed(title=ansr, description=f'السؤال كان: {askingQuestion}', color=assist.embedColors.green, timestamp = datetime.datetime.now())
                ebd.add_field(name=f"اجابتك كانت: {questions['2']}", value=f'الاجابة الصحيحة هي: **{askingAnswer}**')
                try:ebd.set_footer(text=ctx.author, icon_url=ctx.author.avatar.url)
                except:ebd.set_footer(text=ctx.author, icon_url=ctx.author.default_avatar.url)
                ebd.set_author(icon_url=client.user.avatar.url, name='mzooz games bot', url=assist.mzo0zServer)
                choice1.disabled = True
                choice2.disabled = True
                choice3.disabled = True
                await ms.edit(embed=ebd, view=view)
    async def ch3(c):
        global askingalreadyclicked
        global askingstoptimer
        global resultTrue
        global resultFalse
        if c.user.id == askingleader:
            if questions['3'] == askingAnswer:
                ansr = '**:white_check_mark: اجابة صحيحة!**'
                ebd = discord.Embed(title=ansr, description=f'السؤال كان: {askingQuestion}', color=assist.embedColors.green)
                ebd.add_field(name=f"اجابتك كانت: {questions['3']}", value=f'** **')
                try:ebd.set_footer(text=ctx.author, icon_url=ctx.author.avatar.url)
                except:ebd.set_footer(text=ctx.author,icon_url=ctx.author.default_avatar.url)
                ebd.timestamp = datetime.datetime.now()
                ebd.set_author(icon_url=client.user.avatar.url, name='mzooz games bot', url=assist.mzo0zServer)
                choice1.disabled = True
                choice2.disabled = True
                choice3.disabled = True
                await ms.edit(embed=ebd, view=view)
            else:
                ansr = '**:x: اجابة خاطئة!**'
                ebd = discord.Embed(title=ansr, description=f'السؤال كان: {askingQuestion}', color=assist.embedColors.green)
                ebd.add_field(name=f"اجابتك كانت: {questions['3']}", value=f'الاجابة الصحيحة هي: **{askingAnswer}**')
                try:ebd.set_footer(text=ctx.author, icon_url=ctx.author.avatar.url)
                except:ebd.set_footer(text=ctx.author, icon_url=ctx.author.default_avatar.url)
                ebd.timestamp = datetime.datetime.now()
                ebd.set_author(icon_url=client.user.avatar.url, name='mzooz games bot', url=assist.mzo0zServer)
                choice1.disabled = True
                choice2.disabled = True
                choice3.disabled = True
                await ms.edit(embed=ebd, view=view)

    choice1 = discord.ui.Button(style=style, label=questions['1'])
    choice2 = discord.ui.Button(style=style, label=questions['2'])
    choice3 = discord.ui.Button(style=style, label=questions['3'])
    choice1.callback = ch1
    choice2.callback = ch2
    choice3.callback = ch3
    view.add_item(item=choice1)
    view.add_item(item=choice2)
    view.add_item(item=choice3)
    em = discord.Embed(title=f'**{askingQuestion}**', color=0xf1c40f,timestamp = datetime.datetime.now())
    try:em.set_footer(text=ctx.author, icon_url=ctx.author.avatar.url)
    except:em.set_footer(text=ctx.author, icon_url=ctx.author.default_avatar.url)
    em.set_author(icon_url=client.user.avatar.url, name='mzooz games bot', url=assist.mzo0zServer)
    ms = await ctx.channel.send(embed=em, view=view)
