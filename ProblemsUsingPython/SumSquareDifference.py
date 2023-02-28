def CalculateSumSquare(n):
    SumofSquares=0
    SumofNum=0
    for i in range(1,n+1):
        SumofSquares=SumofSquares+i**2
        SumofNum=SumofNum+i
    SquareofSum=SumofNum**2
    Difference = SumSquareDifference(SumofSquares,SquareofSum)
    return Difference

def SumSquareDifference(SumofSquares,SquareofSum):
    Difference=SquareofSum-SumofSquares
    return Difference

Difference=CalculateSumSquare(100)
print(Difference)