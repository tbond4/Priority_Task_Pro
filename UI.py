import inquirer
import csv

def main():
    print('''
    Welcome to Priority Task Pro!


    We will ask you a few questions while you insert tasks to better understand the importance and urgency.
    If a task due date changes, no worries, you can always change your answers and update any task you have 
    already entered. Use the Navigation menu below using the arrows keys on your keyboard, 
    when the option you want is highlighted, press enter to select.
    ''')
    navigation()

 
def navigation():   

    options = [inquirer.List( 
        "main_nav",
        message="Select Action:",
        choices=["View Tasks", "Add Task", "Complete Task", "Update Task", "Exit"])]

    user_choice = inquirer.prompt(options)['main_nav']

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
    print("Task List")

    #Read CSV
    with open('csvfile.csv', 'r') as f:
        csv_reader = csv.reader(f)
        for line in csv_reader:
            print(line)

    navigation()


def add_task():
    """"""
    task =[]
    #Step 1 Title
    print('''
    Add Task

    Step 1/4

    Please enter the title of your task, this will act as a short description of
    the task, ex. Laundry, Assignment 6, Wash Car, ect... Write out your title
    and press enter to move on to the next step.
    ''')
    task_prompt = [inquirer.Text("title", message="Input Task Title: ")]
    task_title = inquirer.prompt(task_prompt)["title"]
    task.append(task_title)

    #Step 2 Due_Date
    print('''
    Add Task

    Step 2/4

    Please enter the Due Date of you task. When does this task
    need to be completed by?
    ''')
    task_prompt = [inquirer.Text("Due_Date", message="Input Task Due Date (MM-DD-YYY): ")]
    task_Due_Date = inquirer.prompt(task_prompt)["Due_Date"]
    task.append(task_Due_Date)

    #Step 3 Urgency
    print('''
    Add Task

    Step 3/4

    Please enter the importance of this task
    on a scale of 1-10. 1 being not important 
    and 10 being of the highest importance.
    Enter the value and press enter.
    ''')
    task_prompt = [inquirer.Text("Importance", message="Input Task Importance (1-10): ")]
    task_Importance = inquirer.prompt(task_prompt)["Importance"]
    task.append(task_Importance)


    #Step 4 Urgency
    print('''
    Add Task

    Step 4/4

    Please enter the Urgency of your task from 1-10.
    1 being not urgent and 10 being the highest urgency.
    Input value and press Enter.
    ''')
    task_prompt = [inquirer.Text("Urgency", message="Input Task Urgency (1-10): ")]
    task_Urgency = inquirer.prompt(task_prompt)["Urgency"]
    task.append(task_Urgency)

    #Add Task
    header = ['title', 'due_date','importance','urgency','priority']
    with open('csvfile.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow(task)
    
    #Add Task Nav
    print('''
    Task Added!

    Your task was added successfully, use the arrow
    keys to select your next action.
    ''')
    navigation()




def user_exit():
    print("Exiting Program, your tasks are awaiting!")
    exit(0)

def complete_task():
    tasks =[]
    #Read CSV
    with open('csvfile.csv', 'r') as f:
        csv_reader = csv.reader(f)
        for task in csv_reader:
            tasks.append(task)

    #View Tasks Nav
    options = [inquirer.List( 
        "complete_task",
        message="Select Action:",
        choices = tasks
        )]

    user_choice = inquirer.prompt(options)['complete_task']
    tasks.remove(user_choice)
   
    with open('csvfile.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerows(tasks)

    #Task Completed
    print('''
    Task Completed!

    Your task was completed successfully, use the arrow
    keys to select your next action.    
    ''')
    navigation()

def update_task():
    tasks =[]
    #Read CSV
    with open('csvfile.csv', 'r') as f:
        csv_reader = csv.reader(f)
        for task in csv_reader:
            tasks.append(task)

    #Update Tasks Nav
    options = [inquirer.List( 
        "update_task",
        message="Select Action:",
        choices = tasks
        )]

    user_choice = inquirer.prompt(options)['update_task']

    #Edit
    #Step 1 Title
    print('''
    Update Task

    Step 1/4

    Your current task title is pre-filled in for you
    press enter to leave it the same or change it 
    and press enter to save and move to the next step.
    ''')
    task_prompt = [inquirer.Text("title", default = user_choice[0], message="Input Task Title: ")]
    task_title = inquirer.prompt(task_prompt)["title"]
    user_choice[0] = task_title

    #Step 2 Due_Date
    print('''
    Add Task

    Step 2/4

    Your current task Due Date is pre-filled in for you
    press enter to leave it the same or change it 
    and press enter to save and move to the next step.  
    ''')
    task_prompt = [inquirer.Text("Due_Date", default = user_choice[1], message="Input Task Due Date (MM-DD-YYY): ")]
    task_Due_Date = inquirer.prompt(task_prompt)["Due_Date"]
    user_choice[1] = task_Due_Date

    #Step 3 Urgency
    print('''
    Add Task

    Step 3/4

    Your current task importnace is pre-filled in for you
    press enter to leave it the same or change it 
    and press enter to save and move to the next step.
    ''')
    task_prompt = [inquirer.Text("Importance",default = user_choice[2], message="Input Task Importance (1-10): ")]
    task_Importance = inquirer.prompt(task_prompt)["Importance"]
    user_choice[2] = task_Importance


    #Step 4 Urgency
    print('''
    Add Task

    Step 4/4

    Your current task Urgeency is pre-filled in for you
    press enter to leave it the same or change it 
    and press enter to save and move to the next step.
    ''')
    task_prompt = [inquirer.Text("Urgency",default = user_choice[3], message="Input Task Urgency (1-10): ")]
    task_Urgency = inquirer.prompt(task_prompt)["Urgency"]
    user_choice[3] = task_Urgency

    #Add Task
    header = ['title', 'due_date','importance','urgency','priority']
    with open('csvfile.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow(task)
    
    #Add Task Nav
    print('''
    Task Added!

    Your task was updated successfully, use the arrow
    keys to select your next action.
    ''')

    with open('csvfile.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerows(tasks)

    navigation()



if __name__ == "__main__":
    main()
