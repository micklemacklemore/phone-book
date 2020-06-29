import abc
import json
import csv

_phone_book = {
    '1':
        {
            'Name' : "Michael Mason",
            'Address' : "109 Hawken Drive",
            'Number' : "0738702959"
        },
    '2':
        {
            'Name' : "Jim Barton",
            'Address' : "653 Highland Terrace, St Lucia",
            'Number' : "0400702089"
        },
    '3':
        {
            'Name' : "Jim Barton",
            'Address' : "987 Corona Street, MichaelTown",
            'Number' : "0400702089"
        },
}

class PhoneBookABC(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def write_to(self, phone_book):
        """
        Required method for writing the phonebook dictionary to a specified format
        :param phone_book: (dict) phone book
        :return: (str) phonebook to be saved in specified format
        """
    def read_from(self, file):
        """
        Required method for reading a file to be turned into a dictionary that pBook can read
        :param file: pass an open file
        :return: (list) python dictionary in phoneBook format
        """

class PhoneBookJSON(PhoneBookABC):
    def write_to(self, phone_book):
        json_string = json.dumps(phone_book, indent=2)  # convert json object to string with nice indentations
        return json_string

    def read_from(self, file):
        data = json.loads(file)  # create python dictionary from string
        return data

class PhoneBookCSV(PhoneBookABC):
    def write_to(self, phone_book):
        pass

    def read_from(self, file_input):
        pass


## DEBUG
string = PhoneBookJSON().write_to(_phone_book)  # string
print string
thing = PhoneBookJSON().read_from(string)

for i in thing:
    print i, thing[i]