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
- Initialize -> DFL(data, tag_format, create_tag_function)
  1. data: 


#### encode_dfl function

#### decode_dfl function

#### write_dfl_in _file function

#### read_dfl_in_file function


## Developed
- [x] \_\_init__.py
- [x] DFL.py
  - [x] DFL class
  - [x] encode_dfl function
  - [x] decode_dfl function
- [x] file.py
  - [x] write_dfl_in_file function
  - [x] read_dfl_in_file function

