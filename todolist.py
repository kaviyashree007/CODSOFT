tasks = []

def add_task():
    task = input("Enter a new task : ")
    tasks.append(task)
    print(" Your Task has been added successfully. ")

def view_task():
    if len(tasks) == 0:
        print(" No tasks available. ")
    else:
        print('Your tasks : ')
        for i, task in enumerate(tasks):
            print(f'{i+1}. {task}')  

def delete_task():
    if len(tasks) == 0:
        print(' There are no tasks available to delete.')
    else:
        print(' Availabe tasks are : ')
        for i, task in enumerate(tasks):
            print(f'{i+1}. {tasks}')
        choice = int(input(" Enter the task Number to delete : "))

        if 0 < choice <= len(tasks):
            del tasks[choice-1]
            print(' The selected task has been successfully deleted.')
        else:
            print('Your choice is invalid. please choose a correct number of task.')

def main():
    while True:
        print('\n##### Your To Do list :) #####')
        print("1. Add Your Task")
        print("2. View the exsiting tasks")
        print("3. Delete a task")
        print("4. Quit")

        choice = int(input("Enter your choice : "))
        if choice == 1:
            add_task()
        elif choice == 2:
            view_task()
        elif choice == 3:
            delete_task()
        elif choice == 4:
            print(" Thank you for using To Do list. Visit again :)")
            break
        else:
            print(" Your choice is invalid. Please try again and choose a valid choice.")


if __name__ == "__main__":
    main()