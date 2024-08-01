def print_warning():
    print("\n")
    print("\033[33m{}".format("[WARNING]: ")+"\033[0m{}".format("Если вы отказываетесь от заполнения, то просто прожмите <enter>!"))
    print("           В имени вмесо пробелов необходимо использовать ТИРЕ!")
    print("           Поля НАИМЕНОВАНИЕ не может быть пустым!")
    print("\n")

def print_tool_id(tool_id):
    print("\033[32m{}".format("[ID ГОТОВ]: ")+"\033[0m{}".format("Осталось только скопировать:"))
    print("\n#######################################################\n\n\n\n\n\n")
    print("     "+tool_id+"    ")
    print("\n\n\n\n\n\n#######################################################\n")
    input("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Нажмите <enter> чтобы продолжить..."))

# Вернет False если ввод не коррктный и True если всё ОК:
def checkin_for_int_and_spaces(line):
    line = line.replace(" ", "")
    if len(line) == 0:
        print("\033[31m{}".format("[ERROR]: ")+"\033[0m{}".format("Пробелы и пустые строки не допустимы!"))
        input("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Нажмите <enter> чтобы продолжить..."))
        return False

    if line.isdigit() == False:
        print("\033[31m{}".format("[ERROR]: ")+"\033[0m{}".format("Допускаются лишь числа и цифры, текст и прч не допустимо!"))
        input("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Нажмите <enter> чтобы продолжить..."))
        return False


def sort_array_tool(array_tool):
    new_array_tool = []
    for tool in array_tool:
        if tool[1] != "":
            new_array_tool.append(tool)
    return new_array_tool

# simple tool_id == [['name', 'gun'], ['damage', '100'], ['charge', '0']]
def compile_tool(array_tool, recharge=False):
    name = array_tool[0][1]
    string_tool = name+"_"
    array_tool.pop(0)
    for char in array_tool:
        if recharge == True:
            string_tool += str(char[0])+":"+str(char[1])+"_"
        else:
            string_tool += str(char[0])+"="+str(char[1])+"_"
    return string_tool.rstrip("_")

def compile_card_access(array_tool):
    print("\033[33m{}".format("\n[WARNING]: ")+"\033[0m{}".format("Отвечайти только 1 или 0 - да или нет!\n"))    
    tool_id = ""
    name = array_tool[0][1] # [["name", simple_name]]
    tool_id += name + "_access_card"
    write = input("\n[Доступ к записи]:\n-> ")
    if checkin_for_int_and_spaces(write) == False:
        return
    read = input("\n[Доступ к чтению]:\n-> ")
    if checkin_for_int_and_spaces(read) == False:
        return
    if write == "1":
        tool_id += "_write"
    if read == "1":
        tool_id += "_read"

    return tool_id

def compile_computer(array_tool):
    tool_id = ""
    name = array_tool[0][1] # [["name", simple_name]]
    tool_id += name + "_smart_electronics=1"
    return tool_id


def id_compile(index=0):
    menu_dict = ["Оружие", "Заряды", "Аптечки", "Броня", "Карты доступа", "Компьютеры"]
    welcom_string = menu_dict[index]


    print("\n#######################################################\n")
    print_warning()
    array_tool = []

    print("\033[32m{}".format("["+welcom_string+"]:")+"\033[0m{}".format(""))

    while True:
        name = input("\n[Наименование]:\n-> ")
        name = name.replace(" ", "-")
        if name != "":
            break
    
    if welcom_string == "Аптечки":
        name = "medkit-"+name
    array_tool.append(["name", name])

    if welcom_string == "Оружие":
        damage = input("\n[Урон]:\n-> ")
        if checkin_for_int_and_spaces(damage) == False:
            return
        array_tool.append(["damage", damage])

    if welcom_string == "Заряды":
        recharge = input("\n[tool_id перезаряжаемого инструмента]:\n-> ")
        array_tool.append(["recharge", recharge])

    tool_id = ""
    if welcom_string == "Карты доступа":
        tool_id = compile_card_access(array_tool)

    if welcom_string == "Компьютеры":
        tool_id = compile_computer(array_tool)

    if welcom_string != "Карты доступа" and welcom_string != "Компьютеры":
        if welcom_string != "Аптечки" and welcom_string != "Броня":
            print("\n#######################################################\n")
        if welcom_string != "Заряды":
            if welcom_string != "Аптечки" and welcom_string != "Броня":
                res = input("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Это всё?(да/нет - 0/1):\n-> "))
                if checkin_for_int_and_spaces(res) == False:
                    return
            else:
                res = "1"
            if res == "1":
                HP = input("\n[HP]:\n-> ")
                if checkin_for_int_and_spaces(HP) == False:
                    return
                array_tool.append(["HP", HP])

                charge = input("\n[Заряженность]:\n-> ")
                if checkin_for_int_and_spaces(charge) == False:
                    return
                array_tool.append(["charge", charge])

                critical_dmg = input("\n[Критический урон(до 45)]:\n-> ")
                if checkin_for_int_and_spaces(critical_dmg) == False:
                    return
                array_tool.append(["critical-dmg", critical_dmg])

                armor = input("\n[Защита]:\n-> ")
                if checkin_for_int_and_spaces(armor) == False:
                    return
                array_tool.append(["armor", armor])

                strong = input("\n[Сила]:\n-> ")
                if checkin_for_int_and_spaces(strong) == False:
                    return
                array_tool.append(["strong", strong])

                intellect = input("\n[Интелект]:\n-> ")
                if checkin_for_int_and_spaces(intellect) == False:
                    return
                array_tool.append(["intellect", intellect])
            print("\n#######################################################\n")

        array_tool = sort_array_tool(array_tool)
        if welcom_string == "Заряды":
            tool_id = compile_tool(array_tool, recharge=True)
        else:
            tool_id = compile_tool(array_tool)
    print_tool_id(tool_id)



def menu():
    while True:
        print("\n#######################################################\n")
        print("\033[32m{}".format("[MAIN MENU]:")+"\033[0m{}".format("Выберите тип инструмента:"))
        print("[1]: Оружие.")
        print("[2]: Заряды.")
        print("[3]: Аптечка.")
        print("[4]: Броня.")
        print("[5]: Карта доступа.")
        print("[6]: Компьютер.")
        print("[0]: Выход.")
        print("\n#######################################################\n")
    
        command = input(":~> ")
    
        if command == "1":
            id_compile(0)
        if command == "2":
            id_compile(1)
        if command == "3":
            id_compile(2)
        if command == "4":
            id_compile(3)
        if command == "5":
            id_compile(4)
        if command == "6":
            id_compile(5)

        if command == "0":
            return

menu()