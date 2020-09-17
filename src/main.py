import variables
from genetic_algorithm import (crossover, fitness, get_initial_generation,
                               get_next_generation, get_total_distance,
                               mutation)
from utils import get_named_route, reached_stability
from variables import GENERATION_MAX

generation = get_initial_generation()

print('#gen\tmin\tavg')

for cnt in range(GENERATION_MAX):
    generation = fitness(generation)

    print(f'{cnt}\t{get_total_distance(generation[0])}\t{variables.avg_distance}')

    if reached_stability(generation):
        break

    new_individuals = crossover(generation)
    new_individuals.extend(mutation(generation))

    if cnt != GENERATION_MAX - 1:
        generation = get_next_generation(generation, new_individuals)

print('best route:')
print(get_named_route(generation[0]))
print('with total distance:', get_total_distance(generation[0]))
