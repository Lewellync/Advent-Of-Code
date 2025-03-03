import os, sys

def answer_one(input):
    map = {}
    coords = [0,0]
    map[(0, 0)] = 1
    for char in input:
        if char == ">":
            coords[0] += 1
        if char == "<":
            coords[0] -= 1
        if char == "^":
            coords[1] += 1
        if char == "v":
            coords[1] -= 1
        
        if (coords[0], coords[1]) in map:
            map[(coords[0], coords[1])] += 1
        else:
            map[(coords[0], coords[1])] = 1
            
    print(len(map))
    
def answer_two(input):
    map = {}
    santa_coords = [0,0]
    robo_coords = [0,0]
    map[(0, 0)] = 1
    for char in input[::2]:
        if char == ">":
            santa_coords[0] += 1
        if char == "<":
            santa_coords[0] -= 1
        if char == "^":
            santa_coords[1] += 1
        if char == "v":
            santa_coords[1] -= 1
        
        if (santa_coords[0], santa_coords[1]) not in map:
            map[(santa_coords[0], santa_coords[1])] = 1
            
    for char in input[1::2]:
        if char == ">":
            robo_coords[0] += 1
        if char == "<":
            robo_coords[0] -= 1
        if char == "^":
            robo_coords[1] += 1
        if char == "v":
            robo_coords[1] -= 1
            
        if (robo_coords[0], robo_coords[1]) not in map:
            map[(robo_coords[0], robo_coords[1])] = 1
            
    print(len(map))

if __name__ == "__main__":
    input_path = os.path.join(sys.argv[0].removesuffix("answer.py"), "input.txt")
    with open(input_path, 'r') as file:
        input = file.read()
        answer_one(input)
        answer_two(input)