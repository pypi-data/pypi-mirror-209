import time
import yaml
import semver

from glom import glom

from .definitions import PIP_FACTS

from .shell import (
    bspec,
    Finder,
)

from .agent import Agent
from .service import Service, AddSudoers, ChangeLocale
from .scanner import Settler
from .modem import ModemConfigurator
from .watch import WatchDog
from .wireguard import WireGuard


class Pastor(Agent):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        self.target = {}

    # --------------------------------------------------
    # Bootstraping
    # --------------------------------------------------
    async def _boot_sentinels(self, *args, **kw):
        """
        Domestic fiber for gathering system info.
        """
        # TODO: load from yaml file
        real = [
            # {
            #'klass': CPUInfoFact,
            #'restart': -1,
            # },
            # {
            #'klass': DeviceInfoFact,
            #'restart': -1,
            # },
            # {
            #'klass': DebListFact,
            #'restart': 30,
            # },
            # {
            #'klass': DiskInfoFact,
            #'restart': 120,
            # },
            # {
            #'klass': IPInfoFact,
            #'restart': 120,
            # },
            # {
            #'klass': PipListFact,
            #'restart': 22,
            #'merge': True,
            # },
            # {
            #'klass': PipListFact,
            #'restart': 22,
            #'outdated': True,
            #'merge': True,
            # },
            {
                'klass': AddSudoers,
            },
            {
                #'klass': ChangeLocale,
            },
            {
                #'klass': Service,
                #'service_name': 'grafana',
                #'restart': 5,
            },
            {
                'klass': Settler,
            },
            {
                'klass': WatchDog,
            },
            {
                'klass': WireGuard,
            },
        ]

        # initial launch
        for action in real:
            self.log.info(f"Launching: {action}")
            if 'klass' in action:
                self.new_action(**action)
                await self.sleep()

        self.log.info(f"All bootstrap ({len(real)}) actions fired.")

        foo = 1

    # --------------------------------------------------
    # Domestic Fibers
    # --------------------------------------------------
    async def hide_fiber_facts(self, *args, **kw):
        # TODO: use an Gathering Action

        while self.running:
            await self.sleep()

            try:
                self.target = yaml.load(
                    open('target.yaml'), Loader=yaml.Loader
                )
                # TODO: review how we update reator context
                self.reactor.ctx['pastor_target'] = self.target
                foo = 1
            except Exception as why:
                self.log.exception(why)
                continue

            self.log.debug("Pastor _fiber_facts!")
            # refresh some actions periodically
            # for key, action in list(self.actions.items()):
            # if action.state != self.ST_STOP:
            # continue

            # fact, kw = key
            # continue

            # if action.restart <= 0:
            # continue

            # died = now - action.t1
            # if died > action.restart:
            # print(f"restart: {fact}:{kw}")
            # self.actions.pop(key)
            # kw = dict(kw)
            # self.new_action(fact, **kw)
            # await self.sleep()

            # compute min lapse for next cycle
            now = time.time() + 5  # wakeup 5 secs earlier
            wakeups = [
                action.t1 + action.restart - now
                for action in self.actions.values()
                if action.restart > 0
            ]
            wakeups.append(60)
            pause = int(max(17, min(wakeups)))
            self.log.debug(
                f"sleeping for {pause} seconds before reload real file"
            )

            await self.sleep(pause)
            foo = 1

    async def hide_fiber_keep_pip(self):
        """
        check differences between target state and current state.

        TODO:

        solve this issue

        ```bash
        pip3 list --outdated
        ...
        pathspec                0.10.3         0.11.1  wheel
        Pillow                  9.0.1          9.5.0   wheel
        pip                     22.0.2         23.0.1  wheel

        # same name allowed, but is a local package !!
        planner                 0.1.0          0.5.1   sdist
        /home/agp/Documents/me/code/planner  <------- same name


        platformdirs            2.6.2          3.2.0   wheel
        protobuf                3.12.4         4.22.1  wheel
        psutil                  5.9.0          5.9.4   wheel
        py                      1.10.0         1.11.0  wheel

        ```

        """

        # TODO: use an Gathering Action
        # ------------------------------------------
        # pip
        # ------------------------------------------
        while self.running:
            await self.sleep()
            current = self.reactor.ctx.get('real', {})
            spec = bspec(PIP_FACTS)
            if not glom(current, spec, default={}):
                continue

            target = glom(self.target, spec, default={})
            for key, dversion in target.items():
                await self.sleep()
                upgrade = False
                info = glom(current, spec[key], default={})
                cversion = info.get('cversion')
                aversion = info.get('aversion') or info.get('cversion')

                if dversion in ('install', None) and cversion:
                    self.log.warning(
                        f"pip: '{key}' already installed with version: '{cversion}', last known version: '{aversion}'. (don't try to upgrade as target version='{dversion}')"
                    )
                    continue

                if dversion == cversion:
                    self.log.warning(
                        f"pip:{key} already installed with exact version"
                    )
                    continue

                if dversion in ('lastest', None) and cversion:
                    # check existing and available version

                    try:
                        aversion = semver.Version.parse(aversion)
                        cversion = semver.Version.parse(cversion)
                    except ValueError as why:
                        continue

                    if aversion > cversion:
                        self.log.warning(
                            f"pip: '{key}' upgrade from '{info['cversion']}' --> '{info['aversion']}'"
                        )
                        upgrade = True
                    else:
                        self.log.warning(
                            f"pip: '{key}'  '{aversion}' == '{cversion}', skipping"
                        )
                        continue
                install = True

                if dversion in ('deinstall',):
                    install = False
                    if key in glom(current, spec):
                        glom(current, spec).pop(key)
                        assert key not in glom(current, spec)
                    else:
                        self.log.info(
                            f"pip: '{key}'  is not installed, skip deleting"
                        )
                        continue

                # install / deinstall `key` package
                self.log.warning(
                    f"updating pip:{key}: install: {install}, upgrade: {upgrade}"
                )

                criteria = {
                    'mro()': '.*PkgInstall.*',
                    'HANDLES': '.*pip.*',
                    #'__name__': 'pepe',
                }
                for factory in Finder.find_objects(**criteria):
                    self.new_action(
                        factory, name=key, install=install, upgrade=upgrade
                    )
                    await self.sleep()
                    break  # just 1st one
                else:
                    self.log.error(
                        f"no factory found that match {criteria} criteria !!"
                    )
                foo = 1
