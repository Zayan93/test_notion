from django.shortcuts import render
from .models import Sheets_content
from django_tables2 import SingleTableView
from .models import Sheets_content
from .tables import PersonTable

class PersonListView(SingleTableView):
    model = Sheets_content
    table_class = PersonTable
    template_name = 'index.html'