import math


def validate_matrix(matrix: list[list[float]], n: int):
	return len(matrix) == n and len(matrix[0]) == n + 1


def to_diag(matrix: list[list[float]], x_order: list[str]) -> bool:
	def find_index(vector: list[float], el: float):
		for i in range(len(vector)):
			if abs(vector[i]) == el: return i

	found_greater = False
	for i in range(len(matrix)):
		max_el = max([abs(el) for el in matrix[i][:-1]])
		sum_of_others = sum([abs(el) for el in matrix[i][:-1]]) - max_el
		if max_el >= sum_of_others:
			if max_el > sum_of_others:
				found_greater = True
			switch_columns(matrix, x_order, i, find_index(matrix[i], max_el))
		else:
			return False
	if not found_greater: return False
	found_greater = False
	for i in range(len(matrix)):
		max_el = matrix[i][i]
		sum_of_others = sum(matrix[i][:-1]) - max_el
		if max_el >= sum_of_others:
			if max_el > sum_of_others:
				found_greater = True
		else:
			return False
	return found_greater


def switch_columns(matrix: list[list[float]], x_order: list[str], ind1: int, ind2: int) -> None:
	if ind1 == ind2: return
	x_order[ind1], x_order[ind2] = x_order[ind2], x_order[ind1]
	for i in range(len(matrix)):
		matrix[i][ind1], matrix[i][ind2] = matrix[i][ind2], matrix[i][ind1]


def vec_abs(vector: list[float]) -> float:
	return math.sqrt(sum([x ** 2 for x in vector]))


def vec_sub(vector1: list[float], vector2: list[float]) -> list[float]:
	return [abs(vector1[i] - vector2[i]) for i in range(len(vector1))]


def solve(diagonalized_matrix: list[list[float]], eps: float, solution: list[float]) -> int:
	x_prev = [0.0] * len(diagonalized_matrix)
	for i in range(len(diagonalized_matrix)):
		x_prev[i] = diagonalized_matrix[i][-1]
	iterations = 0
	while 1:
		x_new = [0.0] * len(diagonalized_matrix)
		iterations += 1
		for i in range(len(x_prev)):
			x_new[i] = diagonalized_matrix[i][-1] / diagonalized_matrix[i][i]
			first_sum = 0.0
			second_sum = 0.0
			for j in range(i - 1):
				first_sum += diagonalized_matrix[i][j] * x_new[j] / diagonalized_matrix[i][i]
			for j in range(i, len(x_prev)):
				second_sum += diagonalized_matrix[i][j] * x_prev[j]
			x_new[i] *= diagonalized_matrix[i][-1] - first_sum - second_sum
		print(f'{iterations}: x(k)= {x_prev} x(k+1) = {x_new} ')
		if iterations > 1000: exit(1)
		if max(vec_sub(x_new, x_prev)) < eps: # vec_abs -> max
			for i in range(len(x_new)):
				solution.append(x_new[i])
			return iterations
		x_prev = x_new
