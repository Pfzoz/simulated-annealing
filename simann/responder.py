from .anntools import *
from numpy.random import random

class Responder:

    # Dependency Injection based object, being that:
    # fitness_func must return a number, preferrably continuous problems
    # neighbor_func must return an indexable array-like

    def __init__(self, fitness_func,
                    neighbor_func,
                    initial_temperature : float, 
                    initial_solution,
                    max_neighbors : float,
                    alpha : float,
                    var_func = min_variation) -> None:
        self.fitness_func = fitness_func
        self.neighbor_func = neighbor_func
        self.initial_temperature = initial_temperature
        self.max_neighbors = max_neighbors
        self.alpha = alpha
        self.initial_solution = initial_solution
        self.var_func = var_func

    def run(self, epochs : int = 1000):
        epoch = 0
        current_solution = self.initial_solution
        global_solution = current_solution
        iter_t = 0
        temperature = self.initial_temperature
        while (temperature > 0 and epoch < epochs):
            print("\nCurrent Solution: ", current_solution)
            print("Global Solution: ", global_solution)
            print("T = ", temperature)
            while (iter_t < self.max_neighbors):
                neighbors = self.neighbor_func(current_solution)
                if len(neighbors) == 0: break
                if iter_t >= len(neighbors): 
                    chosen_neighbor = neighbors[iter_t-len(neighbors)-1]
                else:
                    chosen_neighbor = neighbors[iter_t]
                iter_t += 1
                fitness = self.fitness_func(current_solution)
                neighbor_fitness = self.fitness_func(chosen_neighbor)
                print("Chosen Neighbor: ", chosen_neighbor, neighbor_fitness)
                variation = self.var_func(fitness, neighbor_fitness)
                if (variation < 0):
                    print("-->Picked better neighbor.")
                    current_solution = chosen_neighbor
                    if (self.var_func(self.fitness_func(global_solution), neighbor_fitness) < 0):
                        global_solution = chosen_neighbor
                elif (random() < restructure_chance(variation, temperature)):
                    print("-->Picked neighbor by temperature.")
                    current_solution = chosen_neighbor
            temperature *= self.alpha
            iter_t = 0
            epoch += 1
        return global_solution
