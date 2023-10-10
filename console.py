#!/usr/bin/python3
"""HBNB Console Implementation"""

import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """HBNBCommand class """

    prompt = '(hbnb) '
    __classes = {
        "BaseModel": BaseModel,
    }

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

        args = arg.split()
        if args[0] not in HBNBCommand.__classes.keys():
            return print("** class doesn't exist **")

        if len(args) == 1:
            return print("** instance id missing **")

        key = args[0] + "." + args[1]
        if key not in storage.all():
            return print("** no instance found **")

        print(storage.all()[key])

    def do_destory(self, arg):
        """
        Usage: destory <class> <id>
        Deletes an instance based on the class name and id
        """
        if len(arg) == 0:
            return print("** class name missing **")

        args = arg.split()
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
        if (len(arg) == 0):
            return print([str(x) for x in storage.all().values()])

        args = arg.split()
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

        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
