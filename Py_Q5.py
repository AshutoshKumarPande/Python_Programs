# Program Created by:- Ashutosh Kumar Pandey
# Program created on:- 5th November, 2022

def factorial(n):
    if(n==1 or n==0):
        return 1
    else:
        return n*factorial(n-1)

def sumofser(n,x):
    i =0
    j=1
    sum = 0
    while(j<=n):
        sum += ((-1)**(j-1))*(x**i)/factorial(i)
        j += 1
        i += 2
    print(sum)

k = sumofser(2,2)
print(k)
