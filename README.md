# Групповой проект YaMDb
*Проект YaMDb собирает отзывы пользователей на произведения. Сами произведения в YaMDb не хранятся, здесь нельзя посмотреть фильм или послушать музыку.*

## Описание
#### API дает пользоваться функционалом приложения не посещая сайт.
##### Реализован функционал дающий возможность:
* Просматривать, создавать новые, удалять и изменять произведения и отзывы.
* Просматривать, создавать и удалять категории и жанры.
* Комментировать, смотреть, удалять и обновлять комментарии.

#### Технологии

- Python
- Django 
- Django Rest Framework
- Djoser 
- Simple JWT
- SQLite3
- Django-import-export
- Python-dotenv

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:dariazueva/api_yamdb.git
```

```
cd api_yamdb
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

* Если у вас Linux/macOS

    ```
    source env/bin/activate
    ```

* Если у вас windows

    ```
    source env/Scripts/activate
    ```

```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```
