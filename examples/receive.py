"""
    Hello world `receive.py` example implementation using aioamqp.
    See the documentation for more informations.
"""

import asyncio
import aioamqp

@asyncio.coroutine
def callback(channel, body, envelope, properties):
    global n
    n += 1
    #print(" [x] Received %r" % body)

@asyncio.coroutine
def receive():
    transport, protocol = yield from aioamqp.connect()
    channel = yield from protocol.channel()

    yield from channel.queue_declare(queue_name='hello')

    yield from channel.basic_consume(callback, queue_name='hello', no_ack=True)

    global n
    n = 0
    while True:
        yield from asyncio.sleep(1, loop=event_loop)
        print('n=', n)
        n = 0


event_loop = asyncio.get_event_loop()
event_loop.run_until_complete(receive())
event_loop.run_forever()
