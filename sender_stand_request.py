# Импорт настроек из модуля configuration, который содержит параметры конфигурации, такие как URL сервиса
import configuration

# Импорт библиотеки requests для выполнения HTTP-запросов
import requests

# Импорт данных запроса из модуля data, в котором определены заголовки и тело запроса
import data

# Определяем функцию get_logs, которая отправляет GET-запрос к серверу для получения логов
def get_logs():
    # Складываем базовый URL из конфигурационного файла и путь к основным логам,
    # чтобы сформировать полный URL для запроса.
    # Возвращает объект ответа, полученный от сервера после выполнения GET-запроса
    return requests.get(configuration.URL_SERVICE + configuration.LOG_MAIN_PATH,
                        params={"count": 20})

# Вызываем функцию get_logs и сохраняем ответ сервера в переменную response
response = get_logs()

# Выводим в консоль HTTP-статус код ответа сервера. Коды состояния HTTP сообщают
# о результате выполнения запроса. Например, код 200 означает "OK", а 404 - "Не найдено".
print(response.status_code)

# Выводим в консоль заголовки HTTP-ответа сервера.
# Заголовки могут содержать полезную информацию, например, тип содержимого ответа
# и используемые сервером технологии.
print(response.headers)

# Функция для получения данных из таблицы пользователей
def get_users_table():
    # Составление полного URL пути к данным таблицы пользователей
    # путем конкатенации базового URL сервиса и конечной точки таблицы пользователей
    # Возвращает объект ответа от сервера
    return requests.get(configuration.URL_SERVICE + configuration.USERS_TABLE_PATH)

# Выполнение функции и сохранение ответа в переменную response
response = get_users_table()

# Вывод статус-кода ответа сервера в консоль
# Статус-коды HTTP сообщают о результате выполнения запроса
print(response.status_code)

# Определение функции post_new_user для отправки POST-запроса на создание нового пользователя
def post_new_user(body):
    # Выполнение POST-запроса с использованием URL из конфигурационного файла, тела запроса и заголовков
    # URL_SERVICE и CREATE_USER_PATH объединяются для формирования полного URL для запроса
    # json=body используется для отправки данных пользователя в формате JSON
    # headers=data.headers устанавливает заголовки запроса из модуля data
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH ,
                         json=body,
                         headers=data.headers)

# Вызов функции post_new_user с телом запроса для создания нового пользователя из модуля data
response = post_new_user(data.user_body);

# Вывод HTTP-статус кода ответа на запрос
# Код состояния указывает на результат обработки запроса сервером
print(response.status_code)
print(response.json())