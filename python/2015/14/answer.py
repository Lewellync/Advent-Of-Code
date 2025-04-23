import os, sys

def part_one(input):
    return 1
    
def part_two(input):
    return 2

if __name__ == "__main__":
    input_path = os.path.join(sys.argv[0].removesuffix("answer.py"), "input.txt")
    with open(input_path, 'r') as file:
        input = file.read()
        
        answer_one = part_one(input)
        answer_two = part_two(input)
        
        print(answer_one)
        print(answer_two)