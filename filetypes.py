from filetypes_abstract import PhoneBookABC
import json
import csv


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
        data = json.load(file)
        return data  # return data as dictionary


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
