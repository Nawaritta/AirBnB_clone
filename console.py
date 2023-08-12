#!/usr/bin/python3
"""Entry point of the command interperter"""
import cmd
from re import compile
import re
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage



def tokenize(line, _pattern=compile(r'("[^"]*"|\s*\S+\s*)')):
    """Splits the arguments of a command and handles the double quote case
    handles the <class name>.command() case.
    """

    dot = False
    if "." in line:
        dot = True
        line = line.replace(".", " ", 1).replace(",", " ")
        line = line.replace("(", " ", 1).replace(")", " ", 1)
        line = line.replace("{", " ", 1).replace("}", " ", 1)
        line = line.replace("'", " ")

    tokenized_list = list(map(lambda s: s.strip('" '), _pattern.findall(line)))

    if dot and len(tokenized_list) >= 2:
        tokenized_list[0], tokenized_list[1] = tokenized_list[1], tokenized_list[0]

    return tokenized_list


class HBNBCommand(cmd.Cmd):
    """Class contains the command interperter logic"""

    prompt = '(hbnb) '
    __classes = {
        cls.__name__: cls
        for cls in (BaseModel, User, State, City, Amenity, Place, Review)
    }

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF (Ctrl+d) to exit the program"""
        return True

    def emptyline(self):
        """Do nothing on empty line + <Enter>"""
        pass

    def do_create(self, arg):
        """Creates and saves a new instance"""
        args = tokenize(arg)
        if len(args) == 0:
            print('** class name missing **')
            return
        class_name = args[0]
        if class_name not in self.__classes:
            print('** class doesn\'t exist **')
            return
        instance = self.__classes[class_name]()
        instance.save()
        print(instance.id)

    def do_show(self, arg):
        """Shows the string representation of an instance"""
        args = tokenize(arg)
        if len(args) == 0:
            print('** class name missing **')
            return
        class_name = args[0]
        if class_name not in self.__classes:
            print('** class doesn\'t exist **')
            return
        if len(args) == 1:
            print('** instance id missing **')
            return
        key = f'{class_name}.{args[1]}'
        if key not in storage.all():
            print('** no instance found **')
            return
        print(storage.all()[key])

    def do_destroy(self, arg):
        """Deletes an instance"""
        args = tokenize(arg)
        if len(args) == 0:
            print('** class name missing **')
            return
        class_name = args[0]
        if class_name not in self.__classes:
            print('** class doesn\'t exist **')
            return
        if len(args) == 1:
            print('** instance id missing **')
            return
        key = f'{class_name}.{args[1]}'
        if key not in storage.all():
            print('** no instance found **')
            return
        del storage.all()[key]
        storage.save()

    def do_all(self, arg):
        """Shows all the created instances based or not on class name"""
        args = tokenize(arg)
        if len(args) >= 1:
            class_name = args[0]
            if class_name not in self.__classes:
                print('** class doesn\'t exist **')
                return
            instances = [
                str(value)
                for key, value in storage.all().items()
                if key.startswith(class_name)
            ]
            print(instances)
        else:
            instances = list(map(str, storage.all().values()))
            print(instances)

    def do_update(self, arg):
        """Updates an attribute of an instance using its class and id"""
        args = tokenize(arg)
        if len(args) == 0:
            print('** class name missing **')
            return
        class_name = args[0]
        if class_name not in self.__classes:
            print('** class doesn\'t exist **')
            return
        if len(args) == 1:
            print('** instance id missing **')
            return
        key = f'{class_name}.{args[1]}'
        if key not in storage.all():
            print('** no instance found **')
            return
        instance = storage.all()[key]
        if len(args) == 2:
            print('** attribute name missing **')
            return
        attr_name = args[2]
        if len(args) == 3:
            print('** value missing **')
            return
        class_type = type(getattr(instance, attr_name, ''))
        attr_value = class_type(args[3])
        setattr(instance, attr_name, attr_value)
        instance.save()

    def do_count(self, arg):
        """
        Retrieves the number of instances of a class.
        Usage: <class name>.count()
        """
        args = tokenize(arg)
        if len(args) >= 1:
            class_name = args[0]
            if class_name not in self.__classes:
                print('** class doesn\'t exist **')
                return
            count = 0
            for key in storage.all().keys():
                if key.startswith(class_name + "."):
                    count += 1
        print(count)

    def default(self, line):
        """
        Check for <class>.<cmd>(<args>) syntax and execute corresponding
        method to execute instance
        """
        args = tokenize(line)
        cmd_list = { 'all': self.do_all, 'create': self.do_create,
                     'show': self.do_show, 'destroy': self.do_destroy,
                     'update': self.do_update, 'count':self.do_count
        }
        if args[0] in cmd_list:
            cmd_func = cmd_list[args[0]]
            cmd_func(' '.join(args[1:]))
        else:
            print("*** Unknown syntax:", line)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
