import random

def flip_biased_coin(p):
    return random.randint(0,1)
    pass

# Otestování funkce
print(flip_biased_coin(0.7))  # Simulace hodu s 70% šancí na výhru
