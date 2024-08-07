import profile_wd
import functions
from person import NPC
from hot_scripts.high_speed_task_creation import redirecting_input

    

PS1 = profile_wd.PS1
help = ("1 - меню игры\n"+
        "2 - сохранить и выйти\n"+
        "3 - сохранить\n"+
        "4 - создать NPC_ID\n"+
        "5 - создать SE_ID\n"+
        "6 - создать tool_id\n")
        
def print_NPC():
    npc = NPC.get_instance()
    #print(npc.installed_contender)
    if npc.installed_contender != "" and npc.installed_contender != "None" and npc.installed_contender != None:
        print("\033[31m{}".format("[Противник]: ")+"\033[0m{}".format(""))
        print(npc.print_characteristics())
        print("\n")

while(True):
    print("\n#######################################################\n")
    print("\033[33m{}".format("[WARNING]: ")+"\033[0m{}".format("Используйте команду help, если не разобрались!")+"\n")
    print("\033[33m{}".format("[WARNING]: ")+"\033[0m{}".format("Если игрок погибает, то задания вероятно будут все сброшены!(это баг который стал фичей)"))
    print("\n")
    functions.print_current_date()
    functions.print_counter_tasks()
    print("\n")
    functions.check_relevance_task() # Проверяем, не просрочил ли игрок задания или не пора бы сделать задание активным или вовсе сбросить серии просто у задний привычек
    functions.check_HP()
    print_NPC()
    functions.get_prof()
    print("\n#######################################################\n")
    
    text = input(PS1)

    if text == "help":
        print("\n#######################################################\n")
        print("\033[32m{}".format("Helper:")+"\033[0m{}".format(""))
        print(help)
        print("\n#######################################################\n")
        input("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Нажмите <enter> чтобы продолжить..."))
    else: # если текст, то метод выдаст ошибку, так я исключу попадание текста в него.
        redirecting_input(text) # перенаправка на hot scripts
    if text == "4":
        from hot_scripts.create_NPC_ID import main
        main()
    if text == "5":
        from hot_scripts.create_SE_ID import main
        main()
    if text == "6":
        from hot_scripts.create_tool_id import main
        main()
	
    if text == "2" or text == "3":
        print("\n#######################################################\n")
        functions.save_data_store()
        functions.save_data_profile()
        functions.save_data_person()
        functions.save_data_task()
        functions.save_data_SE()
        print("\n#######################################################\n")
        input("\033[32m{}".format("[INFO]: ")+"\033[0m{}".format("Нажмите <enter> чтобы продолжить..."))
        if text == "2":
            break
	
    if text == "1":
        functions.get_menu()

    
