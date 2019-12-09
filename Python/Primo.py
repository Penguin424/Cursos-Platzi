nums = []

for i in range(2, 101):
    for x in range(3, i):
        if i % x != 0:
            continue
        else:
            break
    else:
        nums.append(i)

for i in nums:
    print(i)