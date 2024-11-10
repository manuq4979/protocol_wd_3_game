import os
import os.path
import rank_arts



newbie = "Новичок"
veteran = "Ветеран"
elite = "Элита"
professional = "Профессионал"
master = "Мастер"
grant_master = "Грант-мастер"
ligend = "Легенда"
reset_day = 90 # было 30 дней, но за 30 дней я не успею, да и сезон длиться не месяц, а вероятнее 3 месяца, это примерно 90 дней.


def get_intelect_award(intellect):
    if intellect >= 6 and intellect < 9:
        return 1
    if intellect >= 9 and intellect < 12:
        return 3
    if intellect >= 12 and intellect < 15:
        return 4
    if intellect == 15:
        return 6

    return 0


# {complexity : [eto, exp]}
# exp это point!!!
table = {newbie : {"+" : [1, 1], "++" : [2, 2], "+++" : [3, 3], "++++" : [4, 4]},
         veteran : {"+" : [4, 2], "++" : [8, 3], "+++" : [15, 5], "++++" : [20, 6]},
         elite : {"+" : [15, 3], "++" : [20, 4], "+++" : [25, 6], "++++" : [30, 7]},
         professional : {"+" : [30, 4], "++" : [35, 5], "+++" : [40, 7], "++++" : [45, 8]},
         master : {"+" : [45, 5], "++" : [50, 6], "+++" : [55, 8], "++++" : [60, 9]},
         grant_master : {"+" : [60, 5], "++" : [65, 6], "+++" : [70, 8], "++++" : [75, 9]},
         ligend : {"+" : [100, 5], "++" : [150, 6], "+++" : [200, 8], "++++" : [250, 9]}}

reward_table = {newbie : 0,
                veteran : 100,
                elite : 200,
                professional : 300,
                master : 450,
                grant_master : 700,
                ligend : 1000}



def get_complexity_table(eto_and_exp_table):
    complexity_table = {}
    for key, value in eto_and_exp_table.items():
        complexity_table[key] = value[0] # {"+" : 1} == complexity : eto
    return complexity_table

# Отвечает на вопрос "повысился ли рейтинг":
def whether_rank_has_increased_or_not(current_raiting, new_raiting):
    raiting_arr = list(table.keys())
    size = len(raiting_arr)
    position_current_raiting = 0
    position_new_raiting = 0

    for i in range(size):
        if raiting_arr[i] == current_raiting:
            position_current_raiting = i
        if raiting_arr[i] == new_raiting:
            position_new_raiting = i

    # если новый рейтинг имеет больший индекс, то значит рейтинг повысился - True, иначе False
    return (position_current_raiting < position_new_raiting)



# Просто определяет в каком диапозоне данная сумма очков и печатает арты рангов:
def is_rank_text(enter):
    global newbie, veteran, elite, professional, master, grant_master, ligend

    enter = int(enter)

    

    arr_newbie = [newbie, 0, 201, 401, 601, 801, 1000]
    arr_veteran = [veteran, 1001, 1201, 1401, 1601, 1801, 2000]
    arr_elite = [elite, 2001, 2201, 2401, 2601, 2801, 3000]
    arr_professional = [professional, 3001, 3301, 3601, 3901, 4201, 4500]
    arr_master = [master, 4501, 4901, 5301, 5701, 6101, 6500]
    arr_grant_master = [grant_master, 6501, 6801, 7101, 7401, 7701, 8000]
    arr_ligend = [ligend, 8001, 0, 0, 0, 0, 8002]

    array_ranks = [arr_newbie, arr_veteran, arr_elite, arr_professional, arr_master, arr_grant_master, arr_ligend]

    dict_numbers = ["I", "II", "III", "IV", "V"]

    is_rank = newbie
    rank_lvl = 1
    points = 0


    points = read_rank()
    points = enter + points

    print(enter)
    if(enter == 1000):
        # print("Текущий ранг: "+arr_newbie[0]+" "+dict_numbers[4])
        var_next_position_rank = 1201
        return [arr_newbie[0], dict_numbers[4], var_next_position_rank]
    if(enter == 2000):
        var_next_position_rank = 2201
        return [arr_veteran[0], dict_numbers[4], var_next_position_rank]
    if(enter == 3000):
        var_next_position_rank = 3301
        return [arr_elite[0], dict_numbers[4], var_next_position_rank]
    if(enter == 4500):
        var_next_position_rank = 4901; return [arr_professional[0], dict_numbers[4], var_next_position_rank]
    if(enter == 6500):
        var_next_position_rank = 6801
        return [arr_master[0], dict_numbers[4], var_next_position_rank]
    if(enter == 8000):
        var_next_position_rank = 10000
        return [arr_grant_master[0], dict_numbers[4], var_next_position_rank]
        
  
    for arr_rank in array_ranks:
        for lvl in range(5):
            print(enter in range(arr_rank[lvl+1], arr_rank[lvl+2]))
            if enter in range(arr_rank[lvl+1], arr_rank[lvl+2]):
            
                rank_lvl = lvl+1
                rank_lvl = dict_numbers[rank_lvl-1]
                var_start_position_interval_rank = arr_rank[lvl+1]
                var_next_position_rank = arr_rank[lvl+2]
                return [arr_rank[0], rank_lvl, var_next_position_rank, var_start_position_interval_rank]
  

def create_point_file():
    file = open("DataApp/points.txt", "w+", encoding='utf-8')
    file.write("1")
    return file

def read_rank():
    file = None
    try:
        file = open("DataApp/points.txt", "r", encoding='utf-8')
    except FileNotFoundError:
        file = create_point_file()
    points = file.read()
    file.close()
  
    if(points == ""):
        # points = 1 equal points = ""
        return 1
    
    return int(points)

def print_status(waiting_for_enter=True):
    print("\033[0m{}".format("--------------------------------------------------"))
    rank_int = read_rank()
    rank_array = is_rank_text(rank_int)
    my_rank_point = rank_int
    rank_array.append(my_rank_point)
            
    rank_arts.print_rank_art(rank_array)
    if waiting_for_enter:
        input("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Нажмите <enter> чтобы продолжить..."))    
        print("\n" * 100) # очищаем экран консоли

def write_rank(points, status=False):
    file = None
    try:
        file = open("DataApp/points.txt", "w")
    except FileNotFoundError:
        file = create_point_file()
    points = str(points)
    file.write(points)
    file.close()
    
    # Теперь будет отображать status после каждого нового добавленного поинта:
    if status == True:
        print_status()

def default_rank():
    from player_profile import Profile
    prof = Profile.get_instance()
    eto_and_exp_table = table[newbie]
    complexity_table = get_complexity_table(eto_and_exp_table)
    prof.quest_reward_setting = complexity_table
    write_rank(1)


def del_rank(points_for_del, status=False):
    points = read_rank()
    if points_for_del <= points:
        default_rank()
        write_rank(points-points_for_del)
        print("\033[32m{}".format("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("delite complite!")))
    if points_for_del > points:
        print("\033[31m{}".format("[ERROR]: ")+"\033[0m{}".format("Вы хотите удалить больше чем у Вас есть!"))
        
    # Теперь будет отображать status после каждого очередного удаленного поинта:
    if status == True:
        print_status()


def create_reset_time_of_points_file(reset_date):
    file = open("DataApp/reset_time_of_points.txt", "w+", encoding='utf-8')
    file.write(str(reset_date))
    return file

def read_reset_time_of_points_file():
    global reset_day
    file = None
    try:
        file = open("DataApp/reset_time_of_points.txt", "r", encoding='utf-8')
    except FileNotFoundError:
        from datetime import datetime, timedelta
        current_date = datetime.now().date()
        reset_date   = current_date + timedelta(days=reset_day)
        create_reset_time_of_points_file(reset_date)
        file = open("DataApp/reset_time_of_points.txt", "r", encoding='utf-8')
    reset_date = file.read()
    file.close()
    return reset_date


def check_reset_time_of_points():
    global reset_day
    from datetime import datetime, timedelta

    current_date = datetime.now().date()

    if os.path.exists("DataApp/reset_time_of_points.txt") == False:
        reset_date  = current_date + timedelta(days=reset_day)
        create_reset_time_of_points_file(reset_date)

    reset_date = read_reset_time_of_points_file()
    reset_date = datetime.strptime(reset_date, "%Y-%m-%d").date()

    if reset_date <= current_date:
        default_rank()
        reset_date  = current_date + timedelta(days=reset_day)
        create_reset_time_of_points_file(reset_date)
        print("\033[33m{}".format("[WARNING]: ")+"\033[0m{}".format("Прошло "+str(reset_day)+" в днях и пришло время сброса рейтинговых очков!"))
        print_status()
        input("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Нажмите <enter> чтобы продолжить..."))

def print_reset_point_counter():
    from datetime import datetime, timedelta
    reset_date = read_reset_time_of_points_file()
    reset_date = datetime.strptime(reset_date, "%Y-%m-%d").date()
    current_date = datetime.now().date()
    str_date_line = reset_date - current_date
    if reset_date == current_date:
        str_date_line = "Дата сброса!"
    str_dates = "От " + str(current_date) + " до " + str(reset_date)
    print("\033[32m{}".format("[Срок до сброса рейтинга]: ")+"\033[0m{}".format(str(str_date_line))) # +"("+str_dates+")"))



# решает, добавить или убавить поинты игроку.
# complexity - "++++" и т.п 
# complite - True или False
def determine_my_ranking(complexity, complite, prof):
    current_raiting = prof.get_current_raiting()
    points = read_rank()
    rank_arr = is_rank_text(points)
    rank = rank_arr[0]
    rank_number = rank_arr[1]
    eto_and_exp_table = table[rank]
    eto_and_exp = eto_and_exp_table[complexity]

    new_points = 0
    if complite == True:
        player_intellect = prof.get_intellect()
        intelect_award = get_intelect_award(player_intellect)
        new_points += points + eto_and_exp[1] + intelect_award
        if intelect_award > 0:
            print("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("У вас надбавка за повышенный интеллект: "+str(intelect_award)+" в поинтах."))
    if complite == False:
        new_points += points - eto_and_exp[1]
    write_rank(new_points)
    points = read_rank()
    rank_arr = is_rank_text(points)
    rank = rank_arr[0]
    current_rank_number = prof.get_current_raiting_number()

    print("\033[32m{}".format("[RAITING]: ")+"\033[0m{}".format("Вашь счет: "+str(points)+" в поинтах."))
    if complite == True:
        print("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Добавлено: "+str(eto_and_exp[1])+" поинтов."))
    if complite == False:
        print("\033[31m{}".format("[INFO]: ")+"\033[0m{}".format("Убавлено: "+str(eto_and_exp[1])+" поинтов."))

    # Определяет был ли ранг изменен - повышен или понижен:
    if current_raiting != rank or rank_number != current_rank_number:
        new_raiting = rank
        if rank_number != current_rank_number:
            prof.set_current_raiting_number(rank_number)
        up_rating_or_not_up = whether_rank_has_increased_or_not(current_raiting, new_raiting)
        if up_rating_or_not_up == True:
            reward_new_rank = reward_table[new_raiting]
            player_ETO = prof.get_ETO()
            history_line = "Награда за повышение ранга с ["+current_raiting+"] до ["+new_raiting+"] в сумме "+str(reward_new_rank)+"ETO."
            reward_new_rank = player_ETO + reward_new_rank
            prof.save_to_history(history_line)
            prof.set_ETO(reward_new_rank)
        prof.set_current_raiting(rank)
        eto_and_exp_table = table[rank]
        print("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Ранг был обнавлнен!"))
        print_status()
        complexity_table = get_complexity_table(eto_and_exp_table)
        prof.quest_reward_setting = complexity_table




def raiting_menu():
    while True:
        print("\n#######################################################\n")
        print_status(waiting_for_enter=False)
        print("\033[32m{}".format("[Raiting menu]: ")+"\033[0m{}".format("\n"))
        print("[1]: Установить поинты по умолчанию.")
        print("[2]: Добавить очки.")
        print("[3]: Удалить очки.")
        print("[4]: Текущий статус.")
        print("[0]: Выход.")
        print("\n#######################################################\n")

        command = input("> ")
        print("\n" * 100) # очищаем экран консоли

        if command == "0":
            return

        if command == "1": 
            default_rank()
            print("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Очки рейтинга сброшены!"))
            print_status()
            continue
                
        if command == "2":
            point = input("points> ")
                
            if point.isdigit():
                point = int(point)
                point = point + read_rank()
                write_rank(point, status=True)
                print("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Done!"))
            continue
        
        if command == "3":
            points_for_del = input("points_for_del> ")
            if points_for_del.isdigit():
                try:
                    points_for_del = int(points_for_del)
                    del_rank(points_for_del)
                except ValueError as e:
                    print("\033[31m{}".format("[ERROR]:\n")+"\033[37m{}".format(traceback.format_exc())+"\nЕсли коротко, то команда была написана неверно!")
            print("\033[0m{}".format(""))
            continue

        if command == "4":
            print_status()
            print("\033[0m{}".format(""))
            input("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Нажмите <enter> чтобы продолжить..."))
            continue
    
    
    
    
# raiting_menu()
