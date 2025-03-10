import argparse

import lib
import prog

help_msg = '''
This is a program for solving systems of linear equations
'''
epilog_msg = '''
The Gauss-Seidel method is used
'''
# parser = argparse.ArgumentParser(description=help_msg, epilog=epilog_msg)
# parser.add_argument('--filename', '-f', help='use file as a source for input data. `var=<data>` syntax is used')
#
# args = parser.parse_args()
#
# if args.filename is None: prog.read_from_console()
# else: prog.read_from_file(args.filename)


def print_mtrx(mtrx: list[list[float]]) -> None:
	for i in range(len(mtrx)):
		print(mtrx[i])

mtrx = [
	[1, 2, 3, 4],
	[1, 10, 1, 8],
	[27, 15, 1, 1]
]
x_order = ['x1', 'x2', 'x3', 'b']
print(x_order)
print_mtrx(mtrx)
if lib.to_diag(mtrx, x_order):
	print()
	print(x_order)
	print_mtrx(mtrx)
	solution = []
	print(f'took {lib.solve(mtrx, 0.1, solution)} iterations')
	print(solution)
else:
	print('failed to diagonalize')
	print(x_order)
	print_mtrx(mtrx)