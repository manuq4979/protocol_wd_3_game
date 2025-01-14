from datetime import datetime, timedelta
import os.path

time_zone_file_path = "DataApp/time_zone.txt"
# Доступные часовые пояса:
MOSCOW = 3 # +3 и дата и время будут по Москве!

def set_time_zone(new_time_zone: int):
    file = open(time_zone_file_path, "w+", encoding='utf-8')
    file.write(new_time_zone)
    file.close()

time_zone = 0
if os.path.exists(file_path):
    file = open(time_zone_file_path, "r", encoding='utf-8')
    time_zone = file.read()
    file.close()
else:
    set_time_zone(new_time_zone=MOSCOW)


current_time = datetime.now() + timedelta(hours=time_zone)

    


