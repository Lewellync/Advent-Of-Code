import os, sys
import hashlib

def answer_one(input):
    counter = 0
    while True:
        hash = hashlib.md5(f"{input}{counter}".encode()).hexdigest()
        if hash[0:5] == "00000":
            print(f"{input}{counter}")
            print(hash)
            break
        counter += 1
    
def answer_two(input):
    counter = 0
    while True:
        hash = hashlib.md5(f"{input}{counter}".encode()).hexdigest()
        if hash[0:6] == "000000":
            print(f"{input}{counter}")
            print(hash)
            break
        counter += 1
    

if __name__ == "__main__":
    input_path = os.path.join(sys.argv[0].removesuffix("answer.py"), "input.txt")
    with open(input_path, 'r') as file:
        input = file.read()
        answer_one(input)
        answer_two(input)