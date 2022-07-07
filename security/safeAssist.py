import os
from itertools import cycle
from shutil import get_terminal_size
from threading import Thread
from time import sleep
import json

LIT           = os.getcwd()  + '\\'
privateFiles  = LIT          + "templates\\"
safejson      = privateFiles + 'system\\security.json'


class embedColors:
    default = 0
    teal = 0x1abc9c
    dark_teal = 0x11806a
    green = 0x2ecc71
    ligh_green = 0x44ff44
    dark_green = 0x1f8b4c
    blue = 0x3498db
    dark_blue = 0x206694
    purple = 0x9b59b6
    dark_purple = 0x71368a
    magenta = 0xe91e63
    dark_magenta = 0xad1457
    yellow = 0xffd000
    gold = 0xf1c40f
    dark_gold = 0xc27c0e
    orange = 0xe67e22
    dark_orange = 0xa84300
    light_orange = 0xff6600
    light_red = 0xe74c3c
    dark_red = 0x992d22
    red = 0x990000
    lighter_grey = 0x95a5a6
    dark_grey = 0x607d8b
    light_grey = 0x979c9f
    darker_grey = 0x546e7a
    blurple = 0x7289da
    greyple = 0x99aab5

class colors():
    def coloring(msg, color):
        black=f'\033[30m{msg}\033[0;0m'
        red=f'\033[31m{msg}\033[0;0m'
        green=f'\033[32m{msg}\033[0;0m'
        orange=f'\033[33m{msg}\033[0;0m'
        blue=f'\033[34m{msg}\033[0;0m'
        purple=f'\033[35m{msg}\033[0;0m'
        cyan=f'\033[36m{msg}\033[0;0m'
        lightgrey=f'\033[37m{msg}\033[0;0m'
        darkgrey=f'\033[90m{msg}\033[0;0m'
        lightred=f'\033[91m{msg}\033[0;0m'
        lightgreen=f'\033[92m{msg}\033[0;0m'
        yellow=f'\033[93m{msg}\033[0;0m'
        lightblue=f'\033[94m{msg}\033[0;0m'
        pink=f'\033[95m{msg}\033[0;0m'
        lightcyan=f'\033[96m{msg}\033[0;0m'
        toReturn = {
            'black'      : black,
            'red'        : red,
            'green'      : green,
            'orange'     : orange,
            'blue'       : blue,
            'cyan'       : cyan,
            'purple'     : purple,
            'lightgrey'  : lightgrey,
            'darkgrey'   : darkgrey,
            'lightred'   : lightred,
            'lightgreen' : lightgreen,
            'yellow'     : yellow,
            'lightblue'  :lightblue,
            'pink'       :pink,
            'lightcyan'  :lightcyan}
        return toReturn[color]