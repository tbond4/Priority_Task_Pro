import inquirer

def main():
    print('''
    Welcome to Priority Task Pro!


    We will ask you a few questions while you insert tasks to better understand the importance and urgency.
    If a task due date changes, no worries, you can always change your answers and update any task you have 
    already entered. Use the Navigation menu below using the arrows keys on your keyboard, 
    when the option you want is highlighted, press enter to select.
    ''')
    navigation()

tasks =[]
    
def navigation():    
   
    options = [inquirer.List( 
        "main_nav",
        message="Select Action:",
        choices=["View Tasks", "Add Task", "Complete Task", "Update Task", "Exit"])]


    user_choice = inquirer.prompt(options)

    if user_choice == "View Tasks":
        view_tasks()
    elif user_choice == "Add Task":
        add_task()
    elif user_choice == "Complete Task":
        complete_task()
    elif user_choice == "Update Task":
        update_task()
    elif user_choice == "Exit":
        user_exit()
    else:
        print("Please make a selection")

def view_tasks():
    for task in tasks:
        print(task)
    navigation()

def add_task():
    tasks.append("1") 
    navigation()

def user_exit():
    print("Exiting Program, your tasks are awaiting!")
    exit(1)

def complete_task():
    print("complete")
    navigation()

def update_task():
    print("update")
    navigation()

if __name__ == "__main__":
    main()
