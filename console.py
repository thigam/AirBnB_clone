#!/usr/bin/python3
"""Contains code for a command line user interface"""

import cmd
from models.base_model import BaseModel
from models.engines.file_storage import FileStorage

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
        args = line.split(" ")
        if not line.strip():
            print("** class name missing **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif args[0] != "BaseModel":
            print("** class doesn't exist **")
        else:
            try:
                print(FileStorage.__objects[args[0], args[1]])
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
            try:
                del FileStorage.__objects[args[0], args[1]]
            except:
                print("** no instance found **")

    def do_all(self, line):
        """Prints all string representation of all instance based or not on the class name"""
        args = line.split(" ")
        if not line.strip():
            for key, value in FileStorage.__objects:
                print(FileStorage.__objects[key])
        elif args[0] == "BaseModel":
            for key, value in FileStorage.__objects:
                if "BaseModel" in key:
                    print(FileStorage.__objects[key])
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
            try:
                FileStorage.__objects[args[0], args[1]].args[2] = args[3]
            except:
                print("** no instance found **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
