"""
Этот модуль предназначен для сгруза всех методов которые,
как мне показалось, слишком перегржают свои модули -
например, buy и sell - в своем модуле store.py они
кажутся слишком громосткими.

также те же buy и sell, могут быть нужны в нецтральном модуле,
иначе может возникнуть конфликт в коде, вроде так.

я это пишу, чтобы поосто не забыть, верно ли я понял,
скорее да чем нет.
"""


#from datetime import datetime, timedelta
from store import *
from person import *
from player_profile import *
from task import *
from smart_electronics import *



# Store

# person.NPC - изначально ниже Tasks в импорте

# Profile - был в импорте выше чем person.NPC

# Tasks



    

def get_menu_SingleTask():
    title_minu = "Одиночные"
    get_menu_task(title_minu, single_task_dict, add_single_task, del_single_task)

def get_menu_DailyTask():
    title_minu = "Ежедневные"
    get_menu_task(title_minu, daily_task_dict, add_daily_task, del_daily_task)

def get_menu_HabitTask():
    title_minu = "Привычки"
    get_menu_task(title_minu, habit_task_dict, add_habit_task, del_habit_task, habit_menu=True)


def get_smart_electronics_menu():
    prof = Profile.get_instance()
    
    # Ищем компьютер по поиску в троке слова:
    inventory = prof.get_tools_id()
    computer = False # изначально буем считать что компьютера нет
    for tool_id, price in inventory.items():
        if tool_id.find("laptop-base_smart_electronics=1") != -1:
            computer = True # Значит есть
            
    poit_of_entry(computer, prof)

def get_menu_developer():
    while True:
        print("\n#######################################################\n")
        print("\nВыберете номер:")
        print("[ 1]: Добавить товар в магазин.")
        print("[ 2]: Удалить товар из магазина.")
        print("[ 3]: Установить ETO игроку.")
        print("[ 4]: Добавить предмет в инвентарь.")
        print("[45]: Удалить предмет из инвенторя.")
        print("[ 5]: Изменить настройки наград.")
        print("[ 6]: Установить профиль в default.")
        print("[ 7]: Установить ID врага в значение по умолчанию.")
        print("[ 8]: Меню рейтинга.")
        print("[ 9]: Удалить все не активные задания.")
        print("[ 0]: Назад.")
        print("\n#######################################################\n")
        
        number = input("> ")
        print("\n" * 100) # очищаем экран консоли
        
        if number == "1":
            add_product()
            input("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Нажмите <enter> чтобы продолжить..."))
            continue
        if number == "2":
            del_product()
            input("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Нажмите <enter> чтобы продолжить..."))
            continue
        if number == "3":
            ETO = input("ETO> ")
            prof = Profile.get_instance()
            prof.save_to_history("Разработчик накинул тебе "+str(ETO)+" ETO ;)\n")
            prof.set_ETO(int(ETO))
            input("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Нажмите <enter> чтобы продолжить..."))
            continue
        if number == "4":
            tool_id = input("tool_id> ")
            price   = input("price> ")
            prof = Profile.get_instance()
            prof.add_tools_id(tool_id, price)
            input("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Нажмите <enter> чтобы продолжить..."))
            continue
        if number == "45":
            prof = Profile.get_instance()
            tool_id = input("tool_id> ")
            prof.del_tools_id(tool_id)
            print("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Предмет " + str(tool_id) + " успешно удален!"))
            input("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Нажмите <enter> чтобы продолжить..."))
            continue
        if number == "5":
            prof = Profile.get_instance()
            prof.edit_quest_reward_setting()
            continue
        if number == "6":
            prof = Profile.get_instance()
            prof.set_all_fields_default()
            input("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Нажмите <enter> чтобы продолжить..."))
            continue
        if number == "7":
            npc = NPC.get_instance()
            npc.set_all_fields_default()
            input("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Нажмите <enter> чтобы продолжить..."))
            continue
        if number == "8":
            from raiting import raiting_menu
            raiting_menu()
            continue
        if number == "9":
            del_no_active_task(task_list=[], developer_menu=True)
            continue
        if number == "0":
            return
        else:
            print("\033[33m{}".format("[WARNING]: ")+"\033[0m{}".format("выбран не верный номер."))



def get_menu():
    while True:
        print("\n#######################################################\n")
        print("Выберете номер:")
        print("[ 1]: Ежедневны задания")
        print("[ 2]: Одиночные задания")
        print("[ 3]: Задания привычки")
        print("[ 4]: История баланса ETO")
        print("[ 5]: Магазин инструментов")
        print("[ 6]: Установить ID врага")
        print("[61]: Установить ID вражеского хакера")
        print("[65]: Открыть Smart Electronics.")
        print("[ 7]: Инвентарь")
        print("[ 8]: Сменить характеристики своего персонажа")
        print("[85]: Вернуть характеристики моего персонажа")
        print("[ 0]: Назад")
        print("[10]: Для разработчиков")
        print("\n#######################################################\n")
    
        number = input("> ")
        print("\n" * 100) # очищаем экран консоли
        
        if number == "0":
            return
        if number == "1":
            get_menu_DailyTask()
            continue
        if number == "2":
            get_menu_SingleTask()
            continue
        if number == "3":
            get_menu_HabitTask()
            continue
        if number == "4":
            get_history()
            continue
        if number == "5":
            get_store()
            continue
        if number == "6":
            get_installer_NPC()
            continue
        if number == "61":
            from hacker_person import add_NPC
            add_NPC()
            continue
        if number == "65":
            get_smart_electronics_menu()
            continue
        if number == "7":
            get_inventory()
            continue
        if number == "8":
            prof = Profile.get_instance()
            prof.set_new_characteristics()
            continue
        if number == "85":
            prof = Profile.get_instance()
            prof.reset_new_characteristics()
            continue
        if number == "9":
            continue
        if number == "10":
            get_menu_developer()
            continue
        else:
            print("\033[33m{}".format("[WARNING]: ")+"\033[0m{}".format("выбран не верный номер."))



def buy(tool_id, no_add_to_inventory=False, service_price=0):
    global store_ETO, store

    prof = Profile.get_instance()
    price = 0
    if no_add_to_inventory == False:
        price = store.get(tool_id)          # получаем цену за инструмент
    elif no_add_to_inventory == True:
        price = service_price
    if price == None:                   # проверяем наличие товара
        print("\033[31m{}".format("[ERROR]: ")+"\033[0m{}".format("Данного товара нет!"))
        input("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Нажмите <enter> чтобы продолжить..."))
        return

    price = int(price)
    if int(prof.get_ETO()) < price:                 # проверяем достаточно ли ETO
        print("\033[31m{}".format("[ERROR]: ")+"\033[0m{}".format("Не достаточно средств!"))
        input("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Нажмите <enter> чтобы продолжить..."))
        return False
    if no_add_to_inventory == False:
    	history_line = "Куплен: "+str(tool_id)+" за "+str(price)
    elif no_add_to_inventory == True:
        history_line = "Списания в размере: "+str(price)+" за доп услуги магазина(по типу за подзарядку инструената)."
    prof.save_to_history(history_line)  # заносим в историю
    prof.set_ETO(int(prof.get_ETO())-price)         # вычетаем из баланса игрока сумму за товар
    if no_add_to_inventory == False:
        del store[tool_id]                  # удаляем инструмент из магазина
    store_ETO = int(store_ETO)
    store_ETO += price         # увеличиваем баланс продавца
    if no_add_to_inventory == False:
        price = price / 2                   # уменьшаем стоимость проданного инструмента
    if no_add_to_inventory == False:   
        prof.add_tools_id(tool_id, price)   # добавляем инструмент в инвентарь
        print("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Товар успешно куплен!"))
    elif no_add_to_inventory == True:
        print("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Услуга успешно оплачена!"))
        save_data_store(store_ETO)
        return True
    save_data_store(store_ETO)
    input("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Нажмите <enter> чтобы продолжить..."))
    
def sell(tool_id):
    global store_ETO, store
    
    prof = Profile.get_instance()                   
    price = prof.get_price_of_tools_id(tool_id)     # получаем цену за инструмент
    if price == None:                               # проверяем наличие предмета для продажи
        print("\033[31m{}".format("ERROR: ")+"\033[0m{}".format("Нет предмета для продажи!"))
        input("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Нажмите <enter> чтобы продолжить..."))
        return

    price = int(price)
    
    # Нужно, чтобы я мог продать хранилище токенов в соответствии с кол-во токенов в нем, ведь если это выпало как трофей, price == 50 не иначе!
    is_it_price = tool_id.split("=")[1]
    if is_it_price.isdigit() == True:
        price = int(is_it_price)
        
    if init_store()[1] < price:                             # проверяем достаточно ли ETO
        print("\033[31m{}".format("ERROR: ")+"\033[0m{}".format("У продовца не достаточно средств :("))
        input("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Нажмите <enter> чтобы продолжить..."))
        return
    history_line = "Продан: "+str(tool_id)+" за "+str(price)
    prof.save_to_history(history_line)              # заносим в историю
    store_ETO = int(store_ETO)
    store_ETO -= price                       # вычетаем из баланса продовца сумму за товар
    prof.del_tools_id(tool_id)                      # удаляем инструмент из магазина
    prof.set_ETO(prof.get_ETO() + price)            # увеличиваем баланс игрока
    price = price*2                                 # делаем наценку на купленный инструмент
    store[tool_id] = price                          # добавляем инструмент в магазин
    save_data_store(store_ETO)
    print("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Товар успешно продан!"))
    input("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Нажмите <enter> чтобы продолжить..."))

# "gun_damage=200_strong=2" == ['gun', ['damage', '200'], ['strong', '2']]
def decoding_of_characteristics(char_line):
    Profile.decoding_of_characteristics(char_line)
    
def apply_to_characteristics(char_line, up=True): # char_line == tool_id
    Profile.apply_to_characteristics(char_line, up=True)

def keeping_tool(tool_id):
    Profile.keeping_tool(tool_id)

def take_off(tool_id):
    Profile.take_off(tool_id)


def checking_input_inventory(input_text):
	if len(input_text) <= 1:
		return False

	if input_text.isdigit() == False:
		print("\033[31m{}".format("[ERROR]: ")+"\033[0m{}".format("Допустимы лишь числовые значения!"))
		input("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Нажмите <enter> чтобы продолжить..."))     
		return False

	return True

def hot_key_inventory(text, prof):
    take_off   = False
    tools      = prof.get_tools_id()
    tools_keep = prof.get_keep_tool()
    if checking_input(text) == False:
        return False
    inventory_menu_item     = int(text[0])
    if inventory_menu_item == 2:
        take_off = True
    inventory_tool_id_index = int(text[1:])
    index                   = inventory_tool_id_index-1
    if take_off == False:
        tool_id             = list(tools.keys())[index]
    elif take_off == True:
        tool_id             = list(tools_keep.keys())[index]
    
    return [inventory_menu_item, tool_id]

def get_inventory_interface(prof, other_menu=None):
        tools = prof.get_tools_id()
        print("\n#######################################################\n")
        print("\033[32m{}".format("Inventory:")+"\033[0m{}".format("\n"))
        index = 0
        for tool, price in tools.items():
            index += 1
            print("\033[34m{}".format("[Инструмент]: ")+"\033[0m{}".format("["+str(index)+"]: "+tool))
            print("Его можно продать в магазине за "+str(price)+" ETO.\n\n")
            
        keep_tool      = prof.get_keep_tool()
        slots          = prof.get_slots()
        slots_occupied = prof.get_slots_occupied()
        print("\033[32m{}".format("\nЭкиперованно")+"\033[0m{}".format("(")+str(slots_occupied)+" из "+str(slots)+"):")
        index = 0
        for tool in keep_tool:
            index += 1
            print("\033[34m{}".format("[Инструмент]: ")+"\033[0m{}".format("["+str(index)+"]: "+tool))
        if index == 0:
            prof.set_slots_occupied(0)
        print("\nMenu: ----------------------")
        if other_menu == None:
            print("[1]: Экипировать")
            print("[2]: Снять предмет")
            print("[0]: Назад.")
        else:
            other_menu()
        print("\n#######################################################\n")
        

def get_inventory():
    
    prof = Profile.get_instance()

    while True:
        get_inventory_interface(prof)

        text = input("> ")
        print("\n" * 100) # очищаем экран консоли

        
        if text == "0":
            return
        
        text = hot_key_inventory(text, prof)
        
        if text == False:
            continue
        
        if text[0] == 1:
            tool_id = text[1]
            keeping_tool(tool_id)
            continue
        if text[0] == 2:
            tool_id = text[1]
            take_off(tool_id)
            continue
        else:
            print("\033[33m{}".format("[WARNING]: ")+"\033[0m{}".format("выбран не верный номер."))

    
   
# метод только проверяет актуальность задачь и наносит урон игроку за про$бы.
def check_relevance_task():
    from datetime import datetime, timedelta
    
    # Проверка Одиночных заданий:
    for ID, task in list(single_task_dict.items()):
        res = task.check_complition_time()
                                                                                # задания требующие финансирования имею другой статус:
        if res == True and task.get_status() == "Active":                         # если игрок просрочил задание
            npc = NPC.get_instance()
            if npc.installed_contender != "None":
                prof = Profile.get_instance()
                npc_attack(prof)                # Наносим игроку урон
            del single_task_dict[ID]            # удалить задачу
            save_data_task(msg_on_or_off=False)
    
    # Проверка заданий Привычек:
    for ID, task in list(habit_task_dict.items()):
        res = task.check_reset_time()
        
        if int(res) == 1 or int(res) == 2:       # если дата уже прошла или она сегодня, то пора произвести сброс серии
            task.reset_series_point()
            save_data_task(msg_on_or_off=False)
    
    # Проверка Ежедневных заданий:
    for ID, task in list(daily_task_dict.items()):
        
        start_date = task.get_start_date()
        if task.check_time(start_date) == False: # если ещё рано!
            save_data_task(msg_on_or_off=False)
            continue
        if task.check_time(start_date) == 2: # если сегодня дата начала задания, то:
            if task.get_status() == "No active": # может быть равен Complite и Failed
                task.set_status("Active")        # сделать задние активным и
            save_data_task(msg_on_or_off=False)
            continue                         # то задание не проверять на просроченное!
        if task.check_time(start_date) == 1: # если дата начала прошла, то:
            if task.get_status() == "Active":
                npc = NPC.get_instance()
                if npc.installed_contender != "None":
                    prof = Profile.get_instance()
                    npc_attack(prof)
                task.set_status("Failed")
                save_data_task(msg_on_or_off=False)
            # ниже я актуализирую дату, ведь если дата начала уже далека от даты повтора, то она без этого ей никак не догнать дату повтора:
    
        if task.check_repeat_time() == True:
                task.set_status("Active")            # Делаем задание активным

                this_day = datetime.now().date()
                task.set_start_date(this_day)        # Устанавливаем новую дату начала - а именно лень активации, потому что если оставить прежний день, то окажется что задание не было выполненно, а было провалено!
                new_description = "[Повтор]: "+str(this_day)+": "+str(task.get_repeat())
                task.set_description(new_description)
                save_data_task(msg_on_or_off=False)
        '''
        if task.get_status() == "Active":        # Если задание активно
            
            start_date = task.get_start_date()   # Получаем дату начала
            if task.check_day_end() == True or task.check_time(start_date) == 1 or task.check_time(start_date) == True: # Если дата начала уже прошла или дата повтора сегодня наступила, то и день прошел с момента создания прошел - итог: игрок не успел выполнить задание в срок, а также если день прошел.
                task.set_status("No active")     # Если так, то сделать задние не активным
                npc = NPC.get_instance()
                if npc.installed_contender != "None":
                    prof = Profile.get_instance()
                    npc_attack(prof)             # и нанести игроку урон от врага, если враг есть
        
        res = task.check_repeat_time()           # Далее, получаем ответ на вопрос: наступила ли дата повтора задания
        # 1 и True для оператора if,то одно и тоже, но явное прописывания что это не одно и тоже помогает избежать неловких ситуаций!!!!
        # 1 более не возвращается!!!
        if res == True:                          # И если дата уже наступила, то пора снова задание делать активным
            task.set_status("Active")            # Делаем задание активным
            from datetime import datetime

            this_day = datetime.now().date()
            task.set_start_date(this_day)        # Устанавливаем новую дату начала - а именно лень активации, потому что если оставить прежний день, то окажется что задание не было выполненно, а было провалено!
            new_description = "[Повтор]: "+str(this_day)+": "+str(task.get_repeat())
            task.set_description(new_description)# Новое описание, в котором дата начала также изменена на сегодня - дату повтора.
        '''
def check_HP():
    prof = Profile.get_instance()
    npc = NPC.get_instance()
    if int(prof.get_HP()) == 0:
        prof.death()
    # Если противник не установлен, то будет пустая строка. Следовательно проверять HP не существующего противника нет смысла
    if npc.installed_contender != "" and npc.installed_contender != "None" and npc.installed_contender != None:
        if int(npc.HP) <= 0:
            player_attack()                                 # костыль, проверка хп врога обычно лишь при атаки происходит, а если после атаки хп врага обнулилось, это не зачтеться
    

def save():
    with open(r'AppData.txt', 'w') as file:
        for line in lines:
            file.write("")


