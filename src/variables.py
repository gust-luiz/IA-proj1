from sys import maxsize

# Population size to manage
POPULATION_SZ = 40
# Generation max attempts
GENERATION_MAX = 1000

# Crossover probability between individuals
CROSSOVER_PBTY = .5
# Individual mutation probability
MUTATION_PBTY = .1

# Current individuals percentage to keep to the next generation
CURRENT_INDV_PERC = .6
# New individuals percentage to select to the next generation
NEW_INDV_PERC = 1 - CURRENT_INDV_PERC

# Stability percentage range between generation
STABILITY_PERC = .15
# Stability max occurrences in a row
STABILITY_MAX = 5

# Shortest distance found so far
distance_min = maxsize
# Stability current counter
stability_base_pnt = None
# Stability current counter
stability_cnt = 0

# Citied coded as 0-9 digit
CODED_CITIES = {
    '0': 'São Paulo',
    '1': 'Salvador',
    '2': 'Rio de Janeiro',
    '3': 'Lima',
    '4': 'Bogotá',
    '5': 'Santiago',
    '6': 'Caracas',
    '7': 'Belo Horizonte',
    '8': 'Porto Alegre',
    '9': 'Brasília',
}

# Known distances between cities
DISTANCES = {
    '01': 17,
    '02': 3,
    '03': 35,
    '04': 43,
    '05': 26,
    '06': 44,
    '07': 5,
    '08': 8,
    '09': 9,
    '12': 20,
    '13': 31,
    '14': 47,
    '15': 11,
    '16': 51,
    '17': 22,
    '18': 8,
    '19': 23,
    '23': 38,
    '24': 45,
    '25': 29,
    '26': 45,
    '27': 3,
    '28': 11,
    '29': 9,
    '34': 19,
    '35': 25,
    '36': 27,
    '37': 36,
    '38': 33,
    '39': 32,
    '45': 43,
    '46': 10,
    '47': 43,
    '48': 46,
    '49': 37,
    '56': 49,
    '57': 30,
    '58': 19,
    '59': 30,
    '67': 42,
    '68': 48,
    '69': 35,
    '78': 13,
    '79': 6,
    '89': 16,
}
