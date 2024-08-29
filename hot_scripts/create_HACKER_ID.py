import json
from hacker_apps import all_scripts




def print_tool_id(HACKER_ID):
    print("\033[32m{}".format("[ID ГОТОВ]: ")+"\033[0m{}".format("Осталось только скопировать:"))
    print("\n#######################################################\n\n\n\n\n\n")
    print("     "+HACKER_ID+"    ")
    print("\n\n\n\n\n\n#######################################################\n")
    input("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Нажмите <enter> чтобы продолжить..."))

all_inventory = ["laptop_s1_smart_electronics=1", {1 : ["smartphone_consumables", 100], 2 : ["smartphone_consumables", 200], 3 : ["smartphone_consumables", 600], 4 : ["smartphone_consumables", 1000], 5 : ["smartphone_consumables", 10000]}]
attack_frequency = {1 : 20, 2 : 40, 3 : 45, 4 : 70, 5 : 80}
likelihood_of_getting_rid_of_hacker ={1 : 50, 2 : 45, 3 : 40, 4 : 35, 5 : 20}



def set_according_to_lvl(lvl):
    sripts_and_inventory = []

    lvl = int(lvl)
    sripts = all_scripts
    inventory = []
    laptop = all_inventory[0]
    inventory = all_inventory[1][lvl]
    sripts_and_inventory.append(sripts)
    sripts_and_inventory.append(inventory)
    return sripts_and_inventory


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

def compile_tool(array_tool):
    return json.dumps(array_tool)

def id_compile():
    print("\n#######################################################\n")
    print("\033[32m{}".format("[HACKER_ID форма]:")+"\033[0m{}".format("заполните форму:"))

    array_tool = []

    while True:
        name = input("\n[Как его будут звать]:\n-> ")
        name = name.replace(" ", "-")
        name = name.replace("_", "-")
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
    drop_trophy = []
    while True:
        print("\n#######################################################\n")
        print("[Уже добавлено]: "+str(i))
        print("--------------------------------")
        print("\n[0]: Готово.\n")
        print("\n#######################################################\n")


        res = input("\n[Какие трофеи будут]:\n-> ")
        if res == "":
            continue
        if res == "0":
            break
        else:
            drop_trophy.append(res)
        i += 1
    array_tool.append(["drop-trophy", drop_trophy])
    print("\n#######################################################\n")

    array_tool.append(["installed-contender", "None"])

    lvl = 1
    while True:
        lvl = input("\n[lvl(1 по 5)]:\n-> ")
        if checkin_for_int_and_spaces(lvl) == False:
            return
        lvl = int(lvl)
        if lvl >= 1 and lvl <= 5:
            lvl = int(lvl)
            array_tool.append(["lvl", lvl])
            break
        print("\033[31m{}".format("[ERROR]: ")+"\033[0m{}".format("Допускаются лишь числа от 1 до 5 включительно!"))
        input("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Нажмите <enter> чтобы продолжить..."))

    sripts_and_inventory = set_according_to_lvl(lvl)
    scripts = sripts_and_inventory[0]
    array_tool.append(["scripts", scripts])
    inventory = sripts_and_inventory[1]
    array_tool.append(["inventory", inventory])

    tool_id = compile_tool(array_tool)
    print_tool_id(tool_id)


def menu():
    while True:
        print("\n#######################################################\n")
        print("\033[32m{}".format("[MAIN MENU]:")+"\033[0m{}".format(" Выберите один из пунктов:\n"))
        print("[1]: Создать HACKER_ID.")
        print("[0]: Выход.")
        print("\n#######################################################\n")

        command = input(":~> ")

        if command == "1":
            id_compile()
        if command == "0":
            return