#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2014 Ritashugisha
# MIT License. <http://opensource.org/licenses/MIT>

"""
globals

.. module:: globals
    :platform: Linux, MacOSX, Windows
    :synopsis: 
    :created:  03-22-2015
    :modified: ritashugisha
.. moduleauthor:: Ritashugisha (ritashugisha@gmail.com)

"""

import os

INFO = {
    'name': 'ASUEvents',
    'authors': [
        'Stephen Bunn (ritashugisha)',
        'Austin Mann',
        'Walt Scarborro',
        'Chun Zheng'
    ],
    'contact': 'ritashugisha@gmail.com',
    'version': {
        'major': 1,
        'minor': 0,
        'revision': 'alpha'
    }
}

# System directory containing this module
DIRECTORY = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

DEFFINITIONS = os.path.join(DIRECTORY, 'deffinitions')
if not os.path.exists(DEFFINITIONS):
    os.makedirs(DEFFINITIONS, 0775)

LOGTOPATH = '{}.log'.format(os.path.join(DIRECTORY, INFO['name']))
# Allow logging to $LOGPATH.log
LOGTOFILE = True
