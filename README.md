# Foodgram


### Описание.

Социальная сеть любителей готовить - делитесь своими рецептами, узнавайте новые и готовьте!

### Как запустить проект.

Клонировать репозиторий, 


Установите Docker. Перейдите в папку infra и соберите образ:

```
docker-compose build
```
```
docker-compose up -d
```
Выполните миграции
```
docker-compose exec web python manage.py migrate 
```

Создайте суперюзера:

```
docker-compose exec web python manage.py createsuperuser
```

Соберите статику

```
docker-compose exec web python manage.py collectstatic --no-input
```

После этого проект будет доступен по ссылке:

```
http://localhost/
```


### Примеры запросов
