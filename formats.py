import abc


class PhoneBookABC(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def write_to(self, phone_book):
        """
        Required method for writing the phonebook dictionary to a string in a specified format
        :param phone_book: (list) phone book
        :return: (str) phonebook to be saved in specified format
        """
    def read_from(self, file_input):
        """
        Required method for reading a file to be turned into a dictionary that pBook can read
        :param file_input: (str) directory of file to be read
        :return: (list) python dictionary in phoneBook format
        """

class PhoneBookJSON(PhoneBookABC):
    def __init__(self):
        pass

    def write_to(self, phone_book):
        pass

    def read_from(self, file_input):
        pass

class PhoneBookCSV(PhoneBookABC):
    def write_to(self, phone_book):
        pass

    def read_from(self, file_input):
        pass
