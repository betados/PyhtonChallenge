# SOLUTION: integrity

from PIL import Image


im = Image.open("text/oxygen.jpg")
im.getdata()
pix = im.load()
width = im.size[0]
print(im.getbands())
last = None
chars = []
for i in range(width-6):
    now = pix[i, 0][0]
    if now != last:
        print(now)
        chars.append(chr(now))
        last = now
string = ''.join(chars)
print(string)
lista = string.split('is [')[-1][:-1].split(', ')
lista2 = [chr(int(a)) for a in lista]
print(lista2)
print(''.join(lista2))

