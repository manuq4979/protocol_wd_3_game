from task import single_task_dict, get_pages, SingleTask, del_single_task, get_dump_single_task_dict
import json, os


STATUS = "requiring funding" # check_relevance_task - проверяет гне просрочено ли задание, этот метод тоже учитывает что этот статус является аналогом статусу "Active"

def init_config_currecy2ETO():
	config_default = [0, {}]
	if os.path.exists("DataApp/config_currecy2ETO.txt") != True:
		with open("DataApp/config_currecy2ETO.txt", "w+", encoding="utf-8") as file:
			json_string = json.dumps(config_default)
			file.write(json_string)
		return config_default

	with open("DataApp/config_currecy2ETO.txt", "r+", encoding="utf-8") as file:
		config = json.load(file)

	new_task_id_and_reward_dict = {}
	for task_id, reward in config[1].items():
		task_id = int(task_id)
		reward = int(reward)
		new_task_id_and_reward_dict[task_id] = reward
	config[1] = new_task_id_and_reward_dict
	return config

config = init_config_currecy2ETO()

def save_config_currecy2ETO():
	global config
	with open("DataApp/config_currecy2ETO.txt", "w+", encoding="utf-8") as file:
		json_string = json.dumps(config)
		file.write(json_string)
	print("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Конфигурация currecy2ETO сохранена!"))

def save_single_task(msg_on_or_off=True):
	new_single_task_dict = get_dump_single_task_dict(single_task_dict)

	arr1 = new_single_task_dict

	with open("DataApp/single_task.txt", "w+", encoding="utf-8") as file:
		json_string = json.dumps(arr1)
		file.write(json_string)
		if msg_on_or_off == True:
			print("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Данные задания сохранены!"))

def check_if_id_is_duplicated(ID):
	global single_task_dict
	for task_id in single_task_dict.keys():
		if task_id == ID:
			return True

	return False

def add_new_task():
	global single_task_dict, config
	new_task = SingleTask()
	ID = new_task.input_single_task()
	if check_if_id_is_duplicated(ID) == True:
		print("\033[31m{}".format("[ERROR]: ")+"\033[0m{}".format("task_id под номером "+str(ID)+" уже занят!"))
		input("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Нажмите <enter> чтобы продолжить..."))
		print("\n" * 100) # очищаем экран консоли
		return

	if type(ID) != str:
		new_task.set_status(STATUS)
		while True:
			required_amount = input("Сколько всего нужно внести> ")
			if required_amount.isdigit() == True:
				tatal_reward = input("Какая общая награда будет в ETO> ")
				if tatal_reward.isdigit() == True:
					break
		new_task.set_description(new_task.get_description() + "\n[Осталось внести]: "+str(required_amount) + "\n[Награда за финансирование]: "+str(tatal_reward)+"\n[Осталось получить]: "+str(tatal_reward))
		single_task_dict[ID] = new_task
		config[1][ID] = tatal_reward
		save_single_task()
		save_config_currecy2ETO()
		print("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Новое задание добавлено !"))
		input("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Нажмите <enter> чтобы продолжить..."))
		print("\n" * 100) # очищаем экран консоли

def del_task():
	global single_task_dict
	ID = input("ID> ")
	ID = int(ID)
	task = None
	try:
		task = single_task_dict[ID]
	except KeyError:
		print("\033[31m{}".format("[ERROR]: ")+"\033[0m{}".format("Задание с ID_"+str(ID)+" не существует!"))
		input("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Нажмите <enter> чтобы продолжить..."))
		print("\n" * 100) # очищаем экран консоли
		return
	if task.get_status() == STATUS:
		del single_task_dict[ID]
		del config[1][ID]
		save_config_currecy2ETO()
		save_single_task()
		print("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Задание ID_"+str(ID)+" удалено!"))
		input("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Нажмите <enter> чтобы продолжить..."))
		print("\n" * 100) # очищаем экран консоли
		return
	else:
		print("\033[31m{}".format("[ERROR]: ")+"\033[0m{}".format("Задание ID_"+str(ID)+" не относиться к заданиям требующих финансирования!"))
		print("\033[33m{}".format("[WARNING]: ")+"\033[0m{}".format("Удаление отменено!"))
		input("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Нажмите <enter> чтобы продолжить..."))
		print("\n" * 100) # очищаем экран консоли

def this_is_the_last_page(pages, index):
	index += 1 # следующая страница
	if 0 <= index < len(pages): # если индекс в диапозоне, то значит он допустим, а значит переданный index не на последней странице
		index -= 1
		return False
	index -= 1
	return True

def print_pages(task_list, index):
	pages = get_pages(task_list, chunk_size=3, flag_del_no_active_task=False)
	last_page = this_is_the_last_page(pages, index) # проверяем последния ли это страница или нет
	counter_task = 0


	if len(pages) != 0:
		for task in pages[index]:
			if task.get_status() == STATUS:# Не активные задания не будут отображены!
				print(task.get_title())
				print(task.get_description())
				counter_task += 1

	if counter_task == 0 and index == 0: # если первая страница не содержит заданий этого статуса, то логично что нет заданий ещё:
		print("\033[33m{}".format("[WARNING]: ")+"\033[0m{}".format("Задания ещё не были добавлены!\n"))
		return last_page

	return last_page # отправляем ответ на вопрос о том последния ли это страница или нет

# меняет сумму на которую было финансирование на ту что в currency:
def add_changes_about_contribution_to_task_description(task, currency, reward, total_reward):
	# 1) Пример: "\n[Уже внесено]: 0", а в итоге станет "\n[Уже внесено]: 100"
	line = task.get_description()
	line = line.split("\n")

	line_2 = line[1]
	index = line_2.find(":")+2

	total_sum = str( (int(line_2[index:]) - int(currency)) )
	line_2 = line_2[:index]
	line_2 += str(total_sum)

	# 2) аналогично с этой строкой: "\n[Награда за финансирование]: 1000"
	line_3 = line[2]
	index = line_3.find(":")+2
	line_3 = line_3[:index]
	line_3 += str(reward)

	# 3) аналогично:
	line_4 = line[3]
	index = line_4.find(":")+2
	line_4 = line_4[:index]
	line_4 += str( (int(total_reward)-int(reward)) )

	total_line = line[0] + "\n" + line_2 + "\n" + line_3 + "\n" + line_4

	task.set_description(total_line)





# выдать награду за финансирование:
def give_an_award(task_id, funding_amount):
	global config, single_task_dict

	if config[0] == 0:
		print("\033[31m{}".format("[ERROR]: ")+"\033[0m{}".format("Для начала поплните вашь счет!"))
		input("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Нажмите <enter> чтобы продолжить..."))
		print("\n" * 100) # очищаем экран консоли
		return False

	from player_profile import Profile
	prof = Profile.get_instance()
	task = single_task_dict[task_id]
	total_reward = int(config[1][task_id])
	funding_amount = int(funding_amount)
	percentage_of_amount = (funding_amount / total_reward) * 100
	if percentage_of_amount == 100:
		prof.set_ETO(prof.get_ETO() + total_reward)
		history_line = "Полчена наград "+str(total_reward)+" ETO за финансирование задания ID_"+str(task_id)+" в сумме "+str(funding_amount) +" полноценной валюты(рубль, доллар и т.п)."
		prof.save_to_history(history_line)
		add_changes_about_contribution_to_task_description(task, funding_amount, total_reward, total_reward)
		save_config_currecy2ETO()
		print("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format(history_line))
		input("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Нажмите <enter> чтобы продолжить..."))
		print("\n" * 100) # очищаем экран консоли
		return
	percentage_of_amount = (100-percentage_of_amount) / 100

	if (config[0] - funding_amount) < 0:
		print("\033[31m{}".format("[ERROR]: ")+"\033[0m{}".format("На счете не достаточно средств!\nТребуется "+str(total_sum)+"  в рублях."))
		input("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Нажмите <enter> чтобы продолжить..."))
		print("\n" * 100) # очищаем экран консоли
		return False

	config[0] -= funding_amount
	print(percentage_of_amount)
	reward = int(total_reward * percentage_of_amount)
	prof.set_ETO(prof.get_ETO() + reward)
	history_line = "Полчена наград "+str(reward)+" ETO за финансирование задания ID_"+str(task_id)+" в сумме "+str(funding_amount) +" полноценной валюты(рубль, доллар и т.п)."
	prof.save_to_history(history_line)
	add_changes_about_contribution_to_task_description(task, funding_amount, reward, total_reward)
	save_config_currecy2ETO()
	print("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format(history_line))
	input("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Нажмите <enter> чтобы продолжить..."))
	print("\n" * 100) # очищаем экран консоли


# профенансировать:
def fund_in():
	global single_task_dict
	ID = input("ID> ")
	ID = int(ID)
	task = None
	try:
		task = single_task_dict[ID]
	except KeyError:
		print("\033[31m{}".format("[ERROR]: ")+"\033[0m{}".format("Задание с ID_"+str(ID)+" не существует!"))
		input("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Нажмите <enter> чтобы продолжить..."))
		print("\n" * 100) # очищаем экран консоли
		return

	while True:
		currency = input("Введите сумму> ")
		if currency.isdigit() == True:
			give_an_award(ID, currency)
			return

def top_up():
	global config
	sum = input("> введите сумму < | > ")
	while True:
		if sum.isdigit() == True:
			config[0] += int(sum)
			save_config_currecy2ETO()
			print("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Успешно поплнено!"))
			input("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Нажмите <enter> чтобы продолжить..."))
			print("\n" * 100) # очищаем экран консоли
			return

def top_down():
	global config
	sum = input("> введите сумму < | > ")
	while True:
		if sum.isdigit() == True:
			config[0] -= int(sum)
			save_config_currecy2ETO()
			print("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Успешно снято!"))
			input("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Нажмите <enter> чтобы продолжить..."))
			print("\n" * 100) # очищаем экран консоли
			return


def verify_assignment_deadlines_and_completion():
	global single_task_dict
	for ID, task in list(single_task_dict.items()):
		if task.get_status() != STATUS:
			continue
		line = task.get_description()
		line = line.split("\n")
		
		line_2 = line[0]
		index = line_2.find(":")+2
		activation_time = line_2[index:]
		
		# пример этой строки: "\n[Награда за финансирование]: 1000"
		line_3 = line[3]
		index = line_3.find(":")+2
		sum = line_3[index:]
		sum.replace(" ", "")
		sum = int(sum)
		
		
		from datetime import datetime
		from player_profile import player_attack, Profile
		from raiting import determine_my_ranking
		prof = Profile.get_instance()
		activation_time = datetime.strptime(activation_time, "%Y-%m-%d").date()
		res = task.check_time(activation_time)
		
		if res == 1 or res == 2:
			from person import npc_attack
			npc_attack(prof)
			complexity = task.complexity
			complite = False
			determine_my_ranking(complexity, complite, prof)
			del single_task_dict[ID]
			print("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Задание завершено - вышло время!"))
			input("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Нажмите <enter> чтобы продолжить..."))
			print("\n" * 100) # очищаем экран консоли
			return
		if sum <= 0:
			player_attack()
			complexity = task.complexity
			complite = True
			determine_my_ranking(complexity, complite, prof)
			del single_task_dict[ID]
			print("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Задание завершено - профинансированно!"))
			input("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Нажмите <enter> чтобы продолжить..."))
			print("\n" * 100) # очищаем экран консоли


def print_amount_on_account():
	global config
	x = int(config[0])
	x = '{0:,}'.format(x).replace(',', '.')
	print("\033[32m{}".format("[СУММА НА СЧЕТУ]: ")+"\033[0m{}".format(str(x) + " рубли.")) 


def currency2ETO_menu():
	global single_task_dict
	index = 0
	while True:
		verify_assignment_deadlines_and_completion()
		print("\n#######################################################\n")
	
		print_amount_on_account()
		print("\033[32m{}".format("[INFO]:")+"\033[0m{}".format("Задания требующие финансирования:\n"))
		
		last_page = print_pages(list(single_task_dict.values()), index)

		print("\n\nMenu: ----------------------")
		print("[1]: Добавить задание требующие финансирования.")
		print("[2]: Профинансировать задние.")
		print("[3]: Завершить задание.")
		if last_page == False:
			print("[4]: Далее.")
		elif index > 0:
			print("[4]: Назад.")
		print("[5]: Пополнить счет.")
		print("[6]: Снять со счета.")
		print("[0]: Назад.")
		print("\n#######################################################\n")

		command = input("> ")
		print("\n" * 100) # очищаем экран консоли

		if command == "0":
			return

		if command == "1":
			add_new_task()

		if command == "2":
			fund_in()

		if command == "3":
			del_task()
			index = 0 # при удалении страница под текущим индесом может не сущестовать

		if command == "4":
			if last_page == False:
				index += 1
			elif index > 0:
				index -= 1

		if command == "5":
			top_up()

		if command == "6":
			top_down()