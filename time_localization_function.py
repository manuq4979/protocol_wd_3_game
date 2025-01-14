from datetime import datetime, timedelta

MOSCOW = 3 # +3 и дата и время будут по Москве!
time_zone = MOSCOW
current_time = datetime.now() + timedelta(hours=time_zone)
    

