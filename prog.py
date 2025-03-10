import os, lib


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
	x_order = [''] * (n + 1)
	for i in range(n):
		x_order[i] = f'x{i + 1}'
	x_order[n] = 'c'
	if lib.to_diag(num_matrix, x_order):
		print('successfully diagonalized matrix')
	else:
		print('failed to diagonalize, calculating norm...')
		norm = lib.find_norm(num_matrix)
		print(f'norm: {norm}')
		if norm > 1:
			print('norm > 1 => cannot use gauss-seidel method')
			exit(1)
	solution = []
	iterations = lib.solve(num_matrix, eps, solution)
	print(f'success! took {iterations} iterations')
	print('solution: {', end='')
	for i in range(n):
		print(f'{x_order[i]}={solution[i]}, ', end='')
	print('}')


def read_from_file(filename: str) -> None:
	if not os.path.exists(filename):
		print("file not found")
		exit(1)
	with open(filename, 'r') as f:
		lines = f.readlines()
