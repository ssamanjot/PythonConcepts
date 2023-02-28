Number =13195
MaxPrimeNumber=2

while Number%2==0:
    Number = Number//2
    MaxPrimeNumber = 2

for j in range(3,(Number)+1,2):
    if Number%j==0:
        Number = Number//j
        if MaxPrimeNumber<j:
            MaxPrimeNumber=j
print('Largest prime factor is ',MaxPrimeNumber)