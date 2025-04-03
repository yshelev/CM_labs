from functools import lru_cache
from typing import Callable


@lru_cache(maxsize=None)
def divided_difference(func: Callable[[float], float],
                       *points) -> float:
	"""
	Вычисление разделенной разности
	:param func: Функция, по которой вычисляются точки
	:param points: Точки, для которых вычисляется разделенная разность
	:return:
	"""
	if len(points) == 1:
		return func(points[0])
	if len(points) == 0:
		return 0
	return (divided_difference(func, *points[1:]) - divided_difference(func, *points[:-1])) / (points[-1] - points[0])
