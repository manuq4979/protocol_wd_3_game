
def print_tool_id(NPC_ID):
    print("\033[32m{}".format("[ID ГОТОВ]: ")+"\033[0m{}".format("Осталось только скопировать:"))
    print("\n#######################################################\n\n\n\n\n\n")
    print("     "+NPC_ID+"    ")
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

def compile_tool(array_tool):
    name = array_tool[0][1]
    string_tool = name+"_"
    array_tool.pop(0)

    for char in array_tool:
        # print(array_tool)
        if char[0] == "drop-trophy":
            string_tool += char[0] + char[1]
            return string_tool
        string_tool += str(char[0])+"="+str(char[1])+"_"

    return string_tool.rstrip("_")




def id_compile():
    print("\n#######################################################\n")
    print("\033[32m{}".format("[NPC_ID форма]:")+"\033[0m{}".format("заполните форму:"))

    array_tool = []

    while True:
        name = input("\n[Как его будут звать]:\n-> ")
        name = name.replace(" ", "-")
        if name != "":
            break
    array_tool.append(["name", name])

    HP = input("\n[HP]:\n-> ")
    if checkin_for_int_and_spaces(HP) == False:
        return
    array_tool.append(["HP", HP])

    armor = input("\n[Защита]:\n-> ")
    if checkin_for_int_and_spaces(armor) == False:
        return
    array_tool.append(["armor", armor])

    damage = input("\n[Урон]:\n-> ")
    if checkin_for_int_and_spaces(damage) == False:
        return
    array_tool.append(["damage", damage])

    strong = input("\n[Сила(до 15)]:\n-> ")
    if checkin_for_int_and_spaces(strong) == False:
        return
    array_tool.append(["strong", strong])

    critical_dmg = input("\n[Критический урон(до 45)]:\n-> ")
    if checkin_for_int_and_spaces(critical_dmg) == False:
        return
    array_tool.append(["critical-dmg", critical_dmg])

    i = 0
    drop_trophy = ""
    while True:
        print("\n#######################################################\n")
        print("[Уже добавлено]: "+str(i))
        print("--------------------------------")
        print("\n[0]: Готово.\n")
        print("\n#######################################################\n")


        res = input("\n[Какие трофеи будут]:\n-> ")
        if res == "0":
            break
        else:
            drop_trophy += ":"+res
        i += 1
    if drop_trophy == "":
        drop_trophy = ":"
    array_tool.append(["drop-trophy", drop_trophy])
    print("\n#######################################################\n")



    array_tool = sort_array_tool(array_tool)
    tool_id = compile_tool(array_tool)
    print_tool_id(tool_id)


def menu():
    while True:
        print("\n#######################################################\n")
        print("\033[32m{}".format("[MAIN MENU]:")+"\033[0m{}".format(" Выберите один из пунктов:\n"))
        print("[1]: Создать NPC_ID.")
        print("[0]: Выход.")
        print("\n#######################################################\n")

        command = input(":~> ")

        if command == "1":
            id_compile()
        if command == "0":
            return

menu()