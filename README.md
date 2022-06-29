Гугл таблица находится по адресу: https://docs.google.com/spreadsheets/d/17X9axZIOkgpkthTBh6RiDkPhgTmdYuEdq9eiC3wnScs/edit#gid=0

<h1> Описание работы скрипта в рамках тестового задания Notion: </h1>

<h2> С использованием Docker container: </h2>

Находясь в корне файла необходимо прописать docker-compose up -d --build , что создаст и запустит контейнеризацию проекта.


<h2> Без использования Докер Контейнеризации: </h2>

1) Для начала нужно скопировать репозиторий git clone <ссылка на репозиторий>
2) Создаем виртуальное окружение проекта python -m venv venv
3) Далее активируем виртуальное окружение source venv/scripts/activate (для мак: . venv/bin/activate)
4) Устанавливаем необходимые библиотеки: pip install -r requirements.txt
5) Пятым шагом запускаем контейнер PosgreSQL

docker run -d \
  --name postgres \
  -p 5432:5432 \
  -v $HOME/postgresql/data:/var/lib/postgresql/data \
  -e POSTGRES_PASSWORD=123qwe \
  -e POSTGRES_USER=app \
  -e POSTGRES_DB=ggl_database  \
  postgres:13 

6) После установки Postresql необходимо подключиться к серверу Postgres: psql -h 127.0.0.1 -U app -d movies_database
7) Внутри сервера создаем схему и таблицу:

CREATE SCHEMA content;
CREATE TABLE IF NOT EXISTS content.sheets_content (
    id uuid PRIMARY KEY,
    num INT,
    order_number INT,
    price_usd FLOAT,
    price_rub FLOAT,
    delivery_date DATE
);

8) Можно переходить в директорию gglsheets и выполнить для начала миграции: python manage.py migrate --fake
9) запускаем сервер: python manage.py runserver
10) Открываем второй терминал и запускаем скрипт по обновлению базы: python main.py
