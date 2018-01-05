

import os
import sys
import pygame
import zlib




un = 'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
pw = 'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'
print(un)
print(pw)
lista = [ord(char) for char in un]
lista.pop(22)
lista.pop(22)
lista2 = [ord(char) for char in pw]

puntos1 = [(lista[i], lista2[i]) for i in range(len(lista2))]
print(puntos1)

# print(lista)

print(lista2)
for i, char in enumerate(lista):
    print(char, end='\t')
print()
for i, char in enumerate(lista2):
    print(char, end='\t')
print()
# print(''.join([chr(code) for code in lista if 128 > code > 13]))
# print(''.join([chr(code) for code in lista2 if 128 > code > 10]))
# print(''.join([chr(code) for i, code in enumerate(lista) if code == lista2[i]]))
coor = [179, 284, 214, 311, 255, 320, 281, 226, 319, 224, 363, 309, 339, 222, 371, 225, 411, 229, 404, 242, 415,
        252, 428, 233, 428, 214, 394, 207, 383, 205, 390, 195, 423, 192, 439, 193, 442, 209, 440, 215, 450, 221,
        457, 226, 469, 202, 475, 187, 494, 188, 494, 169, 498, 147, 491, 121, 477, 136, 481, 96, 471, 94, 458, 98,
        444, 91, 420, 87, 405, 92, 391, 88, 376, 82, 350, 79, 330, 82, 314, 85, 305, 90, 299, 96, 290, 103, 276,
        110, 262, 114, 225, 123, 212, 125, 185, 133, 138, 144, 118, 160, 97, 168, 87, 176, 110, 180, 145, 176,
        153, 176, 150, 182, 137, 190, 126, 194, 121, 198, 126, 203, 151, 205, 160, 195, 168, 217, 169, 234, 170, 260,
        174, 282]
puntos = [(coor[i], coor[i+1]) for i in range(0, len(coor)-1, 2)]
#
# print(puntos)


# print(un)
# for i in range(len(un)):
#     print(un[:i])
#
# for i in range(len(pw)):
#     print(pw[:i])
def deflate(data, compresslevel=9):
    compress = zlib.compressobj(
            compresslevel,        # level: 0-9
            zlib.DEFLATED,        # method: must be DEFLATED
            16 + zlib.MAX_WBITS,  # window size in bits:
                                  #   -15..-8: negate, suppress header
                                  #   8..15: normal
                                  #   16..30: subtract 16, gzip header
            zlib.DEF_MEM_LEVEL,   # mem level: 1..8/9
            0                     # strategy:
                                  #   0 = Z_DEFAULT_STRATEGY
                                  #   1 = Z_FILTERED
                                  #   2 = Z_HUFFMAN_ONLY
                                  #   3 = Z_RLE
                                  #   4 = Z_FIXED
    )
    deflated = compress.compress(data)
    deflated += compress.flush()
    return deflated

def inflate(data):
    decompress = zlib.decompressobj(16 + zlib.MAX_WBITS)  # see above)
    inflated = decompress.decompress(data)
    inflated += decompress.flush()
    return inflated

print(deflate(str.encode(un)))
try:
    print(deflate(str.encode(un)).decode('windows-1252'))
except Exception as e:
    print(e)
print(deflate(str.encode(pw)))
try:
    print(deflate(str.encode(pw)).decode('cp437'))
except Exception as e:
    print(e)

# if sys.platform == 'win32' or sys.platform == 'win64':
#     os.environ['SDL_VIDEO_CENTERED'] = '1'
# resolution = (800, 600)
# pygame.display.set_caption('challenge')
# screen = pygame.display.set_mode(resolution)
# pygame.init()
# reloj = pygame.time.Clock()

# while True:
#
#     screen.fill((0, 0, 0))
#     image = pygame.image.load('text/mosca.jpg')
#     screen.blit(image, (0, 0))
#     pygame.draw.lines(screen, (255, 255, 255), True, puntos, 1)
#     pygame.draw.lines(screen, (255, 10, 255), False, puntos1, 1)
#
#     # --- Avanzamos y actualizamos la pantalla con lo que hemos dibujado.
#     pygame.display.flip()
#
#     # --- Limitamos a 60 fotogramas por segundo (frames per second)
#     reloj.tick(100)


pygame.quit()
