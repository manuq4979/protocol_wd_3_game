import os
try:
	from progress.bar import IncrementalBar
except ModuleNotFoundError:
	print("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Модуль progress не установлен - исправляем..."))
	os.system("pip install progress")
	from progress.bar import IncrementalBar
	print("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("готово!"))
	input("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Нажмите <enter> чтобы продолжить..."))


def num_to_countdown(num):
	num = int(num)
	count_arr = []
	i = 0
	while num != 0:
		num = num-1
		i = i+1
		count_arr.append(i)
	return count_arr
	
def procent_visualization(procent):
	bar = "                                 "
	bar = list(bar)
	three = "█"
	three_int = 3

	itog = round(procent/three_int)
	for i in range(itog):
		bar[i] = three

	progress_bar = ''.join(bar)
	return progress_bar

def print_count_bar(rank_name, rank_lvl, this_position_rank, next_position_rank, procent):
	s1 = rank_name + " " + rank_lvl + " "
	default_coloc = "\033[37m{}"
	color = default_coloc
	
	if procent >= 60  and color == default_coloc:
		color = "\033[32m{}" # зеленый
	if procent >= 40 and color == default_coloc:
		color = "\033[33m{}" # желтый
	if procent <= 50 and color == default_coloc:
		color = "\033[31m{}" # красный
		
	s2 = color.format(procent_visualization(procent))
	s3 = " "+str(this_position_rank)+"/"+str(next_position_rank)
	
	print(s1 + "|"+s2+"|" + s3)






newbie_art = ("░░░░░░░░▒▒▒▒░░░░░░░░░░░░░░░░░░▒░░░▒▓▓▒░░░░░░░\n"+
	     "░░░░░▒▓▓▒▒▒▒▒▓▓▓▒▒░░░░░░▒▒▓▓▓▒▒░░▓▓░░█▒░░░░░░\n"+
	     "░░░░▓▓░░░░░░░░░░▒▒▓▓▒▓▓▓▒░░░░░░░░▒▓▓▓▓░░░░░░░\n"+
	     "░░░░█▒░░░░░░░░░░░░▓▓▓▓▓▒░░░░░░░░░░░░░▒░░░░░░░\n"+
	     "░░░░█▒░░░░░░░░░▒▓▓▒░░░░▒▓▓▒░░░░░░░░░▓▓░░░░░░░\n"+
	     "░░░░▓▓░░░░░░░▒▓▓░░░░░░░░░░▓▓▒░░░░░░░█▒░░░░░░░\n"+
	     "░░░░░▓▓░░░░▒▓▓░░░░░░░░░░░░░░▓▓▒░░░░▓▓░░░░░░░░\n"+
	     "░░░░░░█▒░░▓▓░░░░░▒▓▓▓▓▓▒░░░░░▒▓▓░░▓▓░░░░░░░░░\n"+
	     "░░░░░░▒▓▓▓▒░░░░░▓▓▒░░░▒█▓░░░░░░▓▓▓▓░░░░░░░░░░\n"+
	     "░░░░░░░▓█▓░░░░░░█▒░░░░░▒█░░░░░░░██▓░░░░░░░░░░\n"+
	     "░░░░░░▓▓░▒▓▒░░░░▒█▒░░░▒█▓░░░░░▒█▒░▓▓░░░░░░░░░\n"+
	     "░░░░░▓▓░░░░▓▓░░░░░▒▓▓▒▒░░░░░▒▓▓░░░░▓▓░░░░░░░░\n"+
	     "░░░░▓▓░░░░░░▒▓▓░░░░░░░░░░░▒▓▓░░░░░░░▓▓░░░░░░░\n"+
	     "░░░▒█░░░░░░░░░▒▓▓▒░░░░░░▒▓▓░░░░░░░░░▒█░░░░░░░\n"+
	     "░░░▓▓░░░░░░░░░░░░▓▓▒░▒▓▓▓░░░░░░░░░░░░█▓░░░░░░\n"+
	     "░░░▓▓░░░░░░░░░░░░░▒███▓░░░░░░░░░░░░░░█▒░░░░░░\n"+
	     "░░░░█▒░░░░░░░░▒▒▓▓▒░░░▒▒░▒▓▓▓▓▒░░░░░▓▓░░░░░░░\n"+
	     "░░░░░▒▓▓▓▓▓▓▓▓▒▒░░░░░░░░░▓▓░░▓▓░▒▓▓▓▒░░░░░░░░\n"+
	     "░░░░░░░░░░░░░░░░░░░░░░░░░░▒▓▒▒░░░░░░░░░░░░░░░\n")


veteran_art =	("░░░░░░░░░░░░░░░░░░░░▓█░░░░░░░░░░░░░░░░░░░░░░░░\n"+
		"░░░░░░░░░░░░░░░░░░░▒██▒░░░░░░░░░░░░░░░░░░░░░░░\n"+
		"░░░░░░░░░░░░░░░░░░░████░░░░░░░░░░░░░░░░░░░░░░░\n"+
		"░░░░░░░░░░░░░░░░░░▓████▓░░░░░░░░░░░░░░░░░░░░░░\n"+
		"░░░░░░░░░░░░░░░░░░██████▒░░░░░░░░░░░░░░░░░░░░░\n"+
		"░░░░░░░░░░░░░░░░░████████░░░░░░░░░░░░░░░░░░░░░\n"+
		"░░░▒██████████████████████████████████▒░░░░░░░\n"+
		"░░░░░▒▓████████████████████████████▓▒░░░░░░░░░\n"+
		"░░░░░░░░▒████████████████████████▒░░░░░░░░░░░░\n"+
		"░░░░░░░░░░░▓██████████████████▓░░░░░░░░░░░░░░░\n"+
		"░░░░░░░░░░░░░▒██████████████▓░░░░░░░░░░░░░░░░░\n"+
		"░░░░░░░░░░░░░████████████████░░░░░░░░░░░░░░░░░\n"+
		"░░░░░░░░░░░░▒████████████████▓░░░░░░░░░░░░░░░░\n"+
		"░░░░░░░░░░░░███████▓░░▒███████░░░░░░░░░░░░░░░░\n"+
		"░░░░░░░░░░░█████▓▒░░░░░░░▓█████░░░░░░░░░░░░░░░\n"+
		"░░░░░░░░░░▓▒░░░░░░░░░░░░░░░░░░▒█░░░░░░░░░░░░░░\n"+
		"░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n")

elite_art =	(".......................*+.......................\n"+
		"......................+S;;......................\n"+
		".....................;SS:,;.....................\n"+
		"....................;SSS:.::....................\n"+
		"...................:%SSS:..::...................\n"+
		"..................,%SSSS:...;:..................\n"+
		".................,%SSSSS:....;,.................\n"+
		"......,,,,,,:::::;%SSSSS:....;???********++;;...\n"+
		"...;?*+;::,,......,+%SSS:..:?SSSSSSS%%?*;;;;,...\n"+
		"....:?SSS%%?*++;:,,.,+%S::?SS%%?*+::,...,:,.....\n"+
		"......:*SSSSSSSSSS%%?**%?*+::,........,::.......\n"+
		"........:*SSSSSSSSSS?+*%+??;:,......,::,........\n"+
		"..........:*SSSS?*;,.+SS::?SS%*;:..::,..........\n"+
		"............:*;,...,?SSS:.,*SSSSS%*,............\n"+
		"............,:....:%SSSS:...;SSSSS%,............\n"+
		"............:,...+SSSSSS:....:%SSSS;............\n"+
		"............;..,*SSSSSSS:.....,*SSS*............\n"+
		"...........,;.:%SSSSS%?+::,,....+SS%,...........\n"+
		"...........:,;SSSS?*;,...,,:::,,.:%S;...........\n"+
		"...........+*S%*;,...........,,::::??...........\n"+
		"..........,++:...................,,:*,..........\n"+
		"................................................\n")


professional_art = ("░░░░░░░░░░░░░░░░░░░░░░░░▓▓░░░░░░░░░░░░░░░░░░░░░░░░\n"+
		   "░░░░░░░░░░░░░░░░░░░░░░░▒██▒░░░░░░░░░░░░░░░░░░░░░░░\n"+
		   "░░░░░░░░░░░░░░░░░░░░░░░████░░░░░░░░░░░░░░░░░░░░░░░\n"+
		   "░░░░░░░░░░░░░░░░░░░░░░▓████▓░░░░░░░░░░░░░░░░░░░░░░\n"+
		   "░░░░░░░░░░░░░░░░░░░░░▒██████▒░░░░░░░░░░░░░░░░░░░░░\n"+
		   "░░░░░░░░░░░░░░░░░░░░░████████░░░░░░░░░░░░░░░░░░░░░\n"+
		   "░░░░░░░░░░░░░░░░░░░░▓███▒▒███▓░░░░░░░░░░░░░░░░░░░░\n"+
		   "░░░░░░░░░░░░░░░░░░░▒███▓░░▓███▒░░░░░░░░░░░░░░░░░░░\n"+
		   "░░▓████████████████████░░░░████████████████████▓░░\n"+
		   "░░░░▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒░░░░▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒░░░░\n"+
		   "░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n"+
		   "░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n"+
		   "░░░░░░░░░░░░▒▓██████▓░░░░░░░░▓██████▓▒░░░░░░░░░░░░\n"+
		   "░░░░░░░░░░░░░░░▓████░░░░░░░░░░████▓░░░░░░░░░░░░░░░\n"+
		   "░░░░░░░░░░░░░░░▓███▒░░░░▒▒░░░░▒███▓░░░░░░░░░░░░░░░\n"+
		   "░░░░░░░░░░░░░░▒███▓░░░▓████▓░░░▓███▒░░░░░░░░░░░░░░\n"+
		   "░░░░░░░░░░░░░░████░▒▓████████▓▒░████░░░░░░░░░░░░░░\n"+
		   "░░░░░░░░░░░░░▓████████▓▒░░▒▓████████▓░░░░░░░░░░░░░\n"+
		   "░░░░░░░░░░░░▒███████▒░░░░░░░░▒███████▒░░░░░░░░░░░░\n"+
		   "░░░░░░░░░░░░█████▓░░░░░░░░░░░░░░▓█████░░░░░░░░░░░░\n"+
		   "░░░░░░░░░░░▓██▓▒░░░░░░░░░░░░░░░░░░▒▓██▓░░░░░░░░░░░\n"+
		   "░░░░░░░░░░▒▓▒░░░░░░░░░░░░░░░░░░░░░░░░▒▓▒░░░░░░░░░░\n"+
		   "░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n")
			


master_art =	("░░░░░░░░░░░░░░░░░░░░▒▓░░░░░░░░░░░░░░░░░░\n"+
		"░░░░░░░░░░░░░░░░░░░░██▒░░░░░░░░░░░░░░░░░\n"+
		"░░░░░░░░░░░░░░░░░░░████▒░░░░░░░░░░░░░░░░\n"+
		"░░░░░░░░░░░░░░░░░░██████░░░░░░░░░░░░░░░░\n"+
		"░░░░░░░░░░░░░░░░░████████░░░░░░░░░░░░░░░\n"+
		"░░░░░░░░░░░░░░░░██████████░░░░░░░░░░░░░░\n"+
		"░░░░░░░░░░░░░░░███░░██████▓░░░░░░░░░░░░░\n"+
		"░░░░░░░░░░░░░░███░░░▒██████▒░░░░░░░░░░░░\n"+
		"░░░░░░░░░░░░░▓██░░░░░▒██████▒░░░░░░░░░░░\n"+
		"░░░░░░░░░░░░▓██▒░░░░░░▓██████░░░░░░░░░░░\n"+
		"░░░░░░░░░░░▓██▒░░░░░░░░▓██████░░░░░░░░░░\n"+
		"░░░░░░░░░░▓██▒░░░░░░░░░░██████▓░░░░░░░░░\n"+
		"░░░░░░░░░▒██▒░░░░░░░░░░░░██████▓░░░░░░░░\n"+
		"░░░░░░░░▒██▓░░░░░░░░░░░░░▒██████▒░░░░░░░\n"+
		"░░░░░░░▒██▓░░░░░░░░░░░░░░░▒██████▒░░░░░░\n"+
		"░░░░░░▒██▓░░░░░░░░░░░░░░░░░▓██████░░░░░░\n"+
		"░░░░░▒██▓░░░░░░░░░░░░░░░░░░░███████░░░░░\n"+
		"░░░░░██▓░░░░░░░░░░░░░░░░░░░░░██████▓░░░░\n"+
		"░░░░██▓░░░░░░░░░░░░░░░░░░░░░░░██████▓░░░\n"+
		"░░░███░░░░░░░░░░░░░░░░░░░░░░░░▒██████▒░░\n"+
		"░░███░░░░░░░░░░░░░░░░░░░░░░░░░░▒██████▒░\n"+
		"░██████████████████████████████████████░\n"+
		"░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n")



grant_master_art = ("░░░░░░░░░░░░░░░░░░░░░░░▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░\n"+
		   "░░░░░░░░░░░░░░░░░░░▓██▓▓▒▓███▓░░░░░░░░░░░░░░░░░░░░\n"+
		   "░░░░░░░░░░░░░░░░░▒███░░░░░░░███▒░░░░░░░░░░░░░░░░░░\n"+
		   "░░░░░░░░░░░░░░░░░███░░░░░░░░▒███░░░░░░░░░░░░░░░░░░\n"+
		   "░░░░░░░░░░░░░░░░░███░░░░░░░░▒███░░░░░░░░░░░░░░░░░░\n"+
		   "░░░░░░░░░░░░░░░░▒███░░░░░░░░▓██▒░░░░░░░░░░░░░░░░░░\n"+
		   "░░░░░░░░░░░░░░░░▒███░░░▒▒▒▒▒██▒░░░░░░░░░░░░░░░░░░░\n"+
		   "░░░░░░░░░░░░░░░░▒███░░░▓▓▓▓██▓▒░░░░░░░░░░░░░░░░░░░\n"+
		   "░░░░░░░░░░░░░░░░▒███░░░░░░░░▒███▒░░░░░░░░░░░░░░░░░\n"+
		   "░░░░░░░░░░░░░░░░▒███░░░░░░░░░▓███▒░░░░░░░░░░░░░░░░\n"+
		   "░░░░░░░░░░░░░░░░▒███░░░░░░░░░░████░░░░░░░░░░░░░░░░\n"+
		   "░░░░░░░░░░░░░░░░▒███░░░░░░░░░░████░░░░░░░░░░░░░░░░\n"+
		   "░░░░░░░░░░░░░░░░▒███░░░░░░░░░░███▓░░░░░░░░░░░░░░░░\n"+
		   "░░░░░░░░░░░░░░░░▒███░░░░░░░░░▓██▓░░░░░░░░░░░░░░░░░\n"+
		   "░░░░░░░░░░░░░░░░▒████▒░░░░░▒▓██▒░░░░░░░░░░░░░░░░░░\n"+
		   "░░░░░░░░░░░░░░░░▒███░▒▓▓▓▓█▓▓▒░░░░░░░░░░░░░░░░░░░░\n"+
		   "░░░░░░░░░░░░░░░░▒███░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n"+
		   "░░░░░░░░░░░░░░░░▒███░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n"+
		   "░░░░░░░░░░░░░░░░▓███░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n"+
		   "░░░░░░░░░░░░░░░░███▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n"+
		   "░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n")
		   

ligend_art =	("░░░░░░░░░▓████████▒░░░░░░░░░░░\n"+
		"░░░░░░▒█████████████▒░░░▒██░░░\n"+
		"░░░░░▓█████▓▒▒▒▒█████▒░████░░░\n"+
		"░░░░█████▓░░░░░░░█████████░░░░\n"+
		"░░░█████▒░░░░░░░░▓███████░░░░░\n"+
		"░░▓████▒░░░░░░░░░▒██████░░░░░░\n"+
		"░░████▓░░░░░░░░░░▒█████░░░░░░░\n"+
		"░▒████▒░░░░░░░░░░█████▓░░░░░░░\n"+
		"░▒████▒░░░░░░░░░▓█████▒░░░▒▓▒░\n"+
		"░░████▓░░░░░░░▒███████▒░░███▒░\n"+
		"░░▓████▒░░░░▒████▒▒████▒████░░\n"+
		"░░░▓███████████▒░░░▓███████▒░░\n"+
		"░░░░▒▓██████▓▒░░░░░░▒████▓░░░░\n"+
		"░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n")



rank_art_dict = {
	"Новичок": newbie_art, 
	"Ветеран": veteran_art, 
	"Элита": elite_art, 
	"Профессионал": professional_art, 
	"Мастер": master_art, 
	"Грант-мастер": grant_master_art, 
	"Легенда": ligend_art
	}


def print_rank_art(rank_array):
	print(rank_array)
	rank_name 	   = rank_array[0]
	rank_lvl  	   = rank_array[1]
	next_position_rank = rank_array[2]
	start_position     = rank_array[3]
	this_position_rank = rank_array[4] 			        # начала интервала(напримерБ 201 и 451 - начало, это 201) - нужно чтобы вычеслить интервал.
	
	end_position_interval 	= next_position_rank - start_position   # конец интервала, например 451 - 201 = 250 - это и есть заложенный интервал, от 1 до 250.
	current_position_interval = this_position_rank - start_position	# посмотрим как далеко мы от начала интервала.
	
	rank_art = rank_art_dict[rank_name]
	procent = 100*current_position_interval / end_position_interval
	
	
	print(rank_art)
	print_count_bar(rank_name, rank_lvl, this_position_rank, next_position_rank, round(procent))
	print("\n")
	
	