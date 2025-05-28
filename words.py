# words.py

easy_words = [
    "chat", "chien", "pomme", "bleu", "livre", "porte", "maison", "fleur", "lune", "soleil"
]

medium_words = [
    "ordinateur", "python", "clavier", "fenêtre", "jardin", "bouteille", "musique", "montagne", "magicien", "paysage"
]

hard_words = [
    "intelligence", "programmation", "philosophie", "psychologie", "développement", "extraordinaire", "substantifique", "connaissance", "exponentielle"
]

def get_words(difficulty):
    if difficulty == "Facile":
        return easy_words
    elif difficulty == "Moyen":
        return medium_words
    elif difficulty == "Difficile":
        return hard_words
    else:
        return easy_words
