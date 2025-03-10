import os, lib


def read_from_console() -> None:
	try:
		n = int(input('Введите размерность матрицы: '))
		if n > 20 or n < 1:
			print("n must be between 1 and 20")
			exit(-1)
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
	start_prog(n, eps, num_matrix)


def start_prog(n: int, eps: float, num_matrix: list[list[float]]) -> None:
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


def missing_arg(arg: str) -> None:
	print(f'missing argument "{arg}"')
	exit(-1)


def read_from_file(filename: str) -> None:
	if not os.path.exists(filename):
		print("file not found")
		exit(-1)
	with open(filename, 'r') as f:
		lines = ''.join(f.readlines())
	lines = lines.upper()
	if lines.find('N=') != -1:
		n = int(lines[lines.find('N='):].replace('N=', '$').replace('\n', '$').split('$')[1])
		if n > 20 or n < 1:
			print("n must be between 1 and 20")
			exit(-1)
	else:
		missing_arg('n')
	if lines.find('EPS=') != -1:
		eps = float(lines[lines.find('EPS='):].replace('EPS=', '$').replace('\n', '$').split('$')[1])
	else:
		missing_arg('eps')
	if lines.find('MATRIX:') != -1:
		try:
			num_matrix = [[]] * n
			spl_lines = lines.replace('MATRIX:', '$').split('$')[1].split('\n')[1:]
			for i in range(n):
				num_matrix[i] = [float(el) for el in spl_lines[i].split()]
		except:
			print('error in input file')
			exit(-1)
	else:
		missing_arg('matrix')
	start_prog(n, eps, num_matrix)