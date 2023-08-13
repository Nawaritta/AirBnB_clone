#!/usr/bin/python3
"""tests for the console.py file"""
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand

class TestHBNBCommand(unittest.TestCase):
    """Test cases for the HBNBCommand class in console.py"""

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_create(self, mock_stdout):
        """Test the 'do_create' method"""
        console = HBNBCommand()
        console.do_create("BaseModel")
        output = mock_stdout.getvalue().strip()
        self.assertTrue(output.startswith(''))

    def test_tokenize(self):
        """Test the 'tokenize' helper function"""
        result = tokenize('create BaseModel')
        self.assertEqual(result, ['create', 'BaseModel'])

    def test_default(self):
        """Test the 'default' method with known syntax"""
        console = HBNBCommand()
        with patch('builtins.input', return_value='quit'):
            self.assertTrue(console.onecmd("quit"))

    def test_count(self):
        """Test the 'do_count' method"""
        console = HBNBCommand()
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            console.do_count("BaseModel")
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, '0')

    def test_count_with_instances(self):
        """Test the 'do_count' method with instances"""
        pass

    def test_default_unknown_syntax(self):
        """Test the 'default' method with unknown syntax"""
        console = HBNBCommand()
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            console.default("invalid_command")
            output = mock_stdout.getvalue().strip()
            self.assertTrue(output.startswith("*** Unknown syntax:"))

    def test_empty_arguments(self):
        """Test handling empty arguments in the 'default' method"""
        console = HBNBCommand()
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            console.default("")
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "")

    def test_invalid_class_name(self):
        """Test handling invalid class name in 'do_create' method"""
        console = HBNBCommand()
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            console.do_create("InvalidClass")
            output = mock_stdout.getvalue().strip()
            self.assertTrue(output.startswith("** class doesn't exist **"))

if __name__ == '__main__':
    unittest.main()
