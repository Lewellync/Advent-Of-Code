import os

def answer_one(input):
    floor = 0
    for char in input:
        floor = floor + 1 if char is '(' else floor - 1
    print(floor)
        
    
def answer_two(input):
    floor = 0
    pos = 0
    for char in input:
        floor = floor + 1 if char is '(' else floor - 1
        pos += 1
        if floor < 0:
            break
    print(pos)
    
if __name__ == "__main__":
    with open('input.txt', 'r') as file:
        input = file.read()
        answer_one(input)
        answer_two(input)