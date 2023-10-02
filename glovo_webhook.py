from flask import Flask, request
import json
import hashlib  # Импортируйте модуль hashlib

app = Flask(__name__)

# Здесь вы можете установить секретный ключ вашего приложения
client_secret = '5a7614893783e6a1ada3ce226af2cc9a'

@app.route('/webhook', methods=['POST'])
def webhook():
    # Получаем данные из POST-запроса
    post_data = request.get_json()
    print(post_data)
    # Проверяем валидность данных
    verify_original = post_data.get('verify', '')
    del post_data['verify']

    verify = [
        post_data['account'],
        post_data['object'],
        str(post_data['object_id']),
        post_data['action']
    ]

    # Если есть дополнительные параметры
    if 'data' in post_data:
        verify.append(post_data['data'])

    verify.append(str(post_data['time']))
    verify.append(client_secret)

    # Создаём строку для верификации запроса клиентом
    verify = hashlib.md5(';'.join(verify).encode()).hexdigest()

    # Проверяем валидность данных
    if verify != verify_original:
        return '', 403

    # Проверяем, является ли событие онлайн-заказом
    if post_data['object'] == 'incoming_order' and post_data['action'] == 'added':
        # Получаем информацию о заказе
        order_info = post_data.get('data', {})

        # Выводим информацию о заказе в консоль
        print(f'Получен онлайн заказ: {json.dumps(order_info, indent=2)}')

    # Отвечаем на запрос 200 статусом
    return '', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
