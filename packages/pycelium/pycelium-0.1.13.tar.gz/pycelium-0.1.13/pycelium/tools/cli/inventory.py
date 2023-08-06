import re
import token
import getpass
import yaml

import asyncio

import click

from .main import main, CONTEXT_SETTINGS
from .config import (
    config,
    banner,
    RESET,
    BLUE,
    PINK,
    YELLOW,
    GREEN,
)

from ..sequencers import Sequencer, expand_network
from .. import parse_uri, soft, expandpath
from ..containers import gather_values, deindent_by
from ..mixer import save_yaml
from ..persistence import find_files

from pycelium.definitions import IP_INFO
from pycelium.shell import Reactor, DefaultExecutor
from pycelium.scanner import HostInventory


INVENTORY_ROOT = 'inventory/'


@main.group(context_settings=CONTEXT_SETTINGS)
@click.pass_obj
def inventory(env):
    # banner("User", env.__dict__)
    pass


def explore_host(ctx):
    reactor = Reactor(env=ctx)
    conn = DefaultExecutor(retry=-1, **ctx)
    reactor.attach(conn)

    stm = HostInventory(daemon=False)
    # stm = Pastor(daemon=False)
    reactor.attach(stm)

    # magic ...
    asyncio.run(reactor.main())

    return reactor.ctx


def get_mac(data):
    specs = {
        '.*enp.*mac.*': None,
        '.*enp.*type.*': 'ether',
        '.*wlo.*mac.*': None,
        '.*wlo.*type.*': 'ether',
    }
    blueprint = gather_values(data, **specs)

    # blueprint = deindent_by(blueprint, IP_INFO)
    if 'mac' in blueprint:
        if blueprint.get('type') in ('ether',):
            return blueprint.get('mac')

    keys = list(blueprint)
    keys.sort()
    for iface in keys:
        info = blueprint.get(iface)
        if info.get('type') in ('ether',):
            return info.get('mac')


def get_host_tags(data):
    """Try to figure out which kind of node is"""
    return ['node', 'venoen']


@inventory.command()
# @click.argument('filename', default='sample.gan')
@click.option("--network", multiple=True)
@click.option("--user", multiple=True)
@click.pass_obj
def explore(env, network, user):
    """
    - [ ] get users from config yaml file or command line
    """
    config.callback()
    # analyze_args(env, uri, include, output)
    if not user:
        user = [getpass.getuser()]

    ctx = dict(env.__dict__)

    top = expandpath(INVENTORY_ROOT)
    print(f"network: {network}")
    for pattern in network:
        seq = expand_network(pattern)
        print(f"Exploring: {pattern}  --> {seq.total} items")
        for addr in seq:
            addr = '.'.join(addr)
            for cred in user:
                uri = f'{cred}@{addr}'
                ctx['uri'] = uri

                ctx = parse_uri(uri, **env.__dict__)
                soft(ctx, user=getpass.getuser(), host='localhost')

                print(f"addr: {addr}   {seq.progress:.1%}")
                data = explore_host(ctx)
                mac = get_mac(data)
                if mac:
                    mac = mac.replace(':', '')
                    hostname = data.get('observed_hostname') or ctx.get(
                        'host'
                    )
                    data = data.get('real')
                    tags = get_host_tags(data)
                    tags = '/'.join(tags)
                    path = f"{top}/{tags}/{hostname}.{mac}.yaml"
                    print(f"saved: {path}")

                    save_yaml(data, path)
                    break  # don't try another user in the same computer

            foo = 1


@inventory.command()
# @click.argument('filename', default='sample.gan')
@click.option("--email", default=None)
@click.option("--cost", default=30)
@click.pass_obj
def show(env, email, cost=0):
    config.callback()
    top = expandpath(INVENTORY_ROOT) + '/'
    found = find_files(top, includes=['.*yaml'])
    lines = {k.split(top)[-1]: v for k, v in found.items()}

    banner("Inventory", lines=lines)
    foo = 1


@inventory.command()
# @click.argument('filename', default='sample.gan')
@click.option("--email", default=None)
@click.option("--cost", default=30)
@click.pass_obj
def install(env, email, cost=0):
    config.callback()
    top = expandpath(INVENTORY_ROOT) + '/'
    found = find_files(top, includes=['.*yaml'])
    lines = {k.split(top)[-1]: v for k, v in found.items()}

    banner("Inventory", lines=lines)
    foo = 1


@inventory.command()
# @click.argument('filename', default='sample.gan')
@click.option("--email", default=None)
@click.option("--cost", default=30)
@click.pass_obj
def query(env, email, cost=0):
    raise NotImplementedError("not yet!")
