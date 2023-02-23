from graph import Graph
from numpy import array
from simann.responder import Responder

tsp_example = Graph()
mapping = [
    {1:3,2:7,3:2},
    {2:1,3:5,0:3},
    {1:1,0:7,3:6},
    {0:2,1:5,2:6}
]

tsp_example.set_dots(dot_amount=4, connections=mapping)

print(tsp_example.dots)

responder = Responder(
    fitness_func=tsp_example.connection_fitness,
    neighbor_func=tsp_example.connection_neighbors,
    initial_solution=array([0,2,3,1,0]),
    initial_temperature=5,
    max_neighbors=3,
    alpha=0.75
)

result = responder.run(epochs=10)
print("Intial Solution: [0, 2, 3, 1, 0]", tsp_example.connection_fitness(array([0,2,3,1,0])))
print("Result: ", result, tsp_example.connection_fitness(result))