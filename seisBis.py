import re, zipfile

fileExtension = '.txt'
firstFileName = '90052'
digis = "\d+"
commentList = []

channelZipfile = zipfile.ZipFile("channel.zip")

with open(('text/channel/' + firstFileName + fileExtension), 'r') as f:
    data = f.read()
    print(data)
f.close()
finding = re.search(digis, data)
commentList.append(channelZipfile.getinfo(('text/channel/' + firstFileName + fileExtension)).comment)
try:
    while finding.group(0):
        nothingValue = finding.group(0)
        #In text file is like "Next nothing is ***", name the variable nothingValue
        commentList.append(channelZipfile.getinfo((nothingValue + fileExtension)).comment)
        with open((nothingValue + fileExtension), 'r') as f:
            data = f.read()
            print(data)
        f.close()
        finding = re.search(digis, data)
except AttributeError:
    pass
print(''.join(commentList))
