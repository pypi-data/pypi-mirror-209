#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8 et ts=4 sts=4 sw=4
#
# Copyright © 2022 Maxime “pep” Buquet <pep@bouah.net>
#
# Distributed under terms of the GPLv3+ license.

"""
    Slixmpp OMEMO plugin
    Copyright (C) 2022-2099 Maxime “pep” Buquet <pep@bouah.net>
    This file is part of slixmpp-omemo.

    See the file LICENSE for copying permission.
"""

import logging

from omemo import SessionManager

from slixmpp.plugins.base import BasePlugin, register_plugin

class SessionManagerSlix(SessionManager):
    pass

class XEP_0384(BasePlugin):
    """XEP-0384: OMEMO"""

    name = 'xep_0384'
    decription = 'XEP-0384 OMEMO'
    dependencies = {'xep_0004', 'xep_0030', 'xep_0060', 'xep_0163', 'xep_0334'}
