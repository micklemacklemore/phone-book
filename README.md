# phone-book
A simple Python module that's designed to take a set of personal data and store it in various formats

## project brief 
#### In Python or C++ write a module or small library which shows how you would take a set of personal data, where each record contains:

- name
- address
- phone number

#### And:

- build a simple API allowing you to add new records
- filter users (e.g "name=Joe*") based on some simple search syntax like Glob.
- support serialisation in 2 or more formats (e.g JSON, Yaml, XML, CSV etc)
- Display the data in 2 or more different output formats (no need to use a GUI Framework, use e.g text output/HTML or any other human readable format).
- Add a command line interface to add records, and display/convert/filter the whole data set
- Write it in such a way that it would be easy for a developer to extend the system e.g:
  - to add support for additional storage formats
  - to query a list of currently supported formats
