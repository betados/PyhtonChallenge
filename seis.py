# http://www.pythonchallenge.com/pc/def/channel.html
nothing = '90052'
count = 0
# for i in range(99999):
#     try:
#         f = open('text/channel/' + str(i) + '.txt', 'r')
#         for line in f:
#             print(str(i) + ' ' + line)
#         count += 1
#     except Exception as e:
#         # print(e)
#         pass
# print(count)
count = 0
print('FIN')
lastNothing = 0
while True:
    f = open('text/channel/' + nothing + '.txt', 'r')
    for line in f:
        print(line)
        nothing = line.split(' ')[-1]
        if lastNothing == nothing:
            break
        # print(nothing)

    try:
        int(nothing)
        print('Resta ', int(lastNothing) - int(nothing))
        lastNothing = nothing
        count += 1
    except Exception as e:
        print(e)
        print(count)
        """ It may give a text clue about the next nothing,
        then it should be passed by hand, or it could be the final
        solution"""
        nothing = input("next nothing: ")


