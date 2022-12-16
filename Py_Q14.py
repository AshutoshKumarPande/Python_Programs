# Program Created by:- Ashutosh Kumar Pandey
# Program created on:- 15th November, 2022

def readData(read, write, char):
    fread = open(read, 'rt')
    fwrite = open(write, 'at')
    i = 1
    temp = ""
    for x in fread:
        temp += x
        if i%2 != 0:
            fwrite.write(x)
        i += 1
    print("Given character appeared", temp.count(char), "times.")
    fread.close()
    fwrite.close()
readData("Q2.txt", "copy_Q2.txt", "a")
