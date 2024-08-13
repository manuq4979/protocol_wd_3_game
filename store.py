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

def hot_key(text):
    if checking_input(text) == False:
        return
    store_menu_item     = int(text[0])
    store_tool_id_index = int(text[1:])
    

#-----------------------------------------#
# Тут вывод оставить как есть! пока что.  #
#-----------------------------------------#
def get_store():
    from functions import buy, sell
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
        print("1. Купить")
        print("2. Продать")
        print("0. Назад")
        print("\n#######################################################\n")
        text = input("> ")
        
        if text == "0":
            return
        
        if text == str(BUY):
            index = text
            tool_id = list(store.keys())[index]
            buy(tool_id)
            continue
        if text == str(SELL):
            tool_id = input("tool_id> ")
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
