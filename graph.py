import numpy as np
from numpy.random import choice, random

class Graph:

    def __init__(self, dots : np.ndarray = None) -> None:
        self.dots = dots

    def set_dots(self, dot_amount : int, connections : list[dict[int:float]] = None):
        if connections is None:
            connections = []
            for i in range(dot_amount):
                connections.append({choice(dot_amount) : random()})
        new_dots = np.ndarray((dot_amount, dot_amount), dtype=np.float64)
        new_dots[:, :] = -1
        for i, conns in zip(range(dot_amount), connections):
            for connection in conns.keys():
                new_dots[i, connection] = conns[connection]
        self.dots = new_dots

    def connection_fitness(self, connection : np.ndarray) -> float:
        distance = 0
        for i in range(len(connection)-1):
            distance += self.dots[connection[i], connection[i+1]]
        return distance
    
    def valid_connection(self, connection : np.ndarray) -> bool:
        if connection[0] != connection[-1] or connection[0] != 0:
            return False
        for i in range(len(connection)-1):
            if self.dots[connection[i], connection[i+1]] < 0:
                return False
        
        return True

    def connection_neighbors(self, connection : np.ndarray) -> list[list]:
        neighbors = []
        for i in range(len(connection)):
            for j in range(len(connection)):
                new_neighbor = connection.copy()
                aux = new_neighbor[i]
                new_neighbor[i] = new_neighbor[j]
                new_neighbor[j] = aux
                if self.valid_connection(new_neighbor) and i != j: 
                    neighbors.append(new_neighbor)
        return neighbors
