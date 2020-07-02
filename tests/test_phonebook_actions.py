import unittest
import os

import phonebook.phonebook_actions as phonebook_actions
import phonebook.supported_filetypes.filetypes


#  I wouldn't call this 'reasonable unit testing', but I at least made sure to test for the part
#  of the program which was most likely to be extended, which was the adding of supported formats.
class TestPhoneBookActions(unittest.TestCase):

    def setUp(self):
        self.pb_types = {}
        filetypes = [i for i in phonebook.supported_filetypes.filetypes.query_filetypes()]

        for filetype in filetypes:
            self.pb_types[filetype] = phonebook_actions.PhoneBookActions("pbook.{}".format(filetype))

    def tearDown(self):

        for i in self.pb_types:
            if os.path.exists(self.pb_types[i].file):
                os.remove(self.pb_types[i].file)

    def test_add_remove_record(self):
        for i in self.pb_types:
            self.pb_types[i].add_record("Michael Mason", "109 Hawken Drive", "+61 400 702 089")
            self.pb_types[i].add_record("Gaby Mason", "234 asdd Drive", "+61234232433")
            self.pb_types[i].add_record("Big Guy", "34 Hawkasdfen Drive", "+61 234233423")
            self.pb_types[i].add_record("Famiu Darkson", "3432 Arts Drive", "4444444444444")
            self.pb_types[i].add_record("David Mason", "10349 Hawken Drive", "234234234234")
            self.pb_types[i].add_record("Ding Dong", "109 Hawken Drive", "2342322222")
            self.pb_types[i].add_record("Michael Jackson", "109 Hawken Drive", "93874787873")
            self.pb_types[i].add_record("Fallout New Ve", "109 Hawken Drive", "(03)0049300234")
            self.pb_types[i].add_record("Randal Stevens", "109 Hawken Drive", "61 499 383 8423")

            self.assertDictEqual(self.pb_types[i].database["1"], {"name": "Michael Mason", "address": "109 Hawken Drive", "phone": "+61400702089"})

        for i in self.pb_types:
            for id in range(1, 9):
                self.pb_types[i].remove_record("1")

            # Test that the last record in the database is now the first record after deleting 9 records
            self.assertEqual(self.pb_types[i].database,
                             {'1': {'address': '109 Hawken Drive', 'name': 'Randal Stevens', 'phone': '614993838423'}})

    def test_filter_records(self):
        for i in self.pb_types:
            self.pb_types[i].add_record("Michael Mason", "109 Hawken drive", "3435343243")
            self.pb_types[i].add_record("Grant Powell", "55 Downing Street, St Lucia", "+61 300 402 012")
            self.pb_types[i].add_record("Jerry Cai", "109 Hawken drive", "+61 300 402 012")
            self.pb_types[i].add_record("Michael Marston", "109 Hawken drive", "+61 300 402 012")
            self.pb_types[i].add_record("Gaby Mason", "109 Hawken drive", "+61 300 402 012")
            self.pb_types[i].add_record("David Mason", "109 Hawken drive", "+61 300 402 012")
            self.pb_types[i].add_record("James Dalziel", "109 Hawken drive", "+61 300 402 012")
            filtered = self.pb_types[i].filter_records("*Mason", filter_entry="name")
            self.assertDictEqual(filtered, {'1': dict(phone='3435343243', name='Michael Mason',
                                                      address='109 Hawken drive'),
                                            '5': dict(phone='+61300402012', name='Gaby Mason',
                                                      address='109 Hawken drive'),
                                            '6': dict(phone='+61300402012', name='David Mason',
                                                      address='109 Hawken drive')})


if __name__ == "__main__":
    unittest.main()
