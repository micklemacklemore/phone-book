"""Module that does a thing

27/06/2020
michaelmason@live.com.au
"""
import os
import fnmatch

import supported_filetypes.filetypes
import html_template


class PhoneBookActions(object):  # TODO: figure out which methods of this class are used internally and refactor them

    def __init__(self, input_file):

        self._file = input_file
        self._format = self._format = input_file.rsplit('.')[-1]
        # determine filetype.class to use based on the file extension
        self._reader_writer = self._create_reader_writer(self._format)
        self._database = None

        if os.path.exists(self._file):
            self._database = self.retrieve_records()

    @property
    def file(self):
        return self._file

    @property
    def database(self):
        return self._database

    def query_filetypes(self):
        return [i for i in supported_filetypes.filetypes.query_filetypes()]

    # May have been better to create a record class instead of a dictionary, for extendability
    def add_record(self, name=None, address=None, phone=None):
        record = {"name": str(name),
                  "address": str(address),
                  "phone": str(phone).replace(" ", "")}
        order_id = 1  # order of records starts at 1
        if self._database:
            order_id_list = []
            for i in self._database:
                order_id_list.append(int(i))
            order_id += max(order_id_list)
        else:
            self._database = {}
        self._database[str(order_id)] = record
        self.store_records()
        return order_id, self._database[str(order_id)]

    def remove_record(self, order_id):
        if self._database:
            if order_id not in self._database:
                return
            removed = self._database.copy()[order_id]
            del self._database[order_id]
            database = self._database.copy()
            order_id_list = sorted([int(i) for i in database])
            for i in order_id_list:
                index = order_id_list.index(i) + 1
                self._database[str(index)] = self._database.pop(str(i))
            self.store_records()
            return removed
        else:
            return

    def retrieve_records(self):
        with open(self._file, 'rb') as file:
            database = self._reader_writer.read_from(file)
        return database

    def store_records(self):
        with open(self._file, 'wb') as f:
            self._reader_writer.write_to(f, self._database)

    # TODO: I want to be able to take the _database dictionary and create a HTML formatted table with it
    def publish_records(self):
        if not self._database:
            return
        database = self._database.copy()
        field_names = []
        lines = []
        html_output = self._file.rsplit('.', 1)[0] + '_published.html'  # html published file will save where ever the phonebook is
        html = ""
        html_table = "<table id=\"myTable\">\n" \
                     "<tr class=\"header\">\n"
        # Get field names
        for order_id in database:
            field_names = [record.capitalize() for record in database[order_id]]
            # field_names.insert(0, 'ID')
            break
        # Get every record as a list
        for order_id in database:
            line = [database[order_id][record] for record in database[order_id]]
            # line.insert(0, int(order_id))
            lines.append(line)
        lines = sorted(lines)

        for field in field_names:
            html_table += "<th style=\"width:20%;\">{}</th>\n".format(str(field))
        html_table += "</tr>\n"
        for line in lines:
            html_table += "<tr>\n"
            for entry in line:
                html_table += "<td>{}</td>\n".format(str(entry))
            html_table += "<tr>\n"
        html_table += "</table>\n\n"

        html += html_template.template_top
        html += html_table
        html += html_template.template_bottom

        with open(html_output, 'wb') as f:
            f.write(html)
        return html_output

    def list_records(self, database=None):
        if not database:
            if not self._database:
                return
            database = self._database.copy()

        field_names = []
        lines = []
        for order_id in database:
            field_names = [record for record in database[order_id]]
            field_names.insert(0, 'ID')
            break
        # Get every record as a list
        for order_id in database:
            line = [database[order_id][record] for record in database[order_id]]
            line.insert(0, int(order_id))
            lines.append(line)
        lines = sorted(lines)

        # TODO: format these strings based on maximum possible length of a string
        string = "\n{:<8} {:<15} {:<30} {:<30}".format(*field_names)
        for i in lines:
            string += ("\n{:<8} {:<15} {:<30} {:<30}".format(*i))
        return string

    def convert_records(self, output_file):
        if not self._database:
            return
        format = output_file.rsplit('.')[-1]
        reader_writer = self._create_reader_writer(format)
        with open(output_file, 'wb') as f:
            reader_writer.write_to(f, self._database)

    def filter_records(self, filter_string, filter_entry=None):
        if not self._database:
            return
        filtered_database = {}
        database = self._database.copy()

        if not filter_entry:
            for record in database:
                for record_type in database[record]:
                    to_match = database[record][record_type]
                    is_matched = fnmatch.fnmatch(to_match, filter_string)
                    if is_matched:
                        filtered_database[record] = database[record]
        else:
            for record in database:
                if filter_entry not in database[record]:
                    return
                to_match = database[record][filter_entry]
                is_matched = fnmatch.fnmatch(to_match, filter_string)
                if is_matched:
                    filtered_database[record] = database[record]

        return filtered_database

    def _create_reader_writer(self, format):
        filetypes = supported_filetypes.filetypes.query_filetypes()
        if format in filetypes:
            return filetypes[format]()
        else:
            raise ValueError("file extension '{}' is not supported".format(format))

if __name__ == "__main__":
    pb = PhoneBookActions("../pbook.json")
    pb.publish_records()