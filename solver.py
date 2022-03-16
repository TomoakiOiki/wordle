
import random


class WordleSolver:
    def __init__(self, word_list:list):
        self.word_list:list = word_list
        self.tried:int = 0 # maximum number of tried = 6
        self.unused_letters:list = []  # like ["a","b","c"]
        self.blow_letters: list = []  # like ["a","b","c"]
        self.hit_letters: list = []  # like [{"x":1},{"y":2},{"z":3},{"w":4}]

    def eject_word(self):
        for letter in self.unused_letters:
            self.word_list = list(filter(lambda x: letter not in x, self.word_list))

    def select_word(self,is_random:bool = False):
        candidate = self.word_list
        if is_random:
            return random.choice(candidate)

        for hit_letter in self.hit_letters:
            letter, pos = list(hit_letter.items())[0]
            candidate = list(filter(lambda x: x[pos] == letter, candidate))
        for letter in self.blow_letters:
            candidate = list(filter(lambda x: letter in x, candidate))

        return random.choice(candidate)

    def process_result(self,status:str,word:str):
        for index,s in enumerate(status):
            if s == "-":
                if word[index] not in self.unused_letters:
                    self.unused_letters.append(word[index])
            elif s == "h":
                if word[index] not in self.hit_letters:
                    self.hit_letters.append({word[index]:index})
            elif s == "b":
                if word[index] not in self.blow_letters:
                    self.blow_letters.append(word[index])

    def output_log(self):
        print("------------------")
        print("Try:",self.tried)
        print("unused_letters:",self.unused_letters)
        print("blow_letters:",self.blow_letters)
        print("hit_letters:",self.hit_letters)
        print("Number of candidate:",len(self.word_list))
        print("------------------")

    def solve(self):
        while self.tried < 6:
            self.tried += 1
            self.output_log()
            word = self.select_word(is_random=self.tried == 1)
            print("Selected word is", word)
            status = input("Input status:")
            self.process_result(status,word)
            self.eject_word()

with open("./word/wordlist.txt") as f:
    word_list = f.read().splitlines()
    solver = WordleSolver(word_list)
    solver.solve()
