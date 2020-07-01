import filetypes_abstract

import json
import csv


class PhoneBookJSON(filetypes_abstract.PhoneBookABC):
    def __init__(self):
        self._filetype = 'json'

    @property
    def filetype(self):
        return self._filetype

    def write_to(self, file_output, phone_book):  # get dict
        json_string = json.dumps(phone_book, indent=2)
        file_output.writelines(json_string)
        return file_output  # return file object

    def read_from(self, file_input):  # get file object
        data = json.load(file_input)
        return data  # return data as dictionary


class PhoneBookCSV(filetypes_abstract.PhoneBookABC):
    def __init__(self):
        self._filetype = 'csv'

    @property
    def filetype(self):
        return self._filetype

    def write_to(self, file_output, phone_book):
        field_names = [order_id for order_id in phone_book]
        csv_string = None
        return csv_string

    def read_from(self, file_input):
        pass

class PhoneBookXML(filetypes_abstract.PhoneBookABC):
    def __init__(self):
        self._filetype = 'xml'

    @property
    def filetype(self):
        return self._filetype

    def write_to(self, file_output, phone_book):
        pass

    def read_from(self, file_input):
        pass
