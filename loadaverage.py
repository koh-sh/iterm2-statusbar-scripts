#!/usr/bin/env python3

import os
import iterm2


async def main(connection):
    component = iterm2.StatusBarComponent(
        short_description="Load Average",
        detailed_description="Show Load Average",
        knobs=[],
        exemplar="[Load Average]",
        update_cadence=1,
        identifier="koh-sh.iterm2-statusbar-scripts.loadaverage"
    )

    @iterm2.StatusBarRPC
    async def showloadaverage(knobs):
        la = os.getloadavg()
        return ("LoadAvg: " + " ".join([str(round(x, 2)) for x in la]))

    await component.async_register(connection, showloadaverage)

iterm2.run_forever(main)
