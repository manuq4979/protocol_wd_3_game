# Пример строки:
# "name_NI=1_RM=0_OS=1_PoF=0_AI=0_CP=0_UI=1_CP2=0_W=0_R=0+S;gun_damage=100_charge=100;gun_recharge=100+AAD;bot_HP=100_armor=200_damage=100_strong=3_critical-dmg=45_drop-trophy:smart-card=write=True"
def decoding_of_characteristics(char_line):
        chars = char_line.split("+")
        
        base_char = chars[0]
        storage =  chars[1]
        access_algorithm_dict = chars[2]
        
        base_char = base_char.split("_")
        name = base_char[0]
        base_char.remove(name)
        base_char_res = []
        base_char_res.append(name)
        for char in base_char:
            char = char.split("=")
            base_char_res.append(char)
        
        storage = storage.split(";")
        
        access_algorithm_dict = access_algorithm_dict.split(";")
        
        return [base_char_res, storage, access_algorithm_dict]
        
        
res = decoding_of_characteristics("name_NI=1_RM=0_OS=1_PoF=0_AI=0_CP=0_UI=1_CP2=0_W=0_R=0+S;gun_damage=100_charge=100;gun_recharge=100+AAD;bot_HP=100_armor=200_damage=100_strong=3_critical-dmg=45_drop-trophy:smart-card=write=True")
print(res)
