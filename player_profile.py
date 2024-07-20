import random, json

class Profile:
    @staticmethod
    def get_instance() :
        if "_instance" not in Profile.__dict__:
            Profile._instance = Profile()
            return Profile._instance
        else:
            return Profile._instance
    
    def __init__(self):
        # инициализация должна быть из файла!
        with open("DataApp/profile.txt", "r", encoding="utf-8") as file:
            json_string = file.read()
            #print(json_string)
            try:
                arr = json.loads(json_string)
            
                self.HP = arr[0]                    # 100 по умолчанию
                self.armor = arr[1]                 # 0 по умолчанию
                self.strong = arr[2]                # 1 из 15 по умолчанию
                self.intellect = arr[3]             # 1 из 15 по умолчанию
                self.damage = arr[4]                # 30 по умолчанию
                self.critical_dmg = arr[5]          # 3% шанс по умолчанию, максимум 45%
                
                self.quest_reward_setting = arr[6]  # {"+" : 1, "++" : 2, "+++" : 3, "++++" : 4} по умолчанию
                
                self.ETO = arr[7]                   # 0 по умолчанию
                self.tools_id = arr[8]              # {} == Инструменты по умолчанию - {tool_id : price, ...}
                self.pers_id = arr[9]               # [] Персонажи по умолчанию
                
                self.slots_occupied = arr[10]       # 0 занятые слоты по умолчанию
                self.slots = arr[11]                # всего 5 слотов по умолчанию. вероятно будет возможность расширять, но вряд ли
                self.keep_tool = arr[12]            # {} экипированное снаряжение по умолчанию
                
                self.history = arr[13]              # [] по умолчанию
            except json.decoder.JSONDecodeError:                      # Это исключение значит, что файл конфигурации пуст, код ниже задат дефолтные значения.
                self.set_all_fields_default()
                arr = self.get_all_fields()
                with open("DataApp/profile.txt", "w+", encoding="utf-8") as file:
                    json_string = json.dumps(arr)
                    file.write(json_string)
                    print("Save profile data!")
    
    def get_all_fields(self):
        return [self.HP, self.armor, self.strong, self.intellect, self.damage, self.critical_dmg, self.quest_reward_setting, self.ETO, self.tools_id, self.pers_id, self.slots_occupied, self.slots, self.keep_tool, self.history]
    
    def set_all_fields_default(self):
        self.HP = 100
        self.armor = 0
        self.strong = 1
        self.intellect = 1
        self.damage = 30
        self.critical_dmg = 3
        self.quest_reward_setting = {"+" : 1, "++" : 2, "+++" : 3, "++++" : 4}
        self.ETO = 0
        self.tools_id = {}
        self.pers_id = []
        self.slots_occupied = 0
        self.slots = 5
        self.keep_tool = {}
        self.history = []
        print("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Все значения профиля установлены по умолчанию!"))
        
        
    
    def edit_quest_reward_setting(self):
        difficulty_lvl = input("Введите уровень сложности или 0 для выхода> ")
        if difficulty_lvl == "0":
            return
        if difficulty_lvl == "+" or difficulty_lvl == "++" or difficulty_lvl == "+++" or difficulty_lvl == "++++":
            print("редактируется "+difficulty_lvl+":")
            new_reward = input("Введите награду> ")
            if new_reward.isdigit() == False:
                print("\033[31m{}".format("ERROR: ")+"\033[0m{}".format("Допустимы использовать лишь целые числа!"))
                return "ERROR"
            self.quest_reward_setting[difficulty_lvl] = int(new_reward)
            print("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Настройка успешно применена!"))
        else:
            print("\033[31m{}".format("ERROR: ")+"\033[0m{}".format("Допустимо указывать до 4х + и только плюсы можно указывать !"))
            return "ERROR"
    
    def print_quest_reward_setting(self):
        for plus, reward in self.quest_reward_setting.items():
            print("Сложность - "+plus)
            print("Награда - "+str(reward))
            print("\n")
    
    def save_to_history(self, history_line):
        from datetime import datetime
        self.history.append(str(datetime.now())+"\n"+history_line)
        # print("\033[32m{}".format("[info]:")+"\033[0m{}".format("Готово!\n\n"))
        
    def get_history(self):
        print("\033[32m{}".format("ETO history:")+"\033[0m{}".format("\n"))
        for history_line in self.history:
            print(history_line+"\n")
    
    def get_profile(self):
        print("HP: "+str(self.HP))
        print("armor: "+str(self.armor))
        print("strong: "+str(self.strong))
        print("intellect: "+str(self.intellect))
        print("damage: "+str(self.damage))
        print("critical dmg: "+str(self.critical_dmg)+"%")
        print(str(self.ETO)+" ETO")
        
    def get_HP(self):
        return self.HP
        
    def set_HP(self, HP):
        if HP < 0:  # Аналогично как и в случае с уроном. Броня может иметь отрицательный показатель если была подбита и после этого снята.
            HP = 0
        self.HP = HP
        return 0
    
    def get_armor(self):
        return self.armor
        
    def set_armor(self, armor):
        if armor < 0:  # Аналогично как и в случае с уроном. Броня может иметь отрицательный показатель если была подбита и после этого снята.
            armor = 0
        self.armor = armor
        return 0
    
    def get_strong(self):
        return self.strong
        
    def set_strong(self, strong):
        if strong > 15:
            strong = 15
        self.strong = strong
        return 0
    
    def get_intellect(self):
        return self.intellect
        
    def set_intellect(self, intellect):
        if intellect > 15:
            intellect = 15
        self.intellect = intellect
        return 0
    
    def get_damage(self):
        return self.damage
        
    def set_damage(self, damage):
        if damage < 0: # Если инструмент имеет заряды, то в случае разрядки показатель урона станет 0 и если снять такой инструмент будет отрицательное значение, чего нужно избежать.
            damage = 0
        self.damage = damage
        return 0
    
    def get_critical_dmg(self):
        return self.critical_dmg
    
    def set_critical_dmg(self, critical_dmg):
        critical_dmg = int(critical_dmg)
        if critical_dmg <= 45:              # максимальный крит урон равен 45%
            self.critical_dmg = critical_dmg
            print("\033[31m{}".format("ERROR: ")+"\033[0m{}".format("У игрока как и у NPC, крит урон не может привышать 45%!"))
            return 0
        return 1
    
    def get_ETO(self):
        return self.ETO
        
    def set_ETO(self, ETO):
        self.ETO = ETO
        return 0
    
    def add_reward(self, complexity, ID=0, task_class=""):
        ETO = self.quest_reward_setting[complexity]
        self.ETO += ETO
        self.save_to_history("Награда за задание типа "+task_class+" "+str(complexity)+" с ID_"+str(ID)+" в сумме "+str(ETO)+" получена!")
        
    def get_price_of_tools_id(self, tools_id):
        price = self.tools_id.get(tools_id)
        return price
    
    def get_tools_id(self):
        return self.tools_id
    
    def add_tools_id(self, tool_id, price):
        self.tools_id[tool_id] = price
        return 0
    
    def del_tools_id(self, tool_id):
        del self.tools_id[tool_id]
        return 0
        
    def add_pers_id(self, pers_id):
        self.pers_id.append(pers_id)
        return 0
    
    def del_pers_id(self, pers_id):
        self.pers_id.remove(pers_id)
        return 0
        
    def get_keep_tool(self):
        return self.keep_tool
        
    def add_keep_tool(self, tools_id, price):
        self.keep_tool[tools_id] = price
        return 0
    
    def del_keep_tool(self, tools_id):
        del self.keep_tool[tools_id]
        return 0
    
    def get_slots_occupied(self):
        return self.slots_occupied
        
    def set_slots_occupied(self, slots_occupied):
        self.slots_occupied = slots_occupied
        return 0
        
    def get_slots(self):
        return self.slots
    
    def set_slots(self, slots):
        self.slots = slots
        return 0
    
    def apply_to_characteristics(char_line, up=True): # char_line == tool_id
        chars = Profile.decoding_of_characteristics(char_line)
        name = chars[0]
        chars.remove(name)
        prof = Profile.get_instance()
        for char in chars:
            if char[0] == "HP":
                if up == False:
                    ch = prof.get_HP()-int(char[1])
                else:
                    ch = prof.get_HP()+int(char[1])
                if ch < 0: # если вдруг будут применены характеристики другого персонажа, а потом сняты после того как HP подбили, может тоже быть отрицательное значени, наверное.
                    ch = 0
                prof.set_HP(ch)
            if char[0] == "armor":
                if up == False:
                    ch = prof.get_armor()-int(char[1])
                else:
                    ch = prof.get_armor()+int(char[1])
                if ch < 0: # Аналогично как и в случае с уроном. Броня может иметь отрицательный показатель если была подбита и после этого снята.
                    ch = 0
                prof.set_armor(ch)
            if char[0] == "strong":
                if up == False:
                    ch = prof.get_strong()-int(char[1])
                else:
                    ch = prof.get_strong()+int(char[1])
                prof.set_strong(ch)
            if char[0] == "intellect":
                if up == False:
                    ch = prof.get_intellect()-int(char[1])
                else:
                    ch = prof.get_intellect()+int(char[1])
                prof.set_intellect(ch)
            if char[0] == "damage":
                if up == False:
                    ch = prof.get_damage()-int(char[1])
                else:
                    ch = prof.get_damage()+int(char[1])
                if ch < 0: # Если инструмент имеет заряды, то в случае разрядки показатель урона станет 0 и если снять такой инструмент будет отрицательное значение, чего нужно избежать.
                    ch = 0
                prof.set_damage(ch)
            if char[0] == "critical-dmg":
                if up == False:
                    ch = prof.get_critical_dmg()-int(char[1])
                else:
                    ch = prof.get_critical_dmg()-int(char[1])
                prof.set_critical_dmg(ch)
    
    # "gun_damage=200_strong=2" == ['gun', ['damage', '200'], ['strong', '2']]
    def decoding_of_characteristics(char_line):
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
        return result
        
    def keeping_tool(tool_id):
        prof = Profile.get_instance()
        slots_occupied = prof.get_slots_occupied()
        slots = prof.get_slots()
        
        # Проверяем свободны ли слоты,
        if slots_occupied+1 >= slots:
            print("\033[33m{}".format("[WARNING]: ")+"\033[0m{}".format("Слоты под экипировку закончились, предмет нельзя добавить!"))
            return
        else: # Если да, то указываем что теперь один слот занят.
            prof.set_slots_occupied(slots_occupied+1)
            
        if prof.get_tools_id().get(tool_id) == None:
            print("\033[31m{}".format("ERROR: ")+"\033[0m{}".format("Предмета нет в инвентаре."))
            if prof.get_keep_tool().get(tool_id) != None:
                print("Предмет был экипирован.")
            return
        #if prof.get_keep_tool().get(tool_id) == None:
        #    print("\033[31m{}".format("ERROR: ")+"\033[0m{}".format("Предмет не экипирован."))
        #    return
        price = prof.get_tools_id().get(tool_id)
        prof.add_keep_tool(tool_id, price) # Экиперуем предмет
        prof.del_tools_id(tool_id)  # При этом удаляем его из инвентаря
        Profile.apply_to_characteristics(tool_id) # Меняем характеристики игрока(повышаем)
    
    def take_off(tool_id):
        prof = Profile.get_instance()
        if prof.get_keep_tool().get(tool_id) == None:
            print("\033[31m{}".format("ERROR: ")+"\033[0m{}".format("Предмет не экипирован."))
            return
        price = prof.get_keep_tool().get(tool_id)
        prof.del_keep_tool(tool_id)
        prof.add_tools_id(tool_id, price)
        Profile.apply_to_characteristics(tool_id, up=False) # Меняем характеристики игрока(понижаем)
        slots_occupied = prof.get_slots_occupied()
        prof.set_slots_occupied(slots_occupied-1)   # Указываем что 1 слот был освобожден
    
    
    def death(self):
        history_line = "-"+str(self.ETO)+" ETO"
        self.save_to_history(history_line)
        inventory = list(self.tools_id.keys())              # Получаем ID инструментов
        size_inventory = len(inventory)
        if size_inventory != 0:                             # Проверяем есть ли инструменты в инвентаре и если да то
            r_index = random.randint(0, size_inventory-1)   # Выбераем рандомный индекс в массиве инструментов
            tool_id = inventory[r_index]                    # Получаем рандомный tool_id
            del self.tools_id[tool_id]                      # Удаляем рандомный инструмент
            history_line = "Был удален инструмент - "+str(tool_id)
            self.save_to_history(history_line)
        self.ETO = 0                                        # Обнуляем баланс
        # Тут бы арт смерти распечатать.
        


def get_prof():
    prof = Profile.get_instance()
    if prof.get_HP() == 0:
        print("\033[31m{}".format("[DEATH]: ")+"\033[0m{}".format("Вы проиграли!"))
        print("\n\n\n")
        print("----------------------")
        print("1. Реванш")
        res = input("\033[32m{}".format("> ")+"\033[0m{}".format(""))
        if res == "1":
            prof.set_HP(100)                                # Далее просто восстанавливаем HP и продолжаем игру!
    else:
        print("\033[32m{}".format("Profile:")+"\033[0m{}".format(""))
        prof.get_profile()

def get_history():
    prof = Profile.get_instance()
    prof.get_history()
    
    
    
def calculate_drop_trophy(npc):
    r = random.randint(1, 100)
    print("Трофей: "+str(r))
    if r <= 40:                     # 40% шанс выпадения трафея
        return npc.drop_trophy
    return 0

def calculate_critical_dmg_PLAYER():
    prof = Profile.get_instance()
    crit_dmg = prof.get_critical_dmg()
    r = random.randint(1, 100)
    if r <= crit_dmg:
        strong = prof.get_strong()
        result = 1.5+((strong*50) / (strong+200))
        result = round(result, 1)
        crit_dmg = prof.get_damage() * result
        return crit_dmg
    return prof.get_damage()
    
    
    
    
def compile_tool(array_tool):
    name = array_tool[0]
    string_tool = name+"_"
    array_tool.remove(name)
    for char in array_tool:
        string_tool += str(char[0])+"="+str(char[1])+"_"
    return string_tool.rstrip("_")
    
# Вид инструмента для перезарядки:
# [name, ['recharge', tool_id]]
# Вернет False если нечем перезарядить
# Иначе вернет True
#  ИМЕННО ЭТОТ МЕТОД ПЕРЕЗАРЯЖАЕТ ИНСТРУМЕНТ!
def find_recharge_for_tool_id(prof, finding_tool_id, array_tool=[], i=0):
    inventory = prof.get_tools_id()
    for tool_id, price in inventory.items():
        tool_recharge_id = Profile.decoding_of_characteristics(tool_id)         # tool_recharge_id == ['recharge', tool_id]
        if len(tool_recharge_id) == 2:                                          # Может содержать ['']

            # Инструмент может иметь рандомное значение charge - заряда, из-за чего обычный поиск может не дать результата, поэтому искать инструмент буду по имени.
            finding_tool_id_arr = finding_tool_id.split("_")
            tool_recharge_id_arr = tool_recharge_id[1].split("_")
            
            if tool_recharge_id_arr[0] == finding_tool_id_arr[0]:
                prof.del_tools_id(tool_id)                                      # Удаляем предмет перезарядки, это типа значит что мы перезарядили предммет
                prof.del_keep_tool(finding_tool_id)                             # заряд предмета будет изменен из чего следует что нужно стереть старый tool_id
                charge = 100                                                    # 1 заряд всегда равен 100 уровням заряда!
                array_tool[i][1] = charge                                       # Заряжаем инструмент, тем самым меняя его
                new_tool_id = compile_tool(array_tool)                          # Создаём новый - измененный, инструмент аналогичный исходному но с полным зарядом.
                prof.add_keep_tool(new_tool_id, price)                          # Экипируем новый инструмент
                return True
                

def check_charge(prof):
    take_off_tool = []
    keep_tool = prof.get_keep_tool()

    for tool_id, price in list(keep_tool.items()):                           # Берем по очереди каждый предмет в экипировки, если у предмета есть свойство перезарядки, то
        chars = Profile.decoding_of_characteristics(tool_id)
        array_tool = chars
        name = chars[0]
        chars.remove(name)
        array_tool.insert(0, name)
        i = 0
        for char in chars:                                                   # Пребераем все характеристики отдельно взятого tool_id в поисках charge
            i += 1                                                           # вычесляем какой индекс у charge в tool_id - нужно чтобы потом изменить уровень заряда
            if char[0] == "charge":                                          # [charge, 100] как пример
                charge = int(char[1])                                        # от 0 до 100
                if charge == 0:                                              # Проверяем не равен ли заряд 0, есл да то
                     if find_recharge_for_tool_id(prof, tool_id, array_tool, i-1) != True:    # Проверяем есть ли перезарядка, если да, то просто ничего не делать. Иначе
                        print("\033[33m{}".format("[WARNING]: ")+"\033[0m{}".format("Инструмент - "+tool_id+" разряжен, добавьте новый заряд в инвентарь!"))
                        Profile.take_off(tool_id)                               # Снимаем предмет.
                        take_off_tool.append(tool_id)
                if charge > 0:
                    prof.del_keep_tool(tool_id)                              # заряд предмета будет изменен из чего следует что нужно снять старый tool_id
                    charge = int(array_tool[i-1][1])                         # array_tool == ['gun', ['damage', '500'], ['charge', '100']] - пример
                    charge = charge - 30                                     # Находим по i - индексу - поле charge и отнимаем 30(30 каждый бой отнимается)
                    if charge < 0:                                           # Значение заряда не может быть меньше чем 0!
                        array_tool[i-1][1] = 0
                    else:
                        array_tool[i-1][1] = charge
                    new_tool_id = compile_tool(array_tool)                   # было изменено поле charge, поэтому нужно создать новый tool_id
                    prof.add_keep_tool(new_tool_id, price)                   # Экипируем новый инструмент
                    
                    
    return take_off_tool                                                     # нужно чтобы после боя снова экипировать предметы, чтобы не делать этого вручную.
                    
                    

def player_attack():
    # Это я бы не трогал, потому что это решение я нашел на stackoverflow. Это позволяет избежать цикличного импорта,
    # за счет того что модуль не полностью импортируется в этот модуль, а локально в конкретном методе и потом снова удаляется.
    from person import NPC
    prof = Profile.get_instance()
    npc = NPC.get_instance()
    
    # Игрок не может нанести врагу урон, если тот не был устанволен - игрок не выбрал врага:
    if npc.installed_contender == "None":
        return
    
    take_off_tool = check_charge(prof)
    
    damage = calculate_critical_dmg_PLAYER()
    if int(npc.HP) <= 0:
        npc.HP = 0
        drop = calculate_drop_trophy(npc)
        if drop != 0:
            prof.add_tools_id(drop, 50)
            history_line = "Получен трофей "+str(drop)+" - ценность 50 ETO."
            prof.save_to_history(history_line)
            print("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Получен трофей "+str(drop)+" !"))
        npc.installed_contender = "None"
        
        npc.set_all_fields_default()    # после нейтрализации противника, класс NPC устанавливает свои поля в поля по умолчанию.
        print("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Противник нейтрализован!"))
    if int(npc.armor) == 0:
        HP = int(npc.HP)
        new_HP = HP - damage
        npc.HP = new_HP
    if int(npc.armor) > 0:
        armor = int(npc.armor)
        armor = armor - damage
        if armor < 0:
            HP = npc.HP
            new_HP = int(HP) + int(armor)
            npc.HP = new_HP
            npc.armor = 0
        if armor >= 0:
            npc.armor = armor
    
    for keeping_tool in take_off_tool:
        Profile.keeping_tool(keeping_tool) # Снова экипировываем предметы снятые по причине того что были разряжены.


# Сохранить данные модуля в файл:
def save_data_profile():
    prof = Profile.get_instance()
    arr = prof.get_all_fields()
    with open("DataApp/profile.txt", "w+", encoding="utf-8") as file:
        json_string = json.dumps(arr)
        file.write(json_string)
        print("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Save profile data!"))
