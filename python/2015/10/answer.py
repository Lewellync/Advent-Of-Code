import os, sys, re

def answer_one(input):
    regex = r'(1+|2+|3+|4+|5+|6+|7+|8+|9+|0+)'
    
    for x in range(40):
        components = [block for block in re.findall(regex, input)]
        input = ''.join([f'{len(x)}{x[0]}' for x in components])
    return len(input)
    
def answer_two(input):
    regex = r'(1+|2+|3+|4+|5+|6+|7+|8+|9+|0+)'
    
    for x in range(50):
        components = [block for block in re.findall(regex, input)]
        input = ''.join([f'{len(x)}{x[0]}' for x in components])
    return len(input)

if __name__ == "__main__":
    input_path = os.path.join(sys.argv[0].removesuffix("answer.py"), "input.txt")
    with open(input_path, 'r') as file:
        input = file.read()
        print(answer_one(input))
        print(answer_two(input))