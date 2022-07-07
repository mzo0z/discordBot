import datetime
import discord
import random
import assist
from . import gamesAssist

async def start(ctx, client):

    mode = {
        '1': 'دول',
        '2': 'حيوانات',
        '6': 'اكلات',
        '7': 'مشروبات',
        '8': 'جماد'}

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
    gameName = '**رتب - sort**'
    sortLeader = ctx.author.id
    mds = ['1', '2', '6', '7', '8']
    sortchoose = random.choice(mds)
    sortquestion = [i for i in MODES[str(sortchoose)] if '(' not in i and ' ' not in i]

    fq = random.choice(sortquestion)
    fqAnserIs = fq
    answer = fqAnserIs.replace('أ', 'ا')
    answer = answer.replace("ؤ", 'و')
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

    random_word = random.sample(fqAnserIs, len(fqAnserIs))
    jumbled = ''.join(random_word)

    reverseEmbed = discord.Embed(title=gameName, description=f'المود: {mode[sortchoose]}', color=assist.embedColors.blue, timestamp = datetime.datetime.now())
    reverseEmbed.add_field(name=f'`حاول تعرف ==>` **{jumbled}**', value="** **")
    reverseEmbed.set_author(icon_url=client.user.avatar.url, name = 'mzooz games bot', url=assist.mzo0zServer)
    try:reverseEmbed.set_footer(text=ctx.author, icon_url=ctx.author.avatar.url)
    except:reverseEmbed.set_footer(text=ctx.author, icon_url=ctx.author.default_avatar.url)
    ff = await ctx.channel.send(embed=reverseEmbed)
    def waitForReversingAnser(m):return m.author == ctx.author and m.channel == ctx.channel
    waitforrqansernow = await client.wait_for('message', check=waitForReversingAnser)
    waitforrqansernow = waitforrqansernow.content

    waitforrqanser = waitforrqansernow.replace('أ', 'ا')
    waitforrqanser = waitforrqanser.replace("ؤ", 'و')
    waitforrqanser = waitforrqanser.replace('ة', 'ه')
    waitforrqanser = waitforrqanser.replace('ئ', 'ى')
    waitforrqanser = waitforrqanser.replace('إ', 'ا')
    waitforrqanser = waitforrqanser.replace('آ', 'ا')
    waitforrqanser = waitforrqanser.replace('ّ', '')
    waitforrqanser = waitforrqanser.replace('َ', '')
    waitforrqanser = waitforrqanser.replace('ً', '')
    waitforrqanser = waitforrqanser.replace('ُ', '')
    waitforrqanser = waitforrqanser.replace('ٌ', '')
    waitforrqanser = waitforrqanser.replace('ٍ', '')
    waitforrqanser = waitforrqanser.replace('ِ', '')
    waitforrqanser = waitforrqanser.replace('ْ', '')
    waitforrqanser = waitforrqanser.replace('َ', '')
    waitforrqanser = waitforrqanser.replace('َ', '')
    waitforrqanser = waitforrqanser.replace('َ', '')
    waitforrqanser = waitforrqanser.replace('َ', '')
    waitforrqanser = waitforrqanser.replace('ّ', '')
    waitforrqanser = waitforrqanser.replace('ً', '')
    waitforrqanser = waitforrqanser.replace('ُ', '')
    waitforrqanser = waitforrqanser.replace('ِ', '')
    waitforrqanser = waitforrqanser.replace('ٍ', '')
    waitforrqanser = waitforrqanser.replace('ْ', '')
    waitforrqanser = waitforrqanser.replace('ٌ', '')
    waitforrqanser = waitforrqanser.replace('ـ', '')
    waitforrqanser = waitforrqanser.replace('ٰ', '')
    waitforrqanser = waitforrqanser.replace('ٰ', '')
    waitforrqanser = waitforrqanser.replace('ٓ', '')
    waitforrqanser = waitforrqanser.replace('ال', '')


    if waitforrqanser == answer:reverseResultAnserEmbed = discord.Embed(title='**:white_check_mark: اجابة صحيحة!**', color=assist.embedColors.ligh_green, timestamp = datetime.datetime.now())
    else:reverseResultAnserEmbed = discord.Embed(title='**:x: اجابة خاطئة!**', description=f'الاجابة الصحيحة هي: **{fqAnserIs}**', color=assist.embedColors.red, timestamp = datetime.datetime.now())
    try:reverseResultAnserEmbed.set_footer(text=ctx.author, icon_url=ctx.author.avatar.url)
    except:reverseResultAnserEmbed.set_footer(text=ctx.author, icon_url=ctx.author.default_avatar.url)
    reverseResultAnserEmbed.set_author(icon_url=client.user.avatar.url, name='mzooz games bot', url=assist.mzo0zServer)
    await ff.edit(embed=reverseResultAnserEmbed)


