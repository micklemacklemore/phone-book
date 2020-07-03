"""
    phonebook_actions.py
    --------------------

    This module contains the PhoneBookActions class the implements the actual commands called by phonebook.py
    and writes the actual file.

    :meth:`phonebook.supported_filetypes.filetypes` module is where the serialization happens. Which uses
    :meth:`phonebook.supported_filetypes.filetypes_abstract` as an interface
"""

import os
import fnmatch

import supported_filetypes.filetypes
import html_template


# Records are created as dictionaries. I'm kicking myself right now because I realised
# it would have been better to create pass them as objects. This way I would have been
# able to easily order them and also they would be easily extendable. Alas, I figure
# I don't have the time to redo that. Serialisation is at least extendable, and I
# prioritised that because it was in the brief.
class PhoneBookActions(object):
    """
    The PhoneBookActions class implements actions related to saving/editing/converting a phone book.
    """

    def __init__(self, input_file):
        """
        Create a new PhoneBookActions object, input a filename as a parameter and
        it will determine where the phonebook will be saved and to what format.

        e.g. "pbook.json" will save to working dir and will save as .json

        If the specified file type is not supported a ValueError is raised during construction.
        You can query filetypes using the :meth:`query_filetypes`
        :param input_file: (string) write to this file if database is edited
        """
        # determine file and file extension if there is one
        self._file = input_file
        self._format = self._format = input_file.rsplit('.')[-1]

        # determine what filetypes.class to use based on the file extension
        self._reader_writer = self._create_reader_writer(self._format)
        self._database = None

        # retrieve existing records
        if os.path.exists(self._file):
            self._database = self.retrieve_records()

    @property
    def file(self):
        """
        :return: value of :attr:`_file`
        """
        return self._file

    @property
    def database(self):
        """A dictionary which contains all phone book records.
        :return: value of :attr:`_database`
        """
        return self._database

    # This probably doesn't belong in this class
    def query_filetypes(self):
        """Convenient method that returns list of supported filetypes for serialization
        :return: a list of supported filetypes from :meth:`phonebook.supported_filetypes.filetypes`
        """
        return [i for i in supported_filetypes.filetypes.query_filetypes()]

    # May have been better to create a record class instead of a dictionary, for extendability, and also for the ability
    # to order the damn entries! Curse you python 2 and your un-ordered dictionary! Hmm well I guess I could have at
    # least used an orderedDict...
    def add_record(self, name=None, address=None, phone=None):
        """

        :param name:
        :param address:
        :param phone:
        :return:
        """
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
