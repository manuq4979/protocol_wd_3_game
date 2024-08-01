###

#    Тут приложения в виде обычных def:

###

# METHOD APP 1
percent = 40
original_calculate_drop_trophy = "Unknown"
def hacked_calculate_drop_trophy(npc):
    r = random.randint(1, 100)
    print("Трофей: "+str(r))
    if r <= percent:
        return npc.drop_trophy
    return 0
    
# APP NUMBER 1
def hack_trophy(prof):
    bots_id = [["two-wheeled-bot", 70], ["spider-bot", 100]]
    while True:
        print("\n#######################################################\n")
        print("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Приложение позволяет взламывать вам противника с помощью ботов!\n"))
        print("Hack Menu: ----------------------")
        print("[1]: Выполнить взлом.")
        print("[2]: Отменить взлом.")
        print("[3]: Список поддерживаемых ботов.")
        print("[0]: Выход.")
        print("\n#######################################################\n")
    
        command = input("~# ")
        if command.isdigit() == False:
            print("\033[31m{}".format("[ERROR]: ")+"\033[0m{}".format("Допустимы лишь числовые значения!"))
            input("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Нажмите <enter> чтобы продолжить..."))
            continue
    
        if command == "1":
            inventory = prof.get_tools_id()
            my_bots = []
            for tool_id, price in inventory.items():
                for bot_id in bots_id:
                    if tool_id == bot_id[0]:
                        my_bota.append(bot_id)
            if len(my_bots) == 0:
                print("\033[31m{}".format("[ERROR]: ")+"\033[0m{}".format("Требуется наличие бота в инвентаре!"))
                input("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Нажмите <enter> чтобы продолжить..."))
                continue
            values = []
            for bot_id in my_bots:
                values.append(bot_id[1])
            max_percent = max(values)
            
            from player_profile import calculate_drop_trophy
            global percent, original_calculate_drop_trophy
            percent = max_percent
            original_calculate_drop_trophy = calculate_drop_trophy
            calculate_drop_trophy = hacked_calculate_drop_trophy
            print("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Вероятность выпадения вместо 40 - "+str(percent)+"%."))
            input("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Нажмите <enter> чтобы продолжить..."))
        if command == "2":
            from player_profile import calculate_drop_trophy
            global percent, original_calculate_drop_trophy
            percent = 40
            calculate_drop_trophy = original_calculate_drop_trophy
            print("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Вероятность выпадения снова 40%."))
            input("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Нажмите <enter> чтобы продолжить...")) 
            
                





###

#    Ниже код для отображения приложений:

###

applications_list = [] # [[name, app_address], ...]

def get_applications_and_print():
    size = len(applications_list)
    for i in range(size):
        app = applications_list[i]
        print("["+str(i)+"]: "+ app[0]+".")

# Вернет index или False с текстом ошибки в случае ошибки ввода:
def check_input(input_text):
    if input_text.isdigit() == False:
        print("\033[31m{}".format("[ERROR]: ")+"\033[0m{}".format("Допустимы лишь числовые значения!"))
        input("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Нажмите <enter> чтобы продолжить..."))
        return False
    else:
        index = int(input_text) - 1
        if len(applications_list) < index:
            print("\033[31m{}".format("[ERROR]: ")+"\033[0m{}".format("Данного пункта меню не существует!"))
            input("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Нажмите <enter> чтобы продолжить..."))
            return False
        return index

def application_menu(prof):
    print("\n#######################################################\n")
    print("Menu: ----------------------")
    get_applications_and_print()
    print("[0]: Выход."])
    print("\n#######################################################\n")
    
    index = input("APP-MENU:~# ")
    if index == "0":
        return
    index = check_input(index)
    
    
    applications_list[index][1](prof)