f = open('text/dos.txt', 'r')
charList = []
for line in f:
    for code in line.encode('ascii'):
        if 96 < code < 123:
            # print(code, chr(code))
            charList.append(chr(code))
print(''.join(charList))
