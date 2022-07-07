import datetime
import discord
from discord.ext import commands
import assist
import json
import asyncio
import random
from time import sleep

def load(file):
    with open(file, 'r') as f:DATA = json.load(f);return DATA
def dump(file, DATA):
    with open(file, 'w') as f:json.dump(DATA, f);f.close();return

class start:
    def __init__(self, client):
        @client.command(aliases=['gStart', 'giveaway', 'giveAway', 'give', 'قيف'])
        @commands.has_permissions(manage_events=True)
        async def gstart(ctx):
            give = {
                'prize':'iphone 13 pro max',
                'channel':0,
                'host':ctx.author,
                'time':'10s',
            }
            await ctx.message.delete()
            class questions(discord.ui.View):
                @discord.ui.button(label='إالغاء', style=discord.ButtonStyle.danger, row=0)
                async def callBack(self, button:discord.Button, interaction:discord.Interaction):
                    embed = discord.Embed(title="تم إالغاء القيف اواي", color=assist.embedColors.red ,timestamp=datetime.datetime.now())
                    embed.set_author(name = 'mzooz giveaway bot', icon_url=client.user.avatar.url, url=assist.mzo0zServer)
                    try:embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar.url)
                    except:embed.set_footer(text=ctx.author, icon_url=ctx.author.default_avatar.url)
                    await interaction.message.delete()
                    await ctx.channel.send(embed=embed, delete_after=5)

            embed = discord.Embed(title='ماهي الجائزة؟', color=ctx.author.color, timestamp=datetime.datetime.now())
            embed.set_author(name='mzooz giveaway bot', icon_url=client.user.avatar.url, url=assist.mzo0zServer)
            try:embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar.url)
            except:embed.set_footer(text=ctx.author, icon_url=ctx.author.default_avatar.url)
            msgEmbed = await ctx.channel.send(embed=embed, view=questions())
            def getPrize(m):return m.author == ctx.author and m.channel == ctx.channel
            try:msg = await client.wait_for("message", check=getPrize, timeout=20.0)
            except asyncio.TimeoutError:await ctx.channel.send(embed=discord.Embed(title='انتهى الوقت, لم تجب في الوقت', color=assist.embedColors.red, timestamp=datetime.datetime.now()).set_author(name='mzooz giveaway bot', icon_url=client.user.avatar.url, url=assist.mzo0zServer)); return
            else:give.update({'prize':msg.content});await msg.delete()
            embed.title='منشن قناة القيف اواي'
            await msgEmbed.edit(embed=embed)
            def getChannel(m):return m.author == ctx.author and m.channel == ctx.channel
            try:msg = await client.wait_for("message", check=getChannel, timeout=20.0)
            except asyncio.TimeoutError:await ctx.channel.send(embed=discord.Embed(title='انتهى الوقت, لم تجب في الوقت', color=assist.embedColors.red, timestamp=datetime.datetime.now()).set_author(name='mzooz giveaway bot', icon_url=client.user.avatar.url, url=assist.mzo0zServer)); return
            else:
                try:tm = int(msg.content[2:-1])
                except:await msg.delete();await msgEmbed.delete();await ctx.channel.send(embed=discord.Embed(title=f'يجب عليك منشن القناة', color=assist.embedColors.red, timestamp=datetime.datetime.now()).set_author(name='mzooz giveaway bot', icon_url=client.user.avatar.url, url=assist.mzo0zServer), delete_after=5);return 0
                else:give.update({'channel':tm});await msg.delete()

            embed.title='كم مدة القيف اواي'
            await msgEmbed.edit(embed=embed)
            def getTime(m):return m.author == ctx.author and m.channel == ctx.channel
            try:msg = await client.wait_for("message", check=getTime, timeout=20.0)
            except asyncio.TimeoutError:await ctx.channel.send(embed=discord.Embed(title='انتهى الوقت, لم تجب في الوقت', color=assist.embedColors.red, timestamp=datetime.datetime.now()).set_author(name='mzooz giveaway bot', icon_url=client.user.avatar.url, url=assist.mzo0zServer)); return
            else:give.update({'time':msg.content});await msg.delete()
            await msgEmbed.delete()

            timing = convert(give['time'])
            if timing == -1:await ctx.channel.send(embed=discord.Embed(title='لم تدخل نوع الوقت : ( s | m | h | d )', color=assist.embedColors.red, timestamp=datetime.datetime.now()).set_author(name='mzooz giveaway bot', icon_url=client.user.avatar.url, url=assist.mzo0zServer), delete_after=10); return
            elif timing == -2:await ctx.channel.send(embed=discord.Embed(title='يجب ان يكون الوقت رقم, ولاتنسى كتابة نوع الوقت: ( s | m | h | d )', color=assist.embedColors.red, timestamp=datetime.datetime.now()).set_author(name='mzooz giveaway bot', icon_url=client.user.avatar.url, url=assist.mzo0zServer), delete_after=10); return


            embed = discord.Embed(title='قيف اواي', description=f'**الجائزة: {give["prize"]}**', color=assist.embedColors.blurple, timestamp=datetime.datetime.now())
            eve = f'سيتم اختيار الفائز بعد {timing}'
            embed.add_field(name=eve, value='** **')
            embed.set_author(name='mzooz bot', icon_url=client.user.avatar.url)
            try:embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar.url)
            except:embed.set_footer(text=ctx.author, icon_url=ctx.author.default_avatar.url)
            channel = await client.fetch_channel(give['channel'])
            timer = await channel.send('@everyone', embed=embed)
            await timer.add_reaction("🎉")

            for time in range(timing, 0, -1):
                embed = discord.Embed(title='قيف اواي', description=f'**الجائزة: {give["prize"]}**', color=assist.embedColors.blurple, timestamp=datetime.datetime.now())
                hour = time // 3600
                mint = time // 60
                sec  = time % 60
                t = f'{hour}:{mint}:{sec}'
                eve = f'سيتم اختيار الفائز بعد {t}'
                embed.add_field(name=eve, value='** **')
                embed.set_author(name='mzooz bot', icon_url=client.user.avatar.url)
                try:embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar.url)
                except:embed.set_footer(text=ctx.author)
                await timer.edit(content='@everyone', embed=embed)
                sleep(1)


            newMsg = await channel.fetch_message(timer.id)
            users = await newMsg.reactions[0].users().flatten()
            users.pop(users.index(client.user))

            embed = discord.Embed(title='قيف اواي', description=f'**الجائزة: {give["prize"]}**', color=assist.embedColors.blurple, timestamp=datetime.datetime.now())
            wenner = random.choice(users)
            eve = f'الفائز هو {wenner.mention}\nصاحب القيف اواي: {give["host"].mention}'

            embed.add_field(name="** **", value=eve)
            embed.set_author(name='mzooz bot', icon_url=client.user.avatar.url)
            try:embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar.url)
            except:embed.set_footer(text=ctx.author, icon_url=ctx.author.default_avatar.url)
            await timer.edit(embed=embed)
            await channel.send(f"{wenner.mention} مبروك لقد فزت في الـ {give['prize']}")


        def convert(time):
            pos = ["s", "m", "h", "d"]
            time_dict = {"s":1, "m":60, "h":3600, "d":3600*24}
            unit = time[-1]
            if unit not in pos:return -1
            try:val = int(time[:-1])
            except:return -2
            return val * time_dict[unit]
