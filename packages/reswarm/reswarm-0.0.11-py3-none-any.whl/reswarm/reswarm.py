import asyncio
import os
from autobahn.wamp.types import PublishOptions
from .crossbar import CrossbarConnection

class Reswarm():
    def __init__(self, **options):
        self.quiet = options.get("quiet", False)
        self.serial_number = os.environ.get('DEVICE_SERIAL_NUMBER', options.get("serial_number"))
        if self.serial_number == None:
            raise Exception("serial number is missing")

        self.cb_connection = CrossbarConnection(self.serial_number, self.quiet)
        self.cb_connection.start()

    def register(self, topic: str, procedure):
        session = self.cb_connection.getSession()
        threadedLoop = self.cb_connection.getEventLoop()

        async def registerFunc():
            return await session.register(topic, procedure)

        concurrentFuture = asyncio.run_coroutine_threadsafe(registerFunc(), threadedLoop)
        return asyncio.wrap_future(concurrentFuture)

    def subscribe(self, topic: str, handler):
        session = self.cb_connection.getSession()
        threadedLoop = self.cb_connection.getEventLoop()

        async def subscribeFunc():
            return await session.subscribe(handler, topic)

        concurrentFuture = asyncio.run_coroutine_threadsafe(subscribeFunc(), threadedLoop)
        return asyncio.wrap_future(concurrentFuture)

    def publish(self, topic: str, *args: list):
        device_name = os.environ.get("DEVICE_NAME")

        session = self.cb_connection.getSession()
        threadedLoop = self.cb_connection.getEventLoop()

        extra = {
            "DEVICE_SERIAL_NUMBER": self.serial_number,
            "options": PublishOptions(acknowledge=True)
        }

        if device_name:
            extra["DEVICE_NAME"] = device_name

        async def publishFunc():
            return await session.publish(topic, *args, **extra)

        concurrentFuture = asyncio.run_coroutine_threadsafe(publishFunc(), threadedLoop)
        return asyncio.wrap_future(concurrentFuture)