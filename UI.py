import inquirer
import csv
import time
import Steps
import User_prompts as UP
import constants

def main():
    """Introduce program and start Navigation"""
    print(UP.startup)
    print(UP.new_feature_box)
    navigation()

 
def navigation():   
    """Prompt user with list of actions"""
    options = [inquirer.List( 
        "main_nav",
        message=" \033[1m Select Action: \033[0m ",
        choices=["View Tasks", "Add Task", "Complete Task", "Update Task", "Delete Task", "Exit"])]

    user_choice = inquirer.prompt(options)['main_nav']

    if user_choice == "View Tasks":
        view_tasks()
    elif user_choice == "Add Task":
        add_task()
    elif user_choice == "Complete Task":
        complete_task()
    elif user_choice == "Update Task":
        update_task()
    elif user_choice == "Delete Task":
        delete_task()
    elif user_choice == "Exit":
        user_exit()
    else:
        print("Please make a selection")

def open_and_read(file):
    tasks =[]
    with open(file, 'r') as f:
        csv_reader = csv.reader(f)
        for task in csv_reader:
            tasks.append(task)
    return(tasks)

def open_and_write(file,list):
    with open(file, 'w') as f:
        writer = csv.writer(f)
        writer.writerows(list)

def prioritize_tasks(tasks):
    """Use Microservice to get priority scores in oreded list"""
    # Send Task List
    with open('../CS-361-Task-List-Microservice/tasks.txt','w') as f:
        for line in tasks:
            writer = csv.writer(f)
            writer.writerow(line)

    # Read priority
    time.sleep(1)
    return(open_and_read(constants.MICROSERVICEFILE))


def view_tasks():
    """Display current Priortized Task List"""

    print(UP.view_task_title)
    tasks = tasks = open_and_read(constants.TASKSCSV)
    title = ["Priority score", "Task"]

    print("Prioritizing in progress...")
    prioritized_tasks = prioritize_tasks(tasks)
    print(*title, sep=', ')

    for task in prioritized_tasks:
        print(*task, sep=', ')

    navigation()


def add_task():
    """Get user input to add a task to the list"""
    tasks = open_and_read(constants.TASKSCSV)
    task =[]
    # Get User input
    Step_dict = Steps.add_task_steps

    for step in Step_dict:
        print(Step_dict[step]["intro"])
        task_prompt = [inquirer.Text(Step_dict[step]["title"], message=Step_dict[step]["message"])]
        task_data= inquirer.prompt(task_prompt)[Step_dict[step]["title"]]
        task.append(task_data)

    #Add Task
    tasks.append(task)
    open_and_write(constants.TASKSCSV, tasks)

    print(UP.task_added)
    navigation()


def user_exit():
    """Exit program"""
    print(UP.exit_program)
    exit(0)


def complete_task():
    """Removes Task from List"""
    tasks = open_and_read(constants.TASKSCSV)
    tasks.append("CANCEL")

    #View Tasks Nav
    options = [inquirer.List( 
        "complete_task",
        message="\033[1m Select Action: \033[0m ",
        choices = tasks
        )]

    user_choice = inquirer.prompt(options)['complete_task']

    if user_choice == "CANCEL":
        navigation()
    else:
        tasks.remove(user_choice)
        tasks.remove("CANCEL")

    open_and_write(constants.TASKSCSV, tasks)

    #Task Completed
    print(UP.task_completed)
    navigation()


def delete_task():
    """Removes Task from List"""
    tasks = tasks = open_and_read(constants.TASKSCSV)
    tasks.append("CANCEL")

    #View Tasks Nav
    options = [inquirer.List( 
        "delete_task",
        message="\033[1m Select Action: \033[0m ",
        choices = tasks
        )]

    user_choice = inquirer.prompt(options)['delete_task']

    if user_choice == "CANCEL":
        navigation()
    else:
        tasks.remove(user_choice)
        tasks.remove("CANCEL")

    open_and_write(constants.TASKSCSV, tasks)

    #Task Completed
    print(UP.task_deleted)
    navigation()


def update_task():

    tasks = open_and_read(constants.TASKSCSV)
    tasks.append("CANCEL")
    
    #Update Tasks Nav
    options = [inquirer.List( 
        "update_task",
        message="\033[1m  Select Action: \033[0m ",
        choices = tasks
        )]

    user_choice = inquirer.prompt(options)['update_task']
    if user_choice == "CANCEL":
        navigation()

    tasks.remove("CANCEL")

    Step_dict = Steps.update_task_steps
    i = 0
    for step in Step_dict:
        print(Step_dict[step]["intro"])
        task_prompt = [inquirer.Text(Step_dict[step]["title"],default = user_choice[i], message=Step_dict[step]["message"])]
        task_data= inquirer.prompt(task_prompt)[Step_dict[step]["title"]]
        user_choice[i] = task_data
        i+=1
    print(UP.task_updated)
    open_and_write(constants.TASKSCSV, tasks)
    navigation()
    # Update Task
    #with open('tasks.csv', 'a') as f:
       ## writer = csv.writer(f)
       # writer.writerow(task)

if __name__ == "__main__":
    main()
