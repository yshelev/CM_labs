import math
from typing import Callable

import numpy as np

from functions.FS import f_second_derivative, f_third_derivative
from functions.services import divided_difference


class Interpolation:
	"""
	Класс вычисления интерполяционного многочлена Лагранжа или Ньютона
	"""

	f: Callable[[float], float]
	b: float
	a: float
	x: float
	h: float
	degree: int
	partition: np.ndarray

	def __init__(self,
	             func: Callable[[float], float],
	             a: float,
	             b: float,
	             x: float,
	             degree: int) -> None:
		"""
		Конструктор класса Interpolation.
		:param func: Функция интерполяции
		:param a: Левая граница интервала интерполяции
		:param b: Правая граница интервала интерполяции
		:param x: Искомая точка
		:param degree: Количество узлов интерполяции
		"""

		self.f = func
		self.a = a
		self.b = b
		self.x = x
		self.degree = degree

		self.partition = np.linspace(self.a, self.b, self.degree)

	def true_value(self) -> float:
		"""
		Возвращает значение функции self.f в точке self.x
		:return:
		"""

		return self.f(self.x)

	def __get_interpolation_mesh(self,
	                             m: int) -> np.ndarray:
		index = 0
		while self.partition[index] < self.x:
			index += 1

		count = 0
		l, r = index, index

		while count < m:
			if r <= self.partition.shape[0]:
				r += 1
				count += 1
			if l >= 0 and count < m:
				l -= 1
				count += 1

		return self.partition[l:r]




	def lagrange_interpolation(self,
	                           m: int) -> float:
		"""
		Вычисление интерполяционного многочлена Лагранжа
		:return:
		"""
		result = 0

		interpolation_mesh = self.__get_interpolation_mesh(m)

		for i in range(m):
			temp = self.f(interpolation_mesh[i])
			for j in range(m):
				temp *= (self.x - interpolation_mesh[j]) / (interpolation_mesh[i] - interpolation_mesh[j]) if i != j else 1

			result += temp

		return result

	def newton_interpolation(self,
	                         m: int) -> float:
		"""
		Вычисление интерполяционного многочлена Ньютона
		:return:
		"""

		interpolation_mesh = self.__get_interpolation_mesh(m)

		return (sum(
			[
				divided_difference(self.f, *[interpolation_mesh[j] for j in range(i + 1)]) *
				math.prod([(self.x - interpolation_mesh[j]) for j in range(i)]) for i in range(m)
			]
		))

	def remainder_term(self) -> (np.float64, np.float64):
		"""
		Вычисление остаточного члена полинома
		:return:
		"""
		omega: float = math.prod([self.x - x_i for x_i in self.partition]) / math.factorial(self.degree)
		derivative_: np.ndarray

		print(math.prod([self.x - x_i for x_i in self.partition]))
	
		if self.degree == 2:
			derivative_ = np.array([f_second_derivative(x) for x in self.partition])
		elif self.degree == 3:
			derivative_ = np.array([f_third_derivative(x) for x in self.partition])
		else:
			print("степень вторая или третья и все так решил сам создатель.")
			return -1, -1
		mn, mx = min(derivative_) * omega, max(derivative_) * omega
		return min(mn, mx), max(mn, mx)

