#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2014 Ritashugisha
# MIT License. <http://opensource.org/licenses/MIT>

"""
context_processors

.. module:: context_processors
    :platform: Linux, MacOSX, Windows
    :synopsis: 
    :created:  2015-04-11 17:01:23
    :modified: ritashugisha
.. moduleauthor:: Ritashugisha (ritashugisha@gmail.com)

"""

from django.conf import settings


def core(request):
    return {
        'fonts': settings.FONTS_DEFAULT,
        'styles': settings.STYLES_DEFAULT,
        'scripts': settings.PLUGINS_DEFAULT
    }