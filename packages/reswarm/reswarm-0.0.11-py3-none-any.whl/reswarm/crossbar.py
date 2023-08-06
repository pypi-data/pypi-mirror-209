import asyncio
import os
import threading
import sys
from autobahn.asyncio.wamp import ApplicationSession
from autobahn.wamp import auth
from autobahn.asyncio.wamp import ApplicationSession
from autobahn.wamp import auth
from autobahn.asyncio.wamp import ApplicationRunner

if sys.version_info[:2] >= (3, 7):
    from asyncio import get_running_loop
else:
    from asyncio import _get_running_loop as get_running_loop

DATAPODS_WS_URI = "wss://cbw.datapods.io/ws-ua-usr";
STUDIO_WS_URI = "wss://cbw.record-evolution.com/ws-ua-usr";
LOCALHOST_WS_URI = "ws://crossbar_node1/ws-ua-usr";

socketURIMap = {
    "https://studio.datapods.io": DATAPODS_WS_URI,
    "https://studio.record-evolution.com": STUDIO_WS_URI,
    "http://localhost:8085": LOCALHOST_WS_URI
}

def getWebSocketURI():
    reswarm_url = os.environ.get("RESWARM_URL")
    if not reswarm_url:
        return STUDIO_WS_URI
    return socketURIMap.get(reswarm_url)

class _Component(ApplicationSession):
    def __init__(self, config=None, serial_number=None, setSession=None, quiet=False):
        super().__init__(config=config)

        self.serial_number = serial_number
        self.quiet = quiet
        self.setSession = setSession

    def onConnect(self):
        self.join(u'userapps', [u"wampcra"], self.serial_number)

    def onChallenge(self, challenge):
        if challenge.method == u"wampcra":
            signature = auth.compute_wcs(self.serial_number, challenge.extra['challenge'])
            return signature

        raise Exception("Invalid authmethod {}".format(challenge.method))

    def onJoin(self, details):
        if not self.quiet:
            print(f"Successfully joined {details.realm} realm")

        self.setSession(self)

    def onLeave(self, details):
        self.disconnect()

    def onDisconnect(self):
        loop = get_running_loop()

        loop.stop()
        loop.close()


class CrossbarConnection():
    def __init__(self, serial_number: str, quiet=False) -> None:
        self.session = None
        self.loop = None
        self.quiet = quiet
        self.serial_number = serial_number

    def start(self):
        t = threading.Thread(target=self._initSessionLoop)
        t.start()

    def _setSession(self, session):
        self.session = session

    def getEventLoop(self):
        while self.loop == None:
            continue

        return self.loop

    def getSession(self) -> ApplicationSession:
        while self.session == None:
            continue

        return self.session

    def _componentAdapter(self, serial_number, setSession, quiet):
        def x(config):
            return _Component(config, serial_number, setSession, quiet)

        return x

    def _initSessionLoop(self):
        self.runner = ApplicationRunner(
            url=getWebSocketURI(),
            realm="userapps"
        )

        loop = asyncio.new_event_loop()
        self.loop = loop

        asyncio.set_event_loop(loop)
        component = self._componentAdapter(self.serial_number, self._setSession, self.quiet)
        coro = self.runner.run(component, False)
        loop.run_until_complete(coro)
        loop.run_forever()
