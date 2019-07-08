terms = [1,2]
sum = 0

while terms[-1] <= 4000000:
    n = terms[-1] + terms[-2]
    terms.append(n)

for i in range(len(terms)-1):
    if terms[i] % 2 == 0:
        sum += terms[i]

print(sum)
