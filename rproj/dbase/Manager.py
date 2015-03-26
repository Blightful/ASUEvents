#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2014 Ritashugisha
# MIT License. <http://opensource.org/licenses/MIT>

"""
Manager

.. module:: Manager
    :platform: Linux, MacOSX, Windows
    :synopsis: 
    :created:  03-22-2015
    :modified: ritashugisha
.. moduleauthor:: Ritashugisha (ritashugisha@gmail.com)

"""

from __future__ import unicode_literals
import Database


class Manager(Database.ITable, Database.TableRepresentation):
    """ MANAGER table, defines a table of rooms.

    """

    def __init__(self, dbcon):
        """ Initialize MANAGER table.

            :param dbcon: sqlite database connection
            :type dbcon: ``sqlite.Connection``

        """
        super(Manager, self).__init__(dbcon)

    @property
    def t_deffinition(self):
        """ Define the MANAGER table's attributes.
            
            :returns: List of table attributes
            :rtype: ``list``

        """
        return [
            Database.TableAttribute('managerID', 'integer', unique=True, pk=True),
            Database.TableAttribute('namefirst', 'text'),
            Database.TableAttribute('namemiddle', 'text'),
            Database.TableAttribute('namelast', 'text'),
            Database.TableAttribute('email', 'text'),
            Database.TableAttribute('sex', 'text'),
            Database.TableAttribute('permissions', 'integer', default='0777')
        ] 
