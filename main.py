# main.py

import tkinter as tk
from controller import HangmanController

if __name__ == "__main__":
    root = tk.Tk()
    app = HangmanController(root)
    root.mainloop()
