import json, os

BUY = 1
SELL = 2

with open("DataApp/store.txt", "r", encoding="utf-8") as file:
    json_string = file.read()
    arr = json.loads(json_string)
    store =  arr[0]                 # хранит  tool_id : ETO
    store_ETO = arr[1]


# Сохранить данные модуля в файл:
def save_data_store():
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


def buy_reload_tool(prof, buy):
	charge = 0
	my_tool_id = ""
	my_price = 0
	inventory = list(prof.get_tools_id().keys())
	
	index = input("index> ")

	if checking_input(str(index)) == False:
		print("\033[31m{}".format("[ERROR]: ")+"\033[0m{}".format("Не допустимое числовое значение!"))
		input("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Нажмите <enter> чтобы продолжить..."))
		return
	index = int(index)
	char_line = inventory(index-1)
	my_tool_id = char_line
	my_price = prof.get_tools()[my_tool_id]
	
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
                charge = int(input("charge> "))
                if checking_input(str(charge)) == False:
                        break
                price = int(charge/100)*50 # каждые 100 - это 50
                if buy(price, no_add_to_inventory=True) == False:
                        print("\033[31m{}".format("[ERROR]:")+"\033[0m{}".format("Отменено!"))
                        return
                charge = int(price*100)    # если ввести 453 - то будет округлено до 400, потому что продаётся лишь по 100 зарядов.
                result[i][1] = str(charge)
            new_tool += result[i][0]+"="+result[i][1]+"_"
	prof.del_tools_id(my_tool_id)
	new_tool = new_tool[0:-1]
	prof.add_tools_id(new_tool, my_price)
	print("\033[32m{}".format("[INFO]:")+"\033[0m{}".format("Готово!"))
	input("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Нажмите <enter> чтобы продолжить..."))
	
	

#-----------------------------------------#
# Тут вывод оставить как есть! пока что.  #
#-----------------------------------------#
def get_store():
    from functions import buy, sell, get_inventory, Profile
    prof = Profile.get_instance()
    while True:
        print("\n#######################################################\n")
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
        print("[1]: Купить")
        print("[2]: Продать")
        print("[3]: Инвентарь")
        print("[4]: Зарядить")
        print("[0]: Назад")
        print("\n#######################################################\n")
        text = input("> ")
        
        if text == "0":
            return
        if text == "3":
            get_inventory()
        if text == "4":
            buy_reload_tool(prof, buy)
        
        text = hot_key(text, prof)
        if text == False:
            continue
        
        
        if text[0] == BUY:
            tool_id = text[1]
            buy(tool_id)
            continue
        if text[0] == SELL:
            tool_id = text[1]
            sell(tool_id)
            continue
        else:
            print("\033[33m{}".format("[WARNING]: ")+"\033[0m{}".format("не верный запрос!"))
        


def add_product():
    tool_id = input("tool_id> ")
    price   = input("price> ")
    store[tool_id] = price
    print("\033[32m{}".format("[INFO]:")+"\033[0m{}".format("Готово!\n\n"))
    
def del_product():
    tool_id = input("tool_id> ")
    del store[tool_id]
    print("\033[32m{}".format("[INFO]:")+"\033[0m{}".format("Предмет удален!\n\n"))
