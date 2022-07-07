import json
import assist
import discord

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
        @client.event
        async def on_ipc_error(endpoint, error):
            print(endpoint, "raised", error)

        @client.ipc.route()
        async def getRoles(data):
            roles = {}
            guild = client.guilds[0]
            for role in guild.roles:
                if role.name != "@everyone":roles.update({role.name:role.id})
            return roles

        @client.ipc.route()
        async def getMembers(data):
            members = {}
            guild = client.guilds[0]
            for member in guild.members:
                members.update({member.name:member.id})
            return members
        
        @client.ipc.route()
        async def trustedMembers(data):
            members = {}
            guild = client.guilds[0]
            for memberId in data.safe:
                try:member = await client.fetch_user(memberId)
                except:member = discord.utils.get(guild.roles, id=memberId)
                members.update({member.name:member.id})
            return members

        @client.ipc.route()
        async def getMembersAndRoles(data):
            ALL = {}
            guild = client.guilds[0]
            for role in guild.roles:
                if role.name != "@everyone":ALL.update({role.name:role.id})
            for member in guild.members:
                ALL.update({member.name:member.id})

            return ALL

