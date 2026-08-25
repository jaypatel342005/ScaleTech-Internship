import os
import json
from todos import tasks
from utils import get_menu_choice


data_folder = "data"
file_path = f"{data_folder}/tasks.json"

def check_data_dir():
    if("data" not in os.listdir()):
        os.mkdir("data")
        
def confirm_file_overwrite():
    if(os.path.exists(file_path)):
            if(os.path.getsize(file_path) > 0):
                action = get_menu_choice("File already has data, do you want to overwrite it?", ["Yes", "No"])
                if action == "Yes":
                    print("Overwriting file...")
                    return "overwrite"
                else:
                    print("Operation cancelled.")
                    return "append"
                
    return "overwrite"

def save_tasks():
    check_data_dir()
    
    if(confirm_file_overwrite() == "overwrite"):
        with open(file_path,"w") as file:
            json.dump(tasks,file,indent=4)
    else:
        try:
            with open(file_path,"r") as file:
             data = json.load(file)
        except:
            data = []
            
            data.extend(tasks)
            
            with open(file_path,"w") as file:
                json.dump(data,file,indent=4)
                
                
def load_tasks():
    global tasks
    try:
        with open(file_path,"r") as file:
            tasks[:] = json.load(file) # Modifies the list in-place
            return tasks
    except:
        print("Error loading file")
            
            
                       
