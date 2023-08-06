# This file is placed in the Public Domain.
# pylint: disable=C,I,R

"""write your own commands


The ``opr`` package provides an Object class, that mimics a dict while using
attribute access and provides a save/load to/from json files on disk.
Objects can be searched with database functions and uses read-only files
to improve persistence and a type in filename for reconstruction. Methods
are factored out into functions to have a clean namespace to read JSON data
into.

basic usage is this::

 >>> from opr import Object
 >>> o = Object()
 >>> o.key = "value"
 >>> o.key
 >>> 'value'

Objects try to mimic a dictionary while trying to be an object with normal
attribute access as well. hidden methods are provided, the methods are
factored out into functions like get, items, keys, register, set, update
and values.

read/write from/to disk::

 >>> from opr import Object, read, write
 >>> o = Object()
 >>> o.key = "value"
 >>> p = write(o)
 >>> obj = Object()
 >>> read(obj, p)
 >>> obj.key
 >>> 'value'

great for giving objects peristence by having their state stored in files::

 >>> from opr import Object, write
 >>> o = Object()
 >>> write(o)
 opr.objects.Object/89efa5fd7ad9497b96fdcb5f01477320/2022-11-21/17:20:12.22

"""


__author__ = "B.H.J. Thate <thatebhj@gmail.com>"
__version__ = 330


from opr import classes, clients, default, objects, persist, threads


from opr.classes import Classes
from opr.clients import Client
from opr.default import Default
from opr.objects import Object, edit, items, keys, kind, prt, search, update
from opr.objects import values
from opr.persist import Persist, find, last, read, write
from opr.threads import launch


def __dir__():
    return (
            "Classes",
            "Client",
            "Default",
            "Object",
            "Persist",
            'edit',
            'find',
            'items',
            'keys',
            'kind',
            'last',
            "launch",
            'prt',
            'read',
            'search',
            'update',
            'values',
            'write'
           )


__all__ = __dir__()
