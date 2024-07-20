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
        if tool_id.find("smart_electronics") != -1:
            computer = True # Значит есть
            
    poit_of_entry(computer, prof)

def get_menu_developer():
    while True:
        print("\nВыберете номер:")
        print("1. Добавить товар в магазин.")
        print("2. Удалить товар из магазина.")
        print("3. Установить ETO игроку.")
        print("4. Добавить предмет в инвентарь.")
        print("4.5. Удалить предмет из инвенторя.")
        print("5. Изменить настройки наград.")
        print("6. Установить профиль в default.")
        print("7. Назад.")
        
        number = input("> ")
        
        if number == "1":
            add_product()
            break
        if number == "2":
            del_product()
            break
        if number == "3":
            ETO = input("ETO> ")
            prof = Profile.get_instance()
            prof.save_to_history("Разработчик накинул тебе "+str(ETO)+" ETO ;)\n")
            prof.set_ETO(int(ETO))
            break
        if number == "4":
            tool_id = input("tool_id> ")
            price   = input("price> ")
            prof = Profile.get_instance()
            prof.add_tools_id(tool_id, price)
            break
        if number == "4.5":
            prof = Profile.get_instance()
            tool_id = input("tool_id> ")
            prof.del_tools_id(tool_id)
            print("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Предмет " + str(tool_id) + " успешно удален!"))
            break
        if number == "5":
            prof = Profile.get_instance()
            prof.print_quest_reward_setting()
            prof.edit_quest_reward_setting()
            break
        if number == "6":
            prof = Profile.get_instance()
            prof.set_all_fields_default()
            break
        if number == "7":
            break
        else:
            print("\033[33m{}".format("[WARNING]: ")+"\033[0m{}".format("выбран не верный номер."))



def get_menu():
    while True:
        print("Выберете номер:")
        print("1. Ежедневны задания")
        print("2. Одиночные задания")
        print("3. Задания привычки")
        print("4. История баланса ETO")
        print("5. Магазин инструментов")
        print("6. Установить ID врага")
        print("6.5. Открыть Smart Electronics.")
        print("7. Инвентарь")
        print("8. Правила")
        print("9. Назад")
        print("10. Для разработчиков")
    
        number = input("> ")
        if number == "1":
            get_menu_DailyTask()
            break
        if number == "2":
            get_menu_SingleTask()
            break
        if number == "3":
            get_menu_HabitTask()
            break
        if number == "4":
            get_history()
            break
        if number == "5":
            get_store()
            break
        if number == "6":
            get_installer_NPC()
            break
        if number == "6.5":
            get_smart_electronics_menu()
            break
        if number == "7":
            get_inventory()
            break
        if number == "9":
            break
        if number == "10":
            get_menu_developer()
            break
        else:
            print("\033[33m{}".format("[WARNING]: ")+"\033[0m{}".format("выбран не верный номер."))



def buy(tool_id):
    global store_ETO, store

    prof = Profile.get_instance()
    price = store.get(tool_id)          # получаем цену за инструмент
    if price == None:                   # проверяем наличие товара
        print("\033[31m{}".format("ERROR: ")+"\033[0m{}".format("Данного товара нет!"))
        return
    balance = int(prof.get_ETO())
    price = int(price)
    if balance < price:                 # проверяем достаточно ли ETO
        print("\033[31m{}".format("ERROR: ")+"\033[0m{}".format("Не достаточно средств!"))
        return
    history_line = "Куплен: "+str(tool_id)+" за "+str(price) 
    prof.save_to_history(history_line)  # заносим в историю
    prof.set_ETO(balance-price)         # вычетаем из баланса игрока сумму за товар
    del store[tool_id]                  # удаляем инструмент из магазина
    store_ETO = store_ETO+price         # увеличиваем баланс продавца
    price = price / 2                   # уменьшаем стоимость проданного инструмента
    prof.add_tools_id(tool_id, price)   # добавляем инструмент в инвентарь
    
def sell(tool_id):
    global store_ETO, store
    
    prof = Profile.get_instance()                   
    price = prof.get_price_of_tools_id(tool_id)     # получаем цену за инструмент
    if price == None:                               # проверяем наличие предмета для продажи
        print("\033[31m{}".format("ERROR: ")+"\033[0m{}".format("Нет предмета для продажи!"))
        return
    balance = int(store_ETO)
    price = int(price)
    if balance < price:                             # проверяем достаточно ли ETO
        print("\033[31m{}".format("ERROR: ")+"\033[0m{}".format("У продовца не достаточно средств :("))
        return
    history_line = "Продан: "+str(tool_id)+" за "+str(price)
    prof.save_to_history(history_line)              # заносим в историю
    store_ETO = balance-price                       # вычетаем из баланса продовца сумму за товар
    prof.del_tools_id(tool_id)                      # удаляем инструмент из магазина
    prof.set_ETO(prof.get_ETO() + price)            # увеличиваем баланс игрока
    price = price*2                                 # делаем наценку на купленный инструмент
    store[tool_id] = price                          # добавляем инструмент в магазин

# "gun_damage=200_strong=2" == ['gun', ['damage', '200'], ['strong', '2']]
def decoding_of_characteristics(char_line):
    Profile.decoding_of_characteristics(char_line)
    
def apply_to_characteristics(char_line, up=True): # char_line == tool_id
    Profile.apply_to_characteristics(char_line, up=True)

def keeping_tool(tool_id):
    Profile.keeping_tool(tool_id)

def take_off(tool_id):
    Profile.take_off(tool_id)

def get_inventory():
    print("\033[32m{}".format("Inventory:")+"\033[0m{}".format("\n"))
    prof = Profile.get_instance()
    tools = prof.get_tools_id()
    while True:
        for tool, price in tools.items():
            print("Инструмент: "+tool)
            print("Его можно продать в магазине за "+str(price)+" ETO.\n\n")
            
        keep_tool      = prof.get_keep_tool()
        slots          = prof.get_slots()
        slots_occupied = prof.get_slots_occupied()
        print("\nЭкиперованно("+str(slots_occupied)+" из "+str(slots)+"):")
        for tool in keep_tool:
            print("Инструмент: "+tool)
        print("\nMenu: ----------------------")
        print("1. Экипировать")
        print("2. Снять предмет")
        print("3. Назад.")
        text = input("> ")
        if text == "1":
            tool_id = input("tool_id> ")
            keeping_tool(tool_id)
            break
        if text == "2":
            tool_id = input("tool_id> ")
            take_off(tool_id)
            break
        if text == "3":
            return
        else:
            print("\033[33m{}".format("[WARNING]: ")+"\033[0m{}".format("выбран не верный номер."))
    
   
# метод только проверяет актуальность задачь и наносит урон игроку за про$бы.
def check_relevance_task():
    # Проверка Одиночных заданий:
    for ID, task in list(single_task_dict.items()):
        res = task.check_complition_time()
    
        if res == True:                         # если игрок просрочил задание
            npc = NPC.get_instance()
            if npc.installed_contender != "None":
                prof = Profile.get_instance()
                npc_attack(prof)                # Наносим игроку урон
            del single_task_dict[ID]            # удалить задачу
    
    # Проверка заданий Привычек:
    for ID, task in list(habit_task_dict.items()):
        res = task.check_reset_time()
        if int(res) == 1 or int(res) == 2:       # если дата уже прошла или она сегодня, то пора произвести сброс серии
            task.reset_series_point()
    
    # Проверка Ежедневных заданий:
    for ID, task in list(daily_task_dict.items()):
        if task.get_status() == "Active":        # Если задание активно
            if task.check_day_end() == True:
                task.set_status("No active")     # Если так, то сделать задние не активным, так как день прошел, а задание не выполнено
                npc = NPC.get_instance()
                if npc.installed_contender != "None":
                    prof = Profile.get_instance()
                    npc_attack(prof)             # npc атакует, потому что день прошел, а задание не выполнено!
            start_date = task.get_start_date()   # Получаем дату начала
            if task.check_time(start_date) == 1 or task.check_time(start_date) == True: # Если дата начала уже прошла или дата повтора сегодня наступила, то и день прошел с момента создания прошел - итог: игрок не успел выполнить задание в срок
                task.set_status("No active")     # Если так, то сделать задние не активным
                npc = NPC.get_instance()
                if npc.installed_contender != "None":
                    prof = Profile.get_instance()
                    npc_attack(prof)             # и нанести игроку урон от врага, если враг есть
        res = task.check_repeat_time()           # Далее, получаем ответ на вопрос: наступила ли дата повтора задания
        if res == True:                          # И если дата уже наступила, то пора снова задание делать активным
            task.set_status("Active")            # Делаем задание активным
            


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

