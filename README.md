# Foodgram
84.201.161.52


### Описание.

Социальная сеть любителей готовить - делитесь своими рецептами, узнавайте новые и готовьте!

### Как запустить проект.

Клонируйте репозиторий, выполните команды:

```
docker-compose build
```
```
docker-compose up -d
```
Выполните миграции:
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
загрузите данные в БД из файла postgres.dump, предварительно сохранив его в контейнере:
```
docker-compose exec db -u postgres psql -d postgres -f postgres.dump 
```

После этого проект будет доступен по ссылке:

```
http://localhost/
```

### Примеры запросов
Можно посмотреть по адресу:

```
http://localhost/api/docs/
```