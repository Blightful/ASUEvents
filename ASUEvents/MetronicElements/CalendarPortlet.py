#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2014 Ritashugisha
# MIT License. <http://opensource.org/licenses/MIT>

"""
CalendarPortlet

.. module:: CalendarPortlet
    :platform: Linux, MacOSX, Windows
    :synopsis: 
    :created:  2015-04-11 15:27:32
    :modified: ritashugisha
.. moduleauthor:: Ritashugisha (ritashugisha@gmail.com)

"""

import inspect
import yattag


class CalendarPortlet:

    def __init__(self, text, color='blue-hoki', icon='calendar'):
        [
            setattr(self, k, (str(v) if v else None)) for (k, v,) in \
                    inspect.getargvalues(inspect.currentframe())[-1].items() 
                if k.lower() != 'self'
        ]
        self.document = yattag.Doc()
        with self.document.tag(
            'div', klass='portlet box {} calendar'.format(self.color)
        ):
            with self.document.tag('div', klass='portlet-title'):
                with self.document.tag('div', klass='caption'):
                    with self.document.tag('i', klass='fa fa-{}'.format(self.icon)):
                        pass
                    self.document.text(self.text)
            with self.document.tag('div', klass='portlet-body'):
                with self.document.tag('div', id='calendar'):
                    pass

    def __repr__(self):
        return self.document.getvalue()
