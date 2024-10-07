import random

def generate_schedule(seed=42):
    # Nastavení seedu pro opakovatelnost
    if seed is not None:
        random.seed(seed)

    # Předměty a kolik hodin týdně
    předměty = {
        'INF': 2,
        'VAP': 2,
        'MIT': 2,
        'PRG': 3,
        'TEV': 2,
        'MAT': 4,
        'CJL': 3,
        'MSW': 2,
        'ASW': 2,
        'ANJ': 3,
        'OBN': 1,
        'POS': 3
    }

    # Dny ve školním týdnu 
    dny = ['PO', 'ÚT', 'ST', 'ČT', 'PÁ']
    
    # Inicializace rozvrhu
    schedule = {day: [] for day in dny}

    # Generování rozvrhu
    for subject, hours in předměty.items():
        for _ in range(hours):
            day = random.choice(dny)
            schedule[day].append(subject)

    return schedule

def print_schedule(schedule):
    print("Rozvrh hodin:")
       
    # Vytvoření nadpisu pro hodiny (1-10)
    hour_labels = [f"{i + 1}" for i in range(10)]
    
    # Tisk nadpisu hodin s odsazením
    print("       " + "    ".join(hour_labels))
    
    # Tisk rozvrhu
    for day in ['PO', 'ÚT', 'ST', 'ČT', 'PÁ']:
        hour_subjects = schedule.get(day, [])
     
        # Odstranění čárek a tisk rozvrhu
        print(f"{day}: " + "   ".join(hour_subjects))

# Příklad použití
seed_value = 42  # Zvolený seed pro opakovatelnost
schedule = generate_schedule(seed_value)
print_schedule(schedule)