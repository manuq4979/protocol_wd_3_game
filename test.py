
name = input("Укажите имя для системы:\n-> ")
network_interface = input("Есть ли доступ в интернет:\n-> ")
remote_access = input("Есть ли удаленный доступ:\n-> ")
operation_system = input("Есть ли ОС:\n-> ")
possibility_of_flashing = input("Есть ли возможность поошивки:\n-> ")
artificial_intelligence = input("Есть ли AI:\n-> ")
connection_port = input("Есть ли физические порты доступа:\n-> ")
user_interface = input("Есть ли UI(нужен для удаленного доступа):\n-> ")
control_panel = input("Есть ли панель управления(нужна для физического доступа):\n-> ")
write = input("Есть ли доступ на запись:\n-> ")
read = input("Есть ли доступ на чтение:\n-> ")

i = 0
access_algorithm_dict = ""
while True:
        print("\n#######################################################\n")
        print("Добавлено: "+str(i))
        print("0. Готово")
        print("\n#######################################################\n")
        
        res = input("Цель с доступом к системе:\n-> ")
        if res == "0":
                access_algorithm_dict.pop(-1) # удаляем лишнию ;
                break
        access_algorithm_dict += res + ";"
        i += 1
i = 0
storage = ""
while True:
        print("\n#######################################################\n")
        print("Добавлено: "+str(i))
        print("0. Готово")
        print("\n#######################################################\n")
        
        rea = input("Добавьте tool_id:\n-> ")
        if res == "0":
                storage.pop(-1) # удаляем лишнию ;
                break
        storage += res + ";"
        i += 1

SE_ID = (name+"_"+
         "NI="+network_interface+
         "RA="+remote_access+
         "OS="+operation_system+
         "PoF="+possibility_of_flashing+
         "AI="+artificial_intelligence+
         "CP="+connection_port+
         "UI="+user_interface+
         "CP2="+control_panel+
         "W="+write+
         "R="+read+"+"+
         "S;"+storage+"+"+
         "AAD;"+access_algorithm_dict)

print(SE_ID)
         
 

