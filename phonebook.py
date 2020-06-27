"""Module that does a thing

27/06/2020
michaelmason@live.com.au
"""

class PhoneBook():
    def __init__(self, file=None):
        self.records = {}
        if file:
            self.records = self.retrieve_records(file)

    def add_record(self, name, address, phone):
        pass

    def remove_record(self, name=None, address=None, phone=None):
        pass

    def store_records(self):
        pass

    def retrieve_records(self, file):
        records = {}
        return records

    def display(self):
        pass

