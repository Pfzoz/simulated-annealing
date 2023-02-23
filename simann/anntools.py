import numpy as np
from math import e

def max_variation(x_fitness : float, n_fitness : float) -> float:
    return -(n_fitness - x_fitness)

def min_variation(x_fitness : float, n_fitness : float) -> float:
    return n_fitness - x_fitness

def restructure_chance(variation : float, temperature : float):
    return e**(-(variation/temperature))
