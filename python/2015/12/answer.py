import os, sys, re, json

def part_one(input):
    number_regex = r'(-?\d+)'
    numbers = [int(x) for x in re.findall(number_regex, input)]
    return sum(numbers)
    
def part_two(input):
    structure = json.loads(input)
    return sum_json_no_red(structure)

def sum_json_no_red(input):
    if isinstance(input, int):
        return input
    if isinstance(input, list):
        return sum(sum_json_no_red(x) for x in input)
    if isinstance(input, dict):
        if "red" in input.values():
            return 0
        return sum(sum_json_no_red(x) for x in input.values())
    return 0
    
if __name__ == "__main__":
    input_path = os.path.join(sys.argv[0].removesuffix("answer.py"), "input.txt")
    with open(input_path, 'r') as file:
        input = file.read()
        
        answer_one = part_one(input)
        answer_two = part_two(input)
        
        print(answer_one)
        print(answer_two)