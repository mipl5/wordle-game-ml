from wonderwords import RandomWord
r = RandomWord()
from check_word import CheckWord
cw = CheckWord()
from collections import Counter

class Wordle:
    def __init__(self):
        self.word = r.word(word_min_length=5, word_max_length=5)
        self.guess_count = 0

    def do_counts(self, word:str):
        if len(word) != len(self.word):
            print(f"Guess must be {len(self.word)} letters (got {len(word)}).")
            return

        target = list(self.word)
        guess = list(word)

        statuses = [None] * len(target)  # 'G' = green, 'Y' = yellow, '-' = gray
        remaining = Counter(target)

        for i, (t, g) in enumerate(zip(target, guess)):
            if t == g:
                statuses[i] = 'G'
                remaining[g] -= 1

        for i, g in enumerate(guess):
            if statuses[i] is not None:
                continue
            if remaining.get(g, 0) > 0:
                statuses[i] = 'Y'
                remaining[g] -= 1
            else:
                statuses[i] = '-'

        same_pos_count = statuses.count('G')
        non_pos_count = statuses.count('Y')

        print("Per-letter statuses (G=correct place, Y=wrong place, -=absent):")
        print(' '.join(f"{ch}:{st}" for ch, st in zip(guess, statuses)))
        print(f"Correct letters in correct place: {same_pos_count}")
        print(f"Correct letters in wrong place: {non_pos_count}")


    def make_guess(self, word:str):
        if self.guess_count < 6:
            self.guess_count += 1
            if cw.check_word(word):
                self.do_counts(word)
                if word == self.word:
                    print(f"Congratulations! You've guessed the word '{self.word}' correctly!")
            else:
                print("Word doesn't exist")
        else:
            print("You are out of guesses (max 6)")