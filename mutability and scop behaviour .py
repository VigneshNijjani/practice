# Objective: Demonstrate mutability and scope behavior.

# Input: 
# List and tuple

# Expected Output:
# ● List modification reflected
# ● Tuple unchanged
# ● Slicing results


# while True:
#     print("1.create list")
#     print("2.create tuple")
#     print("3.exit")
#     choice=int(input("enter your choice : "))

#     if choice==1:
#         l_name=input("enter your list name : ")
#         data=list(map(int,input("enter the elements seperated with spaces : ").split()))
#         print(l_name,"=",data)
#         while True:
#             print("1.add elements to list")
#             print("2.remove elements from list")
#             print("3.exit")
#             choice=int(input("enter your choice : "))
#             if choice==1:
#                 add=list(map(int,input("enter the elements seperated with spaces : ").split()))
#                 data.extend(add)
#                 print(data)
#             elif choice==2:
#                 print(data)
#                 rem=int(input("enter element to delete : "))
#                 if rem in data:
#                     data.remove(rem)
#                     print(data)
#                 else:
#                     print("element doent exist")
#             elif choice==3:
#                 break
#             else:
#                 print("invalid choice ")

#     elif choice==2:
#         t_name=input("enter your tuple name : ")
#         data=tuple(map(int,input("enter the elements seperated with spaces : ").split()))
#         print(t_name,"=",data)
#         while True:
#             print("1.add elements to tuple")
#             print("2.remove elements from tuple")
#             print("3.exit")
#             choice=int(input("enter your choice : "))
#             if choice==1:
#                 print("tuple is immutable so cannot modify")
#             elif choice==2:
#                 print("tuple is immutable so cannot modify ")
#             elif choice==3:
#                 break
#             else:
#                 print("invalid option")
#     elif choice==3:
#         break
#     else:
#         print("invalid choice")


