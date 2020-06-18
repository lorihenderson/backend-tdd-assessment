#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""An enhanced version of the 'echo' cmd line utility."""

__author__ = "Lori Henderson with some help from Chris Warren"


import sys
import argparse


def create_parser():
    """Returns an instance of argparse.ArgumentParser"""
    parser = argparse.ArgumentParser(description="Perform transformation on input text")
    parser.add_argument("-l", "--lower", help="Convert text to lowercase", action="store_true")
    parser.add_argument("-t", "--title", help="Convert text to titlecase", action="store_true")
    parser.add_argument("-u", "--upper", help="Convert text to uppercase", action="store_true")
    parser.add_argument("text", help="Text to be changed")
    
    return parser


def main(args):
    """Implementation of echo"""
    parser = create_parser()

    if not in args:
        parser.print_usage()
        sys.exit()
    
    args = parser.parse_args(args)
    text = args.text

    if args.upper:
        text = text.upper()
    elif args.lower:
        text = text.lower()
    elif args.title:
        text = text.title()
        
    return text


if __name__ == '__main__':
    main(sys.argv[1:])
