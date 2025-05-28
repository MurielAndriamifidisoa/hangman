# view.py

import tkinter as tk
from tkinter import messagebox, ttk

class HangmanView:
    def __init__(self, root, controller):
        self.controller = controller
        self.root = root
        self.root.title("🎮 Jeu du Pendu - Modern Edition")
        self.root.geometry("700x550")
        self.root.configure(bg="#F4F4F9")

        self.timer_seconds = 30
        self.timer_label = None
        self.timer_id = None

        self.setup_widgets()

    def setup_widgets(self):
        title = tk.Label(self.root, text="🔠 Jeu du Pendu", font=("Helvetica", 26, "bold"), bg="#F4F4F9", fg="#333")
        title.pack(pady=10)

        self.player_label = tk.Label(self.root, text="", font=("Helvetica", 16, "italic"), bg="#F4F4F9", fg="#555")
        self.player_label.pack()

        # Timer
        self.timer_label = tk.Label(self.root, text="Temps restant : 30s", font=("Helvetica", 14), bg="#F4F4F9", fg="#D9534F")
        self.timer_label.pack()

        diff_frame = tk.Frame(self.root, bg="#F4F4F9")
        diff_frame.pack(pady=5)
        tk.Label(diff_frame, text="Difficulté :", font=("Helvetica", 12), bg="#F4F4F9").pack(side=tk.LEFT)
        self.difficulty = ttk.Combobox(diff_frame, values=["Facile", "Moyen", "Difficile"], state="readonly", width=10)
        self.difficulty.set("Facile")
        self.difficulty.pack(side=tk.LEFT)

        self.word_label = tk.Label(self.root, text="", font=("Courier New", 36), bg="#F4F4F9", fg="#222")
        self.word_label.pack(pady=15)

        self.canvas = tk.Canvas(self.root, width=220, height=220, bg="white", highlightthickness=1, highlightbackground="#ccc")
        self.canvas.pack(pady=5)

        entry_frame = tk.Frame(self.root, bg="#F4F4F9")
        entry_frame.pack(pady=10)

        self.letter_entry = tk.Entry(entry_frame, font=("Helvetica", 20), width=2, justify='center')
        self.letter_entry.grid(row=0, column=0, padx=5)
        self.letter_entry.bind("<Return>", self.submit_guess)

        self.guess_button = tk.Button(entry_frame, text="✔️ Deviner", command=self.submit_guess, font=("Helvetica", 12), bg="#5cb85c", fg="white")
        self.guess_button.grid(row=0, column=1, padx=10)

        self.used_label = tk.Label(self.root, text="", font=("Helvetica", 12), bg="#F4F4F9")
        self.used_label.pack()

        self.attempts_label = tk.Label(self.root, text="", font=("Helvetica", 12), bg="#F4F4F9")
        self.attempts_label.pack()

        self.score_label = tk.Label(self.root, text="", font=("Helvetica", 12), bg="#F4F4F9")
        self.score_label.pack()

        self.restart_button = tk.Button(self.root, text="🔄 Nouvelle Partie", command=self.controller.new_game, bg="#0275d8", fg="white", font=("Helvetica", 12))
        self.restart_button.pack(pady=20)

    def update_ui(self, display_word, used_letters, attempts_left, scores, current_player):
        self.word_label.config(text=" ".join(display_word))
        self.used_label.config(text="Lettres utilisées : " + ", ".join(sorted(used_letters)))
        self.attempts_label.config(text=f"Essais restants : {attempts_left}")
        self.player_label.config(text=f"Tour de : {current_player}")
        self.score_label.config(text=f"Scores : {scores}")
        self.letter_entry.delete(0, tk.END)
        self.draw_hangman(attempts_left)
        self.reset_timer()

    def draw_hangman(self, tries_left):
        self.canvas.delete("all")
        base = 6 - tries_left
        if base >= 1:
            self.canvas.create_line(20, 200, 200, 200)
        if base >= 2:
            self.canvas.create_line(60, 200, 60, 20)
        if base >= 3:
            self.canvas.create_line(60, 20, 150, 20)
        if base >= 4:
            self.canvas.create_line(150, 20, 150, 40)
        if base >= 5:
            self.canvas.create_oval(135, 40, 165, 70)
        if base >= 6:
            self.canvas.create_line(150, 70, 150, 120)
            self.canvas.create_line(150, 90, 130, 110)
            self.canvas.create_line(150, 90, 170, 110)
            self.canvas.create_line(150, 120, 130, 160)
            self.canvas.create_line(150, 120, 170, 160)

    def reset_timer(self):
        self.timer_seconds = 30
        self.update_timer()

    def update_timer(self):
        self.timer_label.config(text=f"Temps restant : {self.timer_seconds}s")
        if self.timer_seconds > 0:
            self.timer_seconds -= 1
            self.timer_id = self.root.after(1000, self.update_timer)
        else:
            self.controller.time_out()

    def cancel_timer(self):
        if self.timer_id:
            self.root.after_cancel(self.timer_id)

    def submit_guess(self, event=None):
        letter = self.letter_entry.get().lower()
        if not letter.isalpha() or len(letter) != 1:
            messagebox.showwarning("Erreur", "Veuillez entrer une seule lettre.")
            return
        self.cancel_timer()
        self.controller.guess_letter(letter)

    def get_selected_difficulty(self):
        return self.difficulty.get()

    def show_message(self, title, message):
        messagebox.showinfo(title, message)
