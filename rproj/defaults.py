#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2014 Ritashugisha
# MIT License. <http://opensource.org/licenses/MIT>

"""
defaults

.. module:: defaults
    :platform: Linux, MacOSX, Windows
    :synopsis: 
    :created:  03-22-2015
    :modified: ritashugisha
.. moduleauthor:: Ritashugisha (ritashugisha@gmail.com)

"""

from __future__ import unicode_literals
import os
import inspect
import logging
import logging.handlers


class Logged(object):

    def __init__(self):
        pass
        
    @property
    def log(self, *args, **kwargs):
        logger = logging.getLogger(self.__class__.__name__)
        if not logger.handlers:
            # if logpath:
            #     if not os.path.exists(os.path.dirname(logpath)):
            #         os.makedirs(os.path.dirname(logpath), 0775)
            #     logfile = logging.handlers.RotatingFileHandler(
            #         logpath,
            #         maxBytes=(1024 * 1024),
            #         backupCount=1
            #     )
            #     logfile.setFormatter(
            #         logging.Formatter(
            #             (
            #                 '%(asctime)s;%(levelname)s;%(pathname)s;%(name)s;'
            #                 '%(funcname)s;%(lineno)s;%(message)s'
            #             ),
            #             datefmt='%y-%m-%d %H:%M:%S'
            #         )
            #     )
            #     logger.addHandler(logfile)
            console = logging.StreamHandler()
            console.setFormatter(
                logging.Formatter(
                    (
                        '[%(asctime)s] [%(levelname)-8s] '
                        '<%(name)s.%(funcName)s:%(lineno)s> %(message)s'
                    ),
                    datefmt='%H:%M:%S'
                )
            )
            logger.addHandler(console)
        logger.propagate = False
        logger.setLevel(logging.DEBUG)
        return logger

