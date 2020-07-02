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

    # arguments are mutually exclusive. I'd like to be able to use sub-commands like git.
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-ls", "--list", help="list records", action='store_true')
    group.add_argument("-a", "--add", nargs="*", help="add record containing name, address and phone number")
    group.add_argument("-rm", "--remove", help="remove record by number ID", metavar="ID_NUMBER")
    group.add_argument("-f", "--filter", help="filter records by unix-style wildcards. e.g. \"name=Joe*\"",
                       metavar="<TYPE>=<WILDCARD>")
    group.add_argument('-c', "--convert", help="convert phonebook to another supported format. e.g. \"pbook.csv\"",
                       metavar="FILE")
    group.add_argument("-p", "--publish", help="save phonebook as fancy HTML table", action='store_true')

    args = parser.parse_args()

    pb = PhoneBookActions(args.file)
    if not pb.database:
        if not os.path.exists(pb.file):
            print "saving new file: {}".format(args.file)
            pb.store_records()

    if args.list:
        pass

    if args.add:
        if len(args.add) != 3:
            if len(args.add) < 3:
                print "phonebook: error: Too few values. Please enter name, address and then phone number"
                return
            elif len(args.add) > 3:
                print "phonebook: error: Too many values. Please enter name, address and then phone number"
                return
        id, result = pb.add_record(name=args.add[0], address=args.add[1], phone=args.add[2])
        print "added:", id, ":",  result

    elif args.add is not None:
        name = raw_input("name : ")
        address = raw_input("address : ")
        phone = raw_input("phone number : ")

        id, result = pb.add_record(name, address, phone)
        print "added:", id, ":", result

    if args.remove:
        removed = pb.remove_record(args.remove)
        if removed:
            print "record removed: {}".format(removed)

    if args.filter:
        pass

    if args.convert:
        try:
            pb.convert_records(args.convert)
        except ValueError:
            print "phonebook: error: {} is not a supported file format".format(args.convert.rsplit('.')[-1])

    if args.publish:
        pass

