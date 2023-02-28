def removeWhiteSpace(Lines):
    LinesRmvdWhiteSpace = []
    for line in Lines:
      line = line.replace(' ','')
      line = line.replace('\n','')
      LinesRmvdWhiteSpace.append(line)
    return LinesRmvdWhiteSpace


def CalculateAverage(Total,Number):
    Average = Total/Number
    return Average


def ASCIIConversion(Lines):
    Ascii = []
    TotalChar = 0
    AsciiTotal = 0
    for line in Lines:
        for i in line:
                i = ord(i)
                AsciiTotal = AsciiTotal + i
                Ascii.append(i)
                TotalChar = TotalChar + 1
    AsciiAverage = CalculateAverage(AsciiTotal, TotalChar)
    AsciiAverage = round(AsciiAverage,2)
    return Ascii,AsciiAverage


with open('C:/Users/cool dude/PycharmProjects/hello/Coroutines/Data/GM.txt',encoding='utf-8') as f:
    lines = f.readlines()
    lines = removeWhiteSpace(lines)
    Ascii,AsciiAverage = ASCIIConversion(lines)
    print(AsciiAverage)



