from collections import defaultdict
from itertools import permutations
import os, sys, re

def part_one(input):
    friendship = defaultdict(dict)
    for line in (line for line in re.split(r'\n', input) if line):
        first, change, amount, second = re.match(r'(\w+) would (\w+) (\d+) happiness units by sitting next to (\w+)', line).groups()
        if change == 'gain':
            friendship[first][second] = friendship.get(first, {}).get(second, 0) + int(amount)
            friendship[second][first] = friendship.get(second, {}).get(first, 0) + int(amount)
        else:
            friendship[first][second] = friendship.get(first, {}).get(second, 0) - int(amount)
            friendship[second][first] = friendship.get(second, {}).get(first, 0) - int(amount)
        
    people = set(friendship.keys())
    max_happiness = 0
    
    # is there a better way to do this? second brute force solution in 2015
    for arrangement in permutations(people):
        happiness = sum(map(lambda x, y: friendship[x][y], arrangement, arrangement[1:] + tuple([arrangement[0]])))
        max_happiness = max(max_happiness, happiness)
    return max_happiness
    
def part_two(input):
    
    friendship = defaultdict(dict)
    for line in (line for line in re.split(r'\n', input) if line):
        first, change, amount, second = re.match(r'(\w+) would (\w+) (\d+) happiness units by sitting next to (\w+)', line).groups()
        if change == 'gain':
            friendship[first][second] = friendship.get(first, {}).get(second, 0) + int(amount)
            friendship[second][first] = friendship.get(second, {}).get(first, 0) + int(amount)
        else:
            friendship[first][second] = friendship.get(first, {}).get(second, 0) - int(amount)
            friendship[second][first] = friendship.get(second, {}).get(first, 0) - int(amount)
    people = set(friendship.keys())
    
    people.add('Me')
    for person in people:
        friendship['Me'][person] = 0
        friendship[person]['Me'] = 0
        
    max_happiness = 0
    
    for arrangement in permutations(people):
        happiness = sum(map(lambda x, y: friendship[x][y], arrangement, arrangement[1:] + tuple([arrangement[0]])))
        max_happiness = max(max_happiness, happiness)
    return max_happiness

if __name__ == "__main__":
    input_path = os.path.join(sys.argv[0].removesuffix("answer.py"), "input.txt")
    with open(input_path, 'r') as file:
        input = file.read()
        
        answer_one = part_one(input)
        answer_two = part_two(input)
        
        print(answer_one)
        print(answer_two)