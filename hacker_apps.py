import json
default_config_dict = {"Tactical camouflage" : 0, "shutdown" : 0, "theft of ETO" : 0, "encryption of inventory" : 0, "encryption of inventory" : 0}

def init_config():
	import json, os.path

	if os.path.exists("DataApp/hacker_apps_config.txt") != True:
		config_dict = default_config_dict
		with open("DataApp/hacker_apps_config.txt", "w+", encoding="utf-8") as file:
			json_string = json.dumps(config_dict)
			file.write(json_string)
			print("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Save DEFAULT-HACKER_APPS_CONFIG data!"))
			return config_dict

	with open("DataApp/hacker_apps_config.txt", "r", encoding="utf-8") as file:
		return json.load(file)

# Должен считываться из файла!
			# Счетчик купленных запусков:
config_dict = init_config()

# ["smartphone_consumables", 1000]
def use_consumables(hacker, script_name):
	global config_dict
	try:
		# print(hacker.inventory)
		index = hacker.inventory.index("smartphone_consumables")
		if int(hacker.inventory[index+1]) > 0:
			hacker.inventory[index+1] = hacker.inventory[index+1] - 1
			counter = config_dict[script_name]
			config_dict[script_name] = counter + 1
			return True
		else:
			return False
	except ValueError:
		return False



# APP #1 --------------------------------------------------------------------------
original_npc = None # Оригинальный NPC - экземпляр противника
original_get_instance = None
points_flag = 0

class FAKE_NPC:
	@staticmethod
	def get_instance() -> 'FAKE_NPC':
		global original_npc
		if "_instance" not in FAKE_NPC.__dict__:
			FAKE_NPC._instance = FAKE_NPC(original_npc)
			return FAKE_NPC._instance
		else:
			return FAKE_NPC._instance

	def __init__(self, original_npc):
		self.default_HP = 10000000000000000000000000000000000000000000000000000000000
		self.name = original_npc.name
		self.HP = self.default_HP
		self.armor = 0
		self.damage = original_npc.damage
		self.strong = original_npc.strong
		self.critical_dmg = original_npc.critical_dmg     # % - максимум 45%
		self.drop_trophy = original_npc.drop_trophy           # Это отдельный tool_id предмета.
		self.installed_contender = original_npc.installed_contender

	def print_characteristics(self): # Этот метод в классе и там нет повторной инициализации - НАДЕЖНО
		print("hacked: "+"𖤀𖤢𖢉ꘘꛃ𖣠𖤢ꚠꚽ𖤢ꛈ𖦪ꛤꘘ𖢉𖤢ꛃ")
		print("HP@: "+"𖤀𖤢𖢉ꘘꛃ𖣠𖤢ꚠꚽ𖤢ꛈ𖦪ꛤꘘ𖢉")
		print("&rmor: "+"𖤀𖤢𖢉ꘘꛃ𖣠𖤢ꚠꚽ𖤢ꛈ𖦪ꛤꘘ𖢉𖤢ꛃ")
		print("d?mage: "+"𖤀𖤢𖢉ꘘꛃ𖣠𖤢𖦪ꛤꘘ𖢉𖤢ꛃ")
		print("criti*** dmg: "+"𖤀𖤢𖢉ꘘꛃ𖣠ꚠꚽ𖤢ꛈ𖦪ꛤꘘ𖢉𖤢ꛃ")
		print("drop $$$y: "+"𖤀𖤢𖢉ꛃ𖣠𖤢ꚠꚽ𖤢ꛈ𖦪ꛤꘘ𖢉𖤢ꛃ")
	

	def get_all_fields(self): 
		return [self.name, self.HP, self.armor, self.damage, self.strong, self.critical_dmg, self.drop_trophy, self.installed_contender]
	
	def set_all_fields_default(self):
		return


def set_original_get_instance(orig_get_instance):
	global original_get_instance
	from person import NPC
	if NPC.get_instance != FAKE_NPC.get_instance and orig_get_instance != FAKE_NPC.get_instance() and orig_get_instance != None:
		original_get_instance = orig_get_instance


# этот метод обязательно должен быть синхронным с главным циклом игры, потому что он проверяет, использовал ли игрок свою атаку, если да то поинты в рейтинге изменяться, а значит камуфляж нужно отключить:
def check_time_to_disable_camouflage():
		global original_npc, original_get_instance, config_dict, points_flag
		from person import NPC
		if original_npc == None and original_get_instance == None:
			return

		from raiting import read_rank
		current_points = int(read_rank())
		counter = config_dict["Tactical camouflage"]

		# идеальный код для отладки:
		#print(current_points != points_flag)
		#print(original_get_instance)
		#print(NPC.get_instance)

		fake_npc = FAKE_NPC.get_instance()
		print(fake_npc.installed_contender)
		if counter != 0 and fake_npc.installed_contender == True:
			if current_points != points_flag: # поинты меняются когда игрок атакует
				config_dict["Tactical camouflage"] = 0
				NPC.get_instance = original_get_instance
				#fake_npc.installed_contender = False # по какой-то причине если эта строчка срабатывает, то переменная всегда станет равна False через один, вроде, оборот цикла
				fake_npc.HP = fake_npc.default_HP
				print("\033[33m{}".format("[HACKER_APPS]: ")+"\033[0m{}".format("Тактический камуфляж отключен!"))
				


def script_tactical_camouflage(hacker=None, command="reactivation"):
	# текущий враг клонирует себя и не даёт игроку нанести урон по оригеналу!
	# Урон получает копия противника!
	global original_npc, config_dict, points_flag
	from person import NPC
	from raiting import read_rank
	points_flag = read_rank()
	npc = NPC.get_instance()
	original_npc = npc
	set_original_get_instance(NPC.get_instance)
	if npc.installed_contender == "None":
		print("\033[33m{}".format("[HACKER_APPS]: ")+"\033[0m{}".format("Отмена скрипта: Тактический камуфляж - не может быть активирован - у игрока нет противника!"))
		return

	if command == "activate":
		if use_consumables(hacker, "Tactical camouflage") == True:
			print("\033[33m{}".format("[HACKER_APPS]: ")+"\033[0m{}".format("Тактический камуфляж - активен!"))
			print("\033[33m{}".format("[HACKER_APPS]: ")+"\033[0m{}".format("Атака игрока не эффективна!"))
			NPC.get_instance = FAKE_NPC.get_instance
			return
		elif use_consumables(hacker) == False:
			print("\033[33m{}".format("[HACKER_APPS]: ")+"\033[0m{}".format("Отмена скрипта: Тактический камуфляж - кончился расходный материал!"))
			return
	# Такая команда расчитана на то, что игрок перезапустил приложение и нужно снова запустить скрипт, ведь его раюота была прервана:
	if command == "reactivation":
		print("\033[33m{}".format("[HACKER_APPS]: ")+"\033[0m{}".format("Повторный запуск скрипта: Тактический камуфляж!"))
		NPC.get_instance = FAKE_NPC.get_instance
		

# APP #2 --------------------------------------------------------------------------
def script_shutdown(hacker=None, command="reactivation"):
	# отключение, враг отклчает текущие подключение в se.
	global config_dict
	from smart_electronics import Smart_Electronics
	se = Smart_Electronics.get_instance()

	if command == "activate":
		if use_consumables(hacker, "shutdown") == True and se.name != "":
			print("\033[33m{}".format("[HACKER_APPS]: ")+"\033[0m{}".format("Отключение - скрипт активирован!"))
			se.set_all_fields_default()
			counter = config_dict["shutdown"]
			if counter > 0: # если игрок захочет отменить действие скрипта перезагрузкой, то скрипт будет активирован повторно, также если игрок снова активирует подключение, то после перезапуска скрипт снова активируется. Сам скрипт будет отменен лишь при повторном его запуске хакером.
				config_dict["shutdown"] = counter - 1

			print("\033[33m{}".format("[HACKER_APPS]: ")+"\033[0m{}".format("smart electronics - подключение разорвано!"))
			return
		elif use_consumables(hacker, "shutdown") == False:
			print("\033[33m{}".format("[HACKER_APPS]: ")+"\033[0m{}".format("Отмена скрипта: Отключение - кончился расходный материал!"))
			return
	if command == "reactivation":
		print("\033[33m{}".format("[HACKER_APPS]: ")+"\033[0m{}".format("Повторный запуск скрипта: Отключение!"))
		se.set_all_fields_default()


# APP #3 --------------------------------------------------------------------------
def script_theft_of_ETO(hacker=None, command="reactivation"):
	# кража ETO
	# то сколько хакер украдет ETO зависит от уровня хакера.
	global config_dict
	from player_profile import Profile, save_data_profile
	prof = Profile.get_instance()
	if command == "activate":
		if use_consumables(hacker, "theft of ETO") == True:
			print("\033[33m{}".format("[HACKER_APPS]: ")+"\033[0m{}".format("Активация скрипта: Кража ETO игрока."))
			# суть простая, чем выше уровень хакера, тем большей процент будет вычтен из суммы - 5 - 50%, 4 - 40% и т.д:
			deductible_percentage = (10 * int(hacker.lvl)) / 100
			deductible_ETO = int(prof.ETO) * deductible_percentage

			if type(prof.ETO) == str: # я не помню какой тип данных там точно будет, поэтому на всякий случай сделал это условие:
				prof.ETO = int(prof.ETO) - int(deductible_ETO)
				prof.ETO = str(prof.ETO)
			else:
				prof.ETO = int(prof.ETO) - int(deductible_ETO)
			print("\033[33m{}".format("[HACKER_APPS]: ")+"\033[0m{}".format("Скрипт выполнен: Кража "+str(deductible_ETO)+" ETO игрока."))
			save_data_profile() # даже если игрок перезагрузит приложение без сохранения, то этот вызов сохранения не даст отменить действие скрипта!
			counter = config_dict["theft of ETO"]
			config_dict["theft of ETO"] = counter - 1
	if command == "reactivation":
		# не требуется!
		return

# APP #4 --------------------------------------------------------------------------
# Для корректной работы метода, возможно потребуется задать парочку уточняющих вопросов игроку!
def check_if_the_player_inventory_has_been_encrypted(): # приметивная проверка отвечающая на вопрос: был ли зашифрован инвентарь игрока?
	from player_profile import Profile
	prof = Profile.get_instance()
	inventory = prof.get_tools_id()
	if len(inventory) == 0: # если инвентарь пуст
		return False

	example_tool_id = list(inventory.keys())[0] # берем первый же в списке инструмент
	if ("RSAWD" in example_tool_id) == False:
		if len(inventory) > 1:
			example_tool_id = list(inventory.values())[1]
			return "RSAWD" in example_tool_id
	
	return "RSAWD" in example_tool_id

def script_encryption_of_inventory(hacker=None, command="reactivation", auto_decrypt_of_inventory=False):
	# шифрование всего инвентаря
	# снять шифрование можно с помощью ключа
	global config_dict
	from cryptography.RSA import encrypt_text, decrypt_text, public_key, private_key
	from player_profile import Profile, save_data_profile
	prof = Profile.get_instance()

	if command == "activate":
		verification_method = None
		if auto_decrypt_of_inventory == False:
			verification_method = lambda: use_consumables(hacker, "encryption of inventory")
		else:
			verification_method = lambda: auto_decrypt_of_inventory

		# расходники не используются при расшифровки, только для шифрования
		# тут определяется, будут ли использоваться расходники или же пропустить бесплатно
		if verification_method() == True:
			keep_inventory = prof.get_keep_tool()
			# 1) Снимаем экипировку игрока и помещаем её обратно в инвентарь:
			if len(keep_inventory) != 0:
				for tool_id in list(keep_inventory.keys()):
					Profile.take_off(tool_id)

			inventory = prof.get_tools_id()
			# 2) Шифруем все tool_id в инвенторе, включая и снятую экипировку, но price оставляем не тронутым:
			if len(inventory) != 0:
				# 3) расшировываем или наоборот зашифровываем
				for tool_id, price in list(inventory.items()):
					if ("RSAWD" in tool_id) == False: # это нужно для избежания повторного шифрования данных!
						if auto_decrypt_of_inventory == False:
							print("\033[33m{}".format("[HACKER_APPS]: ")+"\033[0m{}".format("Активация скрипта: Шифрование инвентаря."))
							encrypt_tool_id = str(encrypt_text(tool_id)) # [1233323, 1232311, 9443794] - что-то похожее выдает этот пункт
							encrypt_tool_id = "RSAWD"+encrypt_tool_id
							prof.del_tools_id(tool_id)
							prof.add_tools_id(encrypt_tool_id, price)

					elif auto_decrypt_of_inventory == True: # расшифровать:
						print("\033[33m{}".format("[HACKER_APPS]: ")+"\033[0m{}".format("Активация скрипта: Дешифровка инвентаря."))
						encrypt_tool_id = tool_id
						while True:
							if "RSAWD" in encrypt_tool_id:
								tool_id = tool_id[5:] # "RSAWD" - удаляем эти символы
								print("tool_id == "+str(tool_id))
								tool_id = json.loads(tool_id)
								tool_id = decrypt_text(tool_id) # [1233323, 1232311, 9443794] - что-то похожее выдает этот пункт
								if ("RSAWD" in tool_id) == False:
									decrypt_tool_id = tool_id
									prof.del_tools_id(encrypt_tool_id)
									prof.add_tools_id(decrypt_tool_id, price)
									break
							else: # если инструмент не зашифрован, то он не содержит "RSAWD", следовательно берем след инсрумент:
								break
				if auto_decrypt_of_inventory == True:
					print("\033[33m{}".format("[HACKER_APPS]: ")+"\033[0m{}".format("Дешифровка инвентаря выполнена."))
					return # о том что была расшифровка, в config_dict не указываем!
				counter = config_dict["encryption of inventory"]
				config_dict["encryption of inventory"] = counter - 1
				print("\033[33m{}".format("[HACKER_APPS]: ")+"\033[0m{}".format("Шифрование инвентаря выполнено."))
	if command == "reactivation":
		# не требуется!
		return

def auto_decrypt_of_inventory(hacker=None, command="reactivation"):
	# полностью снимает шифрование с инвенторя игрока.
	# сначала массив с зашифрованными элементами превращается в строку и снова шифруется и снова в строку и снова шифруется..
	# я должен строку превратить в массив обратно, если не выйдет, значит расшифровка удалась, иначе повторять расшифроку
	script_encryption_of_inventory(hacker, command="activate", auto_decrypt_of_inventory=True)

# CONFIGURATION APPS --------------------------------------------------------------------------
all_scripts = ["Tactical camouflage", "shutdown", "theft of ETO", "encryption of inventory"]
scripts_to_script = {"Tactical camouflage" : script_tactical_camouflage, "shutdown" : script_shutdown, "theft of ETO" : script_theft_of_ETO, "encryption of inventory" : script_encryption_of_inventory}

# Задуменно для вызова исключительно из main.py!
def use_reactivation(hacker):
	global config_dict, original_npc
	for script_name, counter in config_dict.items():
		if counter > 0:
			script = scripts_to_script[script_name]
			if hacker.installed_contender != "None":
				script()
			else:
				config_dict = default_config_dict
				print("\033[33m{}".format("[HACKER_APPS]: ")+"\033[0m{}".format("Скрипт: "+script_name+" отменен - исполнитель не найлен!"))

# SAVE TO CONFIG FILE --------------------------------------------------------------------------
def save_to_config_file():
	global config_dict
	import json
	with open("DataApp/hacker_apps_config.txt", "w+", encoding="utf-8") as file:
		json_string = json.dumps(config_dict)
		file.write(json_string)
		print("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Save HACKER_APPS_CONFIG data!"))