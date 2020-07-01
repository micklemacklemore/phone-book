"""Module that does a thing

27/06/2020
michaelmason@live.com.au
"""
import sys, inspect
import filetypes
import os

class PhoneBookCommands(object):
    def __init__(self, file=None):
        self._file = file
        self._format = file.rsplit('.')[-1]
        self._object = self._create_filetypes_object()  # determine filetype.class to use based on the file extension
        self._database = {}

        if os.path.exists(self._file):
            self._database = self.retrieve_records()

    # TODO: would be better to pass record as object rather than create a dictionary
    def add_record(self, name=None, address=None, phone=None):
        record = {"Name": str(name), "Address": str(address), "Phone": str(phone)}
        order_id = 1  # order of records starts at 1
        if self._database:
            order_id_list = []
            for i in self._database:
                order_id_list.append(int(i))
            order_id += max(order_id_list)
        self._database[str(order_id)] = record
        self.store_records()

    def remove_record(self, order_id):
        if self._database:
            if order_id in self._database:
                del self._database[order_id]
                database = self._database.copy()
                order_id_list = sorted([int(i) for i in database])

                for i in order_id_list:
                    index = order_id_list.index(i) + 1
                    self._database[str(index)] = self._database.pop(str(i))
                self.store_records()
            else:
                return

    def retrieve_records(self):
        with open(self._file, 'rb') as file:
            database = self._object.read_from(file)
        return database

    def store_records(self):
        with open(self._file, 'wb') as f:
            self._object.write_to(f, self._database)

    def display_records(self):
        pass

    def convert_records(self):
        pass

    def filter_records(self):
        pass

    def change_records(self, order_id):
        pass

    # TODO: There is probably a better way to write this?
    def query_filetypes(self):
        # Get available class names and classes from filetypes module
        clsmembers = inspect.getmembers(sys.modules['filetypes'], inspect.isclass)
        classes = {}
        for i in clsmembers:
            classes[i[1]().filetype] = i[1]  # e.g. {'json' : <PhoneBookJSON() instance>}
        return classes

    def _create_filetypes_object(self):
        if self._format in self.query_filetypes():
            return self.query_filetypes()[self._format]()
        else:
            raise ValueError("file extension '{}' is not supported".format(self._format))

if __name__ == "__main__":
    pb = PhoneBookCommands(file="pbook.csv")
    # pb.add_record("Michael Mason", "109 Hawken Drive", "+61 400 702 089")
    # pb.add_record("Gaby Mason", "109 Hawken Drive", "+61 400 702 089")
    # pb.add_record("David Mason", "109 Hawken Drive", "+61 400 702 089")
    # pb.add_record("Jeremy Mason", "109 Hawken Drive", "+61 400 702 089")
    # pb.add_record("James Dalziel", "231 Wayland Terrace", "+38 102 039 209")
    # pb.remove_record(order_id="1")

