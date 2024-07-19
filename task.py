from datetime import datetime, timedelta
from player_profile import *
from person import *


def print_current_date():
    current_date = str(datetime.now())
    print("\033[33m{}".format("[WARNING]: ")+"\033[0m{}".format("Текущая дата и время: ["+current_date+"]."))


class Task:
    # Пример "2000-01-01" времени.
    def __init__(self, title="", description="", complexity="+", activation_time="", reward="", status="Active"):
        self.title = title
        self.description = description
        self.complexity = complexity # максимум ++++
        if activation_time == '':
            self.activation_time = ''
        if str(activation_time).isdigit() == True:
            self.activation_time = activation_time
        if activation_time != '' and type(activation_time) != int:
            self.activation_time = datetime.strptime(activation_time, "%Y-%m-%d").date()
        self.reward = reward
        self.status = status # По умолчанию все задания активны!
        
    def set_title(self, title):
        self.title = title
    
    def set_description(self, description):
        self.description = description
    
    def get_title(self):
        return self.title
    
    def get_description(self):
        return self.description
        
    def get_activation_time(self):
        return self.activation_time
    
    def set_activation_time(self, activation_time):
        self.activation_time = activation_time
    
    def get_reward(self):
        return self.reward
    
    def set_reward(self, reward):
        self.reward = reward
        
    def set_status(self, new):
        self.status = new
        
    def get_status(self):
        return self.status
    
    # Может быть другой часовой пояс!
    # Вернет 1 если дата уже прошла.
    # Вернет 2 если дата сегодня.
    # Вернет False если ещё рано.
    def check_time(self, activation_time):
        now_time = datetime.now().date()
        
        if activation_time < now_time:
            return 1
        if activation_time == now_time:
            return 2
        return False
        
    def input_task(self, description_text, description_text_2, repeat=False, no_date=False):
        # Заполняем поля и проверяем верность их заполнения:
        ID = input("ID> ")
        if ID.isdigit() == False:
            print("\033[31m{}".format("[ERROR]: ")+"\033[0m{}".format("Допустимы только цифры !"))
            return "ERROR"
        ID = int(ID)
        difficulty_lvl = input("Укажите уровень сложности> ")
        if difficulty_lvl == "+" or difficulty_lvl == "++" or difficulty_lvl == "+++" or difficulty_lvl == "++++":
            self.complexity = difficulty_lvl
        else:
            print("\033[31m{}".format("[ERROR]: ")+"\033[0m{}".format("Допустимо указывать до 4х + и только плюсы можно указывать !"))
            return "ERROR"
            
        date = input(description_text+"> ")
        if no_date == False:
            try:
                date = datetime.strptime(date, "%Y-%m-%d").date()
            except ValueError:
                print("\033[31m{}".format("[ERROR]: ")+"\033[0m{}".format("Допустимо писать лишь по шаблону - год-мес-ден и именно через тире !"))
                return "ERROR"
        if no_date == True:
            if date.isdigit() == False:
                print("\033[31m{}".format("[ERROR]: ")+"\033[0m{}".format("Напишите только кол-во дней число, даже год писать нужно днями !"))
                return "ERROR"
            
        
        if repeat != False:
            repeat = input("Повторять каждые> ")
            if repeat.isdigit() == False:
                print("\033[31m{}".format("[ERROR]: ")+"\033[0m{}".format("Напишите только кол-во дней число, даже год писать нужно днями !"))
                return "ERROR"
            repeat = int(repeat)
        
        
        # Создаем заголовок и описание:
        self.title = "ID_"+str(ID)+": "+difficulty_lvl
        
        if repeat == False:
            self.description = "["+description_text_2+"]: "+str(date)
        if repeat != False:
            self.description = "["+description_text_2+"]: "+str(date)+": "+str(repeat)
        
        if repeat != False:
            return [ID, date, repeat]
        return [ID, date]
    
    def dump_task(self):
        arr = []
        arr.append(self.title)
        arr.append(self.description)
        arr.append(self.complexity)
        arr.append(self.activation_time)
        arr.append(self.reward)
        arr.append(self.status)
        return arr
    
        
        
class SingleTask(Task):
    def __init__(self, title="", description="", complexity="", activation_time="", reward="", status="Active", execute_to=""):
        super().__init__(title, description, complexity, activation_time, reward, status)
        if execute_to == '':
            self.execute_to = ''
        else:
            self.execute_to = datetime.strptime(execute_to, "%Y-%m-%d").date() # выполнить до (какой-то даты в формате год-мес-ден)
    
    def get_execute_to(self):
        return self.execute_to
    
    def set_execute_to(self, execute_to):
        self.execute_to = execute_to
    
    # Проверяет просрочил ли игрок выполнение задания или нет.
    # Если игрок просрочил, то задание нужно завершить - убрать из списка заданий.
    # Вернет True если да.
    # Вернет False если нет.
    def check_complition_time(self):
        res = self.check_time(self.execute_to)
        if res == 2:
            return True
        return False
    
    def input_single_task(self):
        meta_data = self.input_task("Выполнить нужно до", "До")
        self.execute_to = meta_data[1]
        return meta_data[0]
        
    def dump_single_task(self):
        arr = self.dump_task()
        arr.append(str(self.execute_to))
        return arr
        
        
    
        
class DailyTask(Task):
    def __init__(self, title="", description="", complexity="", activation_time="", reward="", status="Active", start_date="", repeat="", series=""):
        super().__init__(title, description, complexity, activation_time, reward, status)
        if start_date == '':
            self.start_date = ''
        else:
            self.start_date = datetime.strptime(start_date, "%Y-%m-%d").date() # дата начала - формат г-м-д !
        self.repeat = repeat                                                   # повторение каждый 1 или 30 или еще сколько-та дней.
        self.series = series
    
    def get_start_date(self):
        return self.start_date
    
    def set_start_date(self, start_date):
        self.start_date = start_date
    
    def get_repeat(self):
        return self.repeat
    
    def set_repeat(self, repeat):
        self.repeat = repeat
        
    def get_series(self):
        return self.series
    
    def set_series(self, series):
        self.series = series
    
    
    # Вернет True если уже день закончился
    # и False если ещё дня не прошло.
    def check_day_end(self):
        start_date = self.start_date
        try: # не ожиданный баг тут, а вдруг?)
            start_date = datetime.strptime(start_date, "%Y-%m-%d").date()
        except TypeError:
            pass
        next_date = start_date + timedelta(days=1)
        res = self.check_time(next_date) 
        if res == 1 or res == 2:
            return True
        return False
    
    # Вернеет 1, если дата уже прошла.
    # Вернет True если дата сегодня.
    # Вернет False если ещё рано.
    def check_repeat_time(self):
        # Создаём локальную переменную:
        start_date = self.start_date
        # добавляем день к дате:
        try: # не ожиданный баг тут
            date = datetime.strptime(start_date, "%Y-%m-%d")
        except TypeError:
            date = start_date
        res = date + timedelta(days=self.repeat)
        try: # и тут его последствия
            res = res
        except AttributeError:
            pass
        # Переставляем дату начала на дата начала + день в который запланирован повтор,
        # Это нужно чтобы дата на месте не стояла.
        self.start_data = res
        # проверяем пора ли делать повтор задания,
        # т.е просто проверяем наступила или прошла дата:
        if self.check_time(res) == 1: # дата уже прошла?
            return 1             # дата прошла, ожидаем следующего раза
        if self.check_time(res) == 2: # сегодня запланированная дата для повтора?
            return True          # Да
        return False             # Нет
        
    def input_daily_task(self):
        meta_data = self.input_task("Укажите дату начала", "Повтор", repeat=True)
        self.start_date = meta_data[1]
        self.repeat = meta_data[2]
        
        return meta_data[0]
    
    def dump_daily_task(self):
        arr = self.dump_task()
        arr.append(str(self.start_date))
        arr.append(self.repeat)
        arr.append(self.series)
        return arr
        
        

class HabitTask(Task):
    def __init__(self, title="", description="", complexity="", activation_time="", reward="", status="Active", useful=True, useless=False, series_point=0):
        super().__init__(title, description, complexity, int(activation_time), reward, status)
        self.useful = useful   # полезная
        self.useless = useless # бесполезная
        self.series_point = series_point # серия
    
    def get_useful(self):
        return self.useful
    
    def set_useful(self, useful):
        self.useful = useful
        
    def get_useless(self):
        return self.useless
    
    def set_useless(self, useless):
        self.useless = useless
        
    def get_series_point(self):
        return self.series_point
    
    def add_series_point(self):
        self.series_point += 1
    
    def turn_down_point(self):
        self.series_point -= 1
    
    def reset_series_point(self):
        self.series_point = 0
    
    
    # Аналогично родительскому методу check_time().
    # Вернет 1 если дата уже прошла.
    # Вернет 2 если дата сегодня.
    # Вернет False если ещё рано.
    def check_reset_time(self):
        # Дни прибавляем к дате, чтобы посмотреть, пора ли уже повторять:
        current_date = str(datetime.now().date())
        # добавляем день к дате:
        date = datetime.strptime(current_date, "%Y-%m-%d").date() # Ожидает строку с датой в формате г-м-д !
        res = date + timedelta(days=int(self.activation_time))
        res = res
        return self.check_time(res)
        
    def input_habit_task(self):
        meta_data = self.activation_time = self.input_task("Сбрасывать каждые", "Сброс", repeat=False, no_date=True)
        self.activation_time = meta_data[1]
        return meta_data[0]
    
    def dump_habit_task(self):
        arr = self.dump_task()
        arr.append(self.useful)
        arr.append(self.useless)
        arr.append(self.series_point)
        arr.append(self.activation_time)
        return arr
        
        
        
def get_dump_single_task_dict(single_task_dict):
    new_dict = {}
    for ID, task in single_task_dict.items():
        new_dict[ID] = task.dump_single_task()
    return new_dict

def get_load_single_task_dict(single_task_dict):
    new_dict = {}
    for ID, task in single_task_dict.items():
        ID = int(ID)
        new_dict[ID] = SingleTask(task[0], task[1], task[2], task[3], task[4], task[5], task[6])
    return new_dict

def get_dump_daily_task_dict(daily_task_dict):
    new_dict = {}
    for ID, task in daily_task_dict.items():
        new_dict[ID] = task.dump_daily_task()
    return new_dict

def get_load_daily_task_dict(daily_task_dict):
    new_dict = {}
    for ID, task in daily_task_dict.items():
        ID = int(ID)
        new_dict[ID] = DailyTask(task[0], task[1], task[2], task[3], task[4], task[5], task[6], task[7])
    return new_dict

def get_dump_habit_task_dict(habit_task_dict):
    new_dict = {}
    for ID, task in habit_task_dict.items():
        new_dict[ID] = task.dump_habit_task()
    return new_dict
    
def get_load_habit_task_dict(habit_task_dict):
    new_dict = {}
    for ID, task in habit_task_dict.items():
        ID = int(ID)
        new_dict[ID] = HabitTask(task[0], task[1], task[2], task[3], task[4], task[5], task[6], task[7])
    return new_dict


        
        
# инициализация должна быть из файла!
with open("DataApp/single_task.txt", "r", encoding="utf-8") as file:
    json_string = file.read()
    try:
        arr = json.loads(json_string)
        single_task_dict = get_load_single_task_dict(arr)           # ID : Task
    except json.decoder.JSONDecodeError:                               # Это исключение значит, что файл конфигурации пуст, код ниже задат дефолтные значения.
        single_task_dict = {}
        arr1 = single_task_dict
        with open("DataApp/single_task.txt", "w+", encoding="utf-8") as file:
            json_string = json.dumps(arr1)
            file.write(json_string)
            print("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Save Single Task class data!"))
    

# инициализация должна быть из файла!
with open("DataApp/habit_task.txt", "r", encoding="utf-8") as file:
    json_string = file.read()
    try:
        arr = json.loads(json_string)
        habit_task_dict  = get_load_habit_task_dict(arr)
    except json.decoder.JSONDecodeError: 
        habit_task_dict = {}
        arr2 = habit_task_dict
        with open("DataApp/habit_task.txt", "w+", encoding="utf-8") as file:
            json_string = json.dumps(arr2)
            file.write(json_string)
            print("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Save Habit Task class data!"))
            
            
# инициализация должна быть из файла!
with open("DataApp/daily_task.txt", "r", encoding="utf-8") as file:
    json_string = file.read()
    try:
        arr = json.loads(json_string)
        daily_task_dict  = get_load_daily_task_dict(arr)     
    except json.decoder.JSONDecodeError: 
        daily_task_dict = {}
        arr3 = daily_task_dict
        with open("DataApp/daily_task.txt", "w+", encoding="utf-8") as file:
            json_string = json.dumps(arr3)
            file.write(json_string)
            print("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Save Daily Task class data!"))
        
        
        
        



def add_single_task():
    new_task = SingleTask()
    ID = new_task.input_single_task()
    if type(ID) != str:
        single_task_dict[ID] = new_task
        print("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Новое задание добавлено !"))
    
def add_daily_task():
    new_task = DailyTask()
    ID = new_task.input_daily_task()
    if type(ID) != str:
        daily_task_dict[ID] = new_task
        print("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Новое задание добавлено !"))
    
def add_habit_task():
    new_task = HabitTask()
    ID = new_task.input_habit_task()
    if type(ID) != str:
        habit_task_dict[ID] = new_task
        print("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Новое задание добавлено !"))

def del_single_task():
    ID = input("ID> ")
    ID = int(ID)
    del single_task_dict[ID]
    print("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Задание ID_"+str(ID)+" удалено !"))

def del_habit_task():
    ID = input("ID> ")
    ID = int(ID)
    del habit_task_dict[ID]
    print("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Задание ID_"+str(ID)+" удалено !"))

def del_daily_task():
    ID = input("ID> ")
    ID = int(ID)
    del daily_task_dict[ID]
    print("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Задание ID_"+str(ID)+" удалено !"))
    

def get_pages(task_list, chunk_size=3):
    if len(task_list) == 0:
        return []
    new_task_list = []
    page = []
    size = len(task_list)
    chunk_size = 3
    step = chunk_size
    i = 0
    chunk_size -= 1
    while i < size:
        page.append(task_list[i])
        if i == chunk_size:
            new_task_list.append(page)
            page = []
            chunk_size += step
            print(chunk_size)
        i+=1
    new_task_list.append(page)
    return new_task_list

def get_series_points_menu(task_dict):
    ID = input("ID> ")
    if ID.isdigit() == False:
        print("\033[31m{}".format("ERROR: ")+"\033[0m{}".format("ID указывается лишь в числах!"))
        return
    ID = int(ID)
    task = ""
    try:
        task = task_dict[ID]
    except KeyError:
        print("\033[31m{}".format("ERROR: ")+"\033[0m{}".format("задание не найдено!"))
        return
    
    print("Серия: "+str(task.get_series_point()))
    print("1. +")
    print("2. -")
    print("3. Назад")
    res = input("> ")
    if res == "1":                       # При выборе плюса, игрок отмечает, что выполнил привычку.
        task.add_series_point()
        player_attack()                  # Атакуем врага, потому что мы выполнили задание привычки
        prof = Profile.get_instance()
        prof.add_reward(task.complexity, ID=ID, task_class="привычки или ежедневные")
                                         # Добавляем награду в соответсвии с настройками вознаграждения в зависимости от сложности задания
    if res == "2":                       # При выборе минуса, игрок подтверждает, что не выполнил привычку
        task.turn_down_point()
        prof = Profile.get_instance()
        npc_attack(prof)                 # Получаем урон от врага, потому что не выполнили задание привычки
    if res == "3":
        return

def get_menu_task(title_minu, task_dict, add_task, del_task, habit_menu=False):
    index = 0
    while True:
        task_list = task_dict.values()           # Берем массив задачь - получаем dict_values([])
        task_list = list(task_list)              # dict_values([]) преобразуем в []
        pages = get_pages(task_list)             # Делим на страницы
        print(title_minu+":\n")
        if len(pages) != 0:
            for task in pages[index]:
                if task.get_status() == "Active":# Не активные задания не будут отображены!
                    print(task.get_title())
                    print(task.get_description())
        print("\n-----------")
        print("1. Добавить")
        if habit_menu == False:
            print("2. Завершено")
            print("2.5. Провалено")
        else:
            print("2. Выбрать")
        print("3. Удалить")
        if len(pages) > 1:                       # Если страниц более 1, то отобразить кнопку Далее
            print("4. Далее")
        if index > 0:
            print("5. Назад")
        print("0. Выход")
            
        number = input("> ")
        
        if number == "1":
            add_task()
        if number == "2":
            if habit_menu == False:
                ID = input("ID> ")
                if ID.isdigit() == False:
                    print("\033[31m{}".format("ERROR: ")+"\033[0m{}".format("Допустимы лишь числовые значения!"))
                else:
                    ID = int(ID)
                    task = task_dict[ID]
                    player_attack()                  # Атакуем врага, потому что мы выполнили задание
                    prof = Profile.get_instance()
                    prof.add_reward(task.complexity, ID=ID, task_class="одиночное") 
                                                     # Добавляем награду в соответсвии с настройками вознаграждения в зависимости от сложности задания
                    task.set_status("No active")
                    ID = int(ID)
                    del task_dict[ID]
            if habit_menu == True:
                get_series_points_menu(task_dict)
        if number == "2.5":
            import person
            
            ID = input("ID> ")
            if ID.isdigit() == False:
                print("\033[31m{}".format("ERROR: ")+"\033[0m{}".format("Допустимы лишь числовые значения!"))
                break
            ID = int(ID)
            task = task_dict[ID]
            npc = NPC.get_instance()
            prof = Profile.get_instance()
            npc_attack(prof)
            task.set_status("No active") # Задачи из словарей удаляются вообще?
            del task_dict[ID]            # Теперь - удаляется )
            print("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Поражение зафиксировано !"))
        if number == "3":
            del_task()
        if number == "4":
            if len(pages) > 1:
                index += 1
        if number == "5":
            if index > 0:
                index -= 1
        if number == "0":
            return
        if number.isdigit():
            if int(number) > 5:
                print("\033[33m{}".format("[WARNING]: ")+"\033[0m{}".format("выбран не верный номер."))
                
                


# Сохранить данные модуля в файл:
def save_data_task():
    new_single_task_dict = get_dump_single_task_dict(single_task_dict)
    new_habit_task_dict  = get_dump_habit_task_dict(habit_task_dict)
    new_daily_task_dict  = get_dump_daily_task_dict(daily_task_dict)
    
    arr1 = new_single_task_dict
    arr2 = new_habit_task_dict
    arr3 = new_daily_task_dict
    
    with open("DataApp/daily_task.txt", "w+", encoding="utf-8") as file:
        json_string = json.dumps(arr3)
        file.write(json_string)
        print("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Save Daily Task class data!"))
        
    with open("DataApp/habit_task.txt", "w+", encoding="utf-8") as file:
        json_string = json.dumps(arr2)
        file.write(json_string)
        print("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Save Habit Task class data!"))
    
    with open("DataApp/single_task.txt", "w+", encoding="utf-8") as file:
        json_string = json.dumps(arr1)
        file.write(json_string)
        print("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Save Single Task class data!"))
