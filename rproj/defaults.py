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
from globals import *


class Logged(object):
    """ Logged superclass, allows an object to create and use a logging.Logger.

    """

    def __init__(self):
        """ Initialization placeholder, does nothing.

        """
        pass
        
    @property
    def log(self, *args, **kwargs):
        """ Object log property, creates log for object logging.

            :param *args: List of passed arguments
            :type *args: ``list``
            :param **kwargs: Dictionary of passed arguments
            :type **kwargs: ``dict``
            :returns: Logger instance for the calling object
            :rtype: ``logging.Logger``

        """
        logger = logging.getLogger(self.__class__.__name__)
        if not logger.handlers:
            if LOGTOFILE:
                if not os.path.exists(os.path.dirname(LOGTOPATH)):
                    os.makedirs(os.path.dirname(LOGTOPATH), 0775)
                logfile = logging.handlers.RotatingFileHandler(
                    LOGTOPATH,
                    maxBytes=(1024 * 1024),
                    backupCount=1
                )
                logfile.setFormatter(
                    logging.Formatter(
                        (
                            '%(asctime)s;%(levelname)s;%(pathname)s;%(name)s;'
                            '%(funcName)s;%(lineno)s;%(message)s'
                        ),
                        datefmt='%y-%m-%d %H:%M:%S'
                    )
                )
                logger.addHandler(logfile)
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

