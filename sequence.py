import random

def generate_sequence(n):
    for x in range(n):
        print(random.randint(0, 100))
    pass

# Otestování funkce
generate_sequence(10)  # Vygeneruje 10 náhodných čísel
