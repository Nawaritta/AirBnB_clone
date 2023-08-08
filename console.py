#!/usr/bin/python3
"""Entry point of the command interperter"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Class contains the command interperter logic"""

    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF (Ctrl+d) to exit the program"""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
