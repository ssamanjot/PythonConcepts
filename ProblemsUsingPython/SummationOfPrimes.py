def isPrime(n):
    PrimeFlag=1

    if n <= 1:
        PrimeFlag=0

    for i in range(2, n//2+1):
        if n % i == 0:
            PrimeFlag=0


    return PrimeFlag


def SumOfPrime(n):

    PrimeSum=0
    for i in range(2, n):
        PrimeFlag= isPrime(i)
        if PrimeFlag==1:
            PrimeSum=PrimeSum+i
            print(i)
    return PrimeSum

PrimeSum=SumOfPrime(2000000)
print('Aman',PrimeSum)