import phonebook_actions


def main():
    pb = phonebook_actions.PhoneBookActions("pbook.json")
    print pb.query_filetypes()
    # filtered = pb.filter_records("*Mason*", filter_entry="Name")
    # print filtered
    pb.add_record("Michael Mason", "109 Hawken drive", "3435343243")
    pb.add_record("Grant Powell", "55 Downing Street, St Lucia", "+61 300 402 012")
    pb.add_record("Jerry Cai", "109 Hawken drive", "+61 300 402 012")
    pb.add_record("Michael Marston", "109 Hawken drive", "+61 300 402 012")
    pb.add_record("Gaby Mason", "109 Hawken drive", "+61 300 402 012")
    pb.add_record("David Mason", "109 Hawken drive", "+61 300 402 012")
    pb.add_record("James Dalziel", "109 Hawken drive", "+61 300 402 012")


if __name__ == "__main__":
    main()