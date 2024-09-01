import random, json
from hacker_apps import *


class HACKER_NPC:
	@staticmethod
	def get_instance() -> 'HACKER_NPC':
		if "_instance" not in HACKER_NPC.__dict__:
			HACKER_NPC._instance = HACKER_NPC()
			return HACKER_NPC._instance
		else:
			return HACKER_NPC._instance
	def __init__(self):
			try:
				# инициализация должна быть из файла!
				with open("DataApp/hacker.txt", "r", encoding="utf-8") as file:
					json_string = file.read()
				arr = json.loads(json_string)
				# print(arr)
				try:
					self.apply_to_characteristics_NPC(json.dumps(arr))
				except: # IndexError, TypeError
					self.name = arr[0]
					self.HP = int(arr[1])
					self.armor = int(arr[2])
					self.damage = int(arr[3])
					self.strong = int(arr[4])
					self.critical_dmg = int(arr[5])     # % - максимум 45%
		            
					self.drop_trophy = arr[6]           # Это отдельный tool_id предмета.
					self.installed_contender = arr[7]
	                
					self.lvl = arr[8]
					self.scripts = arr[9]
					self.inventory = arr[10]

				
			except OSError:    # Это исключение значит, что файл конфигурации пуст, код ниже задат дефолтные значения.
				self.set_all_fields_default()
				arr = self.get_all_fields()
				with open("DataApp/hacker.txt", "w+", encoding="utf-8") as file:
					json_string = json.dumps(arr)
					file.write(json_string)
					print("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Save HACKER_NPC default class data!"))

	def get_all_fields(self): 
		return [self.name, self.HP, self.armor, self.damage, self.strong, self.critical_dmg, self.drop_trophy, self.installed_contender, self.lvl, self.scripts, self.inventory]  
	
	def set_all_fields_default(self):
		self.name=""
		self.HP=100
		self.armor=0
		self.damage=0
		self.strong=0
		self.drop_trophy=[]
		self.installed_contender="None"
		self.critical_dmg=3
		self.lvl = 1
		self.inventory = []
		self.scripts = []
		print("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Все значения NPC класса установлены по умолчанию!"))
	
	def print_characteristics(self):
		print("lvl: "+str(self.lvl))
		print("Name: "+self.name)
		print("HP: "+str(self.HP))
		print("armor: "+str(self.armor))
		print("damage: "+str(self.damage))
		print("critical dmg: "+str(self.critical_dmg)+"%")
		print("drop trophy: "+str(self.drop_trophy))

	def decoding_of_characteristics_NPC(self, j_npc_id):
		npc_id = ["anton", 100, 0, 0, 3, 3, ["tool_id_1", "tool_id_2"], False, 3, ["tool_id_3", "tool_id_4", "tool_id_5"],["scripts1", "scripts2"]]
		j_npc_id = json.dumps(npc_id)
		return j_npc_id

	def apply_to_characteristics_NPC(self, j_npc_id, up=True,  new_npc=False):
		arr = json.loads(j_npc_id)

		self.name = arr[0][1]
		self.HP = int(arr[1][1])
		self.armor = int(arr[2][1])
		self.damage = int(arr[3][1])
		self.strong = int(arr[4][1])
		self.critical_dmg = int(arr[5][1])     # % - максимум 45%
		
		self.drop_trophy = arr[6][1]           # Это отдельный tool_id предмета.
		self.installed_contender = arr[7][1]
                
		self.lvl = arr[8][1]
		self.scripts = arr[9][1]
		self.inventory = arr[10][1]

	def menu_for_deal(self, prof):
		x = int(self.lvl) * 100
		y = int(self.lvl) * 1000
		eTo = random.randint(x, y) # 4 уровень, это суммы от 400 до 4000 тысяч
		while True:
			print("\n#######################################################\n\n")
			print("\033[32m{}".format("[MESSAGE]: ")+"\033[0m{}".format("От ["+self.name+"]: я рад что ты решил пойти\nмне на встречу, вот что я могу предложить:\n"))
			print("Сделка:")
			print("\nMenu: ----------------------")
			print("[1]: Могу тебе заплатить "+str(eTo)+" ETO.")
			if check_if_the_player_inventory_has_been_encrypted() == True: # ВНЕШНИЙ МЕТОД ИЗ МОДУЛЯ hacker_apps НЕ БЕЗОПАСНЫЙ ВЫЗОВ
				print("[2]: Расшифрую инвентарь.")
			print("\n\n#######################################################\n")

			command = input("> ")

			if command == "1":
				print("\033[33m{}".format("[WARNING]: ")+"\033[0m{}".format("Принять перевод на сумму: "+str(eTo)+" ETO?"))
				command2 = input("Да/1 или Нет/0 > ")
				if command2 == "1":
					prof.set_ETO(int(prof.get_ETO())+eTo)
					prof.save_to_history("Перевод от "+self.name+" - "+str(eTo)+" ETO.")
					print("\033[32m{}".format("[INFO]:")+"\033[0m{}".format("Перевод в сумме "+str(eTo)+" доставлен!"))
					self.set_all_fields_default() # И хакера как не бывало!
					input("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Нажмите <enter> чтобы продолжить..."))
					return
			if command == "2":
				print("\033[33m{}".format("[WARNING]: ")+"\033[0m{}".format("Надеюсь ты не экипировал зашифрованные инструменты,\nиначе рашифровка будет не полной, также предупреждаю,\nесли инвентарь не зашифрован, то могут быть проблемы,\nмне продолжить?: "))
				command3 = input("Да/1 или Нет/0 > ")
				if command3 == "1":
					auto_decrypt_of_inventory(self, "activation")
					self.set_all_fields_default() # И хакера как не бывало!
					return

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

	def set_this_npc_as_an_enemy(self):
		from person import NPC, save_data_person
		npc = NPC.get_instance()
		npc.name = self.name
		npc.HP = self.HP
		npc.armor = self.armor
		npc.damage = self.damage
		npc.strong = self.strong
		npc.drop_trophy = self.drop_trophy
		npc.installed_contender = True
		npc.critical_dmg = self.critical_dmg
		save_data_person()
		print("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Хакер установлен в качестве вашего противника!"))
		input("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Нажмите <enter> чтобы продолжить..."))
 
def add_NPC():
	print("\n#######################################################\n")
	print("\033[33m{}".format("[WARNING]: ")+"\033[0m{}".format(""))
	print("Вржеский хакер может атаковать без повода, все\nигровые предметы под угрозой!\n\nНажмите 0 или 1:")
	print("\n#######################################################\n")
	command = input("\nNo/0 - Yes/1 > ")
	if command == "0":
		return
	print("\n#######################################################\n\n\n\n\n\n")
	print("Вставьте HACKER_ID в поле ниже для продолжения:")
	print("\n\n\n\n\n\n#######################################################\n")

	HACKER_ID = input("HACKER_NPC_ID> ")

	hacker = HACKER_NPC.get_instance()
	hacker.keeping_tool_NPC(HACKER_ID)
	hacker.installed_contender = True
	arr = hacker.get_all_fields()
	with open("DataApp/hacker.txt", "w+", encoding="utf-8") as file:
		json_string = json.dumps(arr)
		file.write(json_string)
	print("\033[33m{}".format("[WARNING]: ")+"\033[0m{}".format("Вражеский хакер приступил к работе!"))
	input("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Нажмите <enter> чтобы продолжить..."))

    
def del_NPC():
	hacker = HACKER_NPC.get_instance()
	hacker.installed_contender = "None"
	hacker.set_all_fields_default()

def get_installer_hacker_NPC():
	hacker = HACKER_NPC.get_instance()
	print("\033[32m{}".format("[SET HACKER_NPC_ID]:")+"\033[0m{}".format(""))    # NPC_ID- это тот же tool_id, отличается лишь тем что есть drop-trophy
	NPC_ID = input("HACKER_NPC_ID> ")
	if NPC_ID == "" or NPC_ID == None:
		print("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("HACKER_NPC не был добавлен!"))
		return
	hacker.set_new_npc(NPC_ID)

# Метод также прверяет жив ли хакер:
def print_hacker_npc():
	npc = HACKER_NPC.get_instance()
	if npc.HP <= 0:
		self.del_NPC()
	if npc.installed_contender == True:
		print("\033[33m{}".format("[WARNING]:")+"\033[0m{}".format("Обнаружено вторжение в систему!"))
	else:
		print("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Вторжений не обнаружено."))





def hacker_attack():
	from player_profile import Profile
	global all_scripts, scripts_to_script, used_attack


	prof = Profile.get_instance()
	# Тут и будет реализован новый стиль атаки.
	hacker = HACKER_NPC.get_instance()

	if hacker.installed_contender == "None":
		return
	
	lvl = hacker.lvl
	attack_frequency = {1 : 20, 2 : 40, 3 : 45, 4 : 70, 5 : 80}

	probability = random.randint(1, 100)
	probability_app = random.randint(1, len(all_scripts))

	attack_name = all_scripts[probability_app-1]

	if probability <= attack_frequency[lvl]:
		method_attack = scripts_to_script[attack_name]
		method_attack(hacker, "activate")





# Сохранить данные модуля в файл:
def save_data_person():
    hacker = HACKER_NPC.get_instance()
    arr = hacker.get_all_fields()
    with open("DataApp/hacker.txt", "w+", encoding="utf-8") as file:
        json_string = json.dumps(arr)
        file.write(json_string)
        print("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Save HACKER_NPC class data!"))
    save_to_config_file() # сохранение настроек хакерских приложений