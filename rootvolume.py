#!/usr/bin/env python3

import shutil
import iterm2


async def main(connection):
    component = iterm2.StatusBarComponent(
        short_description="RootVolume Usage",
        detailed_description="Show Root Volume Usage",
        knobs=[],
        exemplar="[RootVolume Usage]",
        update_cadence=30,
        identifier="koh-sh.iterm2-statusbar-scripts.rootvolume"
    )

    @iterm2.StatusBarRPC
    async def showrootvolume(knobs):
        rootusage = shutil.disk_usage('/')
        lst = [round(x / 1024 / 1024 / 1024) for x in rootusage]
        return ("RootVolume: {}/{} GB ({}%)".format(lst[1], lst[0], (round(lst[1] / lst[0] * 100))))

    await component.async_register(connection, showrootvolume)

iterm2.run_forever(main)
