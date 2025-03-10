def to_diag(matrix: list[list[float]]) -> bool:
	found_greater = False
	for i in range(len(matrix)):
		max_el = max([abs(el) for el in matrix[i]])
		sum_of_others = sum([abs(el) for el in matrix[i]]) - max_el
		if max_el >= sum_of_others:
			if max_el > sum_of_others:
				found_greater = True
			switch_columns(matrix, i, matrix[i].index(max_el))
		else:
			return False
	return found_greater


def switch_columns(matrix: list[list[float]], ind1: int, ind2: int) -> None:
	if ind1 == ind2: return
	for i in range(len(matrix)):
		matrix[i][ind1], matrix[i][ind2] = matrix[i][ind2], matrix[i][ind1]