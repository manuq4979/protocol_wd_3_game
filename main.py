import profile_wd
import functions
from person import NPC

    

PS1 = profile_wd.PS1
help = ("1 - меню игры\n"+
        "2 - выход из приложения\n")
        
def print_NPC():
    npc = NPC.get_instance()
    #print(npc.installed_contender)
    if npc.installed_contender != "" and npc.installed_contender != "None" and npc.installed_contender != None:
        print("\033[31m{}".format("[Противник]: ")+"\033[0m{}".format(""))
        print(npc.print_characteristics())
        print("\n")

while(True):
    print("\033[33m{}".format("[WARNING]: ")+"\033[0m{}".format("Используйте команду help, если не разобрались!")+"\n")
    functions.check_relevance_task() # Проверяем, не просрочил ли игрок задания или не пора бы сделать задание активным или вовсе сбросить серии просто у задний привычек
    functions.check_HP()
    print_NPC()
    functions.get_prof()
    
    text = input(PS1)
	
    if text == "2":
        functions.save_data_store()
        functions.save_data_profile()
        functions.save_data_person()
        functions.save_data_task()
        functions.save_data_SE()
        break
	
    if text == "help":
        print("\033[32m{}".format("Helper:")+"\033[0m{}".format(""))
        print(help)
	
    if text == "1":
        functions.get_menu()

    
