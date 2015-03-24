#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2014 Ritashugisha
# MIT License. <http://opensource.org/licenses/MIT>

"""
Building

.. module:: Building
    :platform: Linux, MacOSX, Windows
    :synopsis: 
    :created:  03-22-2015
    :modified: ritashugisha
.. moduleauthor:: Ritashugisha (ritashugisha@gmail.com)

"""

from __future__ import unicode_literals
import Database


class Building(Database.ITable):

    def __init__(self, dbcon):
        super(Building, self).__init__(dbcon)

    def __repr__(self):
        return '{}({})'.format(
            self.__class__.__name__,
            ', '.join([i.name for i in self.t_deffinition])
        )

    @property
    def t_deffinition(self):
        return [
            Database.TableAttribute('buildingID', 'integer', pk=True),
            Database.TableAttribute('name', 'text'),
            Database.TableAttribute('roomcount', 'integer'),
            Database.TableAttribute('floorcount', 'integer')
        ]

