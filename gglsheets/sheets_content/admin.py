from django.contrib import admin
from .models import Sheets_content


@admin.register(Sheets_content)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('num', 'order_number', 'price_usd', 'price_rub', 'delivery_date')
    list_filter = ('delivery_date',)
    search_fields = ('order_number', 'num')
    pass


# Register your models here.
