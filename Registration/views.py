from django.shortcuts import render, redirect

from TableManagement.models import Table


def index(request, table_number):
    table = Table.objects.filter(tableNo=table_number)
    if table[0].status == 'vacant':
        table.update(status='seated')

    return redirect('/table')  # TODO url needs to be updated
