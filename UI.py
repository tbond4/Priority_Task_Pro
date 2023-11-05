import inquirer
import csv

def main():
    print('''
    \033[1m Welcome to Priority Task Pro! \033[0m


    We will ask you a few questions while you insert tasks to better understand the importance and urgency.
    If a task due date changes, no worries, you can always change your answers and update any task you have 
    already entered. Use the Navigation menu below using the arrows keys on your keyboard, 
    when the option you want is highlighted, press enter to select.
    ''')
    print(
        '''
        ---------------------------------------------------------
        \033[1m New Feature \033[0m
        Its all new but this is where I would tell you about it!
        ---------------------------------------------------------
        '''
    )
    navigation()

 
def navigation():   

    options = [inquirer.List( 
        "main_nav",
        message=" \033[1m Select Action: \033[0m ",
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
    print("\033[1m Task List \033[0m")

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
    \033[1m  Add Task \033[0m 

    Step 1/4

    Please enter the title of your task, this will act as a short description of
    the task, ex. Laundry, Assignment 6, Wash Car, ect... Write out your title
    and press enter to move on to the next step.
    ''')
    task_prompt = [inquirer.Text("title", message="\033[1m  Input Task Title: \033[0m ")]
    task_title = inquirer.prompt(task_prompt)["title"]
    task.append(task_title)

    #Step 2 Due_Date
    print('''
    033[1m  Add Task \033[0m 

    Step 2/4

    Please enter the Due Date of you task. When does this task
    need to be completed by?
    ''')
    task_prompt = [inquirer.Text("Due_Date", message="\033[1m Input Task Due Date (MM-DD-YYY):\033[0m  ")]
    task_Due_Date = inquirer.prompt(task_prompt)["Due_Date"]
    task.append(task_Due_Date)

    #Step 3 Urgency
    print('''
    033[1m  Add Task \033[0m 

    Step 3/4

    Please enter the importance of this task
    on a scale of 1-10. 1 being not important 
    and 10 being of the highest importance.
    Enter the value and press enter.
    ''')
    task_prompt = [inquirer.Text("Importance", message="\033[1m Input Task Importance (1-10): \033[0m  ")]
    task_Importance = inquirer.prompt(task_prompt)["Importance"]
    task.append(task_Importance)


    #Step 4 Urgency
    print('''
    A033[1m  Add Task \033[0m 

    Step 4/4

    Please enter the Urgency of your task from 1-10.
    1 being not urgent and 10 being the highest urgency.
    Input value and press Enter.
    ''')
    task_prompt = [inquirer.Text("Urgency", message="\033[1m Input Task Urgency (1-10): \033[0m ")]
    task_Urgency = inquirer.prompt(task_prompt)["Urgency"]
    task.append(task_Urgency)

    #Add Task
    header = ['title', 'due_date','importance','urgency','priority']
    with open('csvfile.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow(task)
    
    #Add Task Nav
    print('''
    \033[1m Task Added! \033[0m 

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
        message="\033[1m Select Action: \033[0m ",
        choices = tasks
        )]

    user_choice = inquirer.prompt(options)['complete_task']
    tasks.remove(user_choice)
   
    with open('csvfile.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerows(tasks)

    #Task Completed
    print('''
    \033[1m Task Completed! \033[0m 

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
        message="\033[1m  Select Action: \033[0m ",
        choices = tasks
        )]

    user_choice = inquirer.prompt(options)['update_task']

    #Edit
    #Step 1 Title
    print('''
    \033[1m Update Task \033[0m 

    Step 1/4

    Your current task title is pre-filled in for you
    press enter to leave it the same or change it 
    and press enter to save and move to the next step.
    ''')
    task_prompt = [inquirer.Text("title", default = user_choice[0], message="\033[1m Input Task Title: \033[0m  ")]
    task_title = inquirer.prompt(task_prompt)["title"]
    user_choice[0] = task_title

    #Step 2 Due_Date
    print('''
    \033[1m Update Task \033[0m 

    Step 2/4

    Your current task Due Date is pre-filled in for you
    press enter to leave it the same or change it 
    and press enter to save and move to the next step.  
    ''')
    task_prompt = [inquirer.Text("Due_Date", default = user_choice[1], message="\033[1m Input Task Due Date (MM-DD-YYY): \033[0m")]
    task_Due_Date = inquirer.prompt(task_prompt)["Due_Date"]
    user_choice[1] = task_Due_Date

    #Step 3 Urgency
    print('''
    \033[1m Update Task \033[0m 

    Step 3/4

    Your current task importnace is pre-filled in for you
    press enter to leave it the same or change it 
    and press enter to save and move to the next step.
    ''')
    task_prompt = [inquirer.Text("Importance",default = user_choice[2], message="\033[1m Input Task Importance (1-10): \033[0m")]
    task_Importance = inquirer.prompt(task_prompt)["Importance"]
    user_choice[2] = task_Importance


    #Step 4 Urgency
    print('''
    \033[1m Update Task \033[0m 

    Step 4/4

    Your current task Urgeency is pre-filled in for you
    press enter to leave it the same or change it 
    and press enter to save and move to the next step.
    ''')
    task_prompt = [inquirer.Text("Urgency",default = user_choice[3], message="\033[1m Input Task Urgency (1-10): \033[0m ")]
    task_Urgency = inquirer.prompt(task_prompt)["Urgency"]
    user_choice[3] = task_Urgency

    #Add Task
    header = ['title', 'due_date','importance','urgency','priority']
    with open('csvfile.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow(task)
    
    #Add Task Nav
    print('''
    \033[1m Task Added! \033[0m

    Your task was updated successfully, use the arrow
    keys to select your next action.
    ''')

    with open('csvfile.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerows(tasks)

    navigation()



if __name__ == "__main__":
    main()
