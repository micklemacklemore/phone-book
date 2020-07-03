"""
    filetypes_abstract.py
    ---------------------
    This module contains the abstract class which all subclasses from :meth:`phonebook.supported_filetypes.filetypes`
    When adding support for additional storage formats, you must inherit from this class and use it as a template.
"""

import abc

class PhoneBookABC(object):

    __metaclass__ = abc.ABCMeta

    @abc.abstractproperty
    def filetype(self):
        """ *string* Returns file extension of phonebook format e.g. 'json'
        """

    @abc.abstractmethod
    def write_to(self, file_output, phone_book):
        """
        Method for writing the phonebook dictionary to the specified filetype format

        **file_output** takes a file object to write to

        **phone_book** (dict) phone book

        **returns:** (str) string in specified format
        """
    @abc.abstractmethod
    def read_from(self, file_input):
        """
        Method that takes a file object to read from and creates a dictionary that
        PhoneBookActions can accept

        **file_input** takes a file object to read from

        **return:** (list) python dictionary in phoneBook format
        """