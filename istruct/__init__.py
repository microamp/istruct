# -*- coding: utf-8 -*-

__version__ = "0.1.2"

from collections import namedtuple
from uuid import uuid4


def name(prefix="istruct"):
    return "{prefix}_{uuid}".format(prefix=prefix,
                                    uuid=str(uuid4()).replace("-", ""))


def merge_tuples(*tuples):
    return ", ".join(item for t in tuples for item in t)


def merge_dicts(*dicts):
    return {k: v for d in dicts for k, v in d.items()}


def validate(f):
    """Do simple validation checks on positional and keyword arguments.
    """
    def _validate(*args, **kwargs):
        repeated = set(args).intersection(set(kwargs.keys()))
        if repeated:
            raise ValueError("A field must be either required or optional, "
                             "not both: "
                             "%s" % ", ".join("'%s'" % f for f in repeated))
        return f(*args, **kwargs)

    return _validate


@validate
def istruct(*args, **kwargs):
    """Implement an immutable struct on top of `collections.namedtuple`.
    """
    def _istruct(**attrs):
        nt = namedtuple(__name__,
                        merge_tuples(args, tuple(kwargs.keys())))
        return nt(**merge_dicts(kwargs, attrs))

    return _istruct
