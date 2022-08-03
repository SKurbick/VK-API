import time
import requests
# импортируем pprint для более комфортного вывода информации
from pprint import pprint

# простой get запрос профилей vk-api ###################################################################################

with open('token.txt', 'r') as file_object: #читаем токен с отдельного текстового файла
    token = file_object.read().strip()

URL = 'https://api.vk.com/method/users.get'
params = {
    'user_ids': '1,2', #в значении указано два айди, 1- Дуров, 2-какая-то баба
    'access_token': token, # токен и версия api являются обязательными параметрами во всех запросах к vk
    'v': '5.131', #версия
    'fields': 'education, sex' # указали что бы на выводе показало образование и пол
}
res = requests.get(URL, params=params)
pprint(res.json()) # вывод в формате json