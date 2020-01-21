arithm = int (input("Dwse arithmo\n"))
num = 0
k = 0
while(True):
    num=0
    arithm = arithm*3 +1
    number_string = str(arithm)
    for j in range(0,len(number_string)):
        num = num + int(number_string[j])
    k=k+1
    if(len(str(num))==1):
        break
    else:
        arithm=num
print("Xriastike na trexei %d fores" %k)
