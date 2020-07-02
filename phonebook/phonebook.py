import supported_filetypes.filetypes
from phonebook_actions import PhoneBookActions
import argparse

def help_description():
    description = "phone book command-line by Michael Mason.\n\n" \
                  "supported file types:"
    filetypes = [i for i in supported_filetypes.filetypes.query_filetypes()]
    for filetype in filetypes:
        description += "\n{}".format(filetype)

    return description


def parse_args():
    parser = argparse.ArgumentParser(description=help_description(), formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument("file", help="specify the name of the phonebook file e.g. pbook.json")
    args = parser.parse_args()
    print args.echo
    # parser.add_argument('-f', '--file', type=str, metavar='', required=True, help='save to this file')
    # pb = PhoneBookActions(args.file)
