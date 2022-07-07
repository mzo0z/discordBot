from . import main
from . import ipcThings
from threading import Thread

class start:
    def __init__(self, client):
        def one():
           try:main.start(client)
           except:pass
        def two():
            try:ipcThings.start(client)
            except:pass
        o = Thread(target=one)
        o.start()
        t = Thread(target=two)
        t.start()


