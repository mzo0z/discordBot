from . import main
from . import ipcThings
from threading import Thread

class start:
    def __init__(self, client):
        def two():
            try:ipcThings.start(client)
            except:pass
        t = Thread(target=two)
        t.start()
        try:main.start(client)
        except:pass


