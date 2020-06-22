#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Implements a test fixture for the echo.py module

Students are expected to edit this module, to add more tests to run
against the 'echo.py' program.
"""

__author__ = "Lori Henderson with some help from Chris Warren"

import echo
import unittest
import subprocess


# Stu dent shall complete this TestEcho class so that all tests run and pass.
class TestEcho(unittest.TestCase):
    def setUp(self):
        """Called by parent class ONCE before all tests are run"""
        self.parser = echo.create_parser()

    def test_help(self):
        """Testing help option"""
        process = subprocess.Popen(
            ["python", "./echo.py", "-h"],
            stdout = subprocess.PIPE)
        stdout, _ = process.communicate()
        with open("./USAGE", "r") as f:
            usage = f.read()

        self.assertEqual(stdout.decode(), usage)

    def test_lower_short(self):
        """Check if short option '-l' performs lowercasing"""
        args = ["-l", "HELLO WORLD"]
        namespace = self.parser.parse_args(args)
        self.assertTrue(namespace.lower)
        result = echo.main(args)
        self.assertEqual(result, "hello world")
    
    def test_upper_short(self):
        """Check if short option '-u- performs uppercasing"""
        args = ["-u", "hello world"]
        namespace = self.parser.parse_args(args)
        self.assertTrue(namespace.upper)
        result = echo.main(args)
        self.assertEqual(result, "HELLO WORLD")
    
    def test_lower_long(self):
        """Check if long option '--lower' performs lowercasing"""
        args = ["--lower", "Hello World"]
        namespace = self.parser.parse_args(args)
        self.assertTrue(namespace.lower)
        result = echo.main(args)
        self.assertEqual(result, "hello world")
    
    def test_upper_long(self):
        """Check if long option '--upper' performs uppercasing"""
        args = ["--upper", "hello World"]
        namespace = self.parser.parse_args(args)
        self.assertTrue(namespace.upper)
        result = echo.main(args)
        self.assertEqual(result, "HELLO WORLD")

    def test_title_short(self):
        """"""
        args = ["-t", "hello world"]
        namespace = self.parser.parse_args(args)
        self.assertTrue(namespace.title)
        result = echo.main(args)
        self.assertEqual(result, "Hello World")
    
    def test_title_long(self):
        """"""
        args = ["--title", "hello world"]
        namespace = self.parser.parse_args(args)
        self.assertTrue(namespace.title)
        result = echo.main(args)
        self.assertEqual(result, "Hello World")
    
    def test_all(self):
        """"""
        args = ["-tul", "hello world"]
        namespace = self.parser.parse_args(args)
        self.assertTrue(namespace.upper)
        result = echo.main(args)
        self.assertEqual(result, "HELLO WORLD")
    
    def test_two(self):
        """"""
        args = ["-ul", "hellO wOrld"]
        namespace = self.parser.parse_args(args)
        self.assertTrue(namespace.upper)
        result = echo.main(args)
        self.assertEqual(result, "HELLO WORLD")
    
    def test_none(self):
        """"""
        args = ["hello world"]
        result = echo.main(args)
        self.assertEqual(result, "hello world")


if __name__ == '__main__':
    unittest.main()
