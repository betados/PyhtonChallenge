import urllib.request

nothing = '12345'
while True:
    with urllib.request.urlopen('http://www.pythonchallenge.com/'
                                'pc/def/linkedlist.php?nothing='
                                        + nothing) as response:
        html = response.read().decode("utf-8")
        nothing = html.split(' ')[-1]
        print(html)
        try:
            int(nothing)
        except:
            """ It may give a text clue about the next nothing,
            then it should be passed by hand, or it could be the final
            solution"""
            nothing = input("next nothing: ")