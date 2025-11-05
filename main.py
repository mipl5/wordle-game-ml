from wordle import Wordle
import tkinter as tk

window = tk.Tk()
window.title("Wordle Game App")
window.geometry("400x300")
window.resizable(False, False)

greeting_label = tk.Label(window, text="Enter your word here:", font=("Helvetica", 16))
greeting_label.pack(pady=20)

w = Wordle()
print(w.word)

input_frame = tk.Frame(window)
input_frame.pack(pady=10)

guess_var = tk.StringVar()
guess_entry = tk.Entry(input_frame, textvariable=guess_var, font=("Helvetica", 14), width=10)
guess_entry.pack(side=tk.LEFT, padx=(0, 8))

feedback_label = tk.Label(window, text="", fg="red")
feedback_label.pack()

def submit_guess():
	val = guess_var.get().strip()
	if not val:
		feedback_label.config(text="Please enter a word.")
		return
	if len(val) > 5:
		feedback_label.config(text="Word too long (max 5 letters).")
		return
	if not val.isalpha():
		feedback_label.config(text="Only alphabetic letters are allowed.")
		return

	feedback_label.config(text="")
	w.make_guess(val.lower())
	guess_var.set("")

submit_btn = tk.Button(input_frame, text="Submit", command=submit_guess)
submit_btn.pack(side=tk.LEFT)

window.mainloop()