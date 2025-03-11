import os, sys, re

def answer_one(input):
    code = 0
    memory = 0
    for line in re.split(r'\n', input):
        code += len(line)
        line_in_memory = re.sub(r'(^\")|(\"$)', '', line) # remove beginning and end quotes
        line_in_memory = re.sub(r'(\\\")|(\\\\)|(\\x[\da-f]{2})', '1', line_in_memory) # replace escaped characters with '1', which is the length of whatever expanded version they would be
        memory += len(line_in_memory)
    return code - memory
    
def answer_two(input):
    encode_map = {'"':'\\"', '\\':'\\\\'}
    code = 0
    encode = 0
    for line in re.split(r'\n', input):
        code += len(line)
        encoded_line = '"' + ''.join([encode_map[char] if char in encode_map else char for char in line]) + '"'
        print(line)
        print(encoded_line)
        encode += len(encoded_line)
    return encode - code

if __name__ == "__main__":
    input_path = os.path.join(sys.argv[0].removesuffix("answer.py"), "input.txt")
    with open(input_path, 'r') as file:
        input = file.read()
        print(answer_one(input))
        print(answer_two(input))