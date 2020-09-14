from random import shuffle, sample, randint, random

from variables import POPULATION_SZ, CROSSOVER_PBTY, MUTATION_PBTY, distance_min
from utils import get_total_distance


def get_initial_generation():
    population = []

    for _ in range(POPULATION_SZ):
        another_cities = list(map(str, range(9)))
        shuffle(another_cities)
        population.append(''.join(['9', *another_cities]))

    return population


def get_next_generation(current, new):
    return current


def fitness(generation):
    calculed = list(map(_calc_fitness, generation))
    calculed.sort(key = lambda x: x[1])

    return [c[0] for c in calculed]


def selection(generation):
    n_selected = round(CROSSOVER_PBTY * len(generation)) # number of individuals to create couples
    if n_selected % 2 != 0: # check if number is even
        n_selected += 1
    
    return generation[0:n_selected]


def crossover_2_point(generation):
    selection_list = selection(generation)
    shuffle(selection_list)
    couples = zip(selection_list[0:int(len(selection_list) / 2)], selection_list[int(len(selection_list) / 2):])
    
    sons = []

    for parent_a, parent_b in couples:
        son_a = list(parent_a)
        son_b = list(parent_b)

        points = sorted(sample(range(1, 9), 2))

        idx_changes = []
        for i in range(points[0]+1, points[-1]+1):
            # Verify if the number inside the crossover range already exists in the range outside the crossover
            # range in the other parent
            if (parent_a[0:points[0]+1].find(parent_b[i]) == -1) and (parent_a[points[-1]+1:].find(parent_b[i]) == -1) and \
                (parent_b[0:points[0]+1].find(parent_a[i]) == -1) and (parent_b[points[-1]+1:].find(parent_a[i]) == -1):
                son_a[i], son_b[i] = parent_b[i], parent_a[i]
                idx_changes.append(i)

        # Checking if the changes don't create repetition. Otherwise, undo the change.
        for i in idx_changes:
            if son_a.count(son_a[i]) > 1:
                son_a[i], son_b[i] = parent_a[i], parent_b[i]

        # Add to son list if it is different from parents
        if (son_a != list(parent_a)) and (son_b != list(parent_b)):
            #print("TROCOU!!")
            sons.append(''.join(son_a))
            sons.append(''.join(son_b))
    
    return sons


def mutation(generation):
    individuals_mutated = []
    generation_mutated = generation.copy()

    for id, individual in enumerate(generation_mutated):
        if random() <= MUTATION_PBTY:
            gene_a_idx, gene_b_idx = (int(n) for n in sample(range(1, 10), 2))
            old_gene = individual[gene_a_idx]
            new_gene = individual[gene_b_idx]

            individual_list = list(individual)
            individual_list[gene_a_idx], individual_list[gene_b_idx] = new_gene, old_gene

            individuals_mutated.append(''.join(individual_list))

            generation_mutated[id] = ''.join(individual_list)

    return individuals_mutated, generation_mutated


def _calc_fitness(route):
    return route, get_total_distance(route) / distance_min
