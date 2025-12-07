nums = [int(num) for num in [line.strip() for line in open('day1.txt','r') if line.strip()]]

#Part 1
for num in nums:
    if (2020-num) in nums:
        print(num*(2020-num))

#Part 2
for x in nums:
    for y in nums:
        if (2020-x-y) in nums:
            print(x*y*(2020-x-y))