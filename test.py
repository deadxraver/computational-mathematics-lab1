import lib


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