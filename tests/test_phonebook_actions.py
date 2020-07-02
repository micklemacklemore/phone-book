import unittest
import os

import phonebook.phonebook_actions as phonebook_actions
import phonebook.supported_filetypes.filetypes

# I made sure to automatically test for all file types, in case a supported filetype class is added
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
            for id in range(1, 10):
                self.pb_types[i].remove_record("1")
            self.assertEqual(self.pb_types[i].database, {})


if __name__ == "__main__":
    unittest.main()
