import django_tables2 as tables
from .models import Sheets_content

class PersonTable(tables.Table):
    class Meta:
        model = Sheets_content
        template_name = "django_tables2/bootstrap.html"
        fields = ("num", "order_number", "price_usd", "price_rub", "delivery_date")