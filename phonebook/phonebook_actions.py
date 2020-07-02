"""Module that does a thing

27/06/2020
michaelmason@live.com.au
"""
import sys
import inspect
import os
import fnmatch

import supported_filetypes.filetypes


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
        record = {"Name": str(name),
                  "Address": str(address),
                  "Phone": str(phone).replace(" ", "")}
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

    def remove_record(self, order_id):
        if self._database:
            if order_id not in self._database:
                return False
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
            return False

    def retrieve_records(self):
        with open(self._file, 'rb') as file:
            database = self._reader_writer.read_from(file)
        return database

    def store_records(self):
        with open(self._file, 'wb') as f:
            self._reader_writer.write_to(f, self._database)

    # TODO: I want to be able to take the _database dictionary and create a HTML formatted table with it
    def publish_records(self):
        pass

    def list_records(self, database=None):
        if not database:
            database = self._database
        record_list = []
        return record_list

    def convert_records(self, output_file):
        if not self._database:
            return
        format = output_file.rsplit('.')[-1]
        reader_writer = self._create_reader_writer(format)
        with open(output_file, 'wb') as f:
            reader_writer.write_to(f, self._database)

    def filter_records(self, filter, filter_entry=None):
        if not self._database:
            return
        filtered_database = {}
        database = self._database.copy()

        if not filter_entry:
            for record in database:
                for record_type in database[record]:
                    to_match = database[record][record_type]
                    is_matched = fnmatch.fnmatch(to_match, filter)
                    if is_matched:
                        filtered_database[record] = database[record]
        else:
            for record in database:
                if filter_entry not in database[record]:
                    return
                to_match = database[record][filter_entry]
                is_matched = fnmatch.fnmatch(to_match, filter)
                if is_matched:
                    filtered_database[record] = database[record]

        return filtered_database

    def _create_reader_writer(self, format):
        filetypes = supported_filetypes.filetypes.query_filetypes()
        if format in filetypes:
            return filetypes[format]()
        else:
            raise ValueError("file extension '{}' is not supported".format(format))
