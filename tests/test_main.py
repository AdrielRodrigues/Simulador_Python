import os
import sys
import unittest
from io import StringIO
from unittest.mock import patch

class TestMain(unittest.TestCase):

    def test_with_valid_arguments(self):
        sim_config_file = 'xml/MSP-nsf.json'
        seed = 10
        min_load = 50
        max_load = 200
        step = 50
        with patch('sys.stdout', new=StringIO()) as fake_out:
            main([sim_config_file, seed, min_load, max_load, step])
            self.assertTrue(fake_out.getvalue())

    def test_with_invalid_config_file(self):
        sim_config_file = 'xml/invalid_file.json'
        seed = 10
        min_load = 50
        max_load = 200
        step = 50
        with patch('sys.stdout', new=StringIO()) as fake_out:
            main([sim_config_file, seed, min_load, max_load, step])
            self.assertEqual(fake_out.getvalue(),
                             f"File {sim_config_file} not found\n")

    def test_with_missing_arguments(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            main([])
            self.assertEqual(fake_out.getvalue(
            ), "the following arguments are required: simConfigFile, seed, minload, maxload, step\n")

    def test_with_partial_arguments(self):
        sim_config_file = 'test_config_file.txt'
        seed = 1234
        with patch('sys.stdout', new=StringIO()) as fake_out:
            main([sim_config_file, seed])
            self.assertEqual(fake_out.getvalue(
            ), "the following arguments are required: minload, maxload, step\n")


if __name__ == '__main__':
    unittest.main()
