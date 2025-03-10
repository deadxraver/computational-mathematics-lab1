import os

import lib

def read_from_console() -> None:
	try:
		n = int(input('Введите размерность матрицы: '))
		num_matrix = [[]] * n
		eps = float(input('Введите желаемую точность: '))
	except ValueError:
		print("not a number")
		exit(1)

	print('Введите матрицу:')
	for i in range(n):
		try:
			num_matrix[i] = [float(el) for el in input().split()]
		except ValueError:
			print("not a number")
			exit(1)
		if len(num_matrix[i]) != n + 1:
			print("wrong length")
			exit(1)

	if lib.to_diag(num_matrix): print('successfully diagonalized matrix')
	else: print('failed to diagonalize')


def read_from_file(filename: str) -> None:
	if not os.path.exists(filename):
		print("file not found")
		exit(1)
