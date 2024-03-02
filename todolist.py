
todolist=[]

def addlist():
    item=input("Enter your task: ")
    todolist.append(item)
    print(f"{item} added to the todolist")

def displaylist():
    print('------------')
    print("To do list")
    print('------------')
    for index , item in enumerate(todolist,start=1):
        print(f"{index}-{item}")

def removeList():
    displaylist()
    index=int(input("Enter your item number to remove: "))-1
    if 0<=index<len(todolist):
        removed_item=todolist.pop(index)
        print(f"{removed_item} removed from the list")
    else:
        print("invalid input")

while True :
    print("########")
    print("To Do List")
    print("########")
    print("1-Add to list")
    print("2-Display list")
    print("3-Remove list")
    print("4-Exit")
    option=int(input("Enter your option: "))
    if option==1:
        addlist()
    elif option==2:
        displaylist()
    elif option==3:
        removeList()
    elif option==4:
        print('Exit')
        break
    else:
        print('Invalid option')


        '''For example, if the user wants to remove the first item from the list, 
        they would enter "1". However, since lists are zero-indexed, 
        we subtract 1 to get the index 0, which corresponds to the first item in the list. 
        Similarly, if the user wants to remove the second item, they would enter "2",
         and subtracting 1 gives us the index 1, which corresponds to the second item in the list. 
         This adjustment ensures that we're accessing the correct 
         item in the list based on the user's input.'''





'''