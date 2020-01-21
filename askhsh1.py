import re
file = open("C:\\Users\\Axilleas\\Desktop\\pythonas\\ask1.txt","r").read()
words = file.split()
sortedwords = sorted(words, key=len)  
reversed_prwth = sortedwords[-1][::-1]
reversed_defterh = sortedwords[-2][::-1]
reversed_trith = sortedwords[-3][::-1]
reversed_tetarth = sortedwords[-4][::-1]
reversed_pemth = sortedwords[-5][::-1]
print("1st: %s." % (re.sub("a|e|i|o|u|y", "", reversed_prwth)),"\n2nd: %s." % (re.sub("a|e|i|o|u|y", "", reversed_defterh)),"\n3rd: %s." % (re.sub("a|e|i|o|u|y", "", reversed_trith)),"\n4th: %s." % (re.sub("a|e|i|o|u|y", "", reversed_tetarth)),"\n5th: %s." % (re.sub("a|e|i|o|u|y", "", reversed_pemth)))
