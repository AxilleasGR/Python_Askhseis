s = 'Python'
k=0
for c in s:
        k = k+ ord(c)
if k > 1:
   for i in range(2,k):
       if (k % i) == 0:
           print(k,"is not a prime number")
           print(i,"times",k//i,"is",k)
           break
   else:
       print(k,"is a prime number")
else:
   print(k,"is not a prime number")
