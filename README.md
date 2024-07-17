# protocol_wd_3_game

SE - Smart Electronics:
Пример SE_ID:
```Python
name_NI=1_RA=0_OS=1_PoF=0_AI=0_CP=1_UI=1_CP2=1_W=0_R=0+S;gun_damage=100_charge=100;gun_recharge=100+AAD;bot_HP=100_armor=200_damage=100_strong=3_critical-dmg=45_drop-trophy:smart-card=write=True
```

А вот так буде выглядить карта доступа. tool_id:
```Python
name_access_card_read_write # Чтение Запись
name_access_card_read       # Только чтение
name_access_card_write      # Только запись
```

Пример компьютера, для доступа к полю Smart Electronics. tool_id:
```Python
netbook_smart_electronics=1
```

Пример противника: NPC_ID:
```Python
bot_HP=100_armor=200_damage=100_strong=3_critical-dmg=45_drop-trophy:gun_damage=100
```

Пример зарядов для оружия, относиться к механики зарядов у инструментов. tool_id:
```Python
patron_recharge:gun_damage=500_charge=0
```
