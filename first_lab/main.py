from functions.FS import *
from Interpolation import Interpolation

# [0.6  0.65 0.7  0.75 0.8  0.85 0.9  0.95 1.   1.05 1.1 ]
def main():

	a, b = (0.6, 1.1)
	x_s = 0.84
	true_value = f(x_s)

	default_interpolation = Interpolation(f, a, b, x_s, 11)
	print(f"точное значение: {true_value}")
	print(f"узлы интерполяции: {default_interpolation.partition}")
	print("\n")
	print("-------------------------------------------------------")
	print("ЛИНЕЙНАЯ ИНТЕРПОЛЯЦИЯ")

	a, b = (0.8, 0.85) #выбираем ближайшие узлы интерполяции

	linear_interpolation = Interpolation(f, a, b, x_s, 2)

	mnR, mxR = linear_interpolation.remainder_term()

	print("Многочленом Лагранжа:", lagr_int_2 := linear_interpolation.lagrange_interpolation(2),
	      "\nМногочленом Ньютона:", newton_int_2 := linear_interpolation.newton_interpolation(2))
	print(f"Остаточный член многочлена Лагранжа: {abs(true_value - lagr_int_2)} \n"
	      f"Остаточный член многочлена Ньютона: {abs(true_value - newton_int_2)}")
	print(f"Остаточный член многочлена Лагранжа меньше 10^-4: {abs(true_value - lagr_int_2) < 10e-4}\n"
	      f"Остаточный член многочлена Ньютона меньше 10^-4: {abs(true_value - newton_int_2) < 10e-4}")
	print(f"левая допустимая граница: {mnR.item()}\n"
	      f"остаточный член: {abs(true_value - lagr_int_2).item()}\n"
	      f"правая допустимая граница: {mxR.item()}")

	print("\n")
	print("-------------------------------------------------------")
	print("КВАДРАТИЧНАЯ ИНТЕРПОЛЯЦИЯ")

	a, b = (0.8, 0.9)  # выбираем ближайшие узлы интерполяции

	quadratic_interpolation = Interpolation(f, a, b, x_s, 3)
	mnR, mxR = quadratic_interpolation.remainder_term()

	print("Многочленом Лагранжа:", lagr_int_3 := quadratic_interpolation.lagrange_interpolation(3),"\n"
          "Многочленом Ньютона:", newton_int_3 := quadratic_interpolation.newton_interpolation(3))
	print(f"Остаточный член многочлена Лагранжа: {(true_value - lagr_int_3).item()} \n"
	      f"Остаточный член многочлена Ньютона: {(true_value - newton_int_3).item()}")
	print(f"Остаточный член многочлена Лагранжа меньше 10^-5: {abs(true_value - lagr_int_3) < 10e-5}\n"
	      f"Остаточный член многочлена Ньютона меньше 10^-5: {abs(true_value - newton_int_3) < 10e-5}")
	print(f"левая допустимая граница: {mnR.item()}\n"
	      f"остаточный член: {(true_value - lagr_int_3)}\n"
	      f"правая допустимая граница: {mxR.item()}")


if __name__ == '__main__':
	main()
