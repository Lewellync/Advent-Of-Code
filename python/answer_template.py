import os, sys

def answer_one(input):
    return 1
    
def answer_two(input):
    return 2

if __name__ == "__main__":
    input_path = os.path.join(sys.argv[0].removesuffix("answer.py"), "input.txt")
    with open(input_path, 'r') as file:
        input = file.read()
        print(answer_one(input))
        print(answer_two(input))