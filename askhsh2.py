import re
file = open("C:\\Users\\Axilleas\\Desktop\\pythonas\\ask1.txt","r").read()
words = file.split()
count = len(words)
for i in range(0,count):
    if ("f" in words[i]or"c" in words[i]or"k" in words[i]or"r" in words[i]):
        if(len(re.sub("a|e|i|o|u|y|f|c|k|r", "", words[i])) < (len(re.sub("a|e|i|o|u|y", "", words[i]))-len(re.sub("a|e|i|o|u|y|f|c|k|r", "", words[i])))):
            print("kakia lexh %s." % words[i])
            continue
    else:
        print("kalh lexh %s."%words[i])
