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

Addressing The Challenge Brief
------------------------------

   In Python or C++ write a module or small library which shows how you would take a set of personal data, where each record contains:

   - name
   - address
   - phone number

My module takes these records as strings and stores them in a dictionary. As dictionaries
are unordered, each record has an order_id starting from 1, and then incrementing from 1
as more records are added.

(See: :meth:`phonebook.phonebook_actions.PhoneBookActions.add_record`)

   - filter users (e.g "name=Joe*") based on some simple search syntax like Glob.

I used the :meth:`fnmatch` module to do this easily. It accepts **Unix shell-style wildcards.**
See: :meth:`phonebook.phonebook_actions.PhoneBookActions.filter_records`

   - support serialisation in 2 or more formats (e.g JSON, Yaml, XML, CSV etc)
   - Write it in such a way that it would be easy for a developer to extend the system e.g.
      - to add support for additional formats

Phonebook module supports serialisation in **json and csv.**

I used a **strategy design pattern** to make it easy for someone to be able to add the functionality
for additional formats. I used the :meth:`abc` module to create an abstract class to be used as
an interface. Each subclass must define a file extension property, a write method and a read method.

(See: :meth:`phonebook.supported_filetypes`)

   - to query a list of currently supported formats

**List of supported formats** can be queried through the commandline interface through the --help command,
and the list is created based on the available subclasses in :meth:`phonebook.supported_filetypes.filetypes`.

   - Display the data in 2 or more different output formats

The records are able to be displayed through **text output** (--list command) and **html output** (--publish command)

**Text output** simply prints the records neatly to the commandline. See: :meth:`phonebook.phonebook_actions.PhoneBookActions.list_records`

**HTML output** saves a html file, where the records are displayed in a table, which can be filtered.
See: :meth:`phonebook.phonebook_actions.PhoneBookActions.publish_records`

raw:: html

   <embed>
   </embed>


**Note:** You can check my code for commenting on where I had challenges, and where I think I could extend and
improve the module further.

.. include:: modules.rst

indices and tables
------------------
* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
