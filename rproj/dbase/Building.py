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


class Building(Database.ITable, Database.TableRepresentation):
    """ BUILDING table, defines a table of rooms.

    """

    def __init__(self, dbcon):
        """ Initialize BUILDING table.

            :param dbcon: sqlite database connection
            :type dbcon: ``sqlite.Connection``

        """
        super(Building, self).__init__(dbcon)

    @property
    def t_deffinition(self):
        """ Define the BUILDING table's attributes.
            
            :returns: List of table attributes
            :rtype: ``list``

        """
        return [
            Database.TableAttribute('buildingID', 'integer', pk=True),
            Database.TableAttribute('name', 'text'),
            Database.TableAttribute('roomcount', 'integer'),
            Database.TableAttribute('floorcount', 'integer')
        ]

