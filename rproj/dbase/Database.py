#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2014 Ritashugisha
# MIT License. <http://opensource.org/licenses/MIT>

"""
Database

.. module:: Database
    :platform: Linux, MacOSX, Windows
    :synopsis: 
    :created:  2015-03-23 16:42:00
    :modified: ritashugisha
.. moduleauthor:: Ritashugisha (ritashugisha@gmail.com)

"""

import os
import sys
import abc
import json
import inspect
import collections
from ..globals import *
from ..defaults import Logged

try:
    import cPickle as pickle
except ImportError:
    import pickle


class ITable(Logged, object):
    __metaclass__ = abc.ABCMeta

    def __init__(self, dbcon):
        self.connection = dbcon
        self.cursor = dbcon.cursor()
        self.deffinition = self.load_deffinition()

    @property
    def name(self):
        return self.__class__.__name__.upper()

    @property
    def p_deffinition(self):
        return os.path.join(DEFFINITIONS, self.name)

    @abc.abstractproperty
    def t_deffinition(self):
        return None

    def save_deffinition(self):
        if self.t_deffinition and \
                isinstance(self.t_deffinition, list):
            with open(self.p_deffinition, 'wb') as f:
                pickle.dump(self.t_deffinition, f)
            return self.load_deffinition()
        else:
            self.log.error('property `t_deffinition` must be type list')

    def load_deffinition(self):
        if os.path.exists(self.p_deffinition):
            defread = open(self.p_deffinition, 'rb').read()
            if len(defread) > 0:
                return pickle.loads(defread)
        return self.save_deffinition()

    def drop(self):
        self.log.warning('dropping `{}` table ...'.format(self.name))
        self.cursor.execute("DROP TABLE {};".format(self.name))
        self.connection.commit()

    def describe(self):
        fks = [i for i in self.deffinition if i.fk != None]
        return "CREATE TABLE {}(\n{}{}\n);".format(
                self.name,
                ',\n'.join([i.state for i in self.deffinition]),
                ',\n\t{}'.format(',\n\t'.join([
                    "FOREIGN KEY ({name}) REFERENCES {table}({name})".format(
                        name=i.name,
                        table=i.fk.__name__.upper()
                    ) for i in fks
                ])) if len(fks) > 0 else ''
            )

    def create(self):
        self.log.info('creating `{}` table ...'.format(self.name))
        self.cursor.execute(self.describe())


class TableAttribute(Logged):

    def __init__(
        self, name, typ,
        null=False, unique=False, default=None, pk=False, fk=None
    ):
        self._params = [
            (k, v,) for (k, v,) in 
            inspect.getargvalues(inspect.currentframe())[-1].items()
            if k.lower() != 'self'
        ]
        [setattr(self, k, v) for (k, v,) in self._params]
        self.valids = {
            'name': (str, unicode,),
            'typ': (str, unicode,),
            'null': (bool,),
            'unique': (bool,),
            'pk': (bool,),
        }
        self.valid_typs = ['text', 'integer', 'real', 'blob', 'null']
        if not self.validattrs():
            sys.exit(1)

    def __repr__(self):
        return '{}({})'.format(
            self.__class__.__name__,
            ', '.join([
                '{}={}'.format(k, v) for (k, v,) in self._params
                if k.lower() not in ['k', 'v']
            ])
        )

    @property
    def state(self):
        retn = ''.join([
                self.name,
                ' {}'.format(self.typ.upper()),
                (' NOT NULL' if not self.null else ''),
                (' UNIQUE' if self.unique else ''),
                (' DEFAULT {} '.format(str(self.default)) if self.default else ''),
                (' PRIMARY KEY' if self.pk else '')
            ])
        return '\t{}'.format(retn)

    def validattrs(self):
        valid = True
        if len(self.name) > 0:
            if len(self.typ) > 0:
                for (k, v,) in self.valids.items():
                    if not type(getattr(self, k)) in v:
                        self.log.error((
                            'invalid passed parameter type `{}`, got '
                            '({}) expected ({})'.format(
                                k,
                                type(getattr(self, k)).__name__,
                                ', '.join([i.__name__ for i in v])
                            )
                        ))
                        valid = False
                if self.typ.lower() not in self.valid_typs:
                    self.log.error((
                        'invalid passed attribute type for `{}`, got '
                        '`{}` expected ({})'.format(
                            self.name,
                            self.typ,
                            ', '.join(self.valid_typs)
                        )
                    ))
                    valid = False
            else:
                self.log.error((
                    'invalid passed attribute type `{}`, '
                    'required length > 0'.format(self.typ)
                ))
                valid = False
        else:
            self.log.error((
                'invalid passed attribute name `{}`, '
                'required length > 0'.format(self.name)
            ))
            valid = False
        return valid
