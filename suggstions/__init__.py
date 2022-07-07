from datetime import datetime
import discord
import json
import assist

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
        DATA = load(assist.jsonFile)
        if "suggestions" not in DATA:
            DATA["suggestions"] = {}
            DATA["suggestions"][DATA["serverId"]] = {}
            DATA["suggestions"][DATA["serverId"]]["active"] = 0
            DATA["suggestions"][DATA["serverId"]]["suggestionsChannelId"] = []
            dump(assist.jsonFile, DATA)

        @client.listen("on_message")
        async def on_message(ctx):
            DATA = load(assist.jsonFile)
            if DATA["suggestions"][DATA["serverId"]]["active"] == 1:
                if ctx.author.id != client.user.id:
                    if ctx.channel.id in load(assist.jsonFile)["suggestions"][DATA["serverId"]]["suggestionsChannelId"] or str(ctx.channel.id) in load(assist.jsonFile)["suggestions"][DATA["serverId"]]["suggestionsChannelId"]:
                        try:await ctx.delete()
                        except:pass
                        channel = discord.utils.get(ctx.guild.text_channels, id = ctx.channel.id)
                        suggestEmbed = discord.Embed(description=f'المقترح: {ctx.author.mention}\nالاقتراح: {ctx.content}', color=assist.embedColors.green, timestamp=datetime.now())
                        suggestEmbed.set_author(name='mzooz bot', icon_url = client.user.avatar.url, url=assist.mzo0zServer)
                        try:suggestEmbed.set_footer(text=ctx.author, icon_url=ctx.author.avatar.url)
                        except:suggestEmbed.set_footer(text=ctx.author, icon_url=ctx.author.default_avatar.url)
                        message = await channel.send(embed=suggestEmbed)
                        await message.add_reaction('✅')
                        await message.add_reaction('❌')
