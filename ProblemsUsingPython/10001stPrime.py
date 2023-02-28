def PrimeNumbers():

    n=1000000000
    Primes=[]
    Flag=1

    for j in range(1,n+1):

        if (j <= 1):
            continue

        for i in range(2, j//2+1):

            if (j % i == 0):
                Flag=0
                continue

        if Flag==1 :
            Primes.append(j)

        Flag=1

        if len(Primes)>=10001:
            return Primes


Primes=PrimeNumbers()
print('10001st prime number: ',Primes[10000])