# Program Created by:- Ashutosh Kumar Pandey
# Program created on:- 15th November, 2022

class Student:
    max=0
    def __init__(self,nam:str,mark:list):
        self.name=nam
        self.marks=mark
        sum=0
        for i in self.marks:
            sum+=i
        sum=sum/len(self.marks)
        if(sum>=Student.max):
            Student.max=sum
    def maxavgmarks():
        print("Maximum average marks are: \
              "+str(Student.max))
    def __del__(self):
        del self.name
        del self.marks
        del self
        print("Object is deleted")
        

n=int(input("Enter the number of student: "))
stob=[]
for i in range(n):
    stob.append(0)
for i in range(n):
    print("Enter the name of "+str(i+1)+" Student: ",end="" )
    name=input()
    l=[]
    for j in range(3):
        print("Enter the marks in ",j+1," subject: ",end="")
        x=int(input())
        l.append(x)
    stob[i]=Student(name,l)
Student.maxavgmarks()
