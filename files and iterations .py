# Objective: Analyze a text file efficiently.
# Input: Text file
# Expected Output:
# ● Line count
# ● Word count
# Mandatory Requirements:
# ● Use generator for file reading
# ● Use list comprehension
# ● Use decorator to log execution time
import time
file=input("enter file name u want to see :")
while True:
    print("1.view file data")
    print("2.view file data line by line")
    print("3.view file data i.e : line count")
    print("4.view file data i.e: word count")
    print("5.exit")
    
    
    

    choice=int(input("enter your choice : "))

    if choice==1:
        try:
            with open(file,"r") as f:
                data=f.read()
                print(data)
        except FileNotFoundError:
            print("file doest not exist")
    elif choice==2:
        try:
            with open(file,"r") as f:
                for line in f:
                    print(line.strip())
        except FileNotFoundError:
            print("file doest not exist")
    elif choice==3:
        try:
            with open(file,"r") as f:
                line_count=0
                for line in f:
                    a=line.strip()
                    line_count+=1
                print(line_count)
        except FileNotFoundError:
            print("file doest not exist")
    elif choice==4:
        try:
            with open(file,"r") as f:
                word_count=0
                for word in f:
                    word_count+=len(word.split())
                print(word_count)
        except FileNotFoundError:
            print("file doest not exist")
    elif choice==5:
        break
    else:
        print("invalid choice selected")
