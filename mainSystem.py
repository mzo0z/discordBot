import assist
import os
import json
import discord
import io
import socket
from discord.ext import commands
from time import sleep
from threading import Thread
from itertools import cycle
from shutil import get_terminal_size

class Loader:
    def __init__(self, desc="Loading...", end="done create data!", timeout=0.1):
        self.desc = desc
        self.end = end
        self.timeout = timeout
        self._thread = Thread(target=self._animate, daemon=True)
        self.steps = ["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]
        self.done = False
    def start(self):self._thread.start(); return self
    def _animate(self):
        for c in cycle(self.steps):
            if self.done:break
            print(f"\r{self.desc} {c}", flush=True, end=""); sleep(self.timeout)
    def __enter__(self):self.start()
    def stop(self):self.done = True; cols = get_terminal_size((80, 20)).columns; print("\r" + " " * cols, end="", flush=True); print(assist.colors.coloring(f"\r{self.end}", 'green'), flush=True)
    def __exit__(self, exc_type, exc_value, tb):self.stop()

class creatingInfo:
    def __init__(self, desc="creating data", end="done create data!", timeout=0.1):
        self.desc = desc
        self.end = end
        self.timeout = timeout
        self._thread = Thread(target=self._animate, daemon=True)
        self.steps = ["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]
        self.done = False
    def start(self):
        self._thread.start()
        return self
    def _animate(self):
        for c in cycle(self.steps):
            if self.done:
                break
            print(f"\r{self.desc} {c}", flush=True, end="")
            sleep(self.timeout)
    def __enter__(self):
        self.start()
    def stop(self):
        self.done = True
        cols = get_terminal_size((80, 20)).columns
        print("\r" + " " * cols, end="", flush=True)
        print(assist.colors.coloring(f"\r{self.end}", 'green'), flush=True)
    def __exit__(self, exc_type, exc_value, tb):
        self.stop()


class MyHelpCommand(commands.MinimalHelpCommand):
    async def send_pages(self):
        global pageNumbers
        pageNumbers = {self.context.guild.id:1}
        destination = self.get_destination()
        def zero():
            global pageNumbers
            sleep(30)
            pageNumbers = {self.context.guild.id:1}
            return
        Thread(target=zero).start()
        try:guild   = self.context.guild.icon.url
        except:guild   = 'None'
        class pages(discord.ui.View):
            @discord.ui.button(style=discord.ButtonStyle.green, label='<<', row=1)
            async def BACK(self, button: discord.ui.Button, interaction: discord.Interaction):
                global pageNumbers
                pageNumbers.update({interaction.guild.id:pageNumbers[interaction.guild.id]-1})
                if pageNumbers[interaction.guild.id] <= 0:
                    pageNumbers.update({interaction.guild.id:4})
                    await interaction.response.edit_message(embed=Pages[pageNumbers[interaction.guild.id]], view=pages())
                else:await interaction.response.edit_message(embed=Pages[pageNumbers[interaction.guild.id]], view=pages())
            @discord.ui.button(style=discord.ButtonStyle.primary, label='more help', row=0)
            async def aa(self, button: discord.ui.Button, interaction: discord.Interaction):
                html = assist.helpHtml
                paths = {
                "kickCommands"  : "kick",
                "banCommands"   : "ban",
                "unBanCommands" : "unBan",
                "clearCommands" : "clear",
                "rolesCommands" : "role",
                "unRolesCommands" : "unRole",
                "lockCommands" : "lock",
                "unLockCommands" : "unLock",
                "muteCommands" : "mute",
                "unMuteCommands" : "unMute",
                }
                for i in paths.keys():
                    something = f'{paths[i]}'
                    for o in load(assist.jsonFile)['commands'][paths[i]]:
                        something = something + f' - {o}'
                    html = html.replace("{{"+i+"}}", something)

                htmlF = discord.File(io.BytesIO(html.encode('utf-8')), filename="moreHelp.html")
                await interaction.channel.send(file=htmlF)

            @discord.ui.button(style=discord.ButtonStyle.green, label='>>', row=1)
            async def NEXT(self, button: discord.ui.Button, interaction: discord.Interaction):
                global pageNumbers
                pageNumbers.update({interaction.guild.id:pageNumbers[interaction.guild.id]+1})
                if pageNumbers[interaction.guild.id] >= 5:
                    pageNumbers.update({interaction.guild.id:1})
                    await interaction.response.edit_message(embed=Pages[pageNumbers[interaction.guild.id]], view=pages())
                else:await interaction.response.edit_message(embed=Pages[pageNumbers[interaction.guild.id]], view=pages())
        def new(name, value, page, inline=False, ctx=None):
            hlp = discord.Embed(title=f'**help - مساعدة**', description=f'**{destination.guild.name}**', color=assist.embedColors.ligh_green)
            hlp.set_footer(text = f'الصفحة {page} من 4')
            hlp.set_author(name = 'mzooz bot', url=assist.mzo0zServer)
            if ctx != 'None':hlp.set_thumbnail(url=ctx)
            hlp.add_field(name=f'{name}', value=f'**{value}**', inline=inline)
            return hlp
        prefix = load(assist.jsonFile)["prefix"]
        Pages = {
            1 : new(name='** **', value=f'{assist.publicHelp(prefix)}', page=1, inline=True, ctx=guild),
            2 : new(name='** **', value=f'{assist.publicHelpCommands(prefix)}', page=2,inline=False, ctx=guild),
            3 : new(name='** **', value=f'{assist.adminsHelpCommand(prefix)}', page=3,inline=False, ctx=guild),
            4 : new(name='** **', value=f'{assist.gamesHelp(prefix)}', page=4, inline=False, ctx=guild),
            }
        await destination.send(embed=Pages[1], view=pages())


def load(file):
    with open(file, 'r') as f:
        DATA = json.load(f)
    return DATA

def dump(file, DATA):
    with open(file, 'w') as f:
        json.dump(DATA, f)
        f.close()
    return

def createInfo():
    cr = creatingInfo(assist.colors.coloring("creating data", 'pink'), assist.colors.coloring("done create data!", 'pink'), 0.3).start()
    for i in range(10):
        sleep(0.2)
    os.mkdir(assist.privateFiles)
    os.mkdir(assist.sstm)
    cr.stop()

def createJsonFile():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    host = s.getsockname()[0]
    s.close()
    dump(assist.jsonFile, {})
    DATA = load(assist.jsonFile)
    DATA["supportUrl"] = assist.mzo0zServer
    DATA["ownerId"]    = ""
    DATA["serverId"]   = 0
    DATA["botId"]      = 0
    DATA["prefix"]     = "-"
    DATA["secretKey"]  = assist.redurl
    DATA["botUrl"]     = ""
    DATA['host']       = host
    dump(assist.jsonFile, DATA)
