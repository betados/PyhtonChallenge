string = "g fmnc wms bgblr rpylqjyrc gr zw fylb. " \
         "rfyrq ufyr amknsrcpq ypc dmp. " \
         "bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle." \
         " sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj. "
def decode(string):
    stringOut = ''
    for code in string.encode('ascii'):
        if code not in [32, 46, 39, 40, 41]:
            # print(code, chr(code))
            code += 2
            if code > 122:
                code -= (123-97)
        stringOut += chr(code)
    return stringOut

print(decode(string))
print("New url: ", decode('map'))
