def FibonacciNumbers(Limit):

    a=1
    b=1

    for i in range(2,Limit):

        Sum=a+b

        if len(str(Sum))==1000:
            print(len(str(Sum)))
            Index=i
            ThousandDigitFibNum=Sum
            break

        a=b
        b=Sum

    return ThousandDigitFibNum,Index


ThousandDigitNumber,index=FibonacciNumbers(1000000)
print('First Three Digit Number : '+str(ThousandDigitNumber))
print('Index of 1000 digit Fibonacci Number is ',str(index))