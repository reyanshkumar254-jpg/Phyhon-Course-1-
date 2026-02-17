def shutdown(user_input="no", apps_closed=False, no_background=False):
   

    user_input = user_input.lower()

    if user_input == "yes":
        if apps_closed and no_background:
            print("All conditions satisfied.")
            print("Shutting down...")
        else:
            print("Cannot shut down.")
            print("Please close all apps and stop background activities.")
    elif user_input == "no":
        print("Abort shut down.")
    else:
        print("Sorry! Invalid input. Please enter yes or no.")
        
        new_input = input("Do you want to shut down the system? (yes/no): ")
        shutdown(new_input, apps_closed, no_background)

choice = input("Do you want to shut down the system? (yes/no): ")
apps = input("Are all apps closed? (yes/no): ")
background = input("Are there no background activities? (yes/no): ")


apps_status = True if apps == "yes" else False
background_status = True if background == "yes" else False

shutdown(choice, apps_status, background_status)