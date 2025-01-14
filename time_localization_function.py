from datetime import datetime, timedelta

# Доступные часовые пояса:
MOSCOW = 3 # +3 и дата и время будут по Москве!


file = open("DataApp/time_zone.txt", "r", encoding='utf-8')
time_zone = file.read()
file.close()

current_time = datetime.now() + timedelta(hours=time_zone)

def set_time_zone(new_time_zone: int):
    file = open("DataApp/time_zone.txt", "w+", encoding='utf-8')
    file.write(new_time_zone)
    file.close()

