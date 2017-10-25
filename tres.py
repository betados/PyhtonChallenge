import re
f = open('text/tres.txt', 'r')
out = ''
for line in f:
    for i in range(len(line)):
        p = re.match('[a-z][A-Z][A-Z][A-Z][a-z][A-Z][A-Z][A-Z][a-z]', line[i:i+9])
        if p:
            out += p.group()[4]
print(out)
