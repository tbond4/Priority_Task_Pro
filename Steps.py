add_task_steps = {
    "Title_step" : {
        "intro": '''
                \033[1m Add Task \033[0m 

                Step 1/4

                Please enter the title of your task, this will act as a short description of
                the task, ex. Laundry, Assignment 6, Wash Car, ect... Write out your title
                and press enter to move on to the next step.
                ''',
        "title":"title",
        "message":"\033[1m  Input Task Title: \033[0m "
    },
    "Due_date_step" : {
        "intro": '''
                \033[1m Add Task \033[0m 

                Step 2/4

                Please enter the Due Date of you task. When does this task
                need to be completed by?
                ''',
        "title":"Due_Date",
        "message":"\033[1m Input Task Due Date (MM-DD-YYYY):\033[0m  "
    },
    "Importance_step" : {
        "intro": '''
                \033[1m Add Task \033[0m 

                Step 3/4

                Please enter the importance of this task
                on a scale of 1-10. 1 being not important 
                and 10 being of the highest importance.
                Enter the value and press enter.
                ''',
        "title":"Importance",
        "message":"\033[1m Input Task Importance (1-10): \033[0m  "
    },
    "Urgency_step" : {
        "intro":'''
                \A033[1m Add Task \033[0m 

                Step 4/4

                Please enter the Urgency of your task from 1-10.
                1 being not urgent and 10 being the highest urgency.
                Input value and press Enter.
                ''',
        "title":"Urgency",
        "message":"\033[1m Input Task Urgency (1-10): \033[0m "
    },
}
