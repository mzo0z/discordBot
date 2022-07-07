import random
import discord
import assist
from typing import List


async def start(ctx, client, names=None):
    gameName = '**x - o**'
    ids = []
    players = []
    await ctx.message.delete()
    xoLeader = ctx.author.id
    if names==None:
        mentionPlayers = discord.Embed(title=gameName, description=f"<@{xoLeader}> منشن الشخص الذي ستلعب معه", color=(assist.embedColors.yellow))
        mentionPlayers.set_author(name='mzooz games bot', icon_url=(client.user.avatar.url), url=assist.mzo0zServer)
        msg = await ctx.channel.send(embed=mentionPlayers)
        def playersToPlayDescribe(m):return m.channel == ctx.channel and m.author == ctx.author

        playersToPlay = await client.wait_for('message', check=playersToPlayDescribe)
        await playersToPlay.delete()
        playersToPlay = playersToPlay.content
    else:playersToPlay = names
    for desplayer in playersToPlay.split(' '):
        if desplayer != '' and desplayer != ' ':
            try:
                user = await client.fetch_user(int(desplayer[2:-1]))
                if user.bot != True and user.id != xoLeader:
                    break
            except:pass

    players.append(xoLeader)
    players.append(user.id)

    try:await msg.delete()
    except:pass
    playersToPlayXo = [int(i) for i in players]
    xPlayer = random.choice(playersToPlayXo)
    ids.append(xPlayer)
    playersToPlayXo.remove(xPlayer)
    oPlayer = random.choice(playersToPlayXo)
    ids.append(oPlayer)

    xPlayer = f'<@{xPlayer}>'
    oPlayer = f'<@{oPlayer}>'


    t = f'''
{xPlayer} = X
{oPlayer} = O
--------------
{xPlayer} ابدأ
    '''
    xoEmbed = discord.Embed(title=gameName, description=t, color=assist.embedColors.blue)
    class TicTacToeButton(discord.ui.Button['TicTacToe']):
        def __init__(self, x: int, y: int):
            super().__init__(style=discord.ButtonStyle.secondary, label='\u200b', row=y)
            self.x = x
            self.y = y

        async def callback(self, interaction: discord.Interaction):
            assert self.view is not None
            view: TicTacToe = self.view
            state = view.board[self.y][self.x]
            if state in (view.X, view.O):return
            if interaction.user.id in ids:
                if interaction.user.id == int(xPlayer[2:-1]):
                    if view.current_player == view.X:
                        self.style = discord.ButtonStyle.danger
                        self.label = 'X'
                        self.disabled = True
                        view.board[self.y][self.x] = view.X
                        view.current_player = view.O
                        content = discord.Embed(title=gameName, description=f"دور {oPlayer}", color=assist.embedColors.ligh_green)
                if interaction.user.id == int(oPlayer[2:-1]):
                    if view.current_player == view.O:
                        self.style = discord.ButtonStyle.success
                        self.label = 'O'
                        self.disabled = True
                        view.board[self.y][self.x] = view.O
                        view.current_player = view.X
                        content = discord.Embed(title=gameName, description=f"دور {xPlayer}", color=assist.embedColors.red)

                winner = view.check_board_winner()
                if winner is not None:
                    if winner == view.X:content = discord.Embed(title=gameName, description=f'الفايز {xPlayer}', color=assist.embedColors.gold)
                    elif winner == view.O:content = discord.Embed(title=gameName, description=f'الفايز {oPlayer}', color=assist.embedColors.gold)
                    else:content = discord.Embed(title=gameName, description=f'تعادل', color=assist.embedColors.darker_grey)
                    for child in view.children:child.disabled = True
                    view.stop()
                try:await interaction.response.edit_message(embed=content, view=view)
                except:pass


    class TicTacToe(discord.ui.View):
        children: List[TicTacToeButton]
        X = -1
        O = 1
        Tie = 2

        def __init__(self):
            super().__init__()
            self.current_player = self.X
            self.board = [
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 0],
            ]

            for x in range(3):
                for y in range(3):
                    self.add_item(TicTacToeButton(x, y))

        def check_board_winner(self):
            for across in self.board:
                value = sum(across)
                if value == 3:
                    return self.O
                elif value == -3:
                    return self.X

            for line in range(3):
                value = self.board[0][line] + self.board[1][line] + self.board[2][line]
                if value == 3:
                    return self.O
                elif value == -3:
                    return self.X

            diag = self.board[0][2] + self.board[1][1] + self.board[2][0]
            if diag == 3:
                return self.O
            elif diag == -3:
                return self.X

            diag = self.board[0][0] + self.board[1][1] + self.board[2][2]
            if diag == 3:
                return self.O
            elif diag == -3:
                return self.X

            if all(i != 0 for row in self.board for i in row):
                return self.Tie

            return None

    
    await ctx.channel.send(embed=xoEmbed, view=TicTacToe())
