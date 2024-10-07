import random

def roll_multiple_dice(n, k):
    results = []
    for _ in range(n):
        roll = random.randint(1, k)  
        results.append(roll)         
    return results
    pass

# Otestování funkce
print(roll_multiple_dice(3, 6))  # Simulace hodu 3 kostkami, každá má 6 hran
