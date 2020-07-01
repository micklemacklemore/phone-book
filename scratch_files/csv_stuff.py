import csv

phone_book = {
  "1": {
    "Phone": "+61 400 702 089",
    "Name": "Michael Mason",
    "Address": "109 Hawken Drive"
  },
  "3": {
    "Phone": "+61 400 702 089",
    "Name": "David Mason",
    "Address": "109 Hawken Drive"
  },
  "2": {
    "Phone": "+61 400 702 089",
    "Name": "Gaby Mason",
    "Address": "109 Hawken Drive"
  },
  "5": {
    "Phone": "+38 102 039 209",
    "Name": "James Dalziel",
    "Address": "231 Wayland Terrace"
  },
  "4": {
    "Phone": "+61 400 702 089",
    "Name": "Jeremy Mason",
    "Address": "109 Hawken Drive"
  }
}

def main():
    # print phone_book
    for order_id in phone_book:
        field_names = [record for record in phone_book[order_id]]
        field_names.insert(0, 'ID')
        break
    print field_names


    lines = []
    for order_id in phone_book:
      line = [phone_book[order_id][record] for record in phone_book[order_id]]
      line.insert(0, str(order_id))
      lines.append(line)
    lines = sorted(lines)
    for i in lines:
      print i




if __name__ == "__main__":
    main()