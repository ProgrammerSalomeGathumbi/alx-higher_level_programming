Python - Input/Output  
To open a file in Python, use the built-in open function. For example: f = open("file.txt", "r"). The first argument is the file name and the second argument is the mode in which the file is opened.

To write text to a file, open the file in write mode using f = open("file.txt", "w") and use the write method. For example: f.write("Hello, world!").

To read the full contents of a file, use the read method. For example: text = f.read().

To read a file line by line, use a for loop and the readline method.   
To move the cursor in a file, use the seek method. For example: f.seek(0) moves the cursor to the beginning of the file.

To make sure a file is closed after using it, use the close method. For example: f.close().

The with statement is used as a context manager to automatically close the file after the block of code within the with statement is executed  
JSON (JavaScript Object Notation) is a lightweight data interchange format that is easy for humans to read and write and easy for machines to parse and generate.

Serialization is the process of converting a data structure into a format that can be stored or transmitted over a network, such as JSON or XML.

Deserialization is the reverse process of serialization, converting a format back into a data structure.

To convert a Python data structure to a JSON string, use the json module and the dumps function. For example: import json; json.dumps({"key": "value"}).

To convert a JSON string to a Python data structure, use the json module and the loads function. For example: import json; json.loads('{"key": "value"}').
