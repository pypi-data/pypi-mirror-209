# -*- coding: utf-8 -*-
# Copyright © 2023 Wacom. All rights reserved.

USER_AGENT_STR: str = "Personal Knowledge Library/0.3.0 " \
                      "(+https://github.com/Wacom-Developer/personal-knowledge-library)"

__all__ = ['base', 'graph', 'ontology', 'tenant', 'users', 'USER_AGENT_STR']

from knowledge.services import base
from knowledge.services import graph
from knowledge.services import ontology
from knowledge.services import tenant
from knowledge.services import users
