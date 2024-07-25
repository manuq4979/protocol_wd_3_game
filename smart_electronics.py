import time, json


def hello_user():
	amblema=""
	#print("\033[47m{}".format(" "))
	with open("hello_user_art.txt", "r") as fd:
		amblema = fd.read()
	
	
	i = 0
	for e in amblema:
		if e == "@":
			print("\033[37m{}".format("\033[40m{}".format(e)), end="")
			print("\033[0m{}".format(""), end="")
		else:
			print("\033[30m{}".format("\033[47m{}".format(e)), end="")
			print("\033[0m{}".format(""), end="")
			
		if i == 54:
			time.sleep(0.05)
			i=0
		
		i = i+1
	
	print("\033[32m{}".format("\n[INFO]: ")+"\033[0m{}".format("Welcom to Smart Electronic system!\n\n"))



dns_base_dict = {} # IP : Smart_Electronics
PS1 = "\033[32m{}".format("user_wd@selectronic") + "\033[0m{}".format(":") + "\033[34m{}".format("~#") + "\033[0m{}".format(" ")
 

class Smart_Electronics:
    @staticmethod
    def get_instance():
        if "_instance" not in Smart_Electronics.__dict__:
            Smart_Electronics._instance = Smart_Electronics()
            return Smart_Electronics._instance
        else:
            return Smart_Electronics._instance
    
    def __init__(self):
        # инициализация должна быть из файла!
        with open("DataApp/smart_electronics.txt", "r", encoding="utf-8") as file:
            json_string = file.read()
            try:
                arr = json.loads(json_string)
                
                self.user_profile = ""                          # Профиль игрока, инициализируется в poit_of_entry(...)
                
                self.name = arr[0]
                self.network_interface = int(arr[1])            # имеет или не имеет выход в интернет
                self.remote_access = int(arr[2])                # имеет или не имеет удаленный доступ
                self.operation_system = int(arr[3])             # есть или нет ОС
                self.possibility_of_flashing = int(arr[4])      # возможно ли перепрошить или нет
                self.artificial_intelligence = int(arr[5])      # есть ли ИИ
                self.connection_port = int(arr[6])              # есть ли физические порты для подключения
                self.user_interface = int(arr[7])               # есть ли пользовательский интерфейс или нет(локальный или через интернет, например)
                self.control_panel = int(arr[8])                # есть ли панель управления или нет(типо физичесого терминала)
                self.write = int(arr[9])                        # доступна ли запись в storage или нет
                self.read = int(arr[10])                        # доступно ли чтение из storage или нет
            
                self.access_algorithm_dict = arr[11]            # Список целей, список NPC которые имеют карты доступа.
                self.storage = arr[12]                          # Тут трофеи - инструменты, ETO, карты доступа. Их может быть сколько угодно, но больше чем у NPC.
            except json.decoder.JSONDecodeError:                # Это исключение значит, что файл конфигурации пуст, код ниже задат дефолтные значения.
                self.set_all_fields_default()
                arr = self.get_all_fields()
                with open("DataApp/smart_electronics.txt", "w+", encoding="utf-8") as file:
                    json_string = json.dumps(arr)
                    file.write(json_string)
                    print("Save profile data!")

    def get_all_fields(self):
        return [self.name, self.network_interface, self.remote_access, self.operation_system, self.possibility_of_flashing, self.artificial_intelligence, self.connection_port, self.user_interface, self.control_panel, self.write, self.read, self.access_algorithm_dict, self.storage]

    def set_all_fields_default(self):
        self.user_profile = ""
        
        self.name = ""
        self.network_interface = 1
        self.remote_access = 1
        self.operation_system = 1
        self.possibility_of_flashing = 1
        self.artificial_intelligence = 1
        self.connection_port = 1
        self.user_interface = 1
        self.control_panel = 1
        self.write = 1
        self.read = 1
    
        self.access_algorithm_dict = {}
        self.storage = []
        print("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Все значения Smart Electronics установлены по умолчанию!"))

    def set_access_algorithm_dict(self, access_algorithm_dict):
        self.access_algorithm_dict = access_algorithm_dict
    
    def set_storage(self, storage):
        self.storage = storage
    
    def print_SE(self):
        if self.name == "":
            print("\033[33m{}".format("[WARNING]: ")+"\033[0m{}".format("Ещё нет активвного подключения."))
            connection = False
            return connection
            
        print("\n")
        print("\033[31m{}".format("["+self.name+"]")+"\033[0m{}".format(": "))
        
        access = "Доступно" if self.network_interface == 1 else "Не доступно"
        print("\033[32m{}".format("[Выход в интернет]: ")+"\033[0m{}".format(access))
        
        access = "Доступно" if self.remote_access == 1 else "Не доступно"
        print("\033[32m{}".format("[Удаленный доступ]: ")+"\033[0m{}".format(access))
        
        access = "Есть" if self.operation_system == 1 else "Нет"
        print("\033[32m{}".format("[Операционная система]: ")+"\033[0m{}".format(access))
        
        access = "Доступно" if self.possibility_of_flashing == 1 else "Не доступно"
        print("\033[32m{}".format("[Возможность прошивки]: ")+"\033[0m{}".format(access))
        
        access = "Есть" if self.artificial_intelligence == 1 else "Нет"
        print("\033[32m{}".format("[Исскуственный интелект]: ")+"\033[0m{}".format(access))
        
        access = "Доступно" if self.connection_port == 1 else "Не доступно"
        print("\033[32m{}".format("[Физические порты]: ")+"\033[0m{}".format(access))
        
        access = "Есть" if self.user_interface == 1 else "Нет"
        print("\033[32m{}".format("[Пользовательский интерфейс]: ")+"\033[0m{}".format(access))
        
        access = "Есть" if self.control_panel == 1 else "Нет"
        print("\033[32m{}".format("[Физическая панель управления]: ")+"\033[0m{}".format(access))
        
        access = "Доступно" if self.write == 1 else "Не доступно"
        print("\033[32m{}".format("[Запись в хранилище]: ")+"\033[0m{}".format(access))
        
        access = "Доступно" if self.read == 1 else "Не доступно"
        print("\033[32m{}".format("[Чтение из хранилище]: ")+"\033[0m{}".format(access))
        
        print("\n")
        if self.read == 1:
            print("\033[32m{}".format("[Хранилище]: ")+"\033[0m{}".format(self.storage))
            print("\033[32m{}".format("[Цели имеющие доступ к устройству]: ")+"\033[0m{}".format(self.access_algorithm_dict))
        else:
            print("\033[32m{}".format("[Хранилище]: ")+"\033[0m{}".format("***************"))
            print("\033[32m{}".format("[Цели имеющие доступ к устройству]: ")+"\033[0m{}".format("***************"))
        print("\n")
        
        connection = True
        return connection
        
        

# Пример строки:
# "name_NI=1_RM=0_OS=1_PoF=0_AI=0_CP=0_UI=1_CP2=0_W=0_R=0+S;gun_damage=100_charge=100;gun_recharge=100+AAD;bot_HP=100_armor=200_damage=100_strong=3_critical-dmg=45_drop-trophy:smart-card=write=True"
def decoding_of_characteristics_SE(char_line):
        chars = char_line.split("+")
        
        base_char = chars[0]
        storage =  chars[1]
        access_algorithm_dict = chars[2]
        
        base_char = base_char.split("_")
        name = base_char[0]
        base_char.remove(name)
        base_char_res = []
        base_char_res.append(name)
        for char in base_char:
            char = char.split("=")
            base_char_res.append(char)
        
        storage = storage.split(";")
        
        access_algorithm_dict = access_algorithm_dict.split(";")
        
        return [base_char_res, storage, access_algorithm_dict]

def apply_to_characteristics_SE(char_line):
    se = Smart_Electronics.get_instance()
    
    all_chars = decoding_of_characteristics_SE(char_line)
    # print(all_chars)
    base_char_all           = all_chars[0]
    storage                 = all_chars[1]
    access_algorithm_dict   = all_chars[2]
    
    name = base_char_all[0]
    se.name = name                               # name - имя устройства
    base_char_all.remove(name)
    name = storage[0]
    storage.remove(name)
    name = access_algorithm_dict[0]
    access_algorithm_dict.remove(name)
    
    se = Smart_Electronics.get_instance()
    
    se.network_interface       = int(base_char_all[0][1]) # NI - network_interface
    se.remote_access           = int(base_char_all[1][1]) # RA - remote_access
    se.operation_system        = int(base_char_all[2][1]) # OS - operation_system
    se.possibility_of_flashing = int(base_char_all[3][1]) # PoF - possibility_of_flashing
    se.artificial_intelligence = int(base_char_all[4][1]) # AI - artificial_intelligence
    se.connection_port         = int(base_char_all[5][1]) # CP - connection_port
    se.user_interface          = int(base_char_all[6][1]) # UI - user_interface
    se.control_panel           = int(base_char_all[7][1]) # CP2 - control_panel
    se.write                   = int(base_char_all[8][1]) # W - write
    se.read                    = int(base_char_all[9][1]) # R - read
    
    se.set_access_algorithm_dict(access_algorithm_dict)
    se.set_storage(storage)
    
    print("\033[32m{}".format("\n[INFO]: ")+"\033[0m{}".format("Характеристики успешно пременены к классу SE!"))



def set_new_soft():
    while True:
        print("\n")
        print("NI == "+str(se.network_interface)+" # NI - network_interface")
        print("RA == "+str(se.remote_access)+" # RA - remote_access")
        print("OS == "+str(se.operation_system)+" # OS - operation_system")
        print("PoF == "+str(se.possibility_of_flashing)+" # PoF - possibility_of_flashing")
        print("AI == "+str(se.artificial_intelligence)+" # AI - artificial_intelligence")
        print("CP == "+str(se.connection_port)+" # CP - connection_port")
        print("UI == "+str(se.user_interface)+" # UI - user_interface")
        print("CP2 == "+str(se.control_panel)+" # CP2 - control_panel")
        print("W == "+str(se.write)+" # W - write")
        print("R == "+str(se.read)+" # R - read")
        
        print("\n")
        print("[1]: Назад.")
        
        soft = input("> ")
        if soft == "1":
            return
        
        if soft == "NI":
            new_bool = input("NI> ") # NI - network_interface
            if new_bool == "1" or new_bool == "0":
                se.network_interface = int(new_bool)
            else:
                print("\033[31m{}".format("[ERROR]: ")+"\033[0m{}".format("Только 1 или 0!"))
        if soft == "RA":
            new_bool = input("RA> ") # RA - remote_access
            if new_bool == "1" or new_bool == "0":
                se.remote_access = int(new_bool)
            else:
                print("\033[31m{}".format("[ERROR]: ")+"\033[0m{}".format("Только 1 или 0!"))
        if soft == "OS":
            new_bool = input("OS> ") # OS - operation_system
            if new_bool == "1" or new_bool == "0":
                se.operation_system = int(new_bool)
            else:
                print("\033[31m{}".format("[ERROR]: ")+"\033[0m{}".format("Только 1 или 0!"))
        if soft == "PoF":
            new_bool = input("PoF> ") # PoF - possibility_of_flashing
            if new_bool == "1" or new_bool == "0":
                se.possibility_of_flashing = int(new_bool)
            else:
                print("\033[31m{}".format("[ERROR]: ")+"\033[0m{}".format("Только 1 или 0!"))
        if soft == "AI":
            new_bool = input("AI> ") # AI - artificial_intelligence
            if new_bool == "1" or new_bool == "0":
                se.artificial_intelligence = int(new_bool)
            else:
                print("\033[31m{}".format("[ERROR]: ")+"\033[0m{}".format("Только 1 или 0!"))
        if soft == "CP":
            new_bool = input("CP> ") # CP - connection_port
            if new_bool == "1" or new_bool == "0":
                se.connection_port = int(new_bool)
            else:
                print("\033[31m{}".format("[ERROR]: ")+"\033[0m{}".format("Только 1 или 0!"))
        if soft == "UI":
            new_bool = input("UI> ") # UI - user_interface
            if new_bool == "1" or new_bool == "0":
                se.user_interface = int(new_bool)
            else:
                print("\033[31m{}".format("[ERROR]: ")+"\033[0m{}".format("Только 1 или 0!"))
        if soft == "CP2":
            new_bool = input("CP2> ") # CP2 - control_panel
            if new_bool == "1" or new_bool == "0":
                se.control_panel = int(new_bool)
            else:
                print("\033[31m{}".format("[ERROR]: ")+"\033[0m{}".format("Только 1 или 0!"))
        if soft == "W":
            new_bool = input("W> ") # W - write
            if new_bool == "1" or new_bool == "0":
                se.write = int(new_bool)
            else:
                print("\033[31m{}".format("[ERROR]: ")+"\033[0m{}".format("Только 1 или 0!"))
        if soft == "R":
            new_bool = input("R> ") # R - read
            if new_bool == "1" or new_bool == "0":
                se.read = int(new_bool)
            else:
                print("\033[31m{}".format("[ERROR]: ")+"\033[0m{}".format("Только 1 или 0!"))
        else:
            print("\033[33m{}".format("[WARNING]: ")+"\033[0m{}".format("Не верный пункт меню!"))
            break
            
        
        print("\033[32m{}".format("\n[INFO]: ")+"\033[0m{}".format("Обновление базовых характеристик для SE выполненно успешно!"))
    
def set_storage():
    se = Smart_Electronics.get_instance()
    print("\033[33m{}".format("[WARNING]: ")+"\033[0m{}".format("Изменение подразумевает что вы скопируете харнилище и тут сможите уже измененный вид вставить!"))
    print("\033[33m{}".format("[WARNING]: ")+"\033[0m{}".format("Также подразумевает что будет использован тот же шаблон!"))
    print("storage == "+str(se.get_storage()))
    storage = input("new storage> ")
    se.set_storage(storage)

# Главный код отвечающий за изменение полей SE:
def get_access_card():
    se = Smart_Electronics.get_instance()
    inventory = se.user_profile.get_tools_id()

    for tool_id, price in inventory.items():
        if tool_id.find("access_card") != -1:
            if tool_id.find("read") != -1:
                se.read = 1
                print("\033[32m{}".format("\n[INFO]: ")+"\033[0m{}".format("Чтение доступно!"))
            if tool_id.find("write") != -1:
                se.write = 1
                print("\033[32m{}".format("\n[INFO]: ")+"\033[0m{}".format("Запись доступна!"))
            se.user_profile.del_tools_id(tool_id)
            print("\033[32m{}".format("\n[INFO]: ")+"\033[0m{}".format("Карта доступа израсходована!"))
            return True
    return False

def get_access():
    se = Smart_Electronics.get_instance()
    while True:
        print("\n")
        if se.operation_system == 1 and se.remote_access == 1 and se.network_interface == 1 and se.user_interface == 1:
            print("[1]: Удаленный доступ.")
        if se.operation_system == 1 and se.connection_port == 1 and se.control_panel == 1:
            print("[2]: Физический доступ.")
        
        print("[3]: Назад.")
        print("\n")
        
        command = input(PS1)
        
        if command == "3":
            return
        
        # Удаленный доступ:
        if se.operation_system == 1 and se.remote_access == 1 and se.network_interface == 1 and se.user_interface == 1:
            pass
        # Физичесский доступ:
        if se.operation_system == 1 and se.connection_port == 1 and se.control_panel == 1:
            access = get_access_card()
            if access == False:
                print("\033[31m{}".format("[ERROR]: ")+"\033[0m{}".format("Ошибка доступа! У вас нет карты доступа!\n"))

def get_OS_menu():
    se = Smart_Electronics.get_instance()
    print("\n")
    print("\033[32m{}".format("\n[INFO]: ")+"\033[0m{}".format("Welcom to SE OS!"))

    while True:
        print("\n")
        if se.write == 1 and se.possibility_of_flashing == 1:
            print("[1]: Перепрошить.")
        if se.write == 1:
            print("[2]: Изменить хранилище данных.")
        if se.write == 0 or se.write == 0:
            print("[3]: Получить доступ.")
        print("[4]: Назад.")
        print("\n")
        
        command = input(PS1)
        
        if command == "4":
            return
        
        if command == "1" and se.write == 1 and se.possibility_of_flashing == 1:
            set_new_soft()
            break
        if command == "2" and se.write == 1:
            set_storage()
            break
        if se.write == 0 or se.write == 0:
            get_access()
            break
        else:
            print("\033[33m{}".format("[WARNING]: ")+"\033[0m{}".format("Не верный пункт меню!"))


def set_SE():
    SE_ID = input("SE_ID> ")
    apply_to_characteristics_SE(SE_ID)
    
    
    
def print_menu_smart_electronics():
    print("[1]: Текущие подключение.")
    print("[2]: Подключиться.")
    print("[3]: Назад.")
    
def select_item(command):
    se = Smart_Electronics.get_instance()
    
    if command == "1":
        if (se.operation_system == 1 and se.remote_access == 1 and se.network_interface == 1 and se.user_interface == 1) or (se.operation_system == 1 and se.connection_port == 1 and se.control_panel == 1): # Тут проверяем подключаемое ли вообще устройство.
            connection = se.print_SE()
            if connection != False:
                get_OS_menu()
        else:
            print("\033[31m{}".format("ERROR: ")+"\033[0m{}".format("Устройстов не предусматривает подключение!"))
        return
    if command == "2":
        set_SE()
        return
    
    print("\033[33m{}".format("[WARNING]: ")+"\033[0m{}".format("Не верный пункт меню!"))
    

def poit_of_entry(computer, prof):
    # Нужно чтобы получить доступ к инвентарю игрока, только для получения карты доступа, всё остальное(из хранилища данных) добавляется в инвентарь вручную!
    se = Smart_Electronics.get_instance()
    se.user_profile = prof
    
    if computer == False:
        print("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("У вас нет компьтера чтобы пользоваться сетью!"))
        return
    
    hello_user()
    while True:
        print("\n######################################################\n")
        print_menu_smart_electronics()
        print("\n######################################################\n")
        
        command = input(PS1)
        
        if command == "3":
            return
        select_item(command)
        
            
# Сохранить данные модуля в файл:
def save_data_SE():
    se = Smart_Electronics.get_instance()
    arr = se.get_all_fields()
    with open("DataApp/smart_electronics.txt", "w+", encoding="utf-8") as file:
        json_string = json.dumps(arr)
        file.write(json_string)
        print("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Save Smart Electronics data!"))

# Test main:
# computer = True
# poit_of_entry(computer)
