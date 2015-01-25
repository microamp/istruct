istruct
=======
immutable struct built on top of ``collections.namedtuple`` with sane defaults

goals
-----
- immutability: cannot be modified once created
- allow optional fields (with default values specified)
- strictly disallow positional arguments

quickstart
----------
First, create an ``istruct`` called ``person`` where ``first_name`` and ``last_name`` are *required* whereas ``middle_name``, ``dob`` and ``email`` are *optional* (with default values specified).

.. code-block:: python

    In [1]: from istruct import istruct

    In [2]: person = istruct("first_name", "last_name", middle_name="", dob="2000-01-01", email=None)

Then, create an instance of ``person`` with ``first_name``, ``last_name`` and ``middle_name``.

.. code-block:: python

    In [3]: p = person(first_name="Jim", last_name="Raynor", middle_name="Eugene")

    In [4]: p
    Out[4]: istruct_a3e45e42fb244834bbcbe701210a2931(first_name='Jim', last_name='Raynor', email=None, dob='2000-01-01', middle_name='Eugene')

``p`` is immutable, meaning it cannot be modified after created. Thus, set operations like below would fail, raising an ``AttributeError``.

.. code-block:: python

    In [5]: p.first_name = "James"
    ---------------------------------------------------------------------------
    AttributeError                            Traceback (most recent call last)
    <ipython-input-13-681faedb279a> in <module>()
    ----> 1 p.first_name = "James"

    AttributeError: can't set attribute

``istruct`` only accepts named/keyword arguments. It strictly disallows positional arguments by design.

.. code-block:: python

    In [6]: p = person("Jim", "Raynor")
    ---------------------------------------------------------------------------
    TypeError                                 Traceback (most recent call last)
    <ipython-input-14-c0bdbd269e9f> in <module>()
    ----> 1 p = person("Jim", "Raynor")

    TypeError: _istruct() takes 0 positional arguments but 2 were given

However, it would complain when one or more _required_ fields are omitted.

.. code-block:: python

    In [7]: p = person(last_name="Raynor")
    ---------------------------------------------------------------------------
    TypeError                                 Traceback (most recent call last)
    <ipython-input-15-451d2add9ee8> in <module>()
    ----> 1 p = person(last_name="Raynor")

    /home/microamp/devel/projs/istruct/istruct.py in _istruct(**attrs)
         25     def _istruct(**attrs):
         26         nt = namedtuple(name(), merge_tuples(args, tuple(kwargs.keys())))
    ---> 27         return nt(**merge_dicts(kwargs, attrs))
         28
         29     return _istruct

    TypeError: __new__() missing 1 required positional argument: 'first_name'

TODO
----
- find ways to annotate types

license
-------
MIT
