import os, re

def answer_one(input):
    cloth_length = 0
    for line  in re.split(r'\n', input):
        l, w, h = [int(x) for x in re.split(r'x', line)]
        len_wid = (l*w*2)
        wid_hei = (w*h*2)
        hei_len = (h*l*2)
        cloth_length += len_wid + wid_hei + hei_len + min([len_wid, wid_hei, hei_len])//2
    print(cloth_length)
    
def answer_two(input):
    print("wow two!")

if __name__ == "__main__":
    with open('input.txt', 'r') as file:
        input = file.read()
        answer_one(input)
        answer_two(input)