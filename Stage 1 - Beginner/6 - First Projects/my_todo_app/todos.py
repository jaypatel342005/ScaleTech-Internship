# Task Schema 
# { 
#     "id" : 1,
#     "title":"Learn Python",
#     "completed":False,
#     "priority": "High"
#     "date" : "DD-MM-YYYY"
# }

import re
from utils import get_menu_choice
tasks = []


def create_task(task):
    # Generate id
    task["id"] = str(len(tasks) + 1) 
    tasks.append(task)
    
def view_tasks():
    
    if not tasks:
        print("\n📭 No tasks available.")
        return
    
    for task in tasks:
        print(f"📌 Task #{task['id']}: {task['title']}")
        print(f"📅 Date:     {task['date']}")
        print(f"🔥 Priority: {task['priority']}")
        print(f"⚡ Status:   {'✅ Done' if task['completed'] == 'true' else '❌ Pending'}")        
        print("-" * 20) 
    
def delete_task(task_id):
    task_to_delete = None
    for task in tasks:
        if task["id"] == task_id:
            task_to_delete = task
            break
    
    if task_to_delete:
        tasks.remove(task_to_delete)
    else:
        print("No tasks exists with Task ID : " , task_id)

def update_task(task_id):
    target_task = None
    for task in tasks:
        if task["id"] == task_id:
            target_task = task
            break
    
    if not target_task:
        print("❌ No task exists with Task ID:", )
        return
    
    # Title
    title = target_task["title"]
    new_title = input(f"Enter title [{title}]: ")
    
    if new_title: 
        target_task["title"] = new_title

    # Status
    status = target_task["completed"]
    
    status_choice = get_menu_choice(
        f"Completed Status [{status}]:", 
        ["True", "False", "Keep Current"]
    )
    if status_choice != "Keep Current":
        target_task["completed"] = status_choice.lower()

    # Priority
    priority = target_task["priority"]
    priority_choice = get_menu_choice(
        f"Select Priority [{priority}]:", 
        ["Low", "Medium", "High", "Keep Current"]
    )
    if priority_choice != "Keep Current":
        target_task["priority"] = priority_choice
             
    # Date
    date = target_task["date"]
    while True:
        date_input = input(f"Enter date (DD-MM-YYYY) [{date}]: ")
        if not date_input:  # Pressed Enter to skip
            break
        if re.match(r"^(0[1-9]|[12][0-9]|3[01])-(0[1-9]|1[0-2])-\d{4}$", date_input):
            target_task["date"] = date_input
            break
        print("!!! Invalid Date Format !!!")
    
        
def input_task_info():
    new_task = {}
    
    while True:
        new_task["title"] = input("Enter title: ")
        if(new_task["title"]):
            break
        
        print("!!! Title is required !!!!")
        
    while True:
            completed = get_menu_choice("Completed Status: " ,["True", "False"]).lower()
            if(completed == "false" or completed == "true" ):
                new_task["completed"] = completed
                break
                
            print("!!! Invalid Status !!!!")
    
    while True:
        print("Select Priority from following options: ")
        print("1. Low")
        print("2. Medium")
        print("3. High")
        option = input("Enter option: ")
        priority = ""
        match option:
            case "1":
                priority = "Low"
            case "2":
                priority = "Medium"
            case "3":
                priority = "High"
            case _:
                print("!!! Invalid option !!!")
        
        new_task["priority"] = priority
        if(priority):
            break
             
    while True:
        date = input("Enter date (DD-MM-YYY): ")
          
        # Validates: Days (01-31), Months (01-12), and Years (4 digits)
        if re.match(r"^(0[1-9]|[12][0-9]|3[01])-(0[1-9]|1[0-2])-\d{4}$", date):
            new_task["date"] = date
            break
          
        print("!!! Invalid Date !!!")
    
    return new_task      
        
        

            
            
            
    