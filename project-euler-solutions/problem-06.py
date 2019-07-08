total, square_sum = 0, 0

for i in range(1, 101):
    square_sum += i * i
    total += i

print(total * total - square_sum)
