name = input("Укажите имя для системы> ")
network_interface = input("Есть ли доступ в интернет> ")
remote_access = input("Есть ли удаленный доступ> ")
operation_system = input("Есть ли ОС> ")
possibility_of_flashing = input("Есть ли возможность поошивки> ")
artificial_intelligence = input("Есть ли AI> ")
connection_port = input("Есть ли физические порты доступа> ")
user_interface = input("Есть ли UI(нужен для удаленного доступа)> ")
control_panel = input("Есть ли панель управления(нужна для физического доступа)> ")
write = input("Есть ли доступ на запись> ")
read = input("Есть ли доступ на чтение> ")

i = 0
access_algorithm_dict = ""
while True:
        print("Добавлено: "+str(i))
        print("0. Готово")
        res = input("Цель с доступом к системе> ")
        if res == "0":
                access_algorithm_dict.pop(-1) # удаляем лишнию ;
                break
        access_algorithm_dict += res + ";"
        i += 1
i = 0
storage = ""
while True:
        print("Добавлено: "+str(i))
        print("0. Готово")
        rea = input("Добавьте tool_id> ")
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
         
 

