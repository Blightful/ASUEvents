#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2014 Ritashugisha
# MIT License. <http://opensource.org/licenses/MIT>

"""
Room

.. module:: Room
    :platform: Linux, MacOSX, Windows
    :synopsis: 
    :created:  03-22-2015
    :modified: ritashugisha
.. moduleauthor:: Ritashugisha (ritashugisha@gmail.com)

"""

from __future__ import unicode_literals
import Database
from Building import Building


class Room(Database.ITable):

    def __init__(self, dbcon):
        super(Room, self).__init__(dbcon)

    def __repr__(self):
        return '{}({})'.format(
            self.__class__.__name__,
            ', '.join([i.name for i in self.t_deffinition])
        )

    @property
    def t_deffinition(self):
        return [
            Database.TableAttribute('roomID', 'text', unique=True, pk=True),
            Database.TableAttribute('name', 'text'),
            Database.TableAttribute('capacity', 'integer', default='0'),
            Database.TableAttribute('type', 'text', null=True),
            Database.TableAttribute('permissions', 'integer', default='0777'),
            Database.TableAttribute('buildingID', 'integer', fk=Building)
        ]


