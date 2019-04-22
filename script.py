import vk_api

import datetime # работа с датой и временем

import time

while True:
    vk = vk_api.VkApi(token="text")
    delta = datetime.timedelta(hours=3, minutes=0) # разница от UTC. Можете вписать любое значение вместо 3
    t = (datetime.datetime.now(datetime.timezone.utc) + delta) # Присваиваем дату и время переменной «t»
    nowtime = t.strftime("%H:%M") # текущее время
    nowdate = t.strftime("%d.%m.%Y") # текущая дата
    on = vk.method("friends.getOnline") # получаем список id друзей онлайн
    counted = len(on) # считаем кол-во элементов в списке
    vk.method("status.set", {"Просто текст": nowtime + " ● " + nowdate + " ● " + "Друзей онлайн: " + str(counted)})
    time.sleep(30) # погружаем скрипт в «сон» на 30 секунд
    
