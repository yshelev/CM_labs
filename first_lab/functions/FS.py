from functools import lru_cache

import numpy as np

@lru_cache(maxsize=None)
def f(x: float) -> float:
	"""
	Вычисляет значение функции в точке x
	:param x:
	:return:
	"""
	return 0.5 * x**2 - np.cos(2 * x)

@lru_cache(maxsize=None)
def f_second_derivative(x: float) -> float:
	"""
	Вычисляет значение второй производной функции f в точке x
	:param x:
	:return:
	"""
	return 4 * np.cos(2 * x) - 1

@lru_cache(maxsize=None)
def f_third_derivative(x: float) -> float:
	"""
	Вычисляет значение третьей производной функции f в точке х
	:param x:
	:return:
	"""
	return -8 * np.sin(2 * x)