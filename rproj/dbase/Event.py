#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2014 Ritashugisha
# MIT License. <http://opensource.org/licenses/MIT>

"""
Event

.. module:: Event
    :platform: Linux, MacOSX, Windows
    :synopsis: 
    :created:  03-22-2015
    :modified: ritashugisha
.. moduleauthor:: Ritashugisha (ritashugisha@gmail.com)

"""

from __future__ import unicode_literals
import Database
from Room import Room
from Manager import Manager


class Event(Database.ITable, Database.TableRepresentation):
    """ EVENT table, defines a table of events.

    """

    def __init__(self, dbcon):
        """ Initialize EVENT table.

            :param dbcon: sqlite database connection
            :type dbcon: ``sqlite.Connection``

        """
        super(Event, self).__init__(dbcon)

    @property
    def t_deffinition(self):
        """ Define the EVENT table's attributes.
            
            :returns: List of table attributes
            :rtype: ``list``

        """
        return [
            Database.TableAttribute('eventID', 'integer', pk=True),
            Database.TableAttribute('name', 'text'),
            Database.TableAttribute('timestart', 'real'),
            Database.TableAttribute('timeend', 'real'),
            Database.TableAttribute('datestart', 'real'),
            Database.TableAttribute('dateend', 'real'),
            Database.TableAttribute('yearly', 'integer'),
            Database.TableAttribute('monthly', 'integer'),
            Database.TableAttribute('weekly', 'integer'),
            Database.TableAttribute('daily', 'integer'),
            Database.TableAttribute('roomID', 'text', fk=Room),
            Database.TableAttribute('managerID', 'integer', fk=Manager),
        ]

