import requests
import time

API_URL: str = "https://api.telegram.org/bot"
BOT_TOKEN: str = 
API_ANIMAL: str = "https://random.dog/woof.json"
TEXT: str = "I am Happy"
MAX_COUNTER: int = 100
ERROR_TEXT: str = "Картинки закончились"


offset: int = -2
counter: int = 0
chat_id: int

while True:
    print("attempt = ", counter)
    updates = requests.get(
        f'{API_URL}{BOT_TOKEN}/GetUpdates?offset={offset + 1}').json()
    if updates['result']:
        for result in updates['result']:
            offset = result['update_id']
            chat_id = result['message']['from']['id']
            animal_file = requests.get(f'{API_ANIMAL}')
            print(animal_file)
            if animal_file.status_code == 200:
                file_link = animal_file.json()['url']
                # requests.get(f'{API_URL}{BOT_TOKEN}/SendMessage?chat_id={chat_id}&text={TEXT}') # отправка текстового сообщения
                requests.get(
                    f'{API_URL}{BOT_TOKEN}/sendPhoto?chat_id={chat_id}&photo={file_link}')
            else:
                requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={ERROR_TEXT}')


    time.sleep(1)
    counter += 1
