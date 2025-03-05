import os, sys
import pprint
import re

def answer_one(input):
    lights = [[-1]*1000 for i in range(1000)]
    for line in re.split(r'\n', input):
        
        command, start_x, start_y, end_x, end_y = re.match(
            r"^([^\d]+)\s(\d+),(\d+)[^\d]*(\d+),(\d+)$", line).groups()
                
        for x in range(int(start_x), int(end_x)+1):
            for y in range(int(start_y), int(end_y)+1):
                match command:
                    case "turn on":
                        lights[y][x] = 1
                    case "turn off":
                        lights[y][x] = -1
                    case "toggle":
                        lights[y][x] = lights[y][x]*-1
                        
    print(sum([sum([y for y in lights[x] if y == 1]) for x in range(1000)]))
        
def answer_two(input):
    lights = [[0]*1000 for i in range(1000)]
    for line in re.split(r'\n', input):
        
        command, start_x, start_y, end_x, end_y = re.match(
            r"^([^\d]+)\s(\d+),(\d+)[^\d]*(\d+),(\d+)$", line).groups()
                
        for x in range(int(start_x), int(end_x)+1):
            for y in range(int(start_y), int(end_y)+1):
                match command:
                    case "turn on":
                        lights[y][x] += 1
                    case "turn off":
                        if lights[y][x] > 0:
                            lights[y][x] -= 1
                    case "toggle":
                        lights[y][x] += 2
                        
    print(sum([sum(lights[x]) for x in range(1000)]))

if __name__ == "__main__":
    input_path = os.path.join(sys.argv[0].removesuffix("answer.py"), "input.txt")
    with open(input_path, 'r') as file:
        input = file.read()
        answer_one(input)
        answer_two(input)