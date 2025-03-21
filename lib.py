import copy


def validate_matrix(matrix: list[list[float]], n: int):
	return len(matrix) == n and len(matrix[0]) == n + 1

def find_norm(matrix: list[list[float]]) -> float:
	res = []
	for cond in range(2):
		new_matrix = copy.deepcopy(matrix)
		i_range = [i for i in range(len(matrix))]
		j_range = [i for i in range(len(matrix))]
		i_indexes = []
		j_indexes = []
		for _ in range(len(matrix)):
			i_max = i_range[0]
			j_max = j_range[0]
			for i in i_range:
				for j in j_range:
					if cond and abs(matrix[i][j]) > abs(matrix[i_max][j_max]) or not cond and abs(matrix[i][j]) >= abs(matrix[i_max][j_max]):
						i_max = i
						j_max = j
			i_indexes.append(i_max)
			j_indexes.append(j_max)
			i_range.remove(i_max)
			j_range.remove(j_max)
		for index in range(len(i_indexes)):
			new_matrix[i_indexes[index]][j_indexes[index]] = 0
			for j in range(len(j_indexes)):
				new_matrix[i_indexes[index]][j] /= matrix[i_indexes[index]][j_indexes[index]]
		res.append(max([sum([abs(c) for c in new_matrix[i][:-1]]) for i in range(len(matrix))]))
	return min(res)

def to_diag(matrix: list[list[float]], x_order: list[str]) -> bool:
	def find_index(vector: list[float], el: float):
		for i in range(len(vector)):
			if abs(vector[i]) == el: return i

	for i in range(len(matrix)):
		max_el = max([abs(el) for el in matrix[i][:-1]])
		switch_columns(matrix, x_order, i, find_index(matrix[i], max_el))

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
			for j in range(i):
				first_sum += diagonalized_matrix[i][j] * x_new[j] / diagonalized_matrix[i][i]
			for j in range(i + 1, len(x_prev)):
				second_sum += diagonalized_matrix[i][j] * x_prev[j] / diagonalized_matrix[i][i]
			x_new[i] -= first_sum + second_sum
		if iterations > 1000:
			print('too many iterations, probably no solution for system')
			exit(1)
		approximation = vec_sub(x_new, x_prev)
		if max(approximation) < eps:
			print(f'approximation vector: {approximation}')
			for i in range(len(x_new)):
				solution.append(x_new[i])
			return iterations
		x_prev = x_new
