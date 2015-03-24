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
    :modified: bunnsc
.. moduleauthor:: Ritashugisha (ritashugisha@gmail.com)

"""

import os


DIRECTORY = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
DEFFINITIONS = os.path.join(DIRECTORY, 'deffinitions')
if not os.path.exists(DEFFINITIONS):
    os.makedirs(DEFFINITIONS, 0775)
