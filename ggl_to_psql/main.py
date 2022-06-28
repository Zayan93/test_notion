import gspread
import os
from dataclass import ContentSheets
import dataclasses
import psycopg2
from psycopg2.extras import DictCursor
from psycopg2.extensions import connection as _connection
from dotenv import load_dotenv
from datetime import datetime
from time import sleep
from model import currency_rate, PostgresSaver
from update import get_data


load_dotenv()


def load_from_ggl(data):
    sa = gspread.service_account(filename='service_account.json')
    sh = sa.open('SheetsTest')
    wks = sh.worksheet('PriceData')
    data = wks.get_all_records()
    contents = []
    for item in data:
        date = datetime.strptime(item['срок поставки'], '%d.%m.%Y').strftime('%d/%m/%Y')
        content = ContentSheets(
            num=item['№'],
            order_number=item['заказ №'],
            price_usd=item['стоимость,$'],
            price_rub=item['стоимость,$']*currency_rate(date),
            delivery_date=datetime.strptime(item['срок поставки'], '%d.%m.%Y').strftime('%Y-%m-%d'),
        )
        contents.append(content)
    return contents


def load_data(pg_conn: _connection):
    postgres_saver = PostgresSaver(pg_conn)
    sa = gspread.service_account(filename='service_account.json')
    sh = sa.open('SheetsTest')
    wks = sh.worksheet('PriceData')
    wks_all = wks.get_all_records()
    data = load_from_ggl(wks_all)
    postgres_saver.save_all_data(data)


if __name__ == '__main__':
    dsl = {
        'dbname': os.environ.get('DB_NAME'),
        'user': os.environ.get('DB_USER'),
        'password': os.environ.get('DB_PASSWORD'),
        'host': os.environ.get('HOST'),
        'port': os.environ.get('PORT')
    }
    with psycopg2.connect(
        **dsl, cursor_factory=DictCursor
    ) as pg_conn:
        load_data(pg_conn)
        while True:
            get_data(pg_conn)
            sleep(60)
