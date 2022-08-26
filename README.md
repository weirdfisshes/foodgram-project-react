![example workflow](https://github.com/weirdfisshes/foodgram-project-react/actions/workflows/main.yml/badge.svg)
# Foodgram

Ссылка на проект: http://84.201.161.52/

# тестовые пользователи:

Суперюзер:
```
email: admin@ya.ru
password: admin
```
Обычные пользователи:
```
email: nikita@ya.ru
password: 1234@qwe

email: kritik@ya.ru
password: 1234@qwe
```
### Описание.

Социальная сеть любителей готовить - делитесь своими рецептами, узнавайте новые и готовьте!
Технологии: Python 3, Django 2.2.19, PostgreSQL, DRF, Git.
CI и CD. При пуше в ветку main:
- обновляется образ на Docker Hub,
- осуществляется деплой на боевой сервер.


### Как запустить проект локально.

Клонировать репозиторий, в папке infra создать файл .env, заполнить его по образцу:

```
DB_ENGINE=django.db.backends.postgresql
DB_NAME=имя_базы_данных
POSTGRES_USER=логин_для_подключения_к_базе_данных
POSTGRES_PASSWORD=пароль_для_подключения_к_БД
DB_HOST=название_контейнера
DB_PORT=порт_для_подключения_к_БД
SECRET_KEY=django_secret_key
DEBUG=True или False
```

Установите Docker. Перейдите в папку infra и соберите образ:

```
docker-compose up -d --build
```
Выполните миграции
```
docker-compose exec web python manage.py migrate 
```

Создайте суперюзера:

```
docker-compose exec web python manage.py createsuperuser
```

Соберите статику:

```
docker-compose exec web python manage.py collectstatic --no-input
```

После этого проект будет доступен по ссылке:

```
http://localhost/
```

Для деплоя на сервер нужно добавить action secrets в GitHub.
```
DB_ENGINE # django.db.backends.postgresql
DB_NAME # имя_базы_данных
POSTGRES_USER # логин_для_подключения_к_базе_данных
POSTGRES_PASSWORD # пароль_для_подключения_к_БД
DB_HOST # название_контейнера
DB_PORT # порт_для_подключения_к_БД
DOCKER_PASSWORD # пароль от Docker Hub
DOCKER_USERNAME # логин от Docker Hub
HOST # публичный ip сервера
USER # пользователь сервера
PASSPHRASE # пароль от ssh-ключа (при наличии)
SSH_KEY # приватный ssh-ключ (включая begin и end)
```

### Документация к API

Доступна по адресу http://84.201.161.52/api/docs/. Здесь можно увидеть все возможные запросы к api и ответы.

### Эндпоинты:

api/tags/ - теги
api/ingredients/ - ингредиенты
api/recipes/ - рецепты
api/users/ - пользователи
api/auth/token/ - аутентификация

### Автор:
Никита Бурцев
