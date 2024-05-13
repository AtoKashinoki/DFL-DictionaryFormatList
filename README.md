# DFL-DictionaryFormatList
This module introduces a new data type 'DictionaryFormatList'.


## Overview
By using the DFL type, you can manage multi-dimensional List types into one-dimensional type.

Specifically, we will introduce the following functions.

#### DFL class
DFL (DictionaryFormatList) is a one-dimensional dict type, but data can be extracted in the same way as a normal List type.

#### encode_dfl function
Converts list type data to DFL format data and returns it as DFL format dictionary type data.

#### decode_dfl function
Converts DFL format Dictionary type data and DFL type to List type.

#### write_dfl_in _file function
Describe the List type, DFL type, and DFL format Dictionary type in the File as Text.

#### read_dfl_in_file function
Reads a Text file written in DFL format, gets and returns the DFL type.

## Using

#### DFL class
- class method
  1. create_dfl: Create DFL format data from list.

- instance
  - Initialize 
  -> DFL(data, tag_forma="#{dimension}#{index}", create_tag_function=create_tag)

  - property
    1. data: 
    Return DFL format dictionary data.
    2. tag : 
    Return DFL data tag.
    3. first_tag: 
    Return DFL data first tag.
    4. list: 
    Create and Return list format data from self DFL.
  
  - method
    1. get_list(self): 
    Create and Return list format data from self DFL.
    2. del_values(self, key: str): 
    Delete values.
    3. \_\_getitem__(self, index: int): 
    Get values from self.
    4. \_\_setitem__(self, index: int, value): 
    Set values in self.
    5. \_\_eq__(self, other): 
    Validate self and other.
    6. \_\_iter__(self): 
    Return iterator of list.


#### encode_dfl function
 -> encode_dfl(data: list, tag_format="#{dimension}#{index}#", create_tag_function=create_tag)
 
Encode DFL format dictionary data from list.

#### decode_dfl function
 -> decode_dfl(dfl: dit | DFL, create_tag_function=create_tag)

Create list format DFL format dictionary.

#### write
 -> write(*datas: dict | DFL | list, path: str, encoding: str = "UTF-8")

Write DFL data in file.

#### read
 -> read(path: str, encoding: str = "UTF-8")

Read DFL data in file.


## Developed
- [x] \_\_init__.py
- [x] DFL.py
  - [x] DFL class
  - [x] encode_dfl function
  - [x] decode_dfl function
- [x] file.py
  - [x] write_dfl_in_file function
  - [x] read_dfl_in_file function

