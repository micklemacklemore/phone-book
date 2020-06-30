import abc
import json
import csv


# todo: put this abstract class into it's own file
class PhoneBookABC(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractproperty
    def filetype(self):
        """
        :return: File extension of phonebook format
        """

    @abc.abstractmethod
    def write_to(self, phone_book):
        """
        Required method for writing the phonebook dictionary to a specified format
        :param phone_book: (dict) phone book
        :return: what is to be saved
        """
    @abc.abstractmethod
    def read_from(self, file):
        """
        Required method for reading a file to be turned into a dictionary that pBook can read
        :param file: pass an open file
        :return: (list) python dictionary in phoneBook format
        """

class PhoneBookJSON(PhoneBookABC):
    def __init__(self):
        self._filetype = 'json'

    @property
    def filetype(self):
        return self._filetype

    def write_to(self, phone_book):  # get dict
        json_string = json.dumps(phone_book, indent=2)
        return json_string  # return string

    def read_from(self, file):  # get file object
        json.load(file)

class PhoneBookCSV(PhoneBookABC):
    def __init__(self):
        self._filetype = 'csv'

    @property
    def filetype(self):
        return self._filetype

    def write_to(self, phone_book):
        pass

    def read_from(self, file_input):
        pass
