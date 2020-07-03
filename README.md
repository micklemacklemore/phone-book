# phone-book

##### API Documentation / Journal can be found in [documentation](./Documentation.lnk)

A simple Python module that's designed to take a set of personal data and store it in various formats.
It has a command-line tool that can be run from the root of this directory

##### Requires: Python 2.7
##### Currently supports serialisation in:

- JSON
- CSV

System to support additonal file formats is easily extendable.

  
## Usage
### Help
    $ python phonebook -h
Note that you can query a list of the supported file types through the help command 
    
### Add record (Name, Address, Phone Number)
    $ python phonebook pbook.json -a "Michael Mason" "109 Gregory Drive" "+61400702089"

### Remove record
Delete record using it's number ID

    $ python phonebook pbook.json -rm 1

### List records
    $ python phonebook pbook.json -ls

### Filter records
    $ python phonebook pbook.json -f name=*Mason
    $ python phonebook pbook.json -f address="??? Gregory Drive"
    $ python phonebook pbook.json -f number=+[1-6]1400*

### Publish records
Takes existing records and formats them into a fancy-lookin', human readable and filterable HTML table

    $ python phonebook pbook.json -p

### Convert records
    $ python phonebook pbook.json -c pbook.csv

### Query supported file types
    $ python phonebook pbook.json -q
    