import lib


def print_mtrx(mtrx: list[list[float]]) -> None:
	for i in range(len(mtrx)):
		print(mtrx[i])

mtrx = [
	[10, 2, 3, 4],
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
	print(f'took {lib.solve(mtrx, 0.001, solution)} iterations')
	print(f'solution by g-z: {solution}')
	print(f'putting in first equation: {[sum([mtrx[j][i] * solution[i] for i in range(len(solution))]) for j in range(len(solution))]}')
else:
	print('failed to diagonalize')
	norm = lib.find_norm(mtrx)
	if norm > 1:
		print('norm bigger than ooone')
		exit(0)
	print(f'norm: {norm}')
	print(x_order)
	print_mtrx(mtrx)