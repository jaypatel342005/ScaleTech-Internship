from todos import *
from file_manager import save_tasks, load_tasks

if __name__ == "__main__" :

    while True:
        print("="*20)
        print("Todos Management System")
        print("="*20)
        
        print("1. 👀  View all tasks")
        print("2. ✏️  Update task")
        print("3. ➕  Create task")
        print("4. 🗑️  Delete task") 
        print("5. 💾  Save tasks") 
        print("6. 📂  Load tasks")
        print("7. 🚪  Exit")                        
        selected_option = input("Enter operation to perform: ")

        match selected_option:
            case "1":
                view_tasks()
            case "2":
                task_id = input("Enter task id to task to edit: ")
                update_task(task_id)
                print("\n --- Task Updated Successfully --- \n")
            case "3":
                task = input_task_info()
                create_task(task)
                print("\n --- Task Created Successfully --- \n")
            case "4":
                task_id = input("Enter task id to task to delete: ")
                delete_task(task_id)
                print("\n --- Task Deleted Successfully --- \n")
            case "5":
                save_tasks()
                print("\n --- Task Saved Successfully --- \n")
            case "6":
                load_tasks()
                print("\n --- Task Loaded Successfully --- \n")
            case "7":
                print("\n --- Exiting.... --- \n")
                 
            case _:
                print("Invalid Operation")
            
            
            
        

    





