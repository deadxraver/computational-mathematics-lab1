import argparse

import prog

help_msg = '''
This is a program for solving systems of linear equations
'''
epilog_msg = '''
The Gauss-Seidel method is used
'''
parser = argparse.ArgumentParser(description=help_msg, epilog=epilog_msg)
parser.add_argument('--filename', '-f', help='use file as a source for input data. `var=<data>` syntax is used')

args = parser.parse_args()

if args.filename is None: prog.read_from_console()
else: prog.read_from_file(args.filename)
