# Objective: Read files safely with proper error handling.
# Input: File name
# Expected Output: File contents or user-friendly error message
# Mandatory Requirements:
# ● Use with statement
# ● Handle FileNotFoundError
# ● Use finally
while True:
    print("1.create file")
    print("2.read file")
    print("3.write into particular file")
    print("4.exit")
    choice=int(input("enyer your choice : "))
    if choice==1:
        file=input("enter file name you want to create: ")
        try:
            with open(file,"x"):
                print("file created sucessfully")
        except FileExistsError:
            print("file already exist")
        
    elif choice==2:
        file=input("enter file name u want to read : ")
        try:
            with open(file,"r") as f:
                
                data=f.read()
            print(data)
        except FileNotFoundError:
            print("file does not exist")
        finally:
            print("read operation performed")
   

    elif choice==3:
        file=input("enter file name you want to write into :")
        try:
            data=input("enter the data u want to add into file : ")
            with open(file,"r+") as f:
                f.seek(0, 2)
                f.write(data)
        except FileNotFoundError:
            print("file does not exist")

    elif choice==4:
        break
    else:
        print("invalid option selected")
