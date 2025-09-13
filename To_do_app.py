
# Porject 6 To do App 

tasks= []  #empty 
print("Welcome to the program....")

total_task = int(input("Enter how many task you wanted to add:")) #user se input le liya
for i in range(1, total_task+1):   #total task se ek jyada becoz 1 se start kiya hai
        task_name = input("Enter the task name")
         #append methos se user jo bhi task dalega use add karwa denge tasks varaiable mai  
        tasks.append(task_name)       
print(f"today's tasks are {tasks}")

while True:
        operation = int(input("Enter \n1-Add\n2-Update\n3-Delete\n4-View\n5-Exit"))
        if operation == 1:
                add = input("Enter the task you wanted to add")
                tasks.append(add)
                print(f"Your task '{add}' has been added successfully...")

        elif operation== 2:
                updated_val= input("Enter task name you wanted to update")
                if updated_val in tasks:
                    up = input("Enter updated  Tasks = ")
                    ind = tasks.index(updated_val)
                    tasks[ind] = up 
                    print(f"updated task '{up}'")
        elif operation == 3:
                del_val = input("Bhai Apko kya delete karna hai batao jaldi")
                if del_val in tasks:
                    ind = tasks.index(del_val)
                    del tasks[ind]
                    print(f"Task '{del_val}' has been deleted")
        elif operation == 4:
                print(f"Total Number of tasks is '{tasks}'")
        elif operation== 5: 
                print("Close the Program....")
                break
        else:
                print("Invalid Input")
tasks()


