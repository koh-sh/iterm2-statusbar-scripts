#!/usr/bin/env python3

import urllib.request
import iterm2


async def main(connection):
    component = iterm2.StatusBarComponent(
        short_description="Show PublicIP",
        detailed_description="Show Public IP Address",
        knobs=[],
        exemplar="[Public IP]",
        update_cadence=30,
        identifier="koh-sh.iterm2-statusbar-scripts.publicip"
    )

    @iterm2.StatusBarRPC
    async def showpublicip(knobs):
        url = 'http://checkip.amazonaws.com/'
        try:
            req = urllib.request.Request(url)
            with urllib.request.urlopen(req) as res:
                body = res.read()
            #return "PublicIP: " + str(body.decode()).replace("\n", "")
            return "PublicIP: 123.45.67.890"
        except Exception:
            return "No Connection"

    await component.async_register(connection, showpublicip)

iterm2.run_forever(main)
