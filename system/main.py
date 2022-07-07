import discord
import assist
import json
import asyncio
from discord.ext import commands
from . import system
from . import antiBadWords
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
    def __init__(self, client, invites):
        system.addSafeChannel()
        antiBadWords.start(client)
        @client.listen("on_message")
        async def on_message(ctx):
            await system.onMessage(ctx, client)

        async def example():
            data = load(assist.jsonFile)
            data["welcome"]["invites_dict"][data['serverId']] = []
            for invite in invites:
                data["welcome"]["invites_dict"][data['serverId']].append(tuple((invite.code, invite.uses)))
                data["welcome"]["invites_dict"][data['serverId']] = list(set(data["welcome"]["invites_dict"][data['serverId']]))
            dump(assist.jsonFile, data)
            return
        asyncio.run(example())


        @client.listen("on_invite_create")
        async def on_invite_create(invite):
            await system.set_invites(invite.guild)

        @client.listen("on_invite_delete")
        async def on_invite_delete(invite):
            await system.set_invites(invite.guild)

        @client.listen("on_member_ban")
        async def on_member_ban(guild, user):
            await system.on_member_ban(guild, user, client)

        @client.listen("on_member_unban")
        async def on_member_unban(guild, user):
            await system.on_member_unban(guild, user, client)

        @client.listen('on_member_join')
        async def systemOnMemberJoin(member:discord.Member):
            await system.onMemberJoin(member, client)

        @client.listen('on_member_remove')
        async def on_member_remove(member):
            await system.onMemberRemove(member, client)

        @client.listen("on_message_edit")
        async def on_message_edit(before, after):
            await system.onMessageUpdate(before, after, client)

        @client.listen("on_guild_channel_update")
        async def on_guild_channel_update(before, after):
            await system.on_guild_channel_update(before, after, client)

        @client.listen("on_member_update")
        async def on_member_update(before, after):
            await system.on_member_update(before, after, client)

        @client.listen("on_guild_role_create")
        async def on_guild_role_create(role):
            await system.on_guild_role_create(role, client)

        @client.listen("on_guild_role_delete")
        async def on_guild_role_delete(role):
            await system.on_guild_role_delete(role, client)

        @client.listen("on_guild_role_update")
        async def on_guild_role_update(before, after):
            await system.on_guild_role_update(before, after, client)

        @client.listen('on_message_delete')
        async def on_message_delete(message):
            await system.onMessageDelete(message, client)

        @client.listen("on_guild_channel_delete")
        async def on_guild_channel_delete(channel):
            await system.on_guild_channel_delete(channel, client)

        @client.listen("on_guild_channel_create")
        async def on_guild_channel_create(channel):
            await system.on_guild_channel_create(channel, client)


        @client.command(aliases=['عضو'])
        async def user(ctx, usr:discord.Member=None):
            await system.User(ctx, client, usr)

        @client.command(aliases=['خط'])
        async def line(ctx):
            await system.LINE(ctx)

        @client.command(aliases=['افتار'])
        async def avatar(ctx, user:discord.Member=None):
            await system.Avatar(ctx, client, user)

        @client.command(aliases=['سيرفر'])
        async def server(ctx):
            await system.SERVER(ctx, client)

#        @client.command()
#        async def embed(ctx):
#            await system.addEmbed(ctx, client)

        @client.command(aliases=['بنق'])
        async def ping(ctx):
            await system.png(ctx, client)

        @client.command(aliases=['نرد'])
        async def roll(ctx):
            await system.Roll(ctx, client)

        @client.command(aliases=['رولات'])
        async def roles(ctx):
            await system.ROLES(ctx, client)

        @client.command(aliases=['رومات'])
        async def rooms(ctx):
            await system.ROOMS(ctx, client)

        @client.command(aliases=['ميمز', 'meme', 'ميم'])
        async def memes(ctx):
            await system.mms(ctx, client)

        @client.command()
        async def add_meme(ctx, url):
            await system.AddMeme(ctx, client, url)

        @client.command(aliases=['ضريبة', 'ضريبه'])
        async def tax(ctx, income:int=None):
            await system.TAX(ctx, client, income)

##########################################################################
##########################################################################
########################### managers commands  ###########################
##########################################################################
##########################################################################
#        @client.command(aliases=['حذف', 'ازالة'])
#        @commands.has_permissions(manage_roles=True)
#        async def remove(ctx, user:discord.Member=None):
#            await system.Remove(ctx, client, user)

        @client.listen('on_message')
        async def on(ctx):
            if ctx.author.id != client.user.id:
                if ctx.content.startswith(load(assist.jsonFile)['prefix']):
                    message = ctx.content[1:]

                    ## kick##
                    try:msgg=message.split(' ');msg=msgg[0];user=msgg=ctx.guild.get_member(int(msgg[1][2:-1]))
                    except:msgg=message.split(' ');msg=msgg[0];user=None
                    if msg in load(assist.jsonFile)['commands']['kick'] or msg.lower()=='kick' and ctx.author.guild_permissions.kick_members:await system.KICK(ctx, client, user)

                    ## ban ##
                    try:msgg=message.split(' ');msg=msgg[0];user=msgg=ctx.guild.get_member(int(msgg[1][2:-1]))
                    except:msgg=message.split(' ');msg=msgg[0];user=None
                    if msg in load(assist.jsonFile)['commands']['ban'] or msg.lower()=='ban' and ctx.author.guild_permissions.ban_members:await system.BAN(ctx, client, user)

                    ## unBan ##
                    try:msgg=message.split(' ');msg=msgg[0];user=msgg=await client.fetch_user(int(msgg[1][2:-1]))
                    except:msgg=message.split(' ');msg=msgg[0];user=None
                    if msg in load(assist.jsonFile)['commands']['unBan'] or msg.lower()=='unban'and ctx.author.guild_permissions.ban_members:await system.UNban(ctx, client, user)

                    ## clear ##
                    try:msgg=message.split(' ');msg=msgg[0];limit=int(msgg[1])
                    except:msg=message; limit=100
                    if msg in load(assist.jsonFile)['commands']['clear'] or msg.lower()=='clear' and ctx.author.guild_permissions.manage_messages:await system.Clear(ctx, client, int(limit))

                    ## role ##
                    try:msgg=message.split(' ');msg=msgg[0];user=ctx.guild.get_member(int(msgg[1][2:-1]));role=msgg[2]
                    except:msgg=message.split(' ');msg=msgg[0];user=None; role=None
                    if msg in load(assist.jsonFile)['commands']['role'] or msg.lower()=='role' and ctx.author.guild_permissions.manage_roles:await system.ROLE(ctx, client, user, role)

                    ## unRole ##
                    try:msgg=message.split(' ');msg=msgg[0];user=ctx.guild.get_member(int(msgg[1][2:-1]));role=msgg[2]
                    except:msgg=message.split(' ');msg=msgg[0];user=None; role=None
                    if msg in load(assist.jsonFile)['commands']['unRole'] or msg.lower()=='unrole' and ctx.author.guild_permissions.manage_roles:await system.UNRole(ctx, client, user, role)

                    ## lock ##
                    msgg=message.split(' ');msg=msgg[0]
                    if msg in load(assist.jsonFile)['commands']['lock'] or msg.lower()=='lock' and ctx.author.guild_permissions.manage_channels:await system.LOCK(ctx, client)

                    ## unLock ##
                    msgg=message.split(' ');msg=msgg[0]
                    if msg in load(assist.jsonFile)['commands']['unLock'] or msg.lower()=='unlock' and ctx.author.guild_permissions.manage_channels:await system.UNlock(ctx, client)

                    ## mute ##
                    try:msgg=message.split(' ');msg=msgg[0];user=ctx.guild.get_member(int(msgg[1][2:-1]))
                    except:msgg=message.split(' ');msg=msgg[0];user=None
                    if msg in load(assist.jsonFile)['commands']['mute'] or msg.lower()=='mute' and ctx.author.guild_permissions.manage_roles:await system.MUTE(ctx, client, user)

                    ## unMute ##
                    try:msgg=message.split(' ');msg=msgg[0];user=ctx.guild.get_member(int(msgg[1][2:-1]))
                    except:msgg=message.split(' ');msg=msgg[0];user=None
                    if msg in load(assist.jsonFile)['commands']['unMute'] or msg.lower()=='unmute' and ctx.author.guild_permissions.manage_roles:await system.UNMUTE(ctx, client, user)

