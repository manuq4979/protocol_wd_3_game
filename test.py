print("\n")

name = input("Укажите имя для системы:\n-> ")
print("\n")

network_interface = input("Есть ли доступ в интернет:\n-> ")
print("\n")
if network_interface == "1":
        remote_access = "1"
        # input("Есть ли удаленный доступ:\n-> ")
        # print("\n")
else:
        remote_access = "0"

operation_system = input("Есть ли ОС:\n-> ")
print("\n")
possibility_of_flashing = input("Есть ли возможность прошивки:\n-> ")
print("\n")
artificial_intelligence = input("Есть ли AI:\n-> ")
print("\n")
connection_port = input("Есть ли физические порты доступа:\n-> ")
print("\n")
if network_interface == "1":
        user_interface = "1"
        # input("Есть ли UI(нужен для удаленного доступа):\n-> ")
        # print("\n")
else:
        user_interface = "0"

if connection_port == "1":
        control_panel = "1"
        # input("Есть ли панель управления(нужна для физического доступа):\n-> ")
        # print("\n")
else:
        control_panel = "0"
        
write = input("Есть ли доступ на запись:\n-> ")
print("\n")
read = input("Есть ли доступ на чтение:\n-> ")
print("\n")
        
i = 0
access_algorithm_dict = ""
while True:
        print("\n#######################################################\n")
        print("Уже добавлено: "+str(i))
        print("0. Готово")
        print("\n#######################################################\n")
        
        res = input("Цель с доступом к системе:\n-> ")
        if res == "0":
                access_algorithm_dict = access_algorithm_dict[:-1] # удаляем лишнию ;
                break
        access_algorithm_dict += res + ";"
        i += 1
i = 0
storage = ""
while True:
        print("\n#######################################################\n")
        print("Добавьте награду в хранилище:")
        print("Уже добавлено: "+str(i))
        print("0. Готово")
        print("\n#######################################################\n")
        
        res = input("Добавьте tool_id:\n-> ")
        if res == "0":
                storage = storage[:-1] # удаляем лишнию ;
                break
        storage += res + ";"
        i += 1

SE_ID = (name+"_"+
         "NI="+network_interface+"_"+
         "RA="+remote_access+"_"+
         "OS="+operation_system+"_"+
         "PoF="+possibility_of_flashing+"_"+
         "AI="+artificial_intelligence+"_"+
         "CP="+connection_port+"_"+
         "UI="+user_interface+"_"+
         "CP2="+control_panel+"_"+
         "W="+write+"_"+
         "R="+read+"+"+
         "S;"+storage+"+"+
         "AAD;"+access_algorithm_dict)

print("\n\n\n")
print(SE_ID)
print("\n\n\n")
         
 

