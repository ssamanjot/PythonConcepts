def ProductOfTwoNumber():

    Palindromes=[]

    for i in range(100,1000):
        for j in range(100,1000):

            Numb= i * j
            Num=str(Numb)
            #print(i, '***', j,'=',Num)
            if Num==Num[::-1]:
                Palindromes.append(Numb)

    print(Palindromes)
    MaxPalindrome=max(Palindromes)


    print('Largest Palindrome of Product of two digit numbers:',MaxPalindrome)

ProductOfTwoNumber()