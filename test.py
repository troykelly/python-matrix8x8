#!/usr/bin/env python3
import json
import logging
import asyncio
from matrix8x8_lib import HDMIMatrix

logging.basicConfig(level=logging.DEBUG,
                    format="[%(asctime)s] %(name)s {%(filename)s:%(lineno)d} %(levelname)s - %(message)s")
LOG = logging.getLogger(__name__)

OPTIONS_FILE = 'test/options.json'

loop = asyncio.get_event_loop()
hdmi = None

def handleEvent(event=None, hdmi=None):
    #LOG.info("Received Event: %s" % event.eventType)
    LOG.debug(event.toJson())


def handleConnect(event=None, hdmi=None):
    LOG.info("Connected to HDMI Matrix")
    #dynalite.devices['area'][8].preset[10].turnOn()
    hdmi.state()


if __name__ == '__main__':
    with open(OPTIONS_FILE, 'r') as f:
        cfg = json.load(f)

    hdmi = HDMIMatrix(config=cfg, loop=loop)

    bcstr = hdmi.addListener(listenerFunction=handleEvent)
    bcstr.monitorEvent('*')

    onConnect = hdmi.addListener(listenerFunction=handleConnect)
    onConnect.monitorEvent('CONNECTED')

    hdmi.start()
    loop.run_forever()
