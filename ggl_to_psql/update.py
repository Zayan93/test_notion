import gspread
from psycopg2.extensions import connection as _connection
from dotenv import load_dotenv
from datetime import datetime
from model import PostgresSaver


load_dotenv()

def calculator(lists):
    data = []
    for a in range(0, len(lists)):
        for i in lists[a].values():
            data.append(i)
    return data

def get_data(pg_conn: _connection):
    postgres_saver = PostgresSaver(pg_conn)
    orders = postgres_saver.get_data("SELECT CONCAT (num,'_',order_number,'_',price_usd,'_',delivery_date) as result_string FROM content.sheets_content;")
    a = sorted(calculator(orders))
    b = from_ggl()
    if (len(a) - len(b)) <= 0:
        updated_nums = list(set(b).difference(a))
        if len(updated_nums) > 0:
            postgres_saver.update_order(updated_nums)
            print('вроде обновил')
        else:
            print('Все обновлено')
    else:
        updated_nums = list(set(a).difference(b))
        postgres_saver.delete(updated_nums)
        print('Данные удалены')

def from_ggl():
    sa = gspread.service_account(filename='service_account.json')
    sh = sa.open('SheetsTest')
    wks = sh.worksheet('PriceData')
    data = wks.get_all_records()
    contents = []
    for item in data:
        date = datetime.strptime(item['срок поставки'], '%d.%m.%Y').strftime('%d/%m/%Y')
        content = "_".join((str(item['№']),str(item['заказ №']),str(item['стоимость,$']),str(datetime.strptime(item['срок поставки'], '%d.%m.%Y').strftime('%Y-%m-%d'))))
        contents.append(content)
    return sorted(contents)