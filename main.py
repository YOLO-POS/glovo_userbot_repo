from pyrogram import Client
import requests

api_id = 8927112
api_hash = 'a216a15ebbf50bbbc5d96be7c7e93fbb'

chat_id_01 = -1001581146060
chat_id_03 = -1001957717504

client=Client(name='me_client', api_id=api_id, api_hash=api_hash)

client.start()
flask_server_url = 'http://192.168.1.34:5000/webhook'
response = requests.post(flask_server_url)
if response.status_code == 200:
    # Отправляем сообщение в Telegram
    if <условие из вебхука, для какого заведения>:
        client.send_message(chat_id_01, "Нове замовлення Glovo!")
    if <условие из вебхука, для какого заведения>:
        client.send_message(chat_id_03, "Нове замовлення Glovo!")
else:
    print("Помилка при вiдправцi POST-запиту на сервер Flask")
client.stop()

