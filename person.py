import random, json

# Тут должена быть загрузка из фйла.

class NPC:
    @staticmethod
    def get_instance() -> 'NPC':
        if "_instance" not in NPC.__dict__:
            NPC._instance = NPC()
            return NPC._instance
        else:
            return NPC._instance

    def __init__(self):
        # инициализация должна быть из файла!
        with open("DataApp/person.txt", "r", encoding="utf-8") as file:
            json_string = file.read()
            # print(json_string)
            try:
                arr = json.loads(json_string)
            
                self.name = arr[0]
                self.HP = int(arr[1])
                self.armor = int(arr[2])
                self.damage = int(arr[3])
                self.strong = int(arr[4])
                self.critical_dmg = int(arr[5])     # % - максимум 45%
	            
                self.drop_trophy = arr[6]           # Это отдельный tool_id предмета.
                self.installed_contender = arr[7]
            except json.decoder.JSONDecodeError:    # Это исключение значит, что файл конфигурации пуст, код ниже задат дефолтные значения.
                self.set_all_fields_default()
                arr = self.get_all_fields()
                with open("DataApp/person.txt", "w+", encoding="utf-8") as file:
                    json_string = json.dumps(arr)
                    file.write(json_string)
                    print("Save NPC class data!")
	
    def get_all_fields(self): 
        return [self.name, self.HP, self.armor, self.damage, self.strong, self.critical_dmg, self.drop_trophy, self.installed_contender]  
	
    def set_all_fields_default(self):
        self.name=""
        self.HP=100
        self.armor=0
        self.damage=0
        self.strong=0
        self.drop_trophy=""
        self.installed_contender="None"
        self.critical_dmg=3
        print("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Все значения NPC класса установлены по умолчанию!"))
	
    def print_characteristics(self):
        print("Name: "+self.name)
        print("HP: "+str(self.HP))
        print("armor: "+str(self.armor))
        print("damage: "+str(self.damage))
        print("critical dmg: "+str(self.critical_dmg)+"%")
        print("drop trophy: "+str(self.drop_trophy))
	
	# "gun_damage=200_strong=2" == ['gun', ['damage', '200'], ['strong', '2']]
    def decoding_of_characteristics_NPC(self, char_line):
        res = char_line.find("drop-trophy")
        drop_trophy = char_line[res:]
        drop_trophy = drop_trophy.split(":")
        n = res-1
        char_line = char_line[:n]
        
        drop_trophy = ["drop-trophy", drop_trophy[1:]] # во вложенном массиве под индексом 0 идет имя - "drop-trophy", которое уже добавлялось, пожтому создаем вложенный массив без индекса 0!
        new_dt = []
        print(drop_trophy[1])
        continue_flag = 0
        for i in range(len(drop_trophy[1])):
            continue_flag = 0
            if drop_trophy[1][i].find("recharge") != -1:
                print(i)
                new_tool_id = drop_trophy[1][i] + ":" + drop_trophy[1][i+1]
                new_dt.append(new_tool_id)
                continue_flag = 1
            elif continue_flag == 0:
                new_dt.append(drop_trophy[1][i])
        drop_trophy.pop(1)
        drop_trophy.append(new_dt)
        
        chars = char_line.split("_")
        self.name = chars[0]
        chars.remove(self.name)
        result = []
        result.append(self.name)
        for char in chars:
            char = char.split("=")
            result.append(char)
        if len(drop_trophy) != 0:
            result.append(drop_trophy)
        
        return result
	
    def apply_to_characteristics_NPC(self, tool_id, up=True,  new_npc=False):
        tools = self.decoding_of_characteristics_NPC(tool_id)
        # print(tools)
        name = tools[0]
        tools.remove(name)
        for tool in tools:
            if tool[0] == "HP":
                self.HP = tool[1]
            if tool[0] == "armor":
                if up == False:
                    self.armor -= int(tool[1])
                if new_npc == True:
                    self.armor = int(tool[1])
                else:
                    self.armor += int(tool[1])
            if tool[0] == "damage":
                if up == False:
                    self.damage -= int(tool[1])
                if new_npc == True:
                    self.damage = int(tool[1])
                else:
                    self.damage += int(tool[1])
            if tool[0] == "strong":
                if up == False:
                    self.strong -= int(tool[1])
                if new_npc == True:
                    self.strong = int(tool[1])
                else:
                    self.strong += int(tool[1])
            if tool[0] == "critical-dmg":
                if int(tool[1]) > 45: # проверка - не привышает ли крит урон максимум.
                    print("\033[31m{}".format("[ERROR]: ")+"\033[0m{}".format("Максимум 45% может быть урон у NPC!"))
                    return
	                
                if up == False:
                    self.critical_dmg -= int(tool[1])
                if new_npc == True:
                    self.critical_dmg = int(tool[1])
                else:
                    self.critical_dmg += int(tool[1])
                    if self.critical_dmg > 45:
                        self.critical_dmg = 45
            if tool[0] == "drop-trophy":
                self.drop_trophy = tool[1]

    def keeping_tool_NPC(self, tool_id):
        self.apply_to_characteristics_NPC(tool_id)
	
    def take_off_NPC(self, tool_id):
        self.apply_to_characteristics_NPC(tool_id, up=False)

    def get_drop_trophy(self):
        return self.drop_trophy
    
    def set_drop_trophy(self, drop_trophy):
        self.drop_trophy = drop_trophy

    def set_new_npc(self, NPC_ID):
        self.apply_to_characteristics_NPC(NPC_ID, up=False, new_npc=True)
        self.installed_contender = True
        

def add_NPC(tool_id):
    npc = NPC.get_instance()
    npc.keeping_tool_NPC(tool_id)
    npc.installed_contender = True
    
def del_NPC():
    npc = NPC.get_instance()
    npc.installed_contender = "None"
    
def get_installer_NPC():
    npc = NPC.get_instance()
    print("\033[32m{}".format("Set NPC_ID:")+"\033[0m{}".format(""))    # NPC_ID- это тот же tool_id, отличается лишь тем что есть drop-trophy
    NPC_ID = input("NPC_ID> ")
    if NPC_ID == "" or NPC_ID == None:
        print("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("NPC не был добавлен!"))
        return
    npc.set_new_npc(NPC_ID)

# если выпадет крит урон, вернет урон помноженный в разы
# иначе, вернет обычный урон
def calculate_critical_dmg_NPC():
    npc = NPC.get_instance()
    crit_dmg = npc.critical_dmg
    r = random.randint(1, 100)
    if r <= crit_dmg:
        strong = npc.strong
        result = 1.5+((strong*50) / (strong+200))
        result = round(result, 1)
        crit_dmg = npc.damage * result
        print("\033[32m{}".format("[INFO]:")+"\033[0m{}".format("Враг нанес критический урон, урон был "+str(crit_dmg)))
        return crit_dmg
    return npc.damage

def npc_attack(prof):
    npc = NPC.get_instance()
    damage = calculate_critical_dmg_NPC()  # Получаем значение урона врага, если выпадет крит урон, то игроку не повезло
    
    # Враг не был установлен - игрок врага не ставил:
    if npc.installed_contender == "None":
        return
    
    if int(prof.get_HP()) <= 0:
        prof.death()
    if int(prof.get_armor()) == 0:         # Если защиты нет, то наносим урон по HP игрока
        HP = int(prof.get_HP())          
        new_HP = HP - damage               # Вычетаем из HP значение урона
        prof.set_HP(new_HP)
    if int(prof.get_armor()) > 0:          # Если защита у игрока больше 0 - т.е есть, то
        armor = int(prof.get_armor())
        armor = armor - damage             # Вычетаем из защиты значение урона
        if armor < 0:                      # Если после нанесения урона по защите, защита ушла в минус, значит защиты было меньше чем значение урона и тогда
            HP = prof.get_HP()
            new_HP = int(HP) + int(armor)  # Всё отрицательное значение уходит в HP, т.е защита немного снизела урон, а остаток ударил по HP
            prof.set_HP(new_HP)
            prof.set_armor(0)              # Но значение защиты не может быть отрицательным, поэтому оно устанавливается в 0
        if armor >= 0:
            prof.set_armor(armor)          # Если же значение защиты не отрицательное после вычета значения урона, значит броня выдержала и мы устанавливаем броню в остаток от вычета урона
            



# Сохранить данные модуля в файл:
def save_data_person():
    npc = NPC.get_instance()
    arr = npc.get_all_fields()
    with open("DataApp/person.txt", "w+", encoding="utf-8") as file:
        json_string = json.dumps(arr)
        file.write(json_string)
        print("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Save NPC class data!"))
