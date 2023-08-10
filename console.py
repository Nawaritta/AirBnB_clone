#!/usr/bin/python3
"""Entry point of the command interperter"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


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

    def do_create(self, arg):
        """Creates and saves a new instance"""
        args = arg.split()
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
        pass

    def do_destroy(self, arg):
        pass

    def do_all(self, arg):
        pass

    def do_update(self, arg):
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
