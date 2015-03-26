#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2014 Ritashugisha
# MIT License. <http://opensource.org/licenses/MIT>

"""
Peripheral

.. module:: Peripheral
    :platform: Linux, MacOSX, Windows
    :synopsis: 
    :created:  03-22-2015
    :modified: ritashugisha
.. moduleauthor:: Ritashugisha (ritashugisha@gmail.com)

"""

from __future__ import unicode_literals
import Database
from Room import Room


class Peripheral(Database.ITable, Database.TableRepresentation):
    """ PERIPHERAL table, defines a table of rooms.

    """

    def __init__(self, dbcon):
        """ Initialize PERIPHERAL table.

            :param dbcon: sqlite database connection
            :type dbcon: ``sqlite.Connection``

        """
        super(Peripheral, self).__init__(dbcon)

    @property
    def t_deffinition(self):
        """ Define the PERIPHERAL table's attributes.
            
            :returns: List of table attributes
            :rtype: ``list``

        """
        return [
            Database.TableAttribute('peripheralID', 'text', unique=True, pk=True),
            Database.TableAttribute('name', 'text'),
            Database.TableAttribute('working', 'integer', default='0'),
            Database.TableAttribute('permissions', 'integer', default='0777'),
            Database.TableAttribute('roomId', 'text', fk=Room)
        ]

