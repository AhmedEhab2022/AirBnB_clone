#!/usr/bin/python3
"""HBNB Console Implementation"""

import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


def parse(arg):
    from shlex import split
    """Parses command line arguments"""
    args = split(arg)
    return args


class HBNBCommand(cmd.Cmd):
    """HBNBCommand class """

    prompt = '(hbnb) '
    __classes = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
    }

    def default(self, line):
        """
        handel dot commands
        """

        cls_name = ""
        op_name = ""
        for i in range(len(line)):
            if line[i] == '.':
                i += 1
                break
            cls_name += line[i]

        if cls_name == line:
            return print("*** Unknown syntax: {}".format(line))

        while i < len(line):
            if line[i] == '(':
                i += 1
                break
            op_name += line[i]
            i += 1

        inst_id = ""
        while i < len(line):
            if line[i] == ')':
                break
            inst_id += line[i]
            i += 1

        if cls_name not in HBNBCommand.__classes.keys():
            return print("** class doesn't exist **")

        if op_name == "all":
            print([str(v) for v in storage.all().values()
                   if v.__class__.__name__ == cls_name])

        elif op_name == "count":
            cnt = 0
            for v in storage.all().values():
                if v.__class__.__name__ == cls_name:
                    cnt += 1

            print(cnt)

        elif op_name == "show":
            if inst_id == "":
                return print("** instance id missing **")

            key = cls_name + "." + inst_id
            if key not in storage.all():
                return print("** no instance found **")

            print(storage.all()[key])

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print()
        return True

    def emptyline(self):
        """Empty line + ENTER shouldn't execute anything"""
        pass

    def do_create(self, arg):
        """
        Usage: create <class>
        Creates a new instance of a given class
        """
        if len(arg) == 0:
            return print("** class name missing **")

        if arg not in HBNBCommand.__classes.keys():
            return print("** class doesn't exist **")

        new_instance = HBNBCommand.__classes[arg]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """
        Usage: show <class> <id>
        Prints the string representation of an instance
        based on the class name and id
        """
        if len(arg) == 0:
            return print("** class name missing **")

        args = parse(arg)
        if args[0] not in HBNBCommand.__classes.keys():
            return print("** class doesn't exist **")

        if len(args) == 1:
            return print("** instance id missing **")

        key = args[0] + "." + args[1]
        if key not in storage.all():
            return print("** no instance found **")

        print(storage.all()[key])

    def do_destroy(self, arg):
        """
        Usage: destory <class> <id>
        Deletes an instance based on the class name and id
        """
        if len(arg) == 0:
            return print("** class name missing **")

        args = parse(arg)
        if args[0] not in HBNBCommand.__classes.keys():
            return print("** class doesn't exist **")

        if len(args) == 1:
            return print("** instance id missing **")

        key = args[0] + "." + args[1]
        if key not in storage.all():
            return print("** no instance found **")

        del storage.all()[key]
        storage.save()

    def do_all(self, arg):
        """
        Usage: all or all <class>
        Prints all string representation of all
        instances based or not on the class name
        """
        if len(arg) == 0:
            return print([str(x) for x in storage.all().values()])

        args = parse(arg)
        if args[0] not in HBNBCommand.__classes.keys():
            return print("** class doesn't exist **")

        print([str(v) for v in storage.all().values()
               if v.__class__.__name__ == args[0]])

    def do_update(self, arg):
        """
        Usage: update <class> <id> <attribute name> "<attribute value>"
        Updates an instance based on the class name
        and id by adding or updating an attribute
        """

        if len(arg) == 0:
            return print("** class name missing **")

        args = parse(arg)
        for i in range(3):
            args[i] = str(args[i])

        if "num" in args[3] or "number" in args[3]:
            args[3] = int(args[3])
        else:
            args[3] = str(args[3])

        if args[0] not in HBNBCommand.__classes.keys():
            return print("** class doesn't exist **")

        if len(args) == 1:
            return print("** instance id missing **")

        key = args[0] + "." + args[1]
        if key not in storage.all():
            return print("** no instance found **")

        if len(args) == 2:
            return print("** attribute name missing **")

        if len(args) == 3:
            return print("** value missing **")

        storage_objs = storage.all()

        setattr(storage_objs[key], args[2], args[3])
        storage_objs[key].save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
