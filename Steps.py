import User_prompts as UP

add_task_steps = {
    "Title_step" : {
        "intro": UP.add_task_step1,
        "title":"title",
        "message":"\033[1m  Input Task Title: \033[0m "
    },
    "Due_date_step" : {
        "intro": UP.add_task_step2,
        "title":"Due_Date",
        "message":"\033[1m Input Task Due Date (MM-DD-YYYY):\033[0m  "
    },
    "Importance_step" : {
        "intro": UP.add_task_step3,
        "title":"Importance",
        "message":"\033[1m Input Task Importance (1-10): \033[0m  "
    },
    "Urgency_step" : {
        "intro": UP.add_task_step4,
        "title":"Urgency",
        "message":"\033[1m Input Task Urgency (1-10): \033[0m "
    },
}


update_task_steps = {
    "Title_step" : {
        "intro": UP.update_task_step1,
        "title":"title",
        "message":"\033[1m  Input Task Title: \033[0m "
    },
    "Due_date_step" : {
        "intro": UP.update_task_step2,
        "title":"Due_Date",
        "message":"\033[1m Input Task Due Date (MM-DD-YYYY):\033[0m  "
    },
    "Importance_step" : {
        "intro": UP.update_task_step3,
        "title":"Importance",
        "message":"\033[1m Input Task Importance (1-10): \033[0m  "
    },
    "Urgency_step" : {
        "intro":UP.update_task_step4,
        "title":"Urgency",
        "message":"\033[1m Input Task Urgency (1-10): \033[0m "
    },
}