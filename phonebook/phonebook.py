import supported_filetypes.filetypes
from phonebook_actions import PhoneBookActions

import argparse
import os

def help_description():
    description = "phone book command-line by Michael Mason.\n\n" \
                  "supported file types:"
    filetypes = [i for i in supported_filetypes.filetypes.query_filetypes()]
    for filetype in filetypes:
        description += "\n{}".format(filetype)

    return description


def parse_args():
    parser = argparse.ArgumentParser(description=help_description(), formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument("file", help="specify the name of the phonebook file e.g. \"pbook.json\"")

    group = parser.add_mutually_exclusive_group()
    group.add_argument("-ls", "--list", help="list records", action='store_true')
    group.add_argument("-a", "--add", nargs=3, help="add record containing name, address and phone number",
                        metavar=('NAME', 'ADDRESS', 'PHONE'))
    group.add_argument("-rm", "--remove", help="remove record by number ID", metavar="ID_NUMBER")
    group.add_argument("-f", "--filter", help="filter records by unix-style wildcards. e.g. \"name=Joe*\"",
                       metavar="<TYPE>=<WILDCARD>")
    group.add_argument('-c', "--convert", help="convert phonebook to another supported format. e.g. \"pbook.csv\"",
                       metavar="FILE")
    group.add_argument("-p", "--publish", help="save phonebook as fancy HTML table", action='store_true')



    # group.add_argument("--publish")
    args = parser.parse_args()

    pb = PhoneBookActions(args.file)
    if not pb.database:
        if not os.path.exists(pb.file):
            print "saving new file: {}".format(args.file)
            pb.store_records()

    if args.add:
        print "record added: {}".format(args.add)
