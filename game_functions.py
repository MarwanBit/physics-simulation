from sympy import symbols, diff


def evaluate_vector_field(vector_field, x_pos, y_pos):
	'''
	evaluate the vector field as the position x_pos, y_pos and return the vector...

	inputs:
		vector_field (a vector field of the function (f_1, f_2)) dependent on x,y
		x_pos, y_pos (x,y)

	outputs:
		the vector_field evaluated at (x,y)
	'''

	x, y = symbols('x y', real=True)

	return (vector_field[0].subs([(x, x_pos), (y, y_pos)]).evalf(), vector_field[1].subs([(x, x_pos), (y, y_pos)]).evalf())