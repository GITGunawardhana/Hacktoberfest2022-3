nterms = 10
fiblist=[]
n1, n2 = 0, 1
count = 0

if nterms <= 0:
    pass
elif nterms == 1:
   fiblist.append(n1)
else:
   while count < nterms:
       fiblist.append(n1)
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1

lower_value = 0
upper_value = 24 
  
primelist=[]
for number in range (lower_value, upper_value + 1):  
    if number > 1:  
        for i in range (2, number):  
            if (number % i) == 0:  
                break  
        else:  
            primelist.append(number)


def printNumber(lst, index):
    print(str(lst[index]) + " ", end="")

for i in range(len(primelist)+1):
    printNumber(fiblist, i)
    if len(primelist)!=i:
        printNumber(primelist, i)
