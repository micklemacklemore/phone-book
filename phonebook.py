"""Module that does a thing

27/06/2020
michaelmason@live.com.au
"""
import sys, inspect
import filetypes
import os

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
            'Name' : "Joe Balushi",
            'Address' : "987 Corona Street, MichaelTown",
            'Number' : "0400702089"
        },
}

class PhoneBookCommands(object):
    def __init__(self, file=None):
        self._database = {}
        self._format = file.rsplit('.')[1]
        self._file = file

        self._object = filetypes.PhoneBookJSON()

        if os.path.exists(self._file):
            self._database = self.retrieve_records()

    def add_record(self, name=None, address=None, phone=None):
        record = {"Name" : str(name), "Address" : str(address), "Phone" : str(phone)}
        order_id = 1
        if self._database:
            order_id_list = []
            for i in self._database:
                order_id_list.append(int(i))
            order_id = 1 + max(order_id_list)
        self._database[str(order_id)] = record
        self.store_records()

    def remove_record(self, order_id):
        if self._database:
            if order_id in self._database:
                del self._database[order_id]
                database = self._database.copy()
                for counter, order_id in enumerate(database, start=1):
                    self._database[str(counter)] = self._database.pop(order_id)
            else:
                return
        self.store_records()

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

pb = PhoneBookCommands(file="pbook.json")
# pb.add_record("Mike", "109 Hawken Drive", "+61 400 702 089")
pb.remove_record(order_id="1")

# Query supported formats
# clsmembers = inspect.getmembers(sys.modules['filetypes'], inspect.isclass)
# print clsmembers
# print clsmembers[2][1]().filetype
