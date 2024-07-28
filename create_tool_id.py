
name = input("Введите имя инструмента:\n-> ")
name = name.replace(" ", "-")

i = 0
character = ""
while True:
    print("\n#######################################################\n")
    print("Уже добавлено: "+str(i))
    print("0. Готово")
    print("\n#######################################################\n")
    res = input("Задайте характеристику(Пример: armor=200):\n->")
    if res == "0":
        break
    character = + "_" + res
    i += 1

print("\n\n\n")
print(character)
print("\n\n\n")