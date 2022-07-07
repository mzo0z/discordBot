from . import main
from . import ipcThings
from threading import Thread

class start:
    def __init__(self, client, guild):
        def two():
            try:ipcThings.start(client)
            except:pass
        t = Thread(target=two)
        t.start()
        main.start(client, guild)


