
def print_tool_id(SE_ID):
    print("\033[32m{}".format("[ID ГОТОВ]: ")+"\033[0m{}".format("Осталось только скопировать:"))
    print("\n#######################################################\n\n\n\n\n\n")
    print("     "+SE_ID+"    ")
    print("\n\n\n\n\n\n#######################################################\n")
    input("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Нажмите <enter> чтобы продолжить..."))

# Вернет False если ввод не коррктный и True если всё ОК:
def checkin_for_bool_and_spaces(line):
        line = line.replace(" ", "")
        if len(line) == 0:
                print("\033[31m{}".format("[ERROR]: ")+"\033[0m{}".format("Пробелы и пустые строки не допустимы!"))
                input("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Нажмите <enter> чтобы продолжить..."))
                return False

        if line.isdigit() == False:
                print("\033[31m{}".format("[ERROR]: ")+"\033[0m{}".format("Допускаются лишь 1 или 0, текст и прч не допустимо!"))
                input("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Нажмите <enter> чтобы продолжить..."))
                return False
        else:
                flag = 0
                if line != "0":
                        flag += 1
                if line != "1":
                        flag += 1
                if flag == 2:
                        print("\033[31m{}".format("[ERROR]: ")+"\033[0m{}".format("Допускаются лишь 1 или 0, текст и прч не допустимо!"))
                        input("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Нажмите <enter> чтобы продолжить..."))
                        return False

        return True





def id_compile():

        while True:
                name = input("\n[Укажите имя для системы]:\n-> ")
                name = name.replace(" ", "-")
                if name != "":
                    break

        network_interface = input("\n[Есть ли доступ в интернет]:\n-> ")
        if checkin_for_bool_and_spaces(network_interface) == False:
                return
        
        if network_interface == "1":
                remote_access = "1"
                # input("Есть ли удаленный доступ:\n-> ")
                print("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Удаленный доступ активирован!"))
        else:
                remote_access = "0"
                print("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Удаленный доступ не будет активен!"))

        operation_system = "1"
        # input("\n[Есть ли ОС]:\n-> ")
        #if checkin_for_bool_and_spaces(operation_system) == False:
        #        return
        print("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Без ОС не выйдет подключиться к системе, следовательно, она установлена как 1!"))

        possibility_of_flashing = input("\n[Есть ли возможность прошивки]:\n-> ")
        if checkin_for_bool_and_spaces(possibility_of_flashing) == False:
                return
        
        artificial_intelligence = input("\n[Есть ли AI]:\n-> ")
        if checkin_for_bool_and_spaces(artificial_intelligence) == False:
                return
        
        connection_port = input("\n[Есть ли физические порты доступа]:\n-> ")
        if checkin_for_bool_and_spaces(connection_port) == False:
                return
        
        if network_interface == "1":
                user_interface = "1"
                # input("Есть ли UI(нужен для удаленного доступа):\n-> ")
                print("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Интерфейс удаленного доступа доступен!"))
        else:
                user_interface = "0"
                print("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Интерфейс удаленного доступа не будет доступен!"))

        if connection_port == "1":
                control_panel = "1"
                # input("Есть ли панель управления(нужна для физического доступа):\n-> ")
                print("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Порты физического доступа доступны!"))
        else:
                control_panel = "0"
                print("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Порты физического доступа не будут доступны!"))
                
        write = input("\n[Есть ли доступ на запись]:\n-> ")
        if checkin_for_bool_and_spaces(write) == False:
                return
        
        read = input("\n[Есть ли доступ на чтение]:\n-> ")
        if checkin_for_bool_and_spaces(read) == False:
                return
        
                
        i = 0
        access_algorithm_dict = ""
        while True:
                print("\n#######################################################\n")
                print("\033[33m{}".format("[WARNING]: ")+"\033[0m{}".format("Нет смысла добавлять более 1го объекта, т.к отобразиться лишь первая!"))
                print("[Уже добавлено]: "+str(i))
                print("--------------------------------")
                print("0. Готово")
                print("\n#######################################################\n")
                
                res = input("Цели с доступом к системе:\n-> ")
                if res == "0":
                        access_algorithm_dict = access_algorithm_dict[:-1] # удаляем лишнию ;
                        break
                access_algorithm_dict += res + ";"
                i += 1
        i = 0
        storage = ""
        while True:
                print("\n#######################################################\n")
                print("Добавьте награду в хранилище:")
                print("Уже добавлено: "+str(i))
                print("0. Готово")
                print("\n#######################################################\n")
                
                res = input("Добавьте tool_id:\n-> ")
                if res == "0":
                        storage = storage[:-1] # удаляем лишнию ;
                        break
                storage += res + ";"
                i += 1

        SE_ID = (name+"_"+
                 "NI="+network_interface+"_"+
                 "RA="+remote_access+"_"+
                 "OS="+operation_system+"_"+
                 "PoF="+possibility_of_flashing+"_"+
                 "AI="+artificial_intelligence+"_"+
                 "CP="+connection_port+"_"+
                 "UI="+user_interface+"_"+
                 "CP2="+control_panel+"_"+
                 "W="+write+"_"+
                 "R="+read+"+"+
                 "S;"+storage+"+"+
                 "AAD;"+access_algorithm_dict)

        print_tool_id(SE_ID)


def menu():
    while True:
        print("\n#######################################################\n")
        print("\033[32m{}".format("[MAIN MENU]:")+"\033[0m{}".format(" Выберите один из пунктов:\n"))
        print("[1]: Создать SE_ID.")
        print("[0]: Выход.")
        print("\n#######################################################\n")

        command = input(":~> ")

        if command == "1":
            id_compile()
        if command == "0":
            return