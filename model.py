# model.py

import random
import json
import os
from words import get_words

MAX_ATTEMPTS = 6
SCORE_FILE = "scores.json"

class HangmanModel:
    def __init__(self):
        self.players = ["Joueur 1", "Joueur 2"]
        self.current_player = 0
        self.word = ""
        self.display_word = ""
        self.guessed_letters = set()
        self.attempts_left = MAX_ATTEMPTS
        self.scores = {p: 0 for p in self.players}
        self.difficulty = "Facile"
        self.load_scores()

    def switch_player(self):
        self.current_player = 1 - self.current_player

    def get_current_player(self):
        return self.players[self.current_player]

    def start_new_game(self, difficulty="Facile"):
        self.difficulty = difficulty
        word_list = get_words(difficulty)
        self.word = random.choice(word_list).lower()
        self.display_word = "_" * len(self.word)
        self.guessed_letters = set()
        self.attempts_left = MAX_ATTEMPTS

    def guess_letter(self, letter):
        if letter in self.guessed_letters:
            return False, "Lettre déjà utilisée."

        self.guessed_letters.add(letter)

        if letter in self.word:
            self.display_word = "".join([l if l in self.guessed_letters else "_" for l in self.word])
            if "_" not in self.display_word:
                self.update_score()
            return True, "Bonne lettre !"
        else:
            self.attempts_left -= 1
            return False, "Lettre incorrecte."

    def is_won(self):
        return "_" not in self.display_word

    def is_lost(self):
        return self.attempts_left <= 0

    def update_score(self):
        base = {"Facile": 10, "Moyen": 20, "Difficile": 30}
        self.scores[self.get_current_player()] += base.get(self.difficulty, 10)
        self.save_scores()

    def save_scores(self):
        with open(SCORE_FILE, "w") as f:
            json.dump(self.scores, f)

    def load_scores(self):
        if os.path.exists(SCORE_FILE):
            with open(SCORE_FILE, "r") as f:
                self.scores = json.load(f)
