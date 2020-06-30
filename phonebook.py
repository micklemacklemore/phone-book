"""Module that does a thing

27/06/2020
michaelmason@live.com.au
"""
import sys, inspect
import filetypes
import os

class PhoneBookCommands(object):
    def __init__(self, file=None):
        self._database = {}
        self._format = file.rsplit('.')[1]
        self._file = file

        if self._format in [i[0] for i in self.query_filetypes()]:
            print True
        self._object = filetypes.PhoneBookJSON()  # TODO: determine object to use based on the file extension

        if os.path.exists(self._file):
            self._database = self.retrieve_records()

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
        with open(self._file) as file:
            database = self._object.read_from(file)
        return database

    def store_records(self):
        string = self._object.write_to(self._database)
        with open(self._file, 'w') as file:
            file.writelines(string)

    def display_records(self):
        pass

    def convert_records(self):
        pass

    def search_records(self):
        pass

    def query_filetypes(self):
        clsmembers = inspect.getmembers(sys.modules['filetypes'], inspect.isclass)
        classes = [(i[1]().filetype, i[1]) for i in clsmembers]  # TODO: This would be easier to read as a dictionary
        return classes

pb = PhoneBookCommands(file="pbook.json")
# pb.add_record("1", "asdf", "ASDFasdf")
# pb.add_record("2", "asdf", "ASDFasdf")
# pb.add_record("3", "asdf", "ASDFasdf")
# pb.add_record("4", "asdf", "ASDFasdf")
# pb.add_record("5", "asdf", "ASDFasdf")
# pb.add_record("6", "asdf", "ASDFasdf")
# pb.remove_record(order_id="1")

# Query supported formats
print pb.query_filetypes()
