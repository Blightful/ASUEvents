#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2014 Ritashugisha
# MIT License. <http://opensource.org/licenses/MIT>

"""
DB

.. module:: DB
    :platform: Linux, MacOSX, Windows
    :synopsis: 
    :created:  03-22-2015
    :modified: ritashugisha
.. moduleauthor:: Ritashugisha (ritashugisha@gmail.com)

"""

import os
import sqlite3
import itertools
from Room import Room
from Event import Event
from Manager import Manager
from Building import Building
from Peripheral import Peripheral
from ..defaults import Logged


class DB(Logged):

    def __init__(self, path):
        self.path = os.path.realpath(path)
        if not os.path.exists(os.path.dirname(self.path)):
            os.makedirs(os.path.dirname(self.path), 0775)
        self.connection = sqlite3.connect(self.path)
        self.cursor = self.connection.cursor()
        self.tables = {
            'room': Room(self.connection),
            'event': Event(self.connection),
            'manager': Manager(self.connection),
            'building': Building(self.connection),
            'peripheral': Peripheral(self.connection),
        }
        # [
        #     i.drop() for i in self.tables.values() \
        #             if len(i.t_deffinition) != len(i.deffinition)
        # ]
        [
            i.create() for i in self.tables.values() \
                    if not self.table_exists(i.name)
        ]

    def table_exists(self, name):
        return self.cursor.execute(
            "SELECT name FROM sqlite_master WHERE type='table' AND name=?;",
            (name,)
        ).fetchone() != None
