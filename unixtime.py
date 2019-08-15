#!/usr/bin/env python3

import time
import iterm2


async def main(connection):
    component = iterm2.StatusBarComponent(
        short_description="Unix Time",
        detailed_description="Show Unix Time",
        knobs=[],
        exemplar="[Unix Time]",
        update_cadence=1,
        identifier="koh-sh.iterm2-statusbar-scripts.unixtime"
    )

    @iterm2.StatusBarRPC
    async def showunixtime(knobs):
        return "UnixTime: " + str(int(time.time()))

    await component.async_register(connection, showunixtime)

iterm2.run_forever(main)
