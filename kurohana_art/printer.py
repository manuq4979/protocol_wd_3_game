from termcolor import colored
import time, os, keyboard, random
from kurohana_art.animation_starter import starting_anim, key

# Тут спрашивали про этот буфер:
# https://www.cyberforum.ru/c-beginners/thread1491921.html?ysclid=m1fdn0as5b870627355
# https://www.cyberforum.ru/csharp-beginners/thread951254.html?ysclid=m1fdjoobbd655097982
#
# Источник: https://stackoverflow.com/questions/2520893/how-to-flush-the-input-stream
# Суть такая: помнишь при нажатии enter в цикле, после его завершения enter срабатывал, хотя я его нажимал давно?
# Так вот, это буфер ввода и его нужно очищать чтобы такого не происходило, вот код:
def flush_input():
    try: # пробуем метод для windows
        import msvcrt
        while msvcrt.kbhit():
            msvcrt.getch()
    except ImportError: # значит нужно использовать метод для линукс
        import sys, termios    #for linux/unix
        termios.tcflush(sys.stdin, termios.TCIOFLUSH)

def clear_interface():
	print("\n" * 100)

COLOR_BLACK      = 30 # черный
COLOR_RED        = 31 # красный
COLOR_GREEN      = 32 # зеленый
COLOR_YELLOW     = 33 # желтый
COLOR_BLUE       = 34 # синий
COLOR_VIOLET     = 35 # фиолетовый
COLOR_WHITE      = 37 # белый
COLOR_DARK_GREY  = "grey"  # блекло-белый

SET_OF_COLORS_FOR_SKULL_AND_AXE_ART = [[0, 1, COLOR_WHITE], [2, 8, COLOR_RED], [9, 14, COLOR_WHITE], [15, 20, COLOR_DARK_GREY]]

click_the_button_to_continue = "\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Нажмите <q> чтобы продолжить...")

def print_color_text(text, color, end="\n"):
	color = str(color)
	if color == "grey":
		print(colored(text, "dark_grey"), end=end)
	else:
		print("\033["+color+"m{}".format(text)+"\033[0m{}".format(""), end=end)


def print_skull_and_axe():
	i = 0
	with open("kurohana_art/skull_and_axe.py", "r+", encoding="utf-8") as file:
		while i < 30:
			for color_arr in SET_OF_COLORS_FOR_SKULL_AND_AXE_ART:
				start = color_arr[0]
				end   = color_arr[1]
				color = color_arr[2]
				if i >= start and i <= end:
					print_color_text(file.readline(), color, end="")
			i += 1

	print("\n")
	print_color_text("               -============================-", COLOR_YELLOW)
	print_color_text("		| Name   | ", COLOR_YELLOW, end="")
	print_color_text("BadMod bot v2.0", COLOR_RED, end="")
	print_color_text(" |", COLOR_YELLOW), 
	print_color_text("		| Author | ", COLOR_YELLOW, end="")
	print_color_text("MrSqar", COLOR_BLUE, end="")
	print_color_text("          |", COLOR_YELLOW)
	print_color_text("		| From   | ", COLOR_YELLOW, end="")
	print_color_text("Yemen", COLOR_WHITE, end="")
	print_color_text("           |", COLOR_YELLOW)
	print_color_text("		| Team   | ", COLOR_YELLOW, end="")
	print_color_text("SysteM_CrasherS", COLOR_WHITE, end="")
	print_color_text(" |", COLOR_YELLOW)
	print_color_text("               -============================-", COLOR_YELLOW)
	print_color_text("													", COLOR_YELLOW)
	print_color_text("                      K/O !!!						", COLOR_YELLOW)
	print_color_text("-======================================================-", COLOR_YELLOW)

# print_skull_and_axe()

##
#		МЕТОДЫ ДЛЯ КАЖДОГО ОТДЕЛЬНОГО ИНСТРУМЕНТА С АНИМАЦИЕЙ:
##

# TEST METHOD
def print_cobra():
	clear_interface()
	with open("kurohana_art/cobra.py", "r+", encoding="utf-8") as file:
		i = 0
		while i < 14:
			print_color_text(file.readline(), COLOR_RED, end="")
			time.sleep(0.05)
			i += 1


async def print_cobra_win():
	global key
	with open("kurohana_art/cobra.py", "r+", encoding="utf-8") as file:
		data = []
		file_size = 167
		i = 0
		while i < file_size:
			data.append(file.readline())
			i += 1

		i = 0
		while True:
			if i >= 17:
				if data[i].find("clear") != -1:
					print(click_the_button_to_continue)
					clear_interface()
					continue
				print_color_text(data[i], COLOR_RED, end="")
				await asyncio.sleep(0.1)
            
			i += 1

			if  i >= file_size:
				print('\n') # иначе у змеи сьедит крыша )
				i = 0
			if key == "q":
				clear_interface()  # убераем остатки анимации которые остаются при завершении
				return True
"""
			try:
				if keyboard.is_pressed('q'):
					clear_interface() # убераем остатки анимации которые остаются при завершении
					break
			except:
				break
"""


async def print_cobra_animation_dmg():
	global key
	version=2
	user_text=None
	standart_cadr_size = 14

	fps1 = 0.05
	animation1 = "kurohana_art/animation.py"
	size_file1 = 169

	fps2 = 0.2
	animation2 = "kurohana_art/animation2.py"
	size_file2 = 98

	file_name = animation1
	fps       = fps1
	size_file = size_file1
	cadr_size = standart_cadr_size

	if version == 2:
		file_name = animation2
		fps       = fps2
		size_file = size_file2


	clear_interface()
	data = []
	with open(file_name, "r+", encoding="utf-8") as file:
		i = 0
		while i < size_file:
			data.append(file.readline())
			i += 1
	
	i = 0
	s = cadr_size
	while True:#i < 169:
		text = data[i]
		print_color_text(text, COLOR_RED, end="")
		i += 1
		if i == s:
			print("\n")
			if user_text != None:
				# print(user_text)
				print("key value: "+key)
				pass
			print(print(click_the_button_to_continue))
			await asyncio.sleep(fps)
			clear_interface()
			s += cadr_size
		if i >= size_file:
			i = 0
			s = cadr_size
		if key == "q":
			clear_interface()  # убераем остатки анимации которые остаются при завершении
			return True
"""
        try:
			if keyboard.is_pressed('q'):
				clear_interface()  # убераем остатки анимации которые остаются при завершении
				return True # Значит анимация завершена по просьбе пользователя
		except:
			return False # значит анимацию прервали ошибочно
"""

print_cobra_win_lambda = lambda: starting_anim(print_cobra_win)
print_cobra_animation_dmg_lambda = lambda: starting_anim(print_cobra_animation_dmg)

##
#       MAIN:
##
def default_method(version=None, user_text=None):
	clear_interface()
	print("\033[31m{}".format("[ERROR]: ")+"\033[0m{}".format("Увы, для данного инструмента анимации нет!"))

get_method = {"cobra" : [print_cobra_animation_dmg_lambda, print_cobra_win_lambda], 'default' : [default_method, default_method]}


# вернет False если у игрока в экипированном нет инструмента с анимацией, а иначе вернет kurohana_id
def animation_for_tool(prof):
    kurohana_animation_for_tool = False # переменная отвечающая на вопрос - актиировать анимацию?
    kurohana_tools = [] # инструментов с анимацией может быть несколько
    kurohana_tool = ""
    for tool_id, price in prof.get_keep_tool().items():
        if tool_id.find("kurohana") != -1:
            kurohana_animation_for_tool = True
            kurohana_tools.append(tool_id)
   
    if kurohana_animation_for_tool != False:
        index_kt = random.randint(0, len(kurohana_tools)-1)
        kurohana_tool = kurohana_tools[index_kt] # рандомное из инсрументов берем для использования анимации, если более 1го такого инструмента
        index = kurohana_tool.find("kurohana")
        kurohana_tool = kurohana_tool[index+9:]
        index = kurohana_tool.find("_")
        if index != -1:
            kurohana_tool = kurohana_tool[:index]
        return kurohana_tool
    return False