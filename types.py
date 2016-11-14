import csv

# EFFECTIVENESS
NO_EFFECT = 0
NOT_VERY_EFFECTIVE = 0.5
NEUTRAL = 1
SUPER_EFFECTIVE = 2

ATTACKING = 'ATTACKING'
# TYPES
NORMAL = 'NORMAL'
FIRE = 'FIRE'
WATER = 'WATER'
ELECTRIC = 'ELECTRIC'
GRASS = 'GRASS'
ICE = 'ICE'
FIGHTING = 'FIGHTING'
POISON = 'POISON'
GROUND = 'GROUND'
FLYING = 'FLYING'
PSYCHIC = 'PSYCHIC'
BUG = 'BUG'
ROCK = 'ROCK'
GHOST = 'GHOST'
DRAGON = 'DRAGON'
DARK = 'DARK'
STEEL = 'STEEL'
FAIRY = 'FAIRY'

TYPES = [
    NORMAL, FIRE, WATER, ELECTRIC, GRASS, ICE, FIGHTING, POISON, GROUND,
    FLYING, PSYCHIC, BUG, ROCK, GHOST, DRAGON, DARK, STEEL, FAIRY
]


def load_type_effectiveness():
    type_effectiveness = {}
    with open('type_chart.csv', 'rb') as f:
        reader = csv.reader(f, delimiter=',')
        header = reader.next()

        for row in reader:
            atk = row[header.index(ATTACKING)]
            type_effectiveness[atk] = {}
            for t in TYPES:
                type_effectiveness[atk][t] = row[header.index(t)]
    return type_effectiveness


TYPE_EFFECTIVENESS = load_type_effectiveness()


def types_with_effectiveness_to(type, effectiveness):
    types = []
    for attacker in TYPE_EFFECTIVENESS:
        if float(TYPE_EFFECTIVENESS.get(attacker).get(type)) == effectiveness:
            types.append(attacker)

    return types


if __name__ == '__main__':
    print TYPE_EFFECTIVENESS[FIRE]
    print types_with_effectiveness_to(GRASS, NOT_VERY_EFFECTIVE)
