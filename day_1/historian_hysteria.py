left = []
right = []

with open("historian_hysteria_data") as f:
    # data = f.read()
    for line in f:
        # Split each line into left and right values and convert to integers
        columns = line.split()
        if len(columns) == 2:  # Ensure the line contains two columns
            left.append(int(columns[0]))
            right.append(int(columns[1]))

left.sort()
right.sort()

# total = 0
# for l, r in zip(left, right):
#     total += abs(l - r)


count = 0
total = 0
for l_num in left:
    for r_num in right:
        if l_num == r_num:
            count += 1
    total += l_num * count
    count = 0

print(total)