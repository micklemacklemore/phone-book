.. phone-book documentation master file, created by
   sphinx-quickstart on Fri Jul  3 09:35:13 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.
   sphinx-apidoc -o docs phonebook/ -f -M -E


phone-book documentation
========================

A simple Python module that's designed to take a set of personal data and store it in various formats. It has a command-line tool that can be run from the root of this directory

Requires: Python 2.7

Currently supports serialisation in:

- JSON
- CSV

System to support additional file formats is easily extendable.
check: :meth:`phonebook.supported_filetypes` for more information.

Project Brief
-------------

We will discuss:
""""""""""""""""

- thing
- other thing
- this thing

.. include:: modules.rst

indices and tables
------------------
* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
