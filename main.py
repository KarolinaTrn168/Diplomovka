import LearningMode.learning_mode as learning_mode
import ExecutingMode.executing_mode as execution_mode
from ExecutingMode.get_values import check_parameter, check_url_scheme
# from SQLdb import fill_db
# from LearningMode.convert_params import convert_values
from LearningMode.prepare_perform_NN import perform_NN_DT
from LearningMode.crawling_endpoints import get_endpoints
from SQLdb.fill_db import fill_db_real
# from create_schema import create_scheme
import webbrowser

def main():

# Menu - choose mode
    print("You now have three options you are able to preceed with.\n\
Type the corresponding number of the you want to continue with.\n\
LEARNING MODE - 1\n\
VALIDATION MODE - 2\n\
WITHOUT ANY MODE - 3")
# Mabybe option Help - explaining the main idea of the modes

    choice = ""
    while choice != "exit":
        choice = input()
# Requesting specific URL
        URL = ""
        print("Enter URL you want to access.")
        URL = input()
# Learning Mode:
        if choice == "1":
            print("Learning mode will be executed.")
            LM_NN = learning_mode.check_scheme_NN(URL)
            LM_DT = learning_mode.check_scheme_DT(URL)
            if LM_NN == True & LM_DT == True:
                print("The Learning mode was performed for both methods (Neural Network and Decision Tree).\n\
You may continue with the Execution mode.")
                break
            algo = learning_mode.select_algorithm()
            if algo == 1:
                print("NN")
                if LM_NN == False:
                    print("Neural Network will be executed.")
                    # crawl and get data
                    get_endpoints(URL)
                    fill_db_real(URL)
                    perform_NN_DT('schema_NN.json')
                if LM_NN == True & LM_DT == False:
                    print("The Learning mode was performed for the Neural Network already.\n\
If you wish to perform the Decision Tree, press 1.\n\
If not, and you wish to go back to the main menu, press anything else.")
                    other = input()
                    if other == 1:
                        print("Decision Tree will be executed.")
                        # crawl and get data
                        get_endpoints(URL)
                        fill_db_real(URL)
                        perform_NN_DT('schema_DT.json')
                    else:
                        break
            elif algo == 2:
                print("DT")
                if LM_DT == False:
                    print("Decision Tree will be executed.")
                    # crawl and get data
                    get_endpoints(URL)
                    fill_db_real(URL)
                    perform_NN_DT('schema_DT.json')
                if LM_NN == False & LM_DT == True:
                    print("The Learning mode was performed for the Decision Tree already.\n\
If you wish to perform the Neural Network, press 1.\n\
If not, and you wish to go back to the main menu, press anything else.")
                    other = input()
                    if other == 1:
                        print("Neural Network will be executed.")
                        # crawl and get data
                        get_endpoints(URL)
                        fill_db_real(URL)
                        perform_NN_DT('schema_NN.json')
                    else:
                        break
            else:
                print("Not valid.")
            break
# Execution Mode:
        elif choice == "2":
            scheme_type = ''
            print("Validation mode will be executed. \
If you want to use the Neural Network, press 1.\n\
If you want to use the Decision Tree, press 2.")
            validation = input()
            if validation == 1:
                scheme_type = 'schema_NN.json'
            else:
                scheme_type = 'schema_DT.json'
            check_url_scheme(URL, scheme_type)
            break
# None:
        elif choice == "3":
            print("The request will be send directly to the server.")
            webbrowser.open(URL)
            break
# Exit and stop the process:
        elif choice == "exit":
            print("The process will be exited.")
            break
# Otherwise:
        else:
            print("The number you have chosen does not match with any mode option. You can try again or quit by writing exit.")

main()
