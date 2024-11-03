import json, os

BUY = 1
SELL = 2

def create_default_store_file():
    if os.path.exists("DataApp/store.txt") != True:
        with open("DataApp/store.txt", "w+", encoding="utf-8") as file:
            json_string = json.dumps([{}, 0])
            file.write(json_string)

def init_store():
    create_default_store_file()
    with open("DataApp/store.txt", "r", encoding="utf-8") as file:
        json_string = file.read()
        arr = json.loads(json_string)
        store =  arr[0]                 # хранит  tool_id : ETO
        store_ETO = int(arr[1])

        return [store, store_ETO]

store = init_store()[0]
store_ETO = init_store()[1]

# Сохранить данные модуля в файл:
def save_data_store(store_ETO, save_only_store=False):
    global store

    create_default_store_file()

    if save_only_store == True:
        store_ETO = init_store()[1]

    with open("DataApp/store.txt", "w+", encoding="utf-8") as file:
        json_string = json.dumps([store, store_ETO])
        file.write(json_string)
        print("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Save store data!"))

def checking_input(input_text):  
    if len(input_text) <= 1:
        return False
 
    if input_text.isdigit() == False:
        print("\033[31m{}".format("[ERROR]: ")+"\033[0m{}".format("Допустимы лишь числовые значения!"))
        input("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Нажмите <enter> чтобы продолжить..."))     
        print("\n" * 100) # очищаем экран консоли
        return False
 
    return True

def hot_key(text, prof):
    if checking_input(text) == False:
        return False
    store_menu_item     = int(text[0])
    store_tool_id_index = int(text[1:])
    index               = store_tool_id_index-1
    tool_id = ""
    if store_menu_item == BUY:
        tool_id         = list(store.keys())[index]
    elif store_menu_item == SELL:
        inventory       = list(prof.get_tools_id().keys())
        tool_id         = inventory[index]
    
    return [store_menu_item, tool_id]

def menu_for_buy_reload_tool():
    print("[1]: Индекс(1<INDEX>).")
    print("[0]: Назад.")

def buy_reload_tool(prof, buy):
    charge = 0
    my_tool_id = ""
    my_price = 0
    inventory = list(prof.get_tools_id().keys())

    while True:
        from functions import get_inventory_interface
        get_inventory_interface(prof, other_menu=menu_for_buy_reload_tool)
    
        index = input("> ")
        if index == "0":
            return
        index = index[1:]
        print("\n" * 100) # очищаем экран консоли
    	
        if str(index).isdigit() == False:
            print("\033[31m{}".format("[ERROR]: ")+"\033[0m{}".format("Допустимы лишь числовые значения!"))
            input("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Нажмите <enter> чтобы продолжить..."))
            print("\n" * 100) # очищаем экран консоли
            continue    
        index = int(index)
        size = len(prof.get_tools_id())
        try:
                char_line = inventory[index-1]
        except IndexError:
                print("\033[31m{}".format("[ERROR]: ")+"\033[0m{}".format("Инструмента не может быть по данному индексу!"))
                input("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Нажмите <enter> чтобы продолжить..."))
                print("\n" * 100) # очищаем экран консоли
                continue
        my_tool_id = char_line
        my_price = prof.get_tools_id()[my_tool_id]
    	
        if char_line.find("recharge") != -1:
                res = char_line.find("recharge")
                recharge = char_line[res:]
                recharge = recharge.split(":")
                return recharge
        
        chars = char_line.split("_")
        name = chars[0]
        chars.remove(name)
        result = []
        result.append(name)
        for char in chars:
                char = char.split("=")
                result.append(char)
                
        new_tool = ""
        for i in range(len(result)):
                if i == 0:
                    new_tool += result[i]+"_"
                    continue
                if result[i][0] == "charge":
                    charge = int(result[i][1])
                    charge += int(input("charge> "))
                    if str(charge).isdigit() == False:
                            print("\033[31m{}".format("[ERROR]: ")+"\033[0m{}".format("Допустимы лишь числовые значения!"))
                            input("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Нажмите <enter> чтобы продолжить..."))
                            break
                    price = int(charge/100)*50 # каждые 100 - это 50
                    if buy("no tool", no_add_to_inventory=True, service_price=price) == False:
                            print("\033[31m{}".format("[ERROR]:")+"\033[0m{}".format("Отменено!"))
                            return
                    charge = int(charge/100)*100    # если ввести 453 - то будет округлено до 400, потому что продаётся лишь по 100 зарядов.
                    result[i][1] = str(charge)
                new_tool += result[i][0]+"="+result[i][1]+"_"
        prof.del_tools_id(my_tool_id)
        new_tool = new_tool[0:-1]
        prof.add_tools_id(new_tool, my_price)
        print("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Готово!"))
        input("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Нажмите <enter> чтобы продолжить..."))
        print("\n" * 100) # очищаем экран консоли
        return


def transfer_ETO_to_storage(prof):
    global store_ETO

    print("\n#######################################################\n\n\n\n\n\n")
    print("\033[33m{}".format("[WARNING]: ")+"\033[0m{}".format("Будет взыматься коммисия - 20%!"))
    print("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("\n- Будет создан card-with-tokens_eto=X,\n  где X - это указанная сумма!\n- Предмет в инвентаре нужно просто продать\n  чтобы снять токены с носителя."))
    print("\n\n\n\n\n\n#######################################################\n")

    command = input("Введите сумму> ")
    print("\n" * 100) # очищаем экран консоли

    command.replace(" ", "")
    if command == "":
        return

    if command.isdigit() == False:
        print("\033[31m{}".format("[ERROR]: ")+"\033[0m{}".format("Допускаются лишь числа и цифры, текст и прч не допустимо!"))
        input("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Нажмите <enter> чтобы продолжить..."))
        print("\n" * 100) # очищаем экран консоли
        return

    ETO = int(command)

    if prof.get_ETO() < ETO:
        print("\033[31m{}".format("[ERROR]: ")+"\033[0m{}".format("Не достаточно средств для совершения операции!"))
        input("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Нажмите <enter> чтобы продолжить..."))
        print("\n" * 100) # очищаем экран консоли
        return

    prof.set_ETO(int(prof.get_ETO()-ETO))

    commission_rate = int(ETO * 0.2)
    prof.save_to_history("Покупка услуги \"перенос ETO на носитель\" за "+str(commission_rate)+" ETO - остальная сумму "+str(int(ETO-commission_rate))+" ETO отправилась на сам носитель.")
    storage_card = "card-with-tokens_eto="+str(int(ETO-commission_rate))
    prof.add_tools_id(storage_card, ETO-commission_rate)

    store_ETO = int(store_ETO)
    store_ETO += ETO

    save_data_store(store_ETO)
    print("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Готво, сумма коммисии составила "+str(commission_rate)+" ETO!"))
    input("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Нажмите <enter> чтобы продолжить..."))
    print("\n" * 100) # очищаем экран консоли
    return

def transfer_ETO_to_inventary(prof, tool_id):
    price = tool_id.split("=")[1]
    prof.set_ETO(int(prof.get_ETO())+int(price))
    prof.save_to_history("Продажа особого предмета: "+tool_id+" за цену "+str(price)+" ETO.")
    store_ETO = int(init_store()[1])
    store_ETO -= int(price)
    save_data_store(store_ETO)
    prof.del_tools_id(tool_id)
    print("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Пополнение счета на "+str(price)+" ETO!"))
    input("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Нажмите <enter> чтобы продолжить..."))
    print("\n" * 100) # очищаем экран консоли

# В методе use_consumables модуля se_applications есть проверка на "smartphone_consumables", с помощью str.find(), из чего следует, что строчка просто должна присутствовать.
def buy_consumables(prof):
    global store_ETO
    price = 150 # Такая вот цена за расходный материал, заряды стоят всего 50 при этом.

    i = input("укажите количество> ")

    if i.isdigit() == False:
        print("\033[31m{}".format("[ERROR]: ")+"\033[0m{}".format("Допустимы лишь числовые значения!"))
        input("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Нажмите <enter> чтобы продолжить..."))
        print("\n" * 100) # очищаем экран консоли
        return

    i = int(i)
    copy_i = i
    counter_price = price * i

    # Проверить есть ли у игрока средства
    if prof.get_ETO() < counter_price:
        print("\033[31m{}".format("[ERROR]: ")+"\033[0m{}".format("Не достаточно средств для покупки!"))
        input("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Нажмите <enter> чтобы продолжить..."))
        print("\n" * 100) # очищаем экран консоли
        return

    while i != 0:
        new_consumables_ID = 1
        there_are_coincidences = False # есть_совпадения?

        # Есть ли у игрока уже этот предмет
        size = len(list(prof.get_tools_id().values()))
        for index in range(size):
            for tool_id in list(prof.get_tools_id().keys()):
                if tool_id.find("smartphone_consumables_ID="+str(new_consumables_ID)) == -1:
                    there_are_coincidences = True
                    continue

            if there_are_coincidences == True:
                new_consumables_ID += 1
                there_are_coincidences = False
                continue


        new_consumables = "smartphone_consumables_ID="+str(new_consumables_ID)

        prof.set_ETO(int(prof.get_ETO()-price))
        prof.save_to_history("Покупка расходного материала за "+str(price)+" ETO.")
        prof.add_tools_id(new_consumables, int(price/2))
        i -= 1

    store_ETO = int(init_store()[1])
    store_ETO += counter_price

    save_data_store(store_ETO)
    print("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Готво, расходный матереал куплен в количестве "+str(copy_i)+" штук по цене "+str(counter_price)+"!"))
    input("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Нажмите <enter> чтобы продолжить..."))
    return


#-----------------------------------------#
# Тут вывод оставить как есть! пока что.  #
#-----------------------------------------#
def get_store():

    from functions import buy, sell, get_inventory, Profile
    prof = Profile.get_instance()
    while True:
        print("\n#######################################################\n")
        print("Баланс продовца: "+str(init_store()[1])+" ETO")
        print("Вашь баланс: "+str(prof.get_ETO())+" ETO")
        print("\033[32m{}".format("[Welcom to the Store menu]: ")+"\033[0m{}".format("\n"))
        index = 0
        for tool_id, ETO in store.items():
            index += 1
            print("["+str(index)+"]: "+"ID: "+str(tool_id) + "\nЦена: "+str(ETO)+" ETO")
            print("\n")
        # Элемент дизайна:
        if len(store) == 0: # если в магазине нет товара, то будет рапечатано:
            print("\n")
            print("\033[33m{}".format("[WARNING]: ")+"\033[0m{}".format("В данный момент товаров на продажу нет!\n"))
        
        print("\nMenu: ----------------------")
        print("[ 1]: Купить")
        print("[ 2]: Продать")
        print("[ 3]: Инвентарь")
        print("[ 4]: Зарядить")
        print("[ 5]: Перенести ETO на носитель.")
        print("[ 6]: Купить расходный материал.")
        print("[ 0]: Назад")
        print("\n#######################################################\n")

        text = input("> ")
        print("\n" * 100) # очищаем экран консоли
        
        if text == "0":
            return
        if text == "3":
            get_inventory()
        if text == "4":
            buy_reload_tool(prof, buy)
        if text == "5":
            transfer_ETO_to_storage(prof)
            continue
        if text == "6":
            buy_consumables(prof)
            continue
        
        try:
            text = hot_key(text, prof)
        except IndexError:
            print("\033[31m{}".format("[ERROR]: ")+"\033[0m{}".format("не верный индекс!"))
            input("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Нажмите <enter> чтобы продолжить..."))

        if text == False:
            continue
        
        
        if text[0] == BUY:
            tool_id = text[1]
            buy(tool_id)
            continue
        if text[0] == SELL:
            tool_id = text[1]
            if tool_id.find("card-with-tokens_eto=") != -1:
                transfer_ETO_to_inventary(prof, tool_id)
            else:
                sell(tool_id)
            continue
        else:
            print("\033[33m{}".format("[WARNING]: ")+"\033[0m{}".format("не верный запрос!"))
        


def add_product():
    tool_id = ""
    price = ""
    
    while True:
        tool_id = input("tool_id> ")
        tool_id = tool_id.replace(" ", "")
        if tool_id == "":
            print("\033[31m{}".format("[ERROR]: ")+"\033[0m{}".format("tool_id не указан!"))
            input("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Нажмите <enter> чтобы продолжить..."))
            continue

        price   = input("price> ")
        price = price.replace(" ", "")
        if price == "" or price.isdigit() == False:
            error_text = ""
            if price == "":
                error_text += "price не указан!"
            else:
                error_text += "price должен быть в числовых значения!"
            print("\033[31m{}".format("[ERROR]: ")+"\033[0m{}".format(error_text))
            input("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Нажмите <enter> чтобы продолжить..."))
            continue
        break
    store[tool_id] = int(price)
    save_data_store(store_ETO=0, save_only_store=True)
    print("\033[32m{}".format("[INFO]:")+"\033[0m{}".format("Готово!\n\n"))
    
def del_product():
    tool_id = input("tool_id> ")
    del store[tool_id]
    save_data_store(store_ETO=0, save_only_store=True)
    print("\033[32m{}".format("[INFO]:")+"\033[0m{}".format("Предмет удален!\n\n"))
