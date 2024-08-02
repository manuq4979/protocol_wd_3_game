import json, os


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


    

#-----------------------------------------#
# Тут вывод оставить как есть! пока что.  #
#-----------------------------------------#
def get_store():
    from functions import buy, sell
    while True:
        print("\n#######################################################\n")
        print("\033[32m{}".format("[Welcom to the Store menu]: ")+"\033[0m{}".format("\n"))
        for tool_id, ETO in store.items():
            print("ID: "+str(tool_id) + "\nЦена: "+str(ETO)+" ETO")
            print("\n")
        # Элемент дизайна:
        if len(store) == 0: # если в магазине нет товара, то будет рапечатано:
            print("\n")
            print("\033[33m{}".format("[WARNING]: ")+"\033[0m{}".format("В данный момент товаров на продажу нет!\n"))
        
        print("\nMenu: ----------------------")
        print("1. Купить")
        print("2. Продать")
        print("3. Назад")
        print("\n#######################################################\n")
        text = input("> ")
        
        if text == "3":
            return
        
        if text == "1":
            tool_id = input("tool_id> ")
            buy(tool_id)
            continue
        if text == "2":
            tool_id = input("tool_id> ")
            sell(tool_id)
            continue
        else:
            print("\033[33m{}".format("[WARNING]: ")+"\033[0m{}".format("не верный запрос!"))
        


def add_product():
    tool_id = input("tool_id> ")
    price   = input("price> ")
    store[tool_id] = price
    print("\033[32m{}".format("[info]:")+"\033[0m{}".format("Готово!\n\n"))
    
def del_product():
    tool_id = input("tool_id> ")
    del store[tool_id]
    print("\033[32m{}".format("[info]:")+"\033[0m{}".format("Предмет удален!\n\n"))
