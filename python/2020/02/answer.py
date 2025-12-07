import re

#Part1
with open('day2.txt', 'r') as input:
    valid_one = 0
    valid_two = 0
    for line in input:
        lower, upper, letter, password = re.findall('\d+(?=-)|(?<=-)\d+|\w(?=:)|\w+', line)
        if int(lower) <= password.count(letter) <= int(upper):
            valid_one += 1
        if (password[int(lower)-1] is letter) != (password[int(upper)-1] is letter):
            valid_two += 1
    print(valid_one)
    print(valid_two)