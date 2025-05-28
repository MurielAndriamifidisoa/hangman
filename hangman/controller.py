# controller.py

from model import HangmanModel
from view import HangmanView

class HangmanController:
    def __init__(self, root):
        self.model = HangmanModel()
        self.view = HangmanView(root, self)
        self.new_game()

    def new_game(self):
        self.model.start_new_game(self.view.get_selected_difficulty())
        self.update_view()

    def guess_letter(self, letter):
        success, msg = self.model.guess_letter(letter)
        self.update_view()

        if self.model.is_won():
            self.view.show_message("🎉 Gagné !", f"{self.model.get_current_player()} a gagné ! Le mot était : {self.model.word}")
            self.model.switch_player()
            self.new_game()
        elif self.model.is_lost():
            self.view.show_message("💀 Perdu !", f"{self.model.get_current_player()} a perdu. Le mot était : {self.model.word}")
            self.model.switch_player()
            self.new_game()

    def time_out(self):
        self.view.show_message("⏰ Temps écoulé", f"{self.model.get_current_player()} a dépassé le temps imparti.")
        self.model.switch_player()
        self.new_game()

    def update_view(self):
        self.view.update_ui(
            self.model.display_word,
            self.model.guessed_letters,
            self.model.attempts_left,
            self.model.scores,
            self.model.get_current_player()
        )
