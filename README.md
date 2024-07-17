# protocol_wd_3_game

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
```

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

## NPC:
```Python
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

Пример зарядов для оружия, относиться к механики зарядов у инструментов. tool_id:
```Python
patron_recharge:gun_damage=500_charge=0
```
