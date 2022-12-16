# Program Created by:- Ashutosh Kumar Pandey
# Program created on:- 5th November, 2022.

def digits(n):
    list = []
    while(n>0):
        digit=n%10
        list.append(digit)
        n=n//10
    return set(list)
n = int(input("Enter a number : "))
nls = digits(n)
print(nls)
print("The digits of number as a set")
for x in nls:
    print(x,end=" ")
