pal = 0
pair = []

for a in range(100, 1000):
    for b in range(100, 1000):
        if str(a * b) == str(a * b)[::-1] and a * b > pal:
            pal = a * b
            pair.clear()
            pair.append(a)
            pair.append(b)

print(pal)
print(pair)
