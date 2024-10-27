================
French Pluralize
================

Convert a singular word into plural according french grammar rules.
Plural to singular is available too (but some special cases are probably missing).


Usable as Jinja2 filter.

Licence
-------

BSD license (see LICENCE file)


Features
--------

1. Python code example:

.. code-block:: python

    import pluralizefr
    pluralizefr.pluralize("fromage") # return fromages
    pluralizefr.singularize("fromages") # return fromage


2. Jinja2 exemple:

.. code-block:: jinja2

    {{ 'fromage' | pluralize }}

Installation
------------

https://pypi.org/project/pluralizefr/
