import fnmatch
import glob

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

search_type = "Name"

for record in phone_book:
    if search_type == "All":
        for record_type in phone_book[record]:
            to_match =  phone_book[record][record_type]
            print fnmatch.fnmatch(to_match, "*Hawken*")
    if search_type == "Name":
        to_match = phone_book[record]["Name"]
        print fnmatch.fnmatch(to_match, "*Dalziel")