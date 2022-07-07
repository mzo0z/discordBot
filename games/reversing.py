import discord
import random
import assist
import datetime
from . import gamesAssist
async def start(ctx, client):
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
    gameName = '**اعكس - reverse**'
    mds = ['1', '2', '6', '7']
    reverseChoose = random.choice(mds)
    rq = [mode for mode in MODES[str(reverseChoose)]]
    reverseIs = random.choice(rq)
    rq.remove(reverseIs)
    reversing = ''
    for char in reverseIs[::-1]:reversing = reversing + char
    reverseEmbed = discord.Embed(title=gameName, description=f'`حاول تعرف ==>` **{reversing}**', color=assist.embedColors.blue, timestamp = datetime.datetime.now())
    reverseEmbed.set_author(icon_url=client.user.avatar.url, name = 'mzooz games bot', url=assist.mzo0zServer)
    try:reverseEmbed.set_footer(text=ctx.author, icon_url=ctx.author.avatar.url)
    except:reverseEmbed.set_footer(text=ctx.author, icon_url=ctx.author.default_avatar.url)
    
    ff = await ctx.channel.send(embed=reverseEmbed)
    def waitForReversingAnser(m):return m.author == ctx.author and m.channel == ctx.channel
    waitforrqansernow = await client.wait_for('message', check=waitForReversingAnser)
    waitforrqansernow = waitforrqansernow.content
    if waitforrqansernow == reverseIs:reverseResultAnserEmbed = discord.Embed(title='**:white_check_mark: اجابة صحيحة!**', color=assist.embedColors.ligh_green, timestamp = datetime.datetime.now())
    else:reverseResultAnserEmbed = discord.Embed(title='**:x: اجابة خاطئة!**', description=f'الاجابة الصحيحة هي: **{reverseIs}**', color=assist.embedColors.red, timestamp = datetime.datetime.now())
    try:reverseResultAnserEmbed.set_footer(text=ctx.author, icon_url=ctx.author.avatar.url)
    except:reverseResultAnserEmbed.set_footer(text=ctx.author, icon_url=ctx.author.default_avatar.url)
    reverseResultAnserEmbed.set_author(icon_url=client.user.avatar.url, name='mzooz games bot', url=assist.mzo0zServer)
    await ff.edit(embed=reverseResultAnserEmbed)
