import dataclasses
import psycopg2
from datetime import datetime
import uuid
import requests
import xml.etree.ElementTree as ET


def currency_rate(date):
    response = requests.get(f'https://www.cbr.ru/scripts/XML_daily.asp?date_req={date}')
    
    tree = ET.fromstring(response.text)
    lst = list(tree.iter())
    for i in range(0, len(lst)):
        if lst[i].text == "Доллар США":
            val = lst[i+1].text
            val_changed = val.replace(',', '.')
            return float(val_changed)

class PostgresSaver:

    def __init__(self, pg_conn):
        self.curpg = pg_conn.cursor()
        self.pg_conn = pg_conn

    def save_all_data(self, data):
        psycopg2.extras.register_uuid()

        """Загрузка данных из Google sheets"""
        for item in data:
            self.curpg.execute(
                "INSERT INTO content.sheets_content (id, num, order_number,\
                        price_usd, price_rub, delivery_date)\
                            VALUES (%s, %s, %s, %s, %s, %s) ON\
                                CONFLICT (id) DO NOTHING;",
                dataclasses.astuple(item)
            )
            self.pg_conn.commit()
        self.curpg.close()

    def get_data(self, sql):
        psycopg2.extras.register_uuid()

        """Загрузка данных из Google sheets"""
        self.curpg.execute(
            sql
        )
        result = self.curpg.fetchall()
        return result
    
    def update_order(self, new_data):
        psycopg2.extras.register_uuid()
        for item in new_data:
            item = item.split("_")
            num = item[0]
            order_number = item[1]
            price_usd = item[2]
            delivery_date = item[3]
            date = datetime.strptime(delivery_date, '%Y-%m-%d').strftime('%d/%m/%Y')
            self.curpg.execute(f"SELECT * FROM content.sheets_content WHERE num = {num};")
            result = len(self.curpg.fetchall())
            if result > 0:
                self.curpg.execute(
                    "UPDATE content.sheets_content SET order_number = %s, price_usd = %s, delivery_date = %s\
                     WHERE num = %s;", (order_number,price_usd, delivery_date, num))
                self.pg_conn.commit()
            else:
                self.curpg.execute("INSERT INTO content.sheets_content (id, num, order_number,\
                                    price_usd, price_rub, delivery_date)\
                                    VALUES (%s, %s, %s, %s, %s, %s);",
                                    (uuid.uuid1(), num, order_number, price_usd, float(price_usd)*currency_rate(date), delivery_date)
                )
                self.pg_conn.commit()
        self.curpg.close()


    def delete(self, new_data):
        psycopg2.extras.register_uuid()
        for item in new_data:
            item = item.split("_")
            num = item[0]
            self.curpg.execute(f"DELETE FROM content.sheets_content WHERE num = {num};")
            self.pg_conn.commit()
        self.curpg.close()