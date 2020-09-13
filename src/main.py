from genetic_algorithm import (crossover, fitness, get_initial_generation,
                               get_next_generation, mutation)
from utils import get_named_route, get_total_distance, reached_stability
from variables import GENERATION_MAX


generation = get_initial_generation()

for cnt in range(GENERATION_MAX):
    generation = fitness(generation)

    new_individuals = crossover(generation)
    new_individuals.extend(mutation(generation))

    if reached_stability(generation):
        break

    generation = get_next_generation(generation, new_individuals)

print('best route:')
print(get_named_route(generation[0]))
print('total distance:')
print(get_total_distance(generation[0]))
