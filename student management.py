# Objective: Build a program to store and manage student academic data.
# Input:
# ● Student name
# ● Roll number
# ● List of subjects (may contain duplicates)
# ● Marks for each subject
# Expected Output:
# ● Student details printed clearly
# ● Duplicate subjects removed
# ● Subjects mapped with marks

# Mandatory Requirements:
# ● Use list, set, and dictionary
# ● Follow PEP 8 naming conventions

students_data=[]
while True:
    
    print("=============================================================================================================================")
    print()
    print('1.add student')
    print('2.view')
    print('3.exit')
    print()
    print("=============================================================================================================================")
    
    choice=int(input('enter your choice :'))
    
    if choice==1:
        
        sub=[]
        mark={}
        
        name=input("enter your name: ")
        roll_number=int(input("enter your roll number :"))
        no_of_sub=int(input("enter no of subjects :"))
        
        for i in range(no_of_sub):
            subject=input("enter subject name :")
            marks=int(input("enter marks of subject :"))
            sub.append(subject)
            mark[subject]=marks
            unq_sub=list(set(sub))

            student={
                "name":name,
                "roll_number":roll_number,
                "subjects":unq_sub,
                "marks":mark
            }
            
        students_data.append(student)
    
    elif choice==2:
        for data in students_data:
            for field,value in data.items():
                print(f'{field} : {value}')
   
    elif choice==3:
        break
    
    else:
        print("invalid option entered")






