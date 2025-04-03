from collections import defaultdict
from itertools import permutations
import os, sys, re



def answer_one(input):
    distance = defaultdict(dict)
    places = set()
    
    for line in re.split(r'\n', input):
        start, _, end, _, dist = line.split(' ')
        if start and end:
            places.add(start)
            places.add(end)
            distance[start][end] = int(dist)
            distance[end][start] = int(dist)
    
    shortest = sys.maxsize
    for items in permutations(places):
        dist = sum(map(lambda x, y: distance[x][y], items[:-1], items[1:]))
        shortest = min(shortest, dist)
    return shortest
    
def answer_two(input):
    distance = defaultdict(dict)
    places = set()
    
    for line in re.split(r'\n', input):
        start, _, end, _, dist = line.split(' ')
        if start and end:
            places.add(start)
            places.add(end)
            distance[start][end] = int(dist)
            distance[end][start] = int(dist)
    
    longest = 0
    for items in permutations(places):
        dist = sum(map(lambda x, y: distance[x][y], items[:-1], items[1:]))
        longest = max(longest, dist)
    return longest

if __name__ == "__main__":
    input_path = os.path.join(sys.argv[0].removesuffix("answer.py"), "input.txt")
    with open(input_path, 'r') as file:
        input = file.read()
        print(answer_one(input))
        print(answer_two(input))