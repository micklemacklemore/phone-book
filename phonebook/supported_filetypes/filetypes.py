import filetypes_abstract

import sys
import inspect
import json
import csv


# method to query supported file types in this module
def query_filetypes():
    # Get available class names and classes from filetypes module
    cls_members = inspect.getmembers(sys.modules[__name__], inspect.isclass)
    classes = {}
    for i in cls_members:
        classes[i[1]().filetype] = i[1]  # e.g. {'json' : <PhoneBookJSON() instance>}
    return classes


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
        field_names = []
        lines = []

        # Get the field names for first row (all dict entries)
        for order_id in phone_book:
            field_names = [record for record in phone_book[order_id]]
            field_names.insert(0, 'ID')
            break
        # Get every record as a list
        for order_id in phone_book:
            line = [phone_book[order_id][record] for record in phone_book[order_id]]
            line.insert(0, int(order_id))
            lines.append(line)
        lines = sorted(lines)
        # Write to file using csv writer
        csv_writer = csv.writer(file_output)
        csv_writer.writerow(field_names)
        csv_writer.writerows(lines)
        return file_output

    def read_from(self, file_input):
        data = {}
        csv_reader = csv.DictReader(file_input)
        for line in csv_reader:
            data[line['ID']] = line.copy()
            data[line['ID']].pop('ID')
        return data


# class PhoneBookYaml(filetypes_abstract.PhoneBookABC):
#     def __init__(self):
#         self._filetype = 'yaml'
#
#     @property
#     def filetype(self):
#         return self._filetype
#
#     def write_to(self, file_output, phone_book):
#         pass
#
#     def read_from(self, file_input):
#         pass