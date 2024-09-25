"""
214 - создать одиночное задание 4го уровня сложности.
22 - завершить одиночное задание.
23 - зафисировать провал одиночного задания.
24 - удалить одиночное задание.

114 - создать ежедневное задание 4го уровня сложности.
12 - завершить ежедневное задание.
13 - завершить провал ежедневного задания.
14 - удалить ежедневное задание.

314 - создать задание привычки 4го уровня сложности.
32 - поощрить задание привычки.
33 - зафексировать отрицательное подкрепление в привычки.
34 - удалить задание привычки.


1 - ежедневные
2 - одиночные
3 - привычки

1 - добавить
2 - завершить
3 - поражение
4 - удалить

1 до 4 - сложность.

Далее вводим 3е значение, это будет ID.

После отобразить сообщение и новый метод паузы - input()
"""
# single_task_dict
# habit_task_dict
# daily_task_dict

DAILY = "1"
SINGLE = "2"
HABIT = "3"

ADD = "1"
COMPLITE = "2"
FAILED = "3"
DEL = "4"

def get_title_and_description(task_class):
	pass

def get_deadlines(task_class):
	from datetime import datetime, timedelta

	if task_class == DAILY or task_class == HABIT:
		deadlines = datetime.now().date()
		repeat_day = 1
		# print(deadlines)
		return [deadlines, repeat_day]
	if task_class == SINGLE:
		deadlines = datetime.now().date()
		deadlines = deadlines + timedelta(days=1) # если оставить текущию дату, то окажется что выполнить нужно было ДО: СЕГОДНЯ.
		# print(deadlines)
		return deadlines

def add_hot_task(new_task, task_id, task_class):
	from task import single_task_dict, habit_task_dict, daily_task_dict

	task_id = int(task_id)

	if task_class == SINGLE:
		deadlines = get_deadlines(SINGLE)
		new_task.set_description("[До]: "+str(deadlines))
		new_task.execute_to = deadlines # нету setterА
		single_task_dict[task_id] = new_task
		print("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Новое одиночное задание добавлено!"))
	
	if task_class == HABIT:
		deadlines = get_deadlines(HABIT)
		new_task.set_description("[Сброс]: "+str(deadlines[1]))
		new_task.set_activation_time(deadlines[1]) # только дни для этого класса задач!
		habit_task_dict[task_id] = new_task
		print("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Новое задание привычка добавлено!"))
	
	if task_class == DAILY:
		deadlines = get_deadlines(DAILY)
		new_task.set_description("[Повтор]: "+str(deadlines[0]) +": "+str(deadlines[1]))
		# print(deadlines)
		new_task.set_repeat(deadlines[1])
		new_task.set_start_date(deadlines[0])
		daily_task_dict[task_id] = new_task
		print("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Новое ежедневное задание добавлено!"))

	input("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Нажмите <enter> чтобы продолжить..."))
	print("\n" * 100) # очищаем экран консоли

def up_raiting(task, prof):
	from raiting import determine_my_ranking
	# повышение рейтинга
	complexity = task.complexity
	complite = True
	determine_my_ranking(complexity, complite, prof)

def down_raiting(task, prof):
	from raiting import determine_my_ranking
	# Код понижения рейтинга:
	complexity = task.complexity
	complite = False
	determine_my_ranking(complexity, complite, prof)



def complite_hot_task(task, task_id, task_class, player_attack):
	if task.get_status() != "Active":
		print("\033[31m{}".format("[ERROR]: ")+"\033[0m{}".format("Задача не активна - операция отменена!"))
		input("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Нажмите <enter> чтобы продолжить..."))
		print("\n" * 100) # очищаем экран консоли
		return

	from task import single_task_dict, habit_task_dict, daily_task_dict
	from player_profile import Profile
	from person import NPC

	task_id = int(task_id)
	task_class_str = ""

	if task_class == SINGLE:
		task_class_str = "одиночное"
	if task_class == HABIT:
		task_class_str = "привычка"
	if task_class == DAILY:
		task_class_str = "ежедневное"

	if task_class == HABIT:
		task.add_series_point()
	player_attack() # Атакуем врага, потому что мы выполнили задание
	prof = Profile.get_instance()

	up_raiting(task, prof)

	# task_class ниже используется лишь для того чтобы занести в историю тип задания.
	prof.add_reward(task.complexity, ID=task_id, task_class=task_class_str) # Добавляем награду в соответсвии с настройками вознаграждения в зависимости от сложности задания
	if task_class != HABIT:
		task.set_status("Complite")
	if task_class == DAILY: # Ниже мы переносим дату начала на завтра:
		deadlines = get_deadlines(DAILY)
		from datetime import datetime, timedelta 
		deadlines[0] = deadlines[0] + timedelta(days=1)
		task.set_start_date(deadlines[0])
	if task_class == HABIT:
		task.add_series_point()
	print("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Победа зафиксирована!"))
	input("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Нажмите <enter> чтобы продолжить..."))
	print("\n" * 100) # очищаем экран консоли

def failed_hot_task(task, task_id, task_class, npc_attack):
	if task.get_status() != "Active":
		print("\033[31m{}".format("[ERROR]: ")+"\033[0m{}".format("Задача не активна - операция отменена!"))
		input("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Нажмите <enter> чтобы продолжить..."))
		print("\n" * 100) # очищаем экран консоли
		return

	from task import single_task_dict, habit_task_dict, daily_task_dict
	from player_profile import Profile
	from person import NPC

	task_id = int(task_id)

	npc = NPC.get_instance()
	prof = Profile.get_instance()
	down_raiting(task, prof)
	npc_attack(prof)
	if task_class != HABIT:
		task.set_status("Failed") # Задачи из словарей удаляются вообще? - Ответ: удаляются с помощью пункта "удалить" в меню заданий.
	# Я отказался от удаления заданий, ведь у Ежедневных есть функция повтора.
	print("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Поражение зафиксировано!"))
	input("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Нажмите <enter> чтобы продолжить..."))
	print("\n" * 100) # очищаем экран консоли

def del_hot_task(task_id, task_class):
	from task import single_task_dict, habit_task_dict, daily_task_dict

	task_id = int(task_id)
	task_class_str = ""

	if task_class == SINGLE:
		task_class_str = "Одиночное"
		del single_task_dict[task_id]
	if task_class == HABIT:
		task_class_str = "Привычка - "
		del habit_task_dict[task_id]
	if task_class == DAILY:
		task_class_str = "Ежедневное"
		del daily_task_dict[task_id]

	print("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format(task_class_str+" задание ID_"+str(task_id)+" удалено !"))
	input("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Нажмите <enter> чтобы продолжить..."))
	print("\n" * 100) # очищаем экран консоли

def checking_input(input_text):
	if len(input_text) <= 1:
		return False

	if input_text.isdigit() == False:
		print("\033[31m{}".format("[ERROR]: ")+"\033[0m{}".format("Допустимы лишь числовые значения!"))
		input("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Нажмите <enter> чтобы продолжить..."))     
		print("\n" * 100) # очищаем экран консоли
		return False

	return True

# Вернет 0 в случае, если все ID заняты, а инпче вернет ID от 1 до 30 включительно:
def get_task_id(single_task_dict, habit_task_dict, daily_task_dict):
	task_id = 0
	task_id_list = list(list(single_task_dict.keys())+list(habit_task_dict.keys())+list(daily_task_dict.keys()))
	for i in range(1, 31):
		task_id = i
		if task_id in task_id_list:
			task_id = 0
			continue
		else:
			break

	return task_id

# получить последний task_id, т.е task_id того задание которое пользователь добавил последним:
def get_last_task_id(single_task_dict={}, habit_task_dict={}, daily_task_dict={}, task_class=""):
	if len(single_task_dict) != 0 and task_class == SINGLE:
		return list(single_task_dict.keys())[-1]
	if len(habit_task_dict) != 0 and task_class == HABIT:
		return list(habit_task_dict.keys())[-1]
	if len(daily_task_dict) != 0 and task_class == DAILY:
		return list(daily_task_dict.keys())[-1]


def get_task_complexity(task_complexity):
	if task_complexity == "1":
		return "+"
	if task_complexity == "2":
		return "++"
	if task_complexity == "3":
		return "+++"
	if task_complexity == "4":
		return "++++"



def redirecting_input(input_text):

	if checking_input(input_text) == False:
		return
 # daily_task_dict иногда даже при наличии задач пустым будет, но это условное явление которое редко возникает. Нжуно потом исправить!
	from task import single_task_dict, habit_task_dict, daily_task_dict, DailyTask, SingleTask, HabitTask
	from player_profile import player_attack, Profile
	from person import npc_attack, NPC

	
	task_menu_item = input_text[0]
	task_operation = input_text[1]
	task_complexity = ""
	if task_operation == ADD:
		task_complexity = get_task_complexity(input_text[2])

	task_id = 0
	if task_operation == ADD:
		task_id = input_text[3:]
	else:
		task_id = input_text[2:]
	if task_id == "": # значит пользователь не добавил id:
		task_id = 0
	# если пользователь не добавил ID, то:
	if task_id == 0:
		# Создать новый при условии, что игрок хочет создать новое задание:
		if task_operation == ADD:
			task_id = get_task_id(single_task_dict, habit_task_dict, daily_task_dict)
			if task_id == 0:
				print("\033[31m{}".format("[ERROR]: ")+"\033[0m{}".format("Все ID от 1 до 30 были роздана, вы создали слишком много заданий!"))
				input("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Нажмите <enter> чтобы продолжить..."))
				return
		else: # или, если поьзователь не добавил ID и хочет использовать уже готовую задачу, то:
			task_id = get_last_task_id(single_task_dict, habit_task_dict, daily_task_dict, task_menu_item)
	task_id = int(task_id) # все ID заданий использую числовые значения типа int - перепроверил!


	# print("Вот мой task_id: "+str(task_id))
	if task_menu_item == DAILY:
		if task_operation == ADD:
			new_task = DailyTask()
			new_task.complexity = task_complexity
			new_task.set_title("ID_"+str(task_id)+": "+task_complexity)
			add_hot_task(new_task, task_id, DAILY)
		if task_operation == COMPLITE:
			task = daily_task_dict[task_id]
			complite_hot_task(task, task_id, DAILY, player_attack)
		if task_operation == FAILED:
			task = daily_task_dict[task_id]
			failed_hot_task(task, task_id, DAILY, npc_attack)
		if task_operation == DEL:
			del_hot_task(task_id, DAILY)

	if task_menu_item == SINGLE:
		if task_operation == ADD:
			new_task = SingleTask()
			new_task.set_title("ID_"+str(task_id)+": "+task_complexity)
			new_task.complexity = task_complexity
			add_hot_task(new_task, task_id, SINGLE)
		if task_operation == COMPLITE:
			task = single_task_dict[task_id]
			complite_hot_task(task, task_id, SINGLE, player_attack)
		if task_operation == FAILED:
			task = single_task_dict[task_id]
			failed_hot_task(task, task_id, SINGLE, npc_attack)
		if task_operation == DEL:
			del_hot_task(task_id, SINGLE)

	if task_menu_item == HABIT:
		if task_operation == ADD:
			new_task = HabitTask()
			new_task.set_title("ID_"+str(task_id)+": "+task_complexity)
			new_task.complexity = task_complexity
			add_hot_task(new_task, task_id, HABIT)
		if task_operation == COMPLITE:
			task = habit_task_dict[task_id]
			complite_hot_task(task, task_id, HABIT, player_attack)
		if task_operation == FAILED:
			task = habit_task_dict[task_id]
			failed_hot_task(task, task_id, HABIT, npc_attack)
		if task_operation == DEL:
			del_hot_task(task_id, HABIT)
