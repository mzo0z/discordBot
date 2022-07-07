import datetime
import discord
import random
import assist
from . import gamesAssist

async def start(ctx, client):
    findmemodes = {
        '1': 'دول',
        '2': 'حيوانات',
        '5': 'مشاهير يوتيوب',
        '6': 'اكلات'}  # findme
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

    findmechoose   = '' #findme
    findmeLeader   = '' #findme
    fqAnserIs      = '' #findme
    findmeLeader = ctx.author.id

    mds = ['1', '2', '5', '6']
    findmechoose = random.choice(mds)

    findmequestion = []
    if findmechoose:
        for i in MODES[str(findmechoose)]:
            if len(i) <= 4:
                pass
            elif '(' in i:
                pass
            else:
                findmequestion.append(i)

        fq = random.choice(findmequestion)
        fqAnserIs = fq
        findmequestion.remove(fq)
        lenfq = len(fq)
        fqnums = [i for i in range(lenfq) if i != 0 and fq[i] == ' ']

        if lenfq > 4:
            Fnumtoreminfq = random.choice(fqnums)
            fqnums.remove(Fnumtoreminfq)
            Fnumtoreminfq = fq[Fnumtoreminfq]
            Snumtoreminfq = random.choice(fqnums)
            fqnums.remove(Snumtoreminfq)
            Snumtoreminfq = fq[Snumtoreminfq]
            Tnumtoreminfq = random.choice(fqnums)
            fqnums.remove(Tnumtoreminfq)
            Tnumtoreminfq = fq[Tnumtoreminfq]
            findmequestionis = fq.replace(Fnumtoreminfq, '_ ')
            findmequestionis = findmequestionis.replace(Snumtoreminfq, '_ ')
            findmequestionis = findmequestionis.replace(Tnumtoreminfq, '_ ')

        findmeembedq = discord.Embed(title=f':المود {findmemodes[findmechoose]}', description=f'`{findmequestionis}`', timestamp = datetime.datetime.now(), color=assist.embedColors.blue)
        findmeembedq.set_author(icon_url=client.user.avatar.url, name = 'mzooz games bot')
        try:findmeembedq.set_footer(text=ctx.author, icon_url=ctx.author.avatar.url)
        except:findmeembedq.set_footer(text=ctx.author, icon_url=ctx.author.default_avatar.url)
        q = await ctx.channel.send(embed=findmeembedq)
        def waitForFqAnser(c):return c.author == ctx.author and c.channel == ctx.channel
        waitforfqansernow = await client.wait_for('message', check=waitForFqAnser)
        waitforfqansernow = waitforfqansernow.content
        if waitforfqansernow == fqAnserIs:findMeResultAnserEmbed = discord.Embed(title='**:white_check_mark: اجابة صحيحة!**', color=assist.embedColors.ligh_green, timestamp = datetime.datetime.now())
        else:
            findMeResultAnserEmbed = discord.Embed(title='**:x: اجابة خاطئة!**', color=assist.embedColors.red, timestamp = datetime.datetime.now())
            findMeResultAnserEmbed.add_field(name='الاجابة الصحيحة هي:', value=f"**{fqAnserIs}**", inline=True)
        findMeResultAnserEmbed.set_author(icon_url=client.user.avatar.url, name='mzooz games')
        try:findMeResultAnserEmbed.set_footer(text=ctx.author, icon_url=ctx.author.avatar.url)
        except:findMeResultAnserEmbed.set_footer(text=ctx.author, icon_url=ctx.author.default_avatar.url)
        findMeResultAnserEmbed.timestamp = datetime.datetime.now()
        await q.edit(embed=findMeResultAnserEmbed)

