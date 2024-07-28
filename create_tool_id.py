def print_warning():
    print("\n")
    print(\033[33m{}".format("[WARNING]: ")+"\033[0m{}".format("Если вы отказываетесь от заполнения, то просто прожмите <enter>!"))
    print("\n")

def sort_array_tool(array_tool):
    new_array_tool = []
    for tool in array_tool:
        if tool != "":
            new_array_tool.append(tool)
    return new_array_tool

def compile_tool(array_tool):
    name = array_tool[0]
    string_tool = name+"_"
    array_tool.remove(name)
    for char in array_tool:
        string_tool += str(char[0])+"="+str(char[1])+"_"
    return string_tool.rstrip("_")
    

def gun_compile():
    print_warning()
    array_tool = []
    name = input("Наименование оружия:\n-> ")
    array_tool.append(name)
    damage = input("Урон:\n-> ")
    array_tool.append(damage)
    res = input("Это всё?(да/нет - 0/1):\n-> ")
    if res == 1:
        charge = input("Заряженность:\n-> ")
        array_tool.append(charge)
        critical-dmg = input("Критический урон(до 45):\n-> ")
        array_tool.append(critical-dmg)
        armor = input("Защита:\n-> ")
        array_tool.append(armor)
        HP = input("HP:\n-> ")
        array_tool.append(HP)
        strong = input("Сила:\n-> ")
        array_tool.append(strong)
        intellect = input("Интелект:\n-> ")
        array_tool.append(intellect)
        
    array_tool = sort_array_tool(array_tool)
    print(compile_tool(array_tool))

def menu():
    while True:
        print("Выберите тип инструмента:")
        print("1. Оружие.")
        print("2. Патроны.")
        print("3. Аптечка.")
        print("4. Броня.")
        print("5. Карта доступа.")
        print("6. Компьютер.")
    
        command = input("> ")
    
        if command == "1":
             gun_compile()
    





name = input("Введите имя инструмента:\n-> ")
name = name.replace(" ", "-")

i = 0
character = ""
while True:
    print("\n#######################################################\n")
    print("Уже добавлено: "+str(i))
    print("0. Готово")
    print("\n#######################################################\n")
    res = input("Задайте характеристику(Пример: armor=200):\n->")
    if res == "0":
        break
    character = + "_" + res
    i += 1

print("\n\n\n")
print(character)
print("\n\n\n")
