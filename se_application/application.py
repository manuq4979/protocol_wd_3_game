applications_list = [] # [[name, app_address], ...]

def get_applications_and_print():
    size = len(applications_list)
    for i in range(size):
        app = applications_list[i]
        print("["+str(i)+"]: "+ app[0]+".")

def check_input(input_text):
    if input_text.isdigit() == False:
        print("\033[31m{}".format("[ERROR]: ")+"\033[0m{}".format("Допустимы лишь числовые значения!"))
        input("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Нажмите <enter> чтобы продолжить..."))

        return False

def application_menu():
    print("\n#######################################################\n")
    print("Menu: ----------------------")
    get_applications_and_print()
    print("[0]: Выход."])
    print("\n#######################################################\n")
    
    index = input("APP-MENU:~# ")
    if index == "0":
        return
    
    
    index = int(index) - 1
    applications_list[index][1]()