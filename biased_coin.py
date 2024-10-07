import random

def flip_biased_coin(p):
    random_value = random.random()
    if random_value < p:
        return "Heads"
    else:
        return "Tails"
    pass

# Otestování funkce
print(flip_biased_coin(0.7))  # Simulace hodu s 70% šancí na výhru
