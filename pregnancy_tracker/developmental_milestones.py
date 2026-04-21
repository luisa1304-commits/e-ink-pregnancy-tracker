"""Developmental milestones and anatomy updates for each week of pregnancy."""

def get_milestone_for_week(week):
    """Get developmental milestone information for a specific week.
    
    Returns:
        dict: Contains 'size', 'weight', and 'development' keys with milestone info
    """
    
    milestones = {
        4: {
            "size": "Mohn",
            "weight": "< 1 g",
            "development": "Die Einnistung ist weitgehend abgeschlossen. Das Neuralrohr beginnt sich zu bilden – die Grundlage für Gehirn und Rückenmark."
        },
        5: {
            "size": "Sesam",
            "weight": "< 1 g",
            "development": "Das Herz beginnt zu schlagen. Erste Anlagen von Gehirn, Rückenmark sowie Armen und Beinen werden sichtbar."
        },
        6: {
            "size": "Linse",
            "weight": "< 1 g",
            "development": "Augen- und Ohrenanlagen entwickeln sich weiter. Auch Kiefer, Rachen und erste innere Organe differenzieren sich."
        },
        7: {
            "size": "Blaubeere",
            "weight": "< 1 g",
            "development": "Das Gehirn wächst nun besonders schnell. Arme und Beine werden länger und entwickeln sich weiter."
        },
        8: {
            "size": "Himbeere",
            "weight": "1 g",
            "development": "Finger- und Zehenanlagen sind erkennbar. Gesichtszüge und Augenlider werden deutlicher."
        },
        9: {
            "size": "Traube",
            "weight": "2 g",
            "development": "Aus medizinischer Sicht spricht man jetzt vom Fötus. Die wichtigsten Organsysteme sind angelegt und reifen weiter."
        },
        10: {
            "size": "Zwergenorange",
            "weight": "4 g",
            "development": "Die inneren Organe beginnen schrittweise zu arbeiten. Auch Zahnanlagen und weitere feine Strukturen entstehen."
        },
        11: {
            "size": "Feige",
            "weight": "7 g",
            "development": "Die Knochen beginnen sich zu festigen. Haarfollikel und äußere Geschlechtsmerkmale entwickeln sich weiter."
        },
        12: {
            "size": "Limette",
            "weight": "14 g",
            "development": "Erste Reflexe sind möglich. Die Nieren beginnen mit der Urinproduktion, und das Wachstum wird zunehmend koordinierter."
        },
        13: {
            "size": "Erbsenschote",
            "weight": "23 g",
            "development": "Fingerabdrücke entstehen. Auch die Stimmbänder entwickeln sich, während der Körper weiter wächst."
        },
        14: {
            "size": "Zitrone",
            "weight": "43 g",
            "development": "Die Gesichtsmuskulatur ist weiter gereift. Erste mimische Bewegungen wie Stirnrunzeln sind möglich."
        },
        15: {
            "size": "Apfel",
            "weight": "70 g",
            "development": "Die Beine werden länger, und die Bewegungen wirken zunehmend koordinierter."
        },
        16: {
            "size": "Avocado",
            "weight": "100 g",
            "development": "Das Hörvermögen beginnt sich zu entwickeln. Auch die Augen können sich bereits bewegen."
        },
        17: {
            "size": "Rübe",
            "weight": "140 g",
            "development": "Das Skelett wird stabiler. Erste Fettdepots und Schweißdrüsen beginnen sich zu entwickeln."
        },
        18: {
            "size": "Paprika",
            "weight": "190 g",
            "development": "Die Ohren befinden sich fast in ihrer endgültigen Position. Das Nervensystem reift weiter."
        },
        19: {
            "size": "Mango",
            "weight": "240 g",
            "development": "Die Sinne entwickeln sich weiter. Die Haut wird nun von der schützenden Käseschmiere (Vernix caseosa) bedeckt."
        },
        20: {
            "size": "Banane",
            "weight": "300 g",
            "development": "Das Baby kann schlucken und bildet Mekonium im Darm. Bewegungen werden jetzt oft deutlicher wahrgenommen."
        },
        21: {
            "size": "Karotte",
            "weight": "360 g",
            "development": "Augenbrauen und Augenlider sind weit entwickelt. Das Gehör verbessert sich, und Reaktionen auf Geräusche nehmen zu."
        },
        22: {
            "size": "Papaya",
            "weight": "430 g",
            "development": "Die Augen können Lichtreize wahrnehmen. Muskulatur und Griffbewegungen entwickeln sich weiter."
        },
        23: {
            "size": "Grapefruit",
            "weight": "500 g",
            "development": "Das Hörvermögen ist weiter ausgereift. Im Schlaf treten bereits rasche Augenbewegungen (REM-Phasen) auf."
        },
        24: {
            "size": "Maiskolben",
            "weight": "600 g",
            "development": "Die Lunge entwickelt feinere Verzweigungen. Auch Geschmacksknospen und weitere Organfunktionen reifen weiter."
        },
        25: {
            "size": "Blumenkohl",
            "weight": "660 g",
            "development": "Das Baby reagiert zunehmend auf Stimmen und vertraute Geräusche. Die Nasenöffnungen sind nun offen."
        },
        26: {
            "size": "Salat",
            "weight": "760 g",
            "development": "Die Augen öffnen sich. Atembewegungen mit Fruchtwasser unterstützen die weitere Entwicklung der Lunge."
        },
        27: {
            "size": "Kohl",
            "weight": "875 g",
            "development": "Das Gehirngewebe reift weiter. Schlaf- und Wachphasen werden regelmäßiger."
        },
        28: {
            "size": "Aubergine",
            "weight": "1 kg",
            "development": "Das Baby kann jetzt blinzeln. Die Entwicklung des zentralen Nervensystems macht große Fortschritte."
        },
        29: {
            "size": "Butternut-Kürbis",
            "weight": "1.2 kg",
            "development": "Muskeln und Lunge reifen weiter. Das Wachstum des Kopfes spiegelt die intensive Gehirnentwicklung wider."
        },
        30: {
            "size": "Kokosnuss",
            "weight": "1.3 kg",
            "development": "Das Knochenmark übernimmt zunehmend die Bildung roter Blutkörperchen. Auch das Gehirn entwickelt sich weiterhin sehr schnell."
        },
        31: {
            "size": "Ananas",
            "weight": "1.5 kg",
            "development": "Alle fünf Sinne sind nun in unterschiedlichem Maß aktiv. Reize aus der Umgebung können immer besser verarbeitet werden."
        },
        32: {
            "size": "Pak Choi",
            "weight": "1.7 kg",
            "development": "Die Knochen härten weiter aus, bleiben aber noch flexibel. Das Baby übt regelmäßig Atembewegungen."
        },
        33: {
            "size": "Durian",
            "weight": "1.9 kg",
            "development": "Das Immunsystem entwickelt sich weiter. Lichtreize können zunehmend erkannt und verarbeitet werden."
        },
        34: {
            "size": "Cantaloupe-Melone",
            "weight": "2.1 kg",
            "development": "Das zentrale Nervensystem reift weiter. Vertraute Stimmen oder Melodien können möglicherweise schon wiedererkannt werden."
        },
        35: {
            "size": "Honigmelone",
            "weight": "2.4 kg",
            "development": "Die Nieren sind weitgehend ausgereift. Auch die Leber ist zunehmend in der Lage, Stoffwechselprodukte zu verarbeiten."
        },
        36: {
            "size": "Römersalat",
            "weight": "2.6 kg",
            "development": "Die feine Körperbehaarung (Lanugo) fällt nach und nach aus. Das Verdauungssystem ist fast bereit für die Zeit nach der Geburt."
        },
        37: {
            "size": "Mangold",
            "weight": "2.9 kg",
            "development": "Das Baby gilt nun als termingerecht. Saug-, Greif- und Atembewegungen werden weiter geübt."
        },
        38: {
            "size": "Lauch",
            "weight": "3.1 kg",
            "development": "Die Organe sind funktionell ausgereift. Gehirn und Nervensystem entwickeln sich bis zur Geburt weiter."
        },
        39: {
            "size": "Wassermelone",
            "weight": "3.3 kg",
            "development": "Die Entwicklung ist weitgehend abgeschlossen. Es werden weiterhin wichtige Fettreserven aufgebaut."
        },
        40: {
            "size": "Kürbis",
            "weight": "3.5 kg",
            "development": "Das Baby ist bereit für die Geburt. Alle wichtigen Organsysteme sind funktionsfähig und auf das Leben außerhalb des Mutterleibs vorbereitet."
        }
    }
    
    # Handle weeks outside normal range
    if week < 4:
        return {
            "size": "Mohn",
            "weight": "< 1 g",
            "development": "Die Zellen teilen sich rasch, und die Einnistung in die Gebärmutterschleimhaut findet statt."
        }
    elif week > 40:
        return {
            "size": "Kürbis",
            "weight": "3.5 kg+",
            "development": "Die Entwicklung ist abgeschlossen, und das Baby kann jederzeit geboren werden."
        }
    
    return milestones.get(week, milestones[40])
