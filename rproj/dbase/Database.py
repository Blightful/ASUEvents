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
import itertools
from ..globals import *
from ..defaults import Logged

try:
    import cPickle as pickle
except ImportError:
    import pickle


class ITable(Logged, object):
    """ Table Interface, used to implement a table object.

    """
    __metaclass__ = abc.ABCMeta

    def __init__(self, dbcon):
        """ Initialize the ITable interface.

        :param dbcon: sqlite database connection
        :type dbcon: sqlite.Connection

        """
        self.connection = dbcon
        self.cursor = dbcon.cursor()
        self.deffinition = self.load_deffinition()

    @property
    def name(self):
        """ Table name property, uppercase class name.
            
            :returns: $CLASS_NAME.upper()
            :rtype: ``str``

        """
        return self.__class__.__name__.upper()

    @property
    def p_deffinition(self):
        """ Table deffinition path property, system path to table deffinition.

            :returns: $globals.DEFFINITIONS/$CLASS_NAME.upper()
            :rtype: ``str``

        """
        return os.path.join(DEFFINITIONS, self.name)

    @abc.abstractproperty
    def t_deffinition(self):
        """ Table deffinition abstract property, list of TableAttribute's to
            be inserted into the table.

            :returns: None
            :rtype: ``None``

        """
        return None

    def t_deffinition_edits(self, table_attrs):
        """ Discover changes to the t_deffinition list.

            :param table_attrs: Secondary list of TableAttributes to compare
            :type table_attrs: list
            :returns: Dictionary of added, removed, and altered TableAttributes
            :rtype: ``dict``

        """
        retn = {'add': [], 'rem': [], 'alter': [], 'mod': False}
        for (i, j,) in itertools.izip_longest(self.t_deffinition, table_attrs):
            if i and j:
                if sorted(i.__dict__.keys()) == sorted(j.__dict__.keys()):
                    if not all([
                        (getattr(i, k) == getattr(j, k)) for k in 
                        sorted(i.__dict__.keys())
                    ]):
                        retn['alter'].append(i)
                        retn['mod'] = True
            else:
                retn['add'].append(i) if i else retn['rem'].append(j)
                retn['mod'] = True
        return retn

    def save_deffinition(self):
        """ Save the table deffinition to $p_deffinition.

        """
        if self.t_deffinition and \
                isinstance(self.t_deffinition, list):
            with open(self.p_deffinition, 'wb') as f:
                pickle.dump(self.t_deffinition, f)
            return self.load_deffinition()
        else:
            self.log.error('property `t_deffinition` must be type list')

    def load_deffinition(self):
        """ Load the table deffinition from $p_deffinition.

        """
        if os.path.exists(self.p_deffinition):
            defread = open(self.p_deffinition, 'rb').read()
            if len(defread) > 0:
                return pickle.loads(defread)
        return self.save_deffinition()

    def drop(self):
        """ Drop the table without any safety protection.

        """
        self.log.warning('dropping `{}` table ...'.format(self.name))
        self.cursor.execute("DROP TABLE {};".format(self.name))
        self.connection.commit()

    def describe(self):
        """ Describe the Sqlite equivalent description of the table.

            :returns: Sqlite table description
            :rtype: ``str``

        """
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
        """ Create the table without any safety protection.

        """
        self.log.info('creating `{}` table ...'.format(self.name))
        self.save_deffinition()
        self.cursor.execute(self.describe())


class TableRepresentation(object):
    """ TableRepresentation superclass, used to add representation to tables.

    """

    def __init__(self):
        """ Initialization placeholder, does nothing.

        """
        pass

    def __repr__(self):
        """ Table representation from $t_deffinition.

            :returns: Representation of calling table
            :rtype: ``str``

        """
        return '{}({})'.format(
            self.__class__.__name__,
            ', '.join([i.name for i in self.t_deffinition])
        )


class TableAttribute(Logged):
    """ TableAttribute class, used to create and represent table attributes.

    """

    def __init__(
        self, name, typ,
        null=False, unique=False, default=None, pk=False, fk=None, check=None
    ):
        """ Initialize the TableAttribute.

            :param name: Name of the attribute
            :type name: ``str`` or ``unicode``
            :param typ: Type of the attribute (eg. 'integer', 'text', ...)
            :type typ: ``str`` or ``unicode``
            :param null: Flag if NULL is allowed in this attribute
            :type null: ``bool``
            :param unique: Flag if attribute is unique
            :type unique: ``bool``
            :param default: Default value if any
            :type default: ``str`` or ``unicode``
            :param pk: Flag if this attribute is a primary key in the table
            :type pk: ``bool``
            :param fk: Table to reference this attribute to if foreign
            :type fk: ``ITable``
            :param check: Check statement if any for the current attribute
            :type check: ``str`` or ``unicode``

        """
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
        """ Attribute representation.
            
            :returns: Attribute's representation
            :rtype: ``str``

        """
        return '{}({})'.format(
            self.__class__.__name__,
            ', '.join([
                '{}={}'.format(k, v) for (k, v,) in self._params
                if k.lower() not in ['k', 'v']
            ])
        )

    @property
    def state(self):
        """ Attribute state property, attribute's create description.

            :returns: Attribute's description for creation
            :rtype: ``str``

        """
        retn = ''.join([
                self.name,
                ' {}'.format(self.typ.upper()),
                (' NOT NULL' if not self.null else ''),
                (' UNIQUE' if self.unique else ''),
                (' DEFAULT {}'.format(str(self.default)) if self.default else ''),
                (' PRIMARY KEY' if self.pk else '')
            ])
        retn = ('{} CHECK ({})'.format(retn, self.check) if self.check else retn)
        return '\t{}'.format(retn)

    def validattrs(self):
        """ Validate that the passed TableAttribute parameters are valid.

            :returns: True if all parameters are valid, otherwise False
            :rtype: ``bool``

        """
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
