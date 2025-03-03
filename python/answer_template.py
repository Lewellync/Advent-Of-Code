import os, sys

def answer_one(input):
    print("wow!")
    
def answer_two(input):
    print("wow two!")

if __name__ == "__main__":
    input_path = os.path.join(sys.argv[0].removesuffix("answer.py"), "input.txt")
    with open(input_path, 'r') as file:
        input = file.read()
        answer_one(input)
        answer_two(input)