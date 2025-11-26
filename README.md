# TaskFlow - Система управления задачами

## Описание проекта
Веб-приложение для управления личными и командными задачами с канбан-доской.

## Функциональность
- Создание и управление задачами
- Отслеживание статусов (К выполнению, В работе, Завершено)
- Назначение задач участникам команды
- REST API для работы с задачами
- Отслеживание сроков выполнения

## Технологический стек
- Python 3.x
- Flask веб-фреймворк
- SQLAlchemy ORM
- Система контроля версий Git

## Структура проекта
```
project_Karandasheva/   
├── app/  
│ ├── init.py
│ ├── models.py  
│ └── routes.py   
├── config.py  
├── requirements.txt 
└── run.py 
```


## Быстрый старт

### Предварительные требования
- Python 3.8+
- Git

### Установка и запуск
```bash
# Клонировать репозиторий
git clone https://github.com/seruru/taskflow-system.git
cd project_Karandasheva

# Создать виртуальное окружение
python3 -m venv venv
source venv/bin/activate

# Установить зависимости
pip install -r requirements.txt

# Запустить сервер разработки
python run.py

# Проверить работу (в новом терминале)
python3 -c "import urllib.request; print(urllib.request.urlopen('http://127.0.0.1:5000/').read().decode())"
```
