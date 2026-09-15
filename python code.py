# Карапайым рефлекс агент - тазалагыш робот
# Орын (A, B, C) жане куй (Dirty/Clean) бойынша не icтеу керегiн кесте аркылы аныктаймыз

def simple_reflex_vacuum_agent(percept):
    location, status = percept

    rules = {
        ('A', 'Dirty'): 'Suck',
        ('A', 'Clean'): 'Right',
        ('B', 'Dirty'): 'Suck',
        ('B', 'Clean'): 'Right',
        ('C', 'Dirty'): 'Suck',
        ('C', 'Clean'): 'Left',
    }

    return rules[(location, status)]


# Тексеру - алты турлi жагдай
test_percepts = [
    ('A', 'Dirty'),
    ('A', 'Clean'),
    ('B', 'Dirty'),
    ('B', 'Clean'),
    ('C', 'Dirty'),
    ('C', 'Clean'),
]

for percept in test_percepts:
    action = simple_reflex_vacuum_agent(percept)
    print(f"Percept={percept} -> Action={action}")
