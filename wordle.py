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
        match_list = [1 for c1, c2 in zip(self.word, word) if c1 == c2]

        same_pos_count = sum(match_list)

        print("Correct letters and on their places:")
        print(f"Count: {same_pos_count}: {match_list}")

        target_counts = Counter(self.word)
        guess_counts = Counter(word)

        common_counts = target_counts & guess_counts

        total_possible_matches = sum(common_counts.values())

        non_pos_count = total_possible_matches - same_pos_count

        print("\nCorrect letters but on WRONG places: ")
        print(f'Count: {non_pos_count}')


    def make_guess(self, word:str):
        if self.guess_count < 6:
            self.guess_count += 1
            if cw.check_word(word):
                self.do_counts(word)
            else:
                print("Word doesn't exist")
        else:
            print("You are out of guesses (max 6)")