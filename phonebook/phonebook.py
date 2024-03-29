"""
    phonebook.py
    ------------

    This module contains the commandline parsing stuff.
"""

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

# Ideally I would use a gang of four command strategy here, but for the sake of time / scope,
# it was easier just to keep the commandline argument stuff in one file like this. Would be
# too much complication for this little tool anyway.
def parse_args():
    parser = argparse.ArgumentParser(description=help_description(), formatter_class=argparse.RawTextHelpFormatter)

    parser.add_argument("file", help="specify the name of the phonebook file e.g. \"pbook.json\"")

    # sub-arguments
    sub_commands = parser.add_mutually_exclusive_group()
    sub_commands.add_argument("-q", "--query", help="query supported file types", action='store_true')
    sub_commands.add_argument("-ls", "--list", help="list records", action='store_true')
    sub_commands.add_argument("-a", "--add", nargs=3, help="add record containing name, address and phone number",
                       metavar=('NAME', 'ADDRESS', 'PHONE'))
    sub_commands.add_argument("-rm", "--remove", help="remove record by number ID", metavar="ID_NUMBER")
    sub_commands.add_argument("-f", "--filter", help="filter records by unix-style wildcards. e.g. \"name=Joe*\"",
                       metavar="<TYPE>=<EXPRESSION>")
    sub_commands.add_argument('-c', "--convert", help="convert phonebook to another supported format. e.g. \"pbook.csv\"",
                       metavar="FILE")
    sub_commands.add_argument("-p", "--publish", help="save phonebook as fancy HTML table", action='store_true')

    args = parser.parse_args()

    pb = PhoneBookActions(args.file)
    if not pb.database:
        if not os.path.exists(pb.file):
            print "saving new file: {}".format(args.file)
            pb.store_records()

    if args.query:
        query = ""
        for i in pb.query_filetypes():
            query += i + " "
        print query

    if args.list:
        print pb.list_records(pb.database)

    if args.add:
        order_id, result = pb.add_record(name=args.add[0], address=args.add[1], phone=args.add[2])
        print "added:", order_id, ":",  result

    elif args.add is not None:
        name = raw_input("name : ")
        address = raw_input("address : ")
        phone = raw_input("phone number : ")

        order_id, result = pb.add_record(name, address, phone)
        print "added:", order_id, ":", result

    if args.remove:
        removed = pb.remove_record(args.remove)
        if removed:
            print "record removed: {}".format(removed)

    if args.filter:
        if args.filter.count('=') == 1:
            filter_entry, filter_string = args.filter.split('=')
            if filter_entry.lower() == "all":
                filtered_database = pb.filter_records(filter_string)
                if filtered_database:
                    print pb.list_records(filtered_database)
                return
            filtered_database = pb.filter_records(filter_string, filter_entry.lower())
            if filtered_database:
                print pb.list_records(filtered_database)
            return
        elif args.filter.count('=') != 1:
            print "phonebook: error: incorrect use of filter command. use: <entry type>=<search expression>\n"
            print "e.g. phonebook pbook.json --filter name=Michael*"
            return

    if args.convert:
        try:
            pb.convert_records(args.convert)
            print "writing to file: {}".format(args.convert)
        except ValueError:
            print "phonebook: error: {} is not a supported file format".format(args.convert.rsplit('.')[-1])

    if args.publish:
        result = pb.publish_records()
        if result:
            print "saving new file: {}".format(result)

