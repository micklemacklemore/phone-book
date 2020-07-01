from phonebook_actions import PhoneBookActions
import argparse

# TODO: write a commandline args parser

parser = argparse.ArgumentParser(description='Phonebook commandline by Michael Mason')
parser.add_argument('-f','--file', type=str, metavar='', required=True, help='save to this file')
# parser.add_argument('-n', )
args = parser.parse_args()

def parse_args():
    pb = PhoneBookActions(args.file)
