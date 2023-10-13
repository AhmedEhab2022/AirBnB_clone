# AirBnB Clone - Console

## Description

This is the first step towards building our first full web application: the AirBnB clone. This first step is very important because we will use what we build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration...

Each task is linked and will help us to:

- put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of our future instances
- create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
- create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
- create the first abstracted storage engine of the project: File storage.
- create all unittests to validate all our classes and storage engine

## Usage

### Interactive Mode

To run the console in interactive mode, run the following command:

```
$ ./console.py
```

### Non-Interactive Mode

To run the console in non-interactive mode, echo the command into the console:

```
$ echo "help" | ./console.py
```

### Commands

| Command | Description                                                                        | Usage                                                      |
| ------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------- |
| help    | Displays the documented commands                                                   | `help`                                                     |
| quit    | Exits the program                                                                  | `quit`                                                     |
| EOF     | Exits the program                                                                  | `EOF`                                                      |
| create  | Creates a new instance of a class                                                  | `create <class>`                                           |
| show    | Prints the string representation of an instance based on the class name and id     | `show <class> <id>`                                        |
| destory | Deletes an instance based on the class name and id                                 | `destroy <class> <id>`                                     |
| update  | Updates an instance based on the class name and id by adding or updating attribute | `update <class> <id> <attribute name> "<attribute value>"` |
| all     | Prints all string representation of all instances based or not on the class name   | `all` or `all <class>`                                     |

## Examples

### Interactive Mode

```
$ ./console.py
(hbnb) create BaseModel
d0e7e7e3-9f5a-4a3a-8d9d-1c1a7f8b8c1e
(hbnb) show BaseModel d0e7e7e3-9f5a-4a3a-8d9d-1c1a7f8b8c1e
[BaseModel] (d0e7e7e3-9f5a-4a3a-8d9d-1c1a7f8b8c1e) {'id': 'd0e7e7e3-9f5a-4a3a-8d9d-1c1a7f8b8c1e', 'created_at': datetime.datetime(2020, 7, 1, 0, 0), 'updated_at': datetime.datetime(2020, 7, 1, 0, 0)}
(hbnb) destroy BaseModel d0e7e7e3-9f5a-4a3a-8d9d-1c1a7f8b8c1e
(hbnb) show BaseModel d0e7e7e3-9f5a-4a3a-8d9d-1c1a7f8b8c1e
** no instance found **
(hbnb) quit
$
```

### Non-Interactive Mode

```
$ echo "create BaseModel" | ./console.py
d0e7e7e3-9f5a-4a3a-8d9d-1c1a7f8b8c1e
$ echo "show BaseModel d0e7e7e3-9f5a-4a3a-8d9d-1c1a7f8b8c1e" | ./console.py
[BaseModel] (d0e7e7e3-9f5a-4a3a-8d9d-1c1a7f8b8c1e) {'id': 'd0e7e7e3-9f5a-4a3a-8d9d-1c1a7f8b8c1e', 'created_at': datetime.datetime(2020, 7, 1, 0, 0), 'updated_at': datetime.datetime(2020, 7, 1, 0, 0)}
$ echo "destroy BaseModel d0e7e7e3-9f5a-4a3a-8d9d-1c1a7f8b8c1e" | ./console.py
$ echo "show BaseModel d0e7e7e3-9f5a-4a3a-8d9d-1c1a7f8b8c1e" | ./console.py
** no instance found **
$
```

## Authors

- [Mohammed Shousha](https://github.com/Mohammed-Shousha)
- [Ahmed Ehab](https://github.com/AhmedEhab2022)
