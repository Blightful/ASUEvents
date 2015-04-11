#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2014 Ritashugisha
# MIT License. <http://opensource.org/licenses/MIT>

"""
DashboardStat

.. module:: DashboardStat
    :platform: Linux, MacOSX, Windows
    :synopsis: 
    :created:  2015-04-11 14:55:50
    :modified: ritashugisha
.. moduleauthor:: Ritashugisha (ritashugisha@gmail.com)

"""

import inspect
import yattag


class DashboardStat:

    def __init__(
        self, text, description,
        color='blue-hoki', icon='asterisk', link=None, linktext=None
    ):
        [
            setattr(self, k, (str(v) if v else None)) for (k, v,) in \
                    inspect.getargvalues(inspect.currentframe())[-1].items() 
                if k.lower() != 'self'
        ]
        self.document = yattag.Doc()
        with self.document.tag(
            'div', klass='dashboard-stat {}'.format(self.color)
        ):
            with self.document.tag('div', klass='visual'):
                with self.document.tag('i', klass='fa fa-{}'.format(self.icon)):
                    pass
            with self.document.tag('div', klass='details'):
                with self.document.tag('div', klass='number'):
                    self.document.text(self.text)
                with self.document.tag('div', klass='desc'):
                    self.document.text(self.description)
            if self.link:
                with self.document.tag('a', klass='more', href=self.link):
                    self.document.text(
                        self.linktext if self.linktext else 'View'
                    )
                    with self.document.tag(
                        'i', klass='m-icon-swapright m-icon-white'
                    ):
                        pass

    def __repr__(self):
        return self.document.getvalue()
                    