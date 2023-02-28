def ASCIIConversion():
    try:
        AsciiTotal = 0
        TotalChar = 0
        Ascii = []
        while True:
            line = (yield)
            for i in line:
                i = ord(i)
                AsciiTotal = AsciiTotal + i
                Ascii.append(i)
                TotalChar = TotalChar + 1
    except GeneratorExit:
       print("Average ascii value:" + str(round((AsciiTotal / TotalChar),2)))


with open('C:/Users/cool dude/PycharmProjects/hello/Coroutines/Data/GM.txt',encoding='utf-8') as f:
    lines = f.readlines()
    coroutine = ASCIIConversion()
    next(coroutine)
    for line in lines:
        line = line.replace(' ', '')
        line = line.replace('\n', '')
        coroutine.send(line)
    coroutine.close()



