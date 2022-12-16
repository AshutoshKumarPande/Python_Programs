# Program Created by:- Ashutosh Kumar Pandey
# Program created on:- 15th November, 2022

import matplotlib.pyplot as plt
lis=[]
N = int(input("Enter the number of elements of list:"))
for i in range(0,N,1):
    lis.append(input())
plt.hist(lis,lis,histtype='bar',rwidth=0.2)
plt.xlabel('X Axis')
plt.ylabel("Y Axis")
plt.title("User Entered Data")
plt.legend
plt.show()
