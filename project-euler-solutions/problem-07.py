# modified from https://hackernoon.com/prime-numbers-using-python-824ff4b3ea19

primes = []
possiblePrime = 2

while len(primes) < 10002:
    isPrime = True
    for num in range(2, int(possiblePrime ** 0.5) + 1):
        if possiblePrime % num == 0:
            isPrime = False
            break
    if isPrime:
        primes.append(possiblePrime)
        
    possiblePrime += 1

print(primes[10000])
