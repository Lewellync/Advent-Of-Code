import os

def answer_one(input):
    print("wow!")
    
def answer_two(input):
    print("wow two!")

if __name__ == "__main__":
    with open('input.txt', 'r') as file:
        input = file.read()
        answer_one(input)
        answer_two(input)