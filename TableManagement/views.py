from django.http import HttpResponse
from django.shortcuts import render, redirect

from TableManagement.models import Table


def index(request):
    context = {
        'tables': Table.objects
    }

    return render(request, 'TableManagement/index.html', context)


def edit_table(request, oid, capacity, status):
    if request.method == 'POST':
        Table.objects.filter(id=oid).update(capacity=capacity, status=status)
    return redirect('/table')
