"""
    filetypes_abstract.py
    ------------
    This module contains the abstract class which all subclasses from :meth:`phonebook.supported_filetypes.filetypes`
    When adding support for additional storage formats, you must inherit from this class and use it as a template.
"""

import abc

class PhoneBookABC(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractproperty
    def filetype(self):
        """
        :return: File extension of phonebook format
        """

    @abc.abstractmethod
    def write_to(self, file_output, phone_book):
        """
        Required method for writing the phonebook dictionary to a specified format
        :param file_output: (file object) file to write to
        :param phone_book: (dict) phone book
        :return: (str) string in specified format
        """
    @abc.abstractmethod
    def read_from(self, file_input):
        """
        Required method for reading a file to be turned into a dictionary that pBook can read
        :param file_input: pass an open file
        :return: (list) python dictionary in phoneBook format
        """