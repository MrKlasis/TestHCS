Название проекта - TestHCS (тестовое задание)
Описание проекта:

Модели данных
Дом:
    Адрес
    Список квартир

Квартира:
    Площадь
    Список счётчиков

Счётчик воды:
    Показания за несколько прошедших месяцев

Тариф:
Цена услуги или ресурса

API
Дом:
    Ввод и вывод данных по дому

Расчёт квартплаты:
    Расчёт квартплаты для всех квартир в доме за какой-либо месяц
    
Прогресс расчёта:
    Запуск процесса расчёта квартплаты в фоновом режиме
    Получение прогресса расчёта

Использованный стек:
Django, Celery, PostgreSQL, Docker

Установка и запуск
Клонировать репозиторий:
git clone https://github.com/username/repo.git
Перейти в директорию проекта:
cd repo

Установить зависимости:
pip install -r requirements.txt

Запустить сервер:

python manage.py runserver

Запустить Celery:
celery -A TestHCS worker --loglevel=info

API
Дома:

GET /api/houses/ - получить список всех домов

POST /api/houses/ - создать новый дом

GET /api/houses/{id}/ - получить дом по id

PUT /api/houses/{id}/ - обновить дом по id

DELETE /api/houses/{id}/ - удалить дом по id

Квартиры:

GET /api/apartments/ - получить список всех квартир

POST /api/apartments/ - создать новую квартиру

GET /api/apartments/{id}/ - получить квартиру по id

PUT /api/apartments/{id}/ - обновить квартиру по id

DELETE /api/apartments/{id}/ - удалить квартиру по id

Расчёт квартплаты:

POST /api/start-calculation/ - запустить расчёт квартплаты

GET /api/get-task-status/{task_id}/ - получить прогресс расчёта по id
