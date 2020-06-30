import abc

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
        :return: (str) string in specified format
        """
    @abc.abstractmethod
    def read_from(self, file):
        """
        Required method for reading a file to be turned into a dictionary that pBook can read
        :param file: pass an open file
        :return: (list) python dictionary in phoneBook format
        """