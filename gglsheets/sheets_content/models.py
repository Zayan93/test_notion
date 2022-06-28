import uuid
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.translation import gettext_lazy as _


class UUIDMixin(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True


class Sheets_content(UUIDMixin):
    num = models.IntegerField(verbose_name='№')
    order_number = models.IntegerField(verbose_name='заказ №')
    price_usd = models.FloatField(verbose_name='стоимость,$')
    price_rub = models.FloatField(verbose_name='стоимость,Р')
    delivery_date = models.DateField(verbose_name='срок поставки')

    class Meta:
        db_table = "content\".\"sheets_content"
        verbose_name = 'Гугл таблица'
        verbose_name_plural = 'Гугл таблица'

    def __str__(self):
        return self.num, self.order_number, self.price_usd, self.price_rub, self.delivery_date