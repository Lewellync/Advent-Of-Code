
with open('day3.txt', 'r') as input:
    course = []
    for line in input:
        course.append([x for x in line.strip()])
    tree = 0
    counter = 0
    for line in course[::2]:
        if line[counter] is '#':
            tree += 1
        counter = (counter + 1) % 31
    print(tree)