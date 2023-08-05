#!/usr/bin/env python

"""Tests for `pycelium` package."""

import pytest

from click.testing import CliRunner

from pycelium import pycelium
from pycelium import cli

from pycelium.shell import STM, Reactor, DefaultExecutor
from pycelium.scanner import Pastor


def test_init_instances():
    reactor = Reactor()
    conn = DefaultExecutor()
    reactor.attach(conn)

    stm = Pastor()
    reactor.attach(stm)

    # run(reactor.main())
    # reactor.save()

    # kk = yaml.load(open('reactor.yaml', 'rt'), Loader=yaml.Loader)
    # foo = 1
