#!/usr/bin/python3
"""
Unittest for all the features of the console
"""

import unittest
from unittest.mock import patch
from console import HBNBCommand
import json
import os
from shutil import copy2
import cmd
from models import storage
from io import StringIO

class TestConsoleCommands(unittest.TestCase):
    """
    Tests console commands
    """

    def setUp(self):
        """
        Redirecting stdin and stdout
        """
        self.mock_stdin = create_autospec(sys.stdin)
        self.mock_stdout = create_autospec(sys.stdout)
        self.err = [
            "** class name missing **",
            "** class doesn't exist **",
            "** instance id missing **",
            "** no instance found **",
        ]
        self.cls = [
            "BaseModel",
            "User",
            "State",
            "City",
            "Place",
            "Amenity",
            "Review"
        ]

    def tearDownClass(cls):
        """
        Teardown after all tests in module.
        """
        storage._FileStorage__objects = cls.__objects_backup
        if os.path.exists(cls.json_file_backup):
            copy2(cls.json_file_backup, cls.json_file)
            os.remove(cls.json_file_backup)

    @classmethod
    def tearDownClass(cls):
        """
        Teardown after all tests in module.
        """
        storage._FileStorage__objects = cls.__objects_backup
        if os.path.exists(cls.json_file_backup):
            copy2(cls.json_file_backup, cls.json_file)
            os.remove(cls.json_file_backup)

    def tearDown(self):
        """
        Any needed cleanup, per test method.
        """
        try:
            del (s1, s2)
        except NameError:
            pass
        storage._FileStorage__objects = dict()
        if os.path.exists(type(self).json_file):
            os.remove(type(self).json_file)

    @patch('builtins.print')
    def test_quit(self, mock_print):
        """
        Test the 'quit' command to ensure the console exits.
        """
        with patch('builtins.input', return_value='quit'):
            cmd = HBNBCommand()
            self.assertTrue(cmd.onecmd('quit'))
            mock_print.assert_called_with("Exiting the console...")

    def test_do_EOF(self):
        """
        Test the 'EOF' command.
        """
        console_instance = HBNBCommand()
        self.assertTrue(console_instance.do_EOF(""))

    def test_do_create(self):
        """
        Test the 'create' command.
        """
        console_instance = HBNBCommand()
        output = console_instance.do_create("User")
        self.assertIsNotNone(output)

    def test_do_show(self):
        """
        Test the 'show' command.
        """
        console_instance = HBNBCommand()
        output = console_instance.do_show("User " + output)
        self.assertIn("User", output)


    def test_do_destroy(self):
        """
        Test the 'destroy' command.
        """
        console_instance = HBNBCommand()
        output = console_instance.do_create("User")
        output_destroy = console_instance.do_destroy("User " + output)
        self.assertEqual("", output_destroy)

    def test_do_all(self):
        """
        Test the 'all' command.
        """
        console_instance = HBNBCommand()
        output_all = console_instance.do_all("User")
        self.assertIn("User", output_all)

    def test_do_update(self):
        """
        Test the 'update' command.
        """
        console_instance = HBNBCommand()
        output = console_instance.do_create("User")
        output_update = console_instance.do_update("User " + output + " name John")
        self.assertEqual("", output_update)

    def test_instance_dot_cmd(self):
        """
        Test the 'instance_dot_cmd' method.
        """
        console_instance = HBNBCommand()
        output = console_instance.do_create("User")
        console_instance.do_show("User." + output)


if __name__ == '__main__':
    unittest.main()
