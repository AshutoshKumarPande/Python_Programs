# Program Created by:- Ashutosh Kumar Pandey
# Program created on:- 5th November, 2022

def compute(string):
    obj = dict()
    for i in string:
        if i in obj:
            obj[i]+=1
        else:
            obj[i]=1
    return obj
def displayFrequency(obj):
    for i in obj:
        print(f"Frequency of {i} is : {obj[i]}")
if __name__ == '__main__':
    string = str(input("Enter something : "))
    obj = compute(string)
    displayFrequency(obj)
