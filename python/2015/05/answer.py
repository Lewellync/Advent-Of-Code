import os, sys
import re

def answer_one(input):
    nice_strings = 0
    vowels = ["a","e","i","o","u"]
    bad_combos = ["ab","cd","pq","xy"]
    for line in re.split(r'\n', input):
        vowel_counter = 0
        double = False
        naughty = False
        for ind, char in enumerate(line):
            if char in vowels:
                vowel_counter += 1
            if ind < len(line) - 1:
                if line[ind] == line[ind+1]:
                    double = True
                if f"{line[ind]}{line[ind+1]}" in bad_combos:
                    naughty = True
                    break
        if double and vowel_counter >= 3 and not naughty:
            nice_strings += 1

    print(nice_strings)
    
def answer_two(input):
    nice_strings = 0
    for line in re.split(r'\n', input):
        jump = False
        pair = False
        pairs = []
        for ind, char in enumerate(line):
            if not pair and ind > 0:
                if f"{line[ind-1]}{char}" in pairs[:len(pairs)-1]:
                    pair = True
                else:
                    pairs.append(f"{line[ind-1]}{char}")
            if not jump and ind > 1:
                if char is line[ind-2] and char is not line[ind-1]:
                    jump = True
            if jump and pair:
                nice_strings += 1
                break
    print(nice_strings)

if __name__ == "__main__":
    input_path = os.path.join(sys.argv[0].removesuffix("answer.py"), "input.txt")
    with open(input_path, 'r') as file:
        input = file.read()
        answer_one(input)
        answer_two(input)