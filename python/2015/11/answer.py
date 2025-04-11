import os, sys

def answer_one(input):
    invalid = True
    
    upper = ord('z')
    lower = ord('a')
    invalid_chars = [ord('i'), ord('o'), ord('l')]
    unicode_array = [ord(x) for x in input]
    
    while invalid:
        invalid = False
        
        # Increment
        if unicode_array is [upper] * len(unicode_array):
            unicode_array = [lower] * len(unicode_array)
            invalid = True
            continue
        
        for ind in reversed(range(len(unicode_array))):
            if unicode_array[ind] == upper:
                unicode_array[ind] = lower
            else:
                unicode_array[ind] += 1
                break
        
        # Check validity
        pairs = []
        sequence = False
        for ind, char in enumerate(unicode_array):
            if ind+1 < len(unicode_array) and ind not in pairs:
                if unicode_array[ind] == unicode_array[ind+1]:
                    pairs += [ind, ind+1]
                    
            if ind+2 < len(unicode_array) and not sequence:
                if unicode_array[ind]+1 == unicode_array[ind+1] and unicode_array[ind+1] + 1 == unicode_array[ind+2]:
                    sequence = True
                    
        if len(pairs) != 4 or (set(invalid_chars) & set(unicode_array)) or not sequence:
            invalid = True        
         
    return ''.join([chr(x) for x in unicode_array])

if __name__ == "__main__":
    input_path = os.path.join(sys.argv[0].removesuffix("answer.py"), "input.txt")
    with open(input_path, 'r') as file:
        input = file.read()
        first_part = answer_one(input)
        print(first_part)
        second_part = answer_one(first_part)
        print(second_part)