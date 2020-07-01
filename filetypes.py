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
        field_names = []
        lines = []

        # Get the field names for first row (all dict entries)
        for order_id in phone_book:
            field_names = [record for record in phone_book[order_id]]
            field_names.insert(0, 'ID')
            break
        # Get print line by line
        for order_id in phone_book:
            line = [phone_book[order_id][record] for record in phone_book[order_id]]
            line.insert(0, int(order_id))
            lines.append(line)
        lines = sorted(lines)
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
