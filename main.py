from wordle import Wordle
import tkinter as tk

def start_game():
    global wordle_game, boxes
    wordle_game = Wordle()
    print(wordle_game.word)  # For debugging

    # Clear all boxes
    for r in range(rows):
        for c in range(cols):
            boxes[r][c].config(text="", bg="white")

    entry.config(state="normal")
    guess_button.config(text="Guess", command=on_guess)


def on_guess():
    guess = entry.get().strip().lower()

    if len(guess) != 5:
        print("Please enter a 5-letter word.")
        return

    word = wordle_game.word
    current_row = wordle_game.guess_count

    # Check letter statuses
    colors = ["gray"] * 5
    word_remaining = list(word)

    # First pass: check greens
    for i in range(5):
        if guess[i] == word[i]:
            colors[i] = "green"
            word_remaining[i] = None

    # Second pass: check yellows
    for i in range(5):
        if colors[i] == "gray" and guess[i] in word_remaining:
            colors[i] = "yellow"
            word_remaining[word_remaining.index(guess[i])] = None

    # Apply to GUI boxes
    for i, ch in enumerate(guess):
        boxes[current_row][i].config(
            text=ch.upper(),
            bg=colors[i],
            fg="white"
        )

    wordle_game.make_guess(guess)
    entry.delete(0, tk.END)

    # Check for win or game over
    if guess == word or wordle_game.guess_count >= rows:
        entry.config(state="disabled")
        guess_button.config(text="Restart", command=start_game)


# --- Tkinter UI setup ---
wordle_game = Wordle()
print(wordle_game.word)

window = tk.Tk()
window.title("Wordle Game App")
window.iconbitmap("wordle_app_icon.ico")

rows = 6
cols = 5

title_label = tk.Label(
    window,
    text="Wordle Game: Guess the 5-letter word!",
    font=("Arial", 18, "bold"),
    fg="blue"
)
title_label.pack(pady=(20, 10))

frame = tk.Frame(window)
frame.pack(padx=10, pady=10)

boxes = []

for r in range(rows):
    row_boxes = []
    for c in range(cols):
        lbl = tk.Label(
            frame,
            width=4,
            height=2,
            font=("Helvetica", 24, "bold"),
            relief="solid",
            borderwidth=1,
            bg="white"
        )
        lbl.grid(row=r, column=c, padx=5, pady=5)
        row_boxes.append(lbl)
    boxes.append(row_boxes)

entry = tk.Entry(window, font=("Arial", 14), fg="red")
entry.pack(pady=20)

guess_button = tk.Button(window, text="Guess", command=on_guess, font=("Arial", 12))
guess_button.pack(pady=(0, 40))

window.mainloop()