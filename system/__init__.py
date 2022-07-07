from . import main
from . import ipcThings
from threading import Thread

class start:
    def __init__(self, client, invites):
        def one():
           try:main.start(client, invites)
           except:pass
        def two():
            try:ipcThings.start(client)
            except:pass
        Thread(target=one).start()
        Thread(target=two).start()


