from urllib.request import urlopen
import pickle

h = urlopen("http://www.pythonchallenge.com/pc/return/bull.html")
h.read()
data = pickle.load(h)

for line in data:
    print("".join([k * v for k, v in line]))
