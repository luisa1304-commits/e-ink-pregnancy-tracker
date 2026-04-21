# Größenvergleiche mit Tieren für jede Schwangerschaftswoche
PREGNANCY_SIZES = {
    4:  ("Marienkäfer",         "0.2 cm"),
    5:  ("Ameise",              "0.3 cm"),
    6:  ("Floh",                "0.6 cm"),
    7:  ("Regenwurm",           "1 cm"),
    8:  ("Schmetterlingsraupe", "1.6 cm"),
    9:  ("Weinbergschnecke",    "2.3 cm"),
    10: ("Maus",                "3.1 cm"),
    11: ("Hamster",             "4.1 cm"),
    12: ("Spitzmaus",           "5.4 cm"),
    13: ("Eichhörnchen",        "7.4 cm"),
    14: ("Meerschweinchen",     "8.7 cm"),
    15: ("Ratte",               "10.1 cm"),
    16: ("Chinchilla",          "11.6 cm"),
    17: ("Frettchen",           "13 cm"),
    18: ("Igel",                "14.2 cm"),
    19: ("Ente",                "15.3 cm"),
    20: ("Kaninchen",           "16.4 cm"),
    21: ("Hauskatze",           "26.7 cm"),
    22: ("Dackel",              "27.8 cm"),
    23: ("Fuchs",               "28.9 cm"),
    24: ("Fasan",               "30 cm"),
    25: ("Otter",               "34.6 cm"),
    26: ("Hase",                "35.6 cm"),
    27: ("Waschbär",            "36.6 cm"),
    28: ("Biber",               "37.6 cm"),
    29: ("Koalababy",           "38.6 cm"),
    30: ("Meerkatze",           "39.9 cm"),
    31: ("Pinguin",             "41.1 cm"),
    32: ("Beagle",              "42.4 cm"),
    33: ("Murmeltier",          "43.7 cm"),
    34: ("Rehkitz",             "45 cm"),
    35: ("Schäferhundwelpe",    "46.2 cm"),
    36: ("Leguan",              "47.4 cm"),
    37: ("Kleines Ferkel",      "48.6 cm"),
    38: ("Ziegenlamm",          "49.8 cm"),
    39: ("Neugeborenes Lamm",   "50.7 cm"),
    40: ("Neugeborenes Reh",    "51.2 cm"),
}

def get_size_for_week(week):
    """Gibt den Tiergrößenvergleich für eine bestimmte Schwangerschaftswoche zurück."""
    if week < 4:
        return ("Noch ganz winzig", "< 0.2 cm")
    elif week > 40:
        return ("Voll ausgereift!", "~51 cm")
    else:
        return PREGNANCY_SIZES.get(week, ("Wächst fleißig", f"~{10 + (week-10)*1.5:.1f} cm"))
