#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2014 Ritashugisha
# MIT License. <http://opensource.org/licenses/MIT>

"""
elements

.. module:: elements
    :platform: Linux, MacOSX, Windows
    :synopsis: 
    :created:  2015-04-05 03:12:24
    :modified: ritashugisha
.. moduleauthor:: Ritashugisha (ritashugisha@gmail.com)

"""

import inspect
from html import HTML


class DashboardStat:

    def __init__(
        self, text, description,
        color='blue-hoki', icon='asterisk', link=None, link_text=None
    ):
        [
            setattr(self, k, v) for (k, v,) in \
                    inspect.getargvalues(inspect.currentframe())[-1].items() 
                if k.lower() != 'self'
        ]

        self.e = HTML(escape=True).div(klass='dashboard-stat {}'.format(self.color))
        e_visual = self.e.div(klass='visual')
        e_visual.i(klass='fa fa-{}'.format(self.icon))
        e_details = self.e.div(klass='details')
        e_details.div(self.text, klass='number')
        e_details.div(self.description, klass='desc')
        if self.link:
            e_link = self.e.a(
                (self.link_text if self.link_text else 'View'),
                klass='more', href=self.link
            )
            e_link.i(klass='m-icon-swapright m-icon-white')

    def __str__(self):
        return self.e._stringify(str)

    def __unicode__(self):
        return self.e._stringify(unicode)
