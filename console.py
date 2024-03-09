#!/usr/bin/python3
"""Contains code for a command line user interface"""

import cmd
from models.base_model import BaseModel
from models.engines.file_storage import FileStorage
from models.__init__ import storage

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb)'

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """Nothing id done when enter is pressed"""
        pass

    def do_EOF(self, line):
        """Quit command to exit the program"""
        return True

    def do_create(self, line):
        """Creates a new instance of BaseModel, saves it to the JSON file and prints the id"""
        if not line.strip():
            print("** class name is missing **")
        elif line.strip() != "BaseModel":
            print("** class doesn't exist **")
        else:
            new = BaseModel()
            new.save()
            print(new.id)

    def do_show(self, line):
        """Prints the string representation of an instance based on the class name and id"""
        args = line.split()
        if not args:
            print("** class name missing **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif args[0] != "BaseModel":
            print("** class doesn't exist **")
        else:
            key = "{}.{}".format(args[0], args[1])
            try:
                print(storage.all()[key])
            except:
                print("** no instance found **")

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id and saves the change into the JSON file"""
        args = line.split(" ")
        if not line.strip():
            print("** class name missing **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif args[0] != "BaseModel":
            print("** class doesn't exist **")
        else:
            key = "{}.{}".format(args[0], args[1])
            try:
                del storage.all()[key]
                storage.save()
            except:
                print("** no instance found **")

    def do_all(self, line):
        """Prints all string representation of all instance based or not on the class name"""
        args = line.split(" ")
        all_objs = storage.all()
        if not line.strip():
            for key, value in all_objs.items():
                print(all_objs[key])
        elif args[0] == "BaseModel":
            for key, value in all_objs.items():
                if "BaseModel" in key:
                    print(all_objs[key])
        else:
            print("** class doesn't exist **")

    def do_update(self, line):
        """Updates and instance based on the class name and id by adding or updating attributes and saving them to the JSON file"""
        args = line.split(" ")
        if not line.strip():
            print("** class name missing **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif args[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            object_inst = storage.all()[key]
            new = BaseModel(**object_inst)
            try:
                setattr(new, args[2], args[3])
                del object_inst
                storage.new(new)
                storage.save()
            except KeyError:
                print("** no instance found **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
