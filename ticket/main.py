import json
#import chat_exporter
import discord
import io
import requests
import datetime
import assist
import os
from discord.ext import commands
from . import Ticket
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
        if not os.path.exists(assist.tickjson):
#            os.mkdir(assist.scrpt)
            dump(assist.tickjson, {})
            DATA = load(assist.tickjson)
            DATA[load(assist.jsonFile)["serverId"]] = {}
            DATA[load(assist.jsonFile)["serverId"]]['tickets'] = {}
            DATA[load(assist.jsonFile)["serverId"]]['category'] = 0
            dump(assist.tickjson, DATA)

        @client.command()
        @commands.has_permissions(manage_channels=True)
        async def ticket(ctx):await Ticket.create(ctx, client)

        @client.command()
        @commands.has_permissions(manage_channels=True)
        async def تيكت(ctx):await Ticket.create(ctx, client)

        @client.listen("on_interaction")
        async def on_interaction(interaction):
            cid = interaction.data['custom_id']
            tickets = load(assist.tickjson)
#            n = f'transcriptFor{cid}'
            try:
                if str(interaction.message) == tickets[str(interaction.guild.id)]["tickets"][cid]["msg"]:
                    await Ticket.opn(interaction, client, cid)
            except:
                try:
                    if interaction.channel.id == tickets[str(interaction.guild.id)][cid]["msg"]:
                        ch = await client.fetch_channel(tickets[str(interaction.guild.id)][cid]["msg"])
                        del tickets[str(interaction.guild.id)][cid]
#                        del tickets[str(interaction.guild.id)][n]
                        dump(assist.tickjson, tickets)
                        await ch.delete() 
                except:
                    try:
                        if interaction.channel.id == tickets[str(interaction.guild.id)][cid]["transcript"]:
                            await interaction.response.send_message('هذه النسخة لاندعم نظام النسخ الاحتياطية')
#                            transcript = await chat_exporter.export(interaction.channel)
#                            transcript_file = discord.File(io.BytesIO(transcript.encode('utf-8')), filename=f"{interaction.channel.name}.html")        
#                            channel = await client.fetch_channel(interaction.channel.id)
#                            await channel.send(file=transcript_file)
                    except:
                        try:
                            if interaction.channel.id == tickets[str(interaction.guild.id)][cid]["closeTicket"]:
                                await interaction.channel.set_permissions(interaction.user, read_messages=False)

#                                transcript = await chat_exporter.export(interaction.channel)
#                                transcript_file = discord.File(io.BytesIO(transcript.encode('utf-8')), filename=f"{interaction.channel.name}.html")
#                                with open(assist.scrpt + f"{interaction.channel.name}.html", 'wb') as f:f.write(transcript.encode('utf-8'));f.close()

                                r = requests.get('https://cdn.discordapp.com/attachments/926554426154553354/946555432699306018/mzo0z.png')
                                if r.status_code == 200:
                                    for chunk in r.iter_content(chunk_size=512 * 1024):
                                        if chunk:pass

                                afterClose = discord.ui.View()
#                                transcriptButton = discord.ui.Button(style=discord.ButtonStyle.success, label='transcript', row=0, custom_id=n)
                                deleteTicket = discord.ui.Button(style=discord.ButtonStyle.red, label='حذف التيكت', row=0, custom_id=cid)
#                                afterClose.add_item(transcriptButton)
                                afterClose.add_item(deleteTicket)

#                                embed = discord.Embed(title=f'هل تريد حذف التيكت؟\nام تريد اخذ نسخة؟\nام الاثنين؟', color=assist.embedColors.dark_teal, url='https://discord.gg/7gzWBSCbY6')
                                embed = discord.Embed(title=f'هل تريد حذف التيكت؟', color=assist.embedColors.dark_teal)
                                embed.set_author(name='mzooz bot', icon_url=client.user.avatar.url, url=assist.mzo0zServer)
                                embed.timestamp = datetime.datetime.now()
                                try:embed.set_footer(text=interaction.user, icon_url=interaction.user.avatar.url)
                                except:embed.set_footer(text=interaction.user, icon_url=client.user.avatar.url)
                                await interaction.response.send_message(embed=embed, view = afterClose)
                                dump(assist.tickjson, tickets)
                                t = load(assist.tickjson)
                                t[str(interaction.guild.id)][cid] = {}
                                t[str(interaction.guild.id)][cid]["msg"] = interaction.channel.id
#                                t[str(interaction.guild.id)][n] = {}
#                                t[str(interaction.guild.id)][n]["transcript"] = interaction.channel.id
                                dump(assist.tickjson, t)

                        except:pass
