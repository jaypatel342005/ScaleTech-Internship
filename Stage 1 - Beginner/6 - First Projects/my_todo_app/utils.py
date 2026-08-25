
def get_menu_choice(msg, options):
    while True:
        print(f"\n{msg}")
        for index, item in enumerate(options, 1):
            print(f"  {index}. {item}")
            
        choice = input("Select an option number: ").strip()
        
        # Check if the input is a valid number within our options range
        if choice.isdigit() and 1 <= int(choice) <= len(options):
            return options[int(choice) - 1] 
            
        print("!!! Invalid selection. Please enter a valid number. !!!")
