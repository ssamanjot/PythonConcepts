def CheckPythagoreanTriplet(a,b,c):
    flag=0

    if (a**2)+(b**2)==c**2:
        flag=1

    return flag

def PythagorTriplet(Sum):

    for i in range(1,Sum):

        for j in range(i+1,Sum):

            c=Sum-(i+j)
            flag=CheckPythagoreanTriplet(i,j,c)

            if flag ==1:

                if i+j+c==1000:

                    print(i*j*c)
                    break


PythagorTriplet(1000)