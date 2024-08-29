# protocol_wd_3_game
## Описание:
``Инструменты`` и ``Умная электорника``, ``NPC``, ``Profile``, а также классы ``Task`` - это пять основных класса. ``Умная электроника`` и ``NPC`` - это цели, 
которые нужно атаковать и взламывать, а ``инструменты класс`` общего назначения. Все предметы в ``инвенторе`` - это ``инструменты``, все враги, это ``NPC``, 
а ``умная электроника`` любая электроника - ноутбук, умное оружие, карты доступа. По сути, есть ``игрок`` и ``цели``.

Вся эта пограмма, это движок игры, которая по сути менеджер задачь с элементами ролевой игры. Программа относиться к классу игр по геймификации.

## SE - Smart Electronics:
```Python
class:
	se.network_interface       = int(base_char_all[0][1]) # NI - network_interface
	se.remote_access           = int(base_char_all[1][1]) # RA - remote_access
	se.operation_system        = int(base_char_all[2][1]) # OS - operation_system
	se.possibility_of_flashing = int(base_char_all[3][1]) # PoF - possibility_of_flashing
	se.artificial_intelligence = int(base_char_all[4][1]) # AI - artificial_intelligence
	se.connection_port         = int(base_char_all[5][1]) # CP - connection_port
	se.user_interface          = int(base_char_all[6][1]) # UI - user_interface
	se.control_panel           = int(base_char_all[7][1]) # CP2 - control_panel
	se.write                   = int(base_char_all[8][1]) # W - write
	se.read                    = int(base_char_all[9][1]) # R - read

	access_algorithm_dict = arr[11]            # Список целей, список NPC которые имеют карты доступа. AAD - access_algorithm_dict
	storage = arr[12]                          # Тут трофеи - инструменты, ETO, карты доступа. Их может быть сколько угодно, но больше чем у NPC. S - storage
```

Пример SE_ID:
```Python
name_NI=1_RA=0_OS=1_PoF=0_AI=0_CP=1_UI=1_CP2=1_W=0_R=0+S;gun_damage=100_charge=100;gun_recharge=100+AAD;bot_HP=100_armor=200_damage=100_strong=3_critical-dmg=45_drop-trophy:smart-card=write=True
```

### Характеристики SE зависят друг от друга:
Например, у устройства у которого нет панели управления и портов, не может иметь физического доступа.

``control_panel`` - это интерфейс пользователя для физического доступа.
``user_interface`` - UI для удаленного доступа.

если порты закрыты, а именно ``connection_port == 0``, то физическиц доступ не возможен.

``possibility_of_flashing`` - возможность прошивки - позволяет изменить любое поле, кроме storage и access_algorithm_dict.

Но прошивка доступна лишь если есть права на запись.

А вот так буде выглядить карта доступа. tool_id:
```Python
name_access_card_read_write # Чтение Запись
name_access_card_read       # Только чтение
name_access_card_write      # Только запись
```

Карты доступа являются одноразовыми и они универсальные. Система при попытки получить доступ автоматически возьмет карту из инвентарая!


Пример компьютера, для доступа к полю Smart Electronics. tool_id:
```Python
netbook_smart_electronics=1
```

``storage`` - хранит в себе tool_id или ETO - это награда. Чтобы её получить нужно скопировать его и добавить в инвентарь.
Но чтобы соодержимое отобразилось, нужны права на чтение.

#### Примечание:
Полученные ETO потребуется внести через меню разработчика.

``possibility_of_flashing`` - возможность прошивки.
``access_algorithm_dict`` - тут находяться NPC_ID, строка характеристик противников, чьи трофеи являются картами доступа - для физического доступа или токены для удаленного доступа.
Нужно скопировать NPC_ID и добавить его в качестве врага. Шанс выпадения трофея 40% из чего следует что возможно противника, одного и того же придетсья победить врага возможно ни один раз.
Но чтобы можно было скопировать NPC_ID врага, потребуется получить доступ к чтению.

Но как получить доступ если нет возможности выбить карту у врага?

Тут на помощь приходит магазин или запас карт доступа.
#### ВАЖНО!
Протвник может быть лишь 1! т.е только один NPC_ID может быть в словаре, если противников несколко - используйте группу врага - это один NPC_ID!

## NPC:
```Python
class:
                self.name = arr[0]
                self.HP = int(arr[1])
                self.armor = int(arr[2])
                self.damage = int(arr[3])
                self.strong = int(arr[4])
                self.critical_dmg = int(arr[5])     # % - максимум 45%
	            
                self.drop_trophy = arr[6]           # Это отдельный tool_id предмета.
                self.installed_contender = arr[7]
```

Пример противника: NPC_ID:
```Python
bot_HP=100_armor=200_damage=100_strong=3_critical-dmg=45_drop-trophy:gun_damage=100
```

``critical_dmg`` - тоже самое что в Profile игрока, только относительно врага.

``drop_trophy`` - если с врага палают патроны, то там можно указать так трофей:
```Python
patron_recharge:patron_recharge:<tool_id>
```

Потом просто удалить из инаенторя скопировав и написав в tool_id своё оружие и снова добавить.
Делать это нужно через меню разработчика.

#### Важно !!!
Ниже часть кода передачи трофея игроку:
```Python
drop = calculate_drop_trophy(npc)
if drop != 0:
         prof.add_tools_id(drop, 50)
```
При добавлении трофея в инвентарь, его цена(price) составит 50 ETO.



## tool_id:
На основе этоц строки характеристик были реализованы другие ID.
Шаблон оружия:
```Python
nane_damage=500_charge=100
```
По сути, не обязательно чтобы были именно эти характеристики или вообще какие-то.
Суть инструмента влиять на характеристики.


## Оружие. tool_id:
Пример зарядов для оружия, относиться к механики зарядов у инструментов. tool_id:

Боеприпас конкретного инструмента:
```Python
patron_recharge:gun_damage=500_charge=0
```

#### Важно:
имя инструмента должно быть уникальным, 2го такого быть не должно. Это связано с тем, что
при поиске зарядов для конкретного инструмента, поиск ведется исключительно по его имени!

Пример оружие:
```Python
gun_damage=500_charge=0
```

Пример аптечки:
```Python
medkit-militech_HP=100
```
В таком tool_id обязательно должно быть слово medkit, в качестве части имени!!!
Иначе игра будет работать не корректно.


## Инвентарь и экипировка:

Из инвентаря можно экипировать предмет в слот. Кол-во досьупных слотов 5.

#### Важно!!!
Экипировывать следует лишь оружие, броню. Заряды, компьютеры и карты доступа должны быть в
инвентаре! Иначе возникнет не предвиденная ошибка!

Также если броня была израсходована, то она будет удалена при снятии!
Если броня поменяла значение, то инструмент также будет изменен!

## Как играть за других персонаже?
Играбельный персонаж это набор характеристик. Можно считать, что по сюжету это конструкт личности.
Конструкт личности можно просто надеть, ведь это инструмент - tool_id. Который имеет все
базовые характеристики профиля игрока.

## Profile:

Профиль игрока:
```Python
class:
    self.HP = arr[0]                    # 100 по умолчанию
    self.armor = arr[1]                 # 0 по умолчанию
    self.strong = arr[2]                # 1 из 15 по умолчанию
    self.intellect = arr[3]             # 1 из 15 по умолчанию
    self.damage = arr[4]                # 30 по умолчанию
    self.critical_dmg = arr[5]          # 3% шанс по умолчанию, максимум 45%
                
    self.quest_reward_setting = arr[6]  # {"+" : 1, "++" : 2, "+++" : 3, "++++" : 4} по умолчанию
                
    self.ETO = arr[7]                   # 0 по умолчанию
    self.tools_id = arr[8]              # {} == Инструменты по умолчанию - {tool_id : price, ...}
    self.pers_id = arr[9]               # [] Персонажи по умолчанию
                
    self.slots_occupied = arr[10]       # 0 занятые слоты по умолчанию
    self.slots = arr[11]                # всего 5 слотов по умолчанию. вероятно будет возможность расширять, но вряд ли
    self.keep_tool = arr[12]            # {} экипированное снаряжение по умолчанию
                
    self.history = arr[13]          
    
```

ETO - это локальная, игровая валюта. eToken.

tools_id - инвентарь, содержит tool_id : price - цену за которую можно продать.
pers_id - не используется.
slots_occupied - число занятых слотов экипировки.
slots - максимальное кол-во слотов.
keep_tool - тут все экипированные tool_id : price.
history - история получения ETO.

HP - падает когда игрок провалил задание или проигнорировал. Падает ровно столько, сколько урона у врага.
Если ``HP == 0``, то игрок теряет все ETO и рандомный инструмент в инвентаре. Можно попробовать экипировать предмет, чтобы не потерять.

урон наноситься врагу за выполнение задания.
``critical_dmg`` - критический урон, если экипировать оружие которое имеет более высокую вероятность нанесения урона
то можно нанести врагу до 250% от текущего урона!

Враг также может нанести крит урон.
Крит урон не может привышать 45%. Крит урон зависит от силы(``strong``) персонажа!

``intellect`` - изначально должен был влиять на получаемый опыт, но система уровней в игру так и не была добавлена. Возможно применять для
сюжетов, где на задании будет ограничение по интеллекту или на работу с SE - Smart Electronic, типа, работа с компьютером требует интеллект.


## Store:

Стоит помнить, если у продавца нет денег, то продать ему товар вряд ли выйдет.

Товар добавляется через меню разработчика, но может быть ситуация что нет понимаеия какой товар добавить.
На этот случай, есть решение - просто добавить товар, на который копить нужно какое-то время.


## Task - задания:

#### Ежедневные задания(daily task)
>  - указывается дата начала и через сколько дней должен быть повтор.
Болжны быть выполнены в теаении 24 часов после даты начал, иначе враг нагесет урон, если он есть.
За завершение задания будет выдана награда и нанесен урон врагу, если тот есть.

#### Одиночные задания(single task)
>  - указывается до кокого числа требуется выполнить.
Если забание не выполнено до наступления указанной даты, то враг наносит урон, если он есть.
За завершение задания будет выдана награда и нанесен урон врагу, если тот есть.

#### Задания привычки(habit task)
>  - указывается лишь дата начала и через сколько дней повторять.
Враг наносит урон лишь если выбрать «-», если выбрать «+», то урон наносит игрок, срока выполнения нет!


## Hot scripts:

#### Создание ID:
В help вы можите посмотреть пункт для создания нужного вам ID, что делать вручную крайне не удобно.

#### Создавай задания быстрее:
Наберите в терминале номер и готово!

##### Для одиночных заданий:
- 214 - создать одиночное задание 4го уровня сложности.
- 22 - завершить одиночное задание.
- 23 - зафисировать провал одиночного задания.
- 24 - удалить одиночное задание.

##### Для ежедневных заданий:
- 114 - создать ежедневное задание 4го уровня сложности.
- 12 - завершить ежедневное задание.
- 13 - завершить провал ежедневного задания.
- 14 - удалить ежедневное задание.

##### Для заданий привычек:
- 314 - создать задание привычки 4го уровня сложности.
- 32 - поощрить задание привычки.
- 33 - зафексировать отрицательное подкрепление в привычки.
- 34 - удалить задание привычки.

#### Важно !!!
- Также не стоит указывать никаких пробелов и прч, только числовые значения!
- Если вам необходимо указать ID задания, то добавьте его в самый конец номера. для этого нет ограничений по длине.


## Рейтинговая система:
exp - это points и наоборот.<br/>
``Новичок`` - от 0 до 1000(не награждается):<br/>
[ <space><space><space>+ ]: 1 eto и 1 exp<br/>
[ &nbsp; &nbsp; ++ ]: 2 eto и 2 exp<br/>
[ &nbsp; +++ ]: 3 eto и 3 exp<br/>
[ ++++ ]: 4 eto и 4 exp<br/>

``Ветеран`` - от 1001 до 2000(награда за достижение этого ранга 100 eto):<br/>
[    + ]: 4 eto и 2 exp<br/>
[   ++ ]: 8 eto и 3 exp<br/>
[  +++ ]: 15 eto и 5 exp<br/>
[ ++++ ]: 20 eto и 6 exp<br/>

``Элита`` - от 2001 до 3000(награда за достижение этого ранга 200 eto):<br/>
[    + ]: 15 eto и 3 exp<br/>
[   ++ ]: 20 eto и 4 exp<br/>
[  +++ ]: 25 eto и 6 exp<br/>
[ ++++ ]: 30 eto и 7 exp<br/>

``Профессионал`` - от 3001 до 4500(награда за достижение этого ранга 300 eto):<br/>
[    + ]: 30 eto и 4 exp<br/>
[   ++ ]: 35 eto и 5 exp<br/>
[  +++ ]: 40 eto и 7 exp<br/>
[ ++++ ]: 45 eto и 8 exp<br/>

``Мастер`` - от 4501 до 6500(награда за достижение этого ранга 450 eto):<br/>
[    + ]: 45 eto и 5 exp<br/>
[   ++ ]: 50 eto и 6 exp<br/>
[  +++ ]: 55 eto и 8 exp<br/>
[ ++++ ]: 60 eto и 9 exp<br/>

``Грант-Мастер`` - от 6501 до 8000(награда за достижение этого ранга 700 eto):<br/>
[    + ]: 60 eto и 5 exp<br/>
[   ++ ]: 65 eto и 6 exp<br/>
[  +++ ]: 70 eto и 8 exp<br/>
[ ++++ ]: 75 eto и 9 exp<br/>

``Легенда`` - от 8001 и далее(награда за достижение этого ранга 1000 eto):<br/>
[    + ]: 100 eto и 5 exp<br/>
[   ++ ]: 150 eto и 6 exp<br/>
[  +++ ]: 200 eto и 8 exp<br/>
[ ++++ ]: 250 eto и 9 exp<br/>

Каждый ранг имеет следующие локальных 5 уровня:
["I", "II", "III", "IV", "V"]<br/>
- За каждый локальный уровень не полагается награда, это просто дополнительные трудноости
перед переходом на новый ранг.

