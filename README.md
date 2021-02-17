# AirBnB Clone - The Console

![hbnb logo](./hbnb_logo.png)
___

## Description of the project

This is the first part toward building a full web application of an AirBnB clone.  The console is a tool to validate the storage engine of 

![diagram of the console and file_storage engine](./console_diagram.png)

## Table of contents :scroll:
* [Environment](#environment)
* [Installation](#installation)
* [Using the console](#using-the-console)
* [File Descriptions](#file-descriptions)
* [Examples](#examples)
* [Authors](#authors)

___

## Environment
This project was created, interpreted, and tested on Ubuntu 14.04 LTS using python3 (version 3.4.3).
Code conforms to PEP 8 style (version 1.7.0).

## Installation and how to use it.
* Clone this repo.

## Using the console
* Running the console in interactive mode:
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
(hbnb)
(hbnb) quit
$
```

* Running the console/shell in non-interactive mode:
```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$

```
---

## File descriptions
[console.py](./console.py) - the console is the entry point of the command interpreter.
[models](./models)
[amenity.py](./models/amenity.py)
[base_model.py](./models/base_model.py)
[city.py](./models/city.py)
[engine](./engine)
[file_storage.py](./models/engine/file_storage.py)
__init__.py
place.py
review.py
state.py
user.py
README.md
tests
__init__.py
test_console.py
test_models
test_amenity.py
test_base_model.py
test_city.py
test_place.py
test_review.py
test_state.py
test_user.py
[AUTHORS](./AUTHORS)


## Examples
* [objectObject]

## Authors :black_nib:
* **Amilcar Armmand** - [AmilcarArmmand](https://github.com/AmilcarArmmand)
* **Maxwell Lovell** - [Johnbogey](https://github.com/JohnBogey)
* **Matthew Feliciano** - [Mfeliciano778](https://github.com/Mfeliciano778)

