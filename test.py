#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2014 Ritashugisha
# MIT License. <http://opensource.org/licenses/MIT>

"""
test

.. module:: test
    :platform: Linux, MacOSX, Windows
    :synopsis: 
    :created:  03-22-2015
    :modified: ritashugisha
.. moduleauthor:: Ritashugisha (ritashugisha@gmail.com)

"""

import os
import rproj

db = rproj.DB(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'db'))
for i in db.tables.values():
    print i
    for j in i.t_deffinition:
        print '\t{}'.format(j)
    print

