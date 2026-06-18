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

def time_log(func):
        def wrap(*args,**kwargs):
            start=time.perf_counter()
            result=func(*args,**kwargs)
            end=time.perf_counter()
            print("time taken",end-start)
            return result
        return wrap
        
file=input("enter file name u want to see :")
while True:
    print("-------------------------------------------------------------------------")
    print("1.view file data")
    print("2.view file data line by line")
    print("3.view file data i.e : line count")
    print("4.view file data i.e: word count")
    print("5.exit")
    print("-------------------------------------------------------------------------\n")
    

    choice=int(input("enter your choice : "))

    if choice==1:
        @time_log
        def open_file():
           
            try:
                with open(file,"r") as f:
                    data=f.read()
                    print(data)

            except FileNotFoundError:
                print("file doest not exist")
            
        open_file()

    elif choice==2:
        @time_log
        def line_by_line():
           
            try:
                def line():
                    with open(file,"r") as f:
                        for line in f:
                            yield line.strip()
                d=line()

            except FileNotFoundError:
                print("file doest not exist")

            while True:
                print("1.next line")
                print("2.exit")
                choice=int(input("enter your choice : "))

                if choice==1:
                    try:
                        print(next(d))

                    except StopIteration:
                        print("data file is completed")    

                elif choice==2:
                    break

                else:
                    print("invalid choice")
            

        line_by_line()


    elif choice==3:
        @time_log
        def no_Of_lines():
           
            try:
                with open(file,"r") as f:
                    line_count=len([line for line in f])
                    print(line_count)

            except FileNotFoundError:
                print("file doest not exist")
            

        no_Of_lines()

    elif choice==4:
        @time_log
        def no_of_words():
            
            try:
                with open(file,"r") as f:
                    word_count=sum([len(line.split())for line in f])
                    print(word_count)
            except FileNotFoundError:
                print("file doest not exist")
           

        no_of_words()
       
    elif choice==5:
        break
    else:
        print("invalid choice selected")


    