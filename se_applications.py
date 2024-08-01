###

#    Тут приложения в виде обычных def:

###

# METHOD APP 1
percent = 40
original_calculate_drop_trophy = "Unknown"
def hacked_calculate_drop_trophy(npc):
    import random
    print("\033[32m{}".format("[DONE]: ")+"\033[0m{}".format("THIS CODE HAS BEEN HACKED!"))
    r = random.randint(1, 100)
    print("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Шанс выпадения трофея был: "+str(r)))
    if r <= percent:
        return npc.drop_trophy
    return 0
    
# APP NUMBER 1
def hack_trophy(prof):
    global percent, original_calculate_drop_trophy
    bots_id = [["two-wheeled-bot", 70], ["spider-bot", 100]]
    while True:
        print("\n#######################################################\n")
        print("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Приложение позволяет взламывать вам противника с помощью ботов!\n"))
        print("Hack Menu: ----------------------")
        print("[1]: Выполнить взлом.")
        print("[2]: Список поддерживаемых ботов.")
        print("[3]: Список моих ботов.")
        print("[0]: Выход.")
        print("\n#######################################################\n")
    
        command = input("~# ")
        
        if command == "0":
            return
        
        if command.isdigit() == False:
            print("\033[31m{}".format("[ERROR]: ")+"\033[0m{}".format("Допустимы лишь числовые значения!"))
            input("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Нажмите <enter> чтобы продолжить..."))
            continue
            
    
        if command == "1" or command == "3":
            inventory = prof.get_tools_id()
            my_bots = []
            for tool_id, price in inventory.items():
                for bot_id in bots_id:
                    if tool_id == bot_id[0]:
                        my_bots.append(bot_id)
            if command == "3":
                print("\n#######################################################\n")
                if len(my_bots) == 0:
                    print("\033[33m{}".format("[WARNING]: ")+"\033[0m{}".format("Доступных ботов не найдено!"))
                else:
                    for my_bot_id in my_bots:
                        print("\033[34m{}".format("[tool_id]: ")+"\033[0m{}".format(my_bot_id[0]))
                        print("\n")
                print("\n#######################################################\n")
                input("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Нажмите <enter> чтобы продолжить..."))
                continue
                
            if len(my_bots) == 0:
                print("\033[31m{}".format("[ERROR]: ")+"\033[0m{}".format("Требуется наличие бота в инвентаре!"))
                input("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Нажмите <enter> чтобы продолжить..."))
                continue
            values = []
            for bot_id in my_bots:
                values.append(bot_id[1])
            max_percent = max(values)
            percent = max_percent
            print("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Вероятность успеха взлома: "+str(percent)+"%."))
            
            from person import NPC
            npc = NPC.get_instance()
            
            if npc.installed_contender != True:
                print("\033[31m{}".format("[ERROR]: ")+"\033[0m{}".format("Нет цели для взлома!"))
                input("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Нажмите <enter> чтобы продолжить..."))
                continue
            
            drop = hacked_calculate_drop_trophy(npc)
            if drop == 0:
                print("\033[31m{}".format("[FAILED]: ")+"\033[0m{}".format("Взлом провалился!"))
                input("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Нажмите <enter> чтобы продолжить..."))
                continue
            
            prof.add_tools_id(drop, 50)
            npc.drop_trophy = []
            history_line = "Получен трофей "+str(drop)+" - ценность 50 ETO при помощи взлома."
            prof.save_to_history(history_line)
            print("\033[32m{}".format("[COMPLITE]: ")+"\033[0m{}".format(history_line))
            input("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Нажмите <enter> чтобы продолжить..."))
        
        if command == "2":
            print("\n#######################################################\n")
            for bot_id in bots_id:
                print("\033[34m{}".format("[tool_id]: ")+"\033[0m{}".format(bot_id[0]))
                print("С ним шанс выпадения трофея будет: "+str(bot_id[1])+"%.")
                print("\n")
            print("\n#######################################################\n")
            input("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Нажмите <enter> чтобы продолжить..."))
            

# APP NUMBER 2
def get_ability_to_flash_firmware(prof):
    access = 0
    while True:
        print("\n#######################################################\n")
        print("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Приложение позволяет вам получать возможность устанавливать прошивку для подключенного устройтсва!\n"))
        print("Hack Menu: ----------------------")
        print("[1]: Получить возможность перепрошивки.")
        if access == 1:
            print("[2]: Меню прошивки.")
        print("[0]: Выход.")
        print("\n#######################################################\n")
    
        command = input("~# ")
    
        if command.isdigit() == False:
            print("\033[31m{}".format("[ERROR]: ")+"\033[0m{}".format("Допустимы лишь числовые значения!"))
            input("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Нажмите <enter> чтобы продолжить..."))
            continue
    
        if command == "0":
            return
    
        if command == "1":
            from smart_electronics import Smart_Electronics, set_new_soft
            se = Smart_Electronics.get_instance()
            if se.name == "": # по умолчанию имя name
                print("\033[33m{}".format("[WARNING]: ")+"\033[0m{}".format("Нет подключенных устройств!"))
                input("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Нажмите <enter> чтобы продолжить..."))
                continue
            if se.possibility_of_flashing == 1:
                print("\033[33m{}".format("[WARNING]: ")+"\033[0m{}".format("Доступ уже получен!"))
                input("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Нажмите <enter> чтобы продолжить..."))
                continue
            se.possibility_of_flashing = 1
            access = 1
        
            print("\033[32m{}".format("[COMPLITE]: ")+"\033[0m{}".format("Взлом успешно выполнен!"))
            input("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Нажмите <enter> чтобы продолжить..."))
        if command == "2" and access = 1:
            while True:
                print("\n#######################################################\n")
                print("[1]: Установить новые параметры..")
                print("[0]: Назад.")
                print("\n#######################################################\n")
                
                command_2 = input("~# ")
                
                if command_2 == "0":
                    break
                
                if command_2.isdigit() == False:
                    print("\033[31m{}".format("[ERROR]: ")+"\033[0m{}".format("Допустимы лишь числовые значения!"))
                    input("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Нажмите <enter> чтобы продолжить..."))
                    continue
                    
                if command_2 == "1":
                    set_new_soft()



###

#    Ниже код для отображения приложений:

###

applications_list = [["hack_trophy_systems", hack_trophy], ["get_ability_to_flash_firmware", get_ability_to_flash_firmware]] # [[name, app_address], ...]

def get_applications_and_print():
    size = len(applications_list)
    for i in range(size):
        app = applications_list[i]
        print("["+str(i+1)+"]: "+ app[0]+".")

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
    print("[0]: Выход.")
    print("\n#######################################################\n")
    
    index = input("APP-MENU:~# ")
    if index == "0":
        return
    index = check_input(index)
    
    
    applications_list[index][1](prof)
