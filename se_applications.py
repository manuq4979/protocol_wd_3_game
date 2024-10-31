import random

###

#    Тут приложения в виде обычных def:

###

def counter_consumables(prof, get_consumables=False):
    inventory = prof.get_tools_id()
    consumables_array = []
    for tool_id, price in inventory.items():
        if tool_id.find("smartphone_consumables") != -1:
            consumables_array.append(tool_id) # добавлчем для начала в массив, если в инвентаре насчитается нужное кол-во необходимых расходников, тогда они будут все удалены - использованы позже
    
    if get_consumables != False:
        return [len(consumables_array), consumables_array]
    return len(consumables_array)

def use_consumables(prof, quantity=1): # Если расходный материал успешно использован вернет True иначе False:
    inventory = prof.get_tools_id()
    flag = False
    consumables_array = []
    # подсчитываем есть ли в инвентаре нужное кол-во расхолников
    arr = counter_consumables(prof, get_consumables=True)
    count = arr[0]
    consumables_array = arr[1]
    if count != quantity:
        return False
    
    for consumables in consumables_array:
        prof.del_tools_id(consumables)
    return True


# APP 1 --------------------------------------------------------------------------
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
        print("\n" * 100) # очищаем экран консоли
        
        if command == "0":
            return
        
        if command.isdigit() == False:
            print("\033[31m{}".format("[ERROR]: ")+"\033[0m{}".format("Допустимы лишь числовые значения!"))
            input("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Нажмите <enter> чтобы продолжить..."))
            print("\n" * 100) # очищаем экран консоли
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
                print("\n" * 100) # очищаем экран консоли
                continue
                
            if len(my_bots) == 0:
                print("\033[31m{}".format("[ERROR]: ")+"\033[0m{}".format("Требуется наличие бота в инвентаре!"))
                input("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Нажмите <enter> чтобы продолжить..."))
                print("\n" * 100) # очищаем экран консоли
                continue
            values = []
            for bot_id in my_bots:
                values.append(bot_id[1])
            max_percent = max(values)
            percent = max_percent
            print("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Вероятность успеха взлома: "+str(percent)+"%."))
            
            if use_consumables(prof) == False:
                print("\033[31m{}".format("[ERROR]: ")+"\033[0m{}".format("Отсутствует расходный материал - смартфон!"))
                input("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Нажмите <enter> чтобы продолжить..."))
                print("\n" * 100) # очищаем экран консоли
                continue
            
            from person import NPC
            npc = NPC.get_instance()
            
            if npc.installed_contender != True:
                print("\033[31m{}".format("[ERROR]: ")+"\033[0m{}".format("Нет цели для взлома!"))
                input("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Нажмите <enter> чтобы продолжить..."))
                print("\n" * 100) # очищаем экран консоли
                continue
            
            drop = hacked_calculate_drop_trophy(npc)
            if drop == 0:
                print("\033[31m{}".format("[FAILED]: ")+"\033[0m{}".format("Взлом провалился!"))
                input("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Нажмите <enter> чтобы продолжить..."))
                print("\n" * 100) # очищаем экран консоли
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
            print("\n" * 100) # очищаем экран консоли


# APP 2 --------------------------------------------------------------------------
def get_ability_to_flash_firmware(prof):
    from smart_electronics import Smart_Electronics, set_new_soft
    se = Smart_Electronics.get_instance()
    access = se.possibility_of_flashing
    while True:
        print("\n#######################################################\n\n\n\n")
        print("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Приложение позволяет вам получать возможность устанавливать прошивку для подключенного устройтсва!\n"))
        number = int(se.valuation_storage * 30) # расчет количества требуемых для взлома расходников(зависит от оценки ценности хранилеща у SE обьекта)
        print("\033[33m{}".format("[WARNING]: ")+"\033[0m{}".format("Требуется расходников: "+str(number)+" штук!"))
        print("\n\n\nHack Menu: ----------------------")
        print("[1]: Получить возможность перепрошивки.")
        if access == 1:
            print("[2]: Меню прошивки.")
        print("[0]: Выход.")
        print("\n#######################################################\n")
    
        command = input("~# ")
        print("\n" * 100) # очищаем экран консоли
    
        if command.isdigit() == False:
            print("\033[31m{}".format("[ERROR]: ")+"\033[0m{}".format("Допустимы лишь числовые значения!"))
            input("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Нажмите <enter> чтобы продолжить..."))
            print("\n" * 100) # очищаем экран консоли
            continue
    
        if command == "0":
            return
    
        if command == "1":
            if se.name == "": # по умолчанию имя name
                print("\033[33m{}".format("[WARNING]: ")+"\033[0m{}".format("Нет подключенных устройств!"))
                input("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Нажмите <enter> чтобы продолжить..."))
                print("\n" * 100) # очищаем экран консоли
                continue
            if se.possibility_of_flashing == 1:
                print("\033[33m{}".format("[WARNING]: ")+"\033[0m{}".format("Доступ уже получен!"))
                input("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Нажмите <enter> чтобы продолжить..."))
                print("\n" * 100) # очищаем экран консоли
                continue
                
            if use_consumables(prof, quantity=number) == False:
                print("\033[31m{}".format("[ERROR]: ")+"\033[0m{}".format("Отсутствует расходный материал - смартфон!"))
                input("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Нажмите <enter> чтобы продолжить..."))
                print("\n" * 100) # очищаем экран консоли
                continue
            
            se.possibility_of_flashing = 1
            access = 1
        
            print("\033[32m{}".format("[COMPLITE]: ")+"\033[0m{}".format("Взлом успешно выполнен!"))
            input("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Нажмите <enter> чтобы продолжить..."))
            print("\n" * 100) # очищаем экран консоли
        if command == "2" and access == 1:
            set_new_soft()

# ЗАГЛУШКА НА ВЫЗОВ МЕТОДОВ ВЫШЕ:
def check_access_2(prof):
    inventory = prof.get_tools_id() # ДЛЯ APP 2
    for tool_id, price in inventory.items():
        if tool_id == "dedsec_flash-driver=retro4979":
            get_ability_to_flash_firmware(prof)
            return
    print("\033[31m{}".format("[ACCESS DENIED]: ")+"\033[0m{}".format("Требуется доступ уровня DedSec!"))
    input("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Нажмите <enter> чтобы продолжить..."))
    print("\n" * 100) # очищаем экран консоли
    return

def check_access_1(prof): # ДЛЯ APP 1
    inventory = prof.get_tools_id()
    for tool_id, price in inventory.items():
        if tool_id == "dedsec_flash-driver=retro4979":
            hack_trophy(prof)
            return
    print("\033[31m{}".format("[ACCESS DENIED]: ")+"\033[0m{}".format("Требуется доступ уровня DedSec!"))
    input("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Нажмите <enter> чтобы продолжить..."))
    print("\n" * 100) # очищаем экран консоли
    return
    
    
# APP 3 --------------------------------------------------------------------------
def to_see_if_enemy_has_already_been_installed():
    from person import NPC
    npc = NPC.get_instance()
    return npc.installed_contender

def menu_detect_an_enemy_hacker(hacker, prof):
    while True:
        print("\n#######################################################\n")
        print("\033[32m{}".format("[Решите что сделать с хакером]:")+"\033[0m{}".format(""))
        if to_see_if_enemy_has_already_been_installed() == True:
            print("\033[31m{}".format("[1]: Установить хакера в качестве врага.")+"\033[0m{}".format(""))
        else:
            print("[1]: Установить хакера в качестве врага.")
        print("[2]: Предложить сделку.")
        print("\n#######################################################\n")

        command = input("> ")
        print("\n" * 100) # очищаем экран консоли

        if command == "1":
            if to_see_if_enemy_has_already_been_installed() == False:
                hacker.set_this_npc_as_an_enemy()
                return
            print("\033[33m{}".format("[WARNING]: ")+"\033[0m{}".format("Враг уже установлен! Он является прикрытием для хакера!"))
            print("\n" * 100) # очищаем экран консоли
            return
        if command == "2":
            hacker.menu_for_deal(prof)
            return


def detect_an_enemy_hacker(prof):
    if use_consumables(prof) == False:
        print("\033[31m{}".format("[FAILED]: ")+"\033[0m{}".format("Нет расходного материала!"))
        input("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Нажмите <enter> чтобы продолжить..."))
        print("\n" * 100) # очищаем экран консоли
        return

    from hacker_person import HACKER_NPC
    hacker = HACKER_NPC.get_instance()
    hacker_lvl = int(hacker.lvl)
    probability_of_success = 90 -(hacker_lvl * 10) # если уровень хакера 5, то итоговая будет 5*10 - 90 и того: 40% успеха, формула вычисления простая, уровень это x, а фрмула: x*10 - 90
    if probability_of_success <= 50: # если вероятность ниже 50%, то:
        if prof.get_intellect() >= 9: # начиная от интелекта 9 и выше, то:
            probability_of_success += 35 # к итоговой вероятноти +35

    print("\n#######################################################\n\n\n\n\n\n")
    print("\033[33m{}".format("[WARNING]: ")+"\033[0m{}".format("Вероятность успеха: "+str(probability_of_success)+"%"))
    print("\n\n\n\n\n\n#######################################################\n")

    probability = random.randint(1, 100)
    if probability <= probability_of_success:
        print("\033[32m{}".format("[COMPLITE]: ")+"\033[0m{}".format("Местоположение вражеского хакера вычислено!"))
        input("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Нажмите <enter> чтобы продолжить..."))
        menu_detect_an_enemy_hacker(hacker, prof)
        print("\n" * 100) # очищаем экран консоли
        return
    else:
        print("\033[31m{}".format("[FAILED]: ")+"\033[0m{}".format("Попытка вычислить местоположение провалилась!"))
        input("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Нажмите <enter> чтобы продолжить..."))
        print("\n" * 100) # очищаем экран консоли


###

#    Ниже код для отображения приложений:

###

applications_list = [["Взломать систему трофеев врага", check_access_1], ["Получить возможность перепрошивки", check_access_2], ["Обнаружить вражеского хакера", detect_an_enemy_hacker]] # [[name, app_address], ...]

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
            print("\n" * 100) # очищаем экран консоли
            return False
        return index

def application_menu(prof):
    while True:
        print("\n#######################################################\n")
        print("У вас расходников: "+str(counter_consumables(prof))+" штук.")
        print("Menu: ----------------------")
        get_applications_and_print()
        print("[0]: Выход.")
        print("\n#######################################################\n")
        
        index = input("APP-MENU:~# ")
        print("\n" * 100) # очищаем экран консоли
    
        index = index.replace(" ", "")
        if index == "":
            continue
        if index == "0":
            return
        index = check_input(index)
        
        
        applications_list[index][1](prof)
