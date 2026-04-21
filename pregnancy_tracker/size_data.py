# Size comparisons for different pregnancy weeks
# Format: week -> (size comparison, length in cm/inches)

PREGNANCY_SIZES = {
    4: ("Mohn", "0.2 cm"),
    5: ("Sesam", "0.3 cm"),
    6: ("Linse", "0.6 cm"),
    7: ("Blaubeere", "1 cm"),
    8: ("Himbeere", "1.6 cm"),
    9: ("Traube", "2.3 cm"),
    10: ("Zwergenorange", "3.1 cm"),
    11: ("Feige", "4.1 cm"),
    12: ("Limette", "5.4 cm"),
    13: ("Erbsenschote", "7.4 cm"),
    14: ("Zitrone", "8.7 cm"),
    15: ("Apfel", "10.1 cm"),
    16: ("Avocado", "11.6 cm"),
    17: ("Rübe", "13 cm"),
    18: ("Paprika", "14.2 cm"),
    19: ("Mango", "15.3 cm"),
    20: ("Banane", "16.4 cm"),
    21: ("Karotte", "26.7 cm"),
    22: ("Papaya", "27.8 cm"),
    23: ("Grapefruit", "28.9 cm"),
    24: ("Maiskolben", "30 cm"),
    25: ("Blumenkohl", "34.6 cm"),
    26: ("Salat", "35.6 cm"),
    27: ("Kohl", "36.6 cm"),
    28: ("Aubergine", "37.6 cm"),
    29: ("Butternut-Kürbis", "38.6 cm"),
    30: ("Kokosnuss", "39.9 cm"),
    31: ("Ananas", "41.1 cm"),
    32: ("Pak Choi", "42.4 cm"),
    33: ("Durian", "43.7 cm"),
    34: ("Cantaloupe-Melone", "45 cm"),
    35: ("Honigmelone", "46.2 cm"),
    36: ("Römersalat", "47.4 cm"),
    37: ("Mangold", "48.6 cm"),
    38: ("Lauch", "49.8 cm"),
    39: ("Wassermelone", "50.7 cm"),
    40: ("Kürbis", "51.2 cm"),
}

def get_size_for_week(week):
    """Get the size comparison for a given pregnancy week"""
    if week < 4:
        return ("Too early", "< 0.2 cm")
    elif week > 40:
        return ("Full term!", "~51 cm")
    else:
        return PREGNANCY_SIZES.get(week, ("Growing", f"~{10 + (week-10)*1.5:.1f} cm"))
