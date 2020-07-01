from phonebook_actions import PhoneBookActions
import argparse

parser = argparse.ArgumentParser(description='Phonebook commandline by Michael Mason')
parser.add_argument('-f','--file', type=str, metavar='', required=True, help='save to this file')
# parser.add_argument('-n', )
args = parser.parse_args()

def main():
    pb = PhoneBookActions(args.file)
    pb.add_record("Michael Mason", "109 Hawken Drive", "+61 400 702 089")
    pb.add_record("Gaby Mason", "109 Hawken Drive", "+61 400 702 089")
    pb.add_record("David Mason", "109 Hawken Drive", "+61 400 702 089")
    pb.add_record("Jeremy Mason", "109 Hawken Drive", "+61 400 702 089")
    pb.add_record("James Dalziel", "231 Wayland Terrace", "+38 102 039 209")


if __name__ == "__main__":
    main()
