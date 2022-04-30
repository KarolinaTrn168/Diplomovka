import LearningMode.learning_mode as learning_mode
import ExecutingMode.executing_mode as execution_mode

# from SQLdb import fill_db
# from LearningMode.convert_params import convert_values
from LearningMode.prepare_perform_NN import perform_NN
# from create_schema import create_scheme

# Menu - choose mode
print("You now have three options you are able to preceed with.\nType the corresponding number you want to be performed.\nLEARNING MODE - 1\nVALIDATION MODE - 2\nWITHOUT ANY MODE - 3")
# Mabybe option Help - explaining the main idea of the modes

choice = ""

while choice != "exit":
    choice = input()
    # Learning Mode:
    if choice == "1":
        print("Learning mode will be executed.")
        # Beginning with crawling
        # learning_mode.crawling()

        # Fill DB, Convert values, create scheme, prepare for NN
        # fill_db()
        perform_NN()
        

        break
    # Execution Mode:
    elif choice == "2":
        print("Validation mode will be executed.")
        execution_mode.executing()
        break
    # None:
    elif choice == "3":
        print("The request will be send directly to the server.")
        break
    # Exit and stop the process:
    elif choice == "exit":
        print("The process will be exited.")
        break
    # Otherwise:
    else:
        print("The number you have chosen does not match with any mode option. You can try again or quit by writing exit.")