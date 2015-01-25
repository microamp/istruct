# -*- coding: utf-8 -*-

from collections import namedtuple
from uuid import uuid4


def name(prefix=__name__):
    return "{prefix}_{uuid}".format(prefix=prefix,
                                    uuid=str(uuid4()).replace("-", ""))


def merge_tuples(*tuples, sep=", "):
    return sep.join(item for t in tuples for item in t)


def merge_dicts(*dicts):
    return {k: v for d in dicts for k, v in d.items()}


def istruct(*args, **kwargs):
    """Implement an immutable struct on top of `collections.namedtuple` with
    saner defaults.
    """

    def _istruct(**attrs):
        nt = namedtuple(name(), merge_tuples(args, tuple(kwargs.keys())))
        return nt(**merge_dicts(kwargs, attrs))

    return _istruct
