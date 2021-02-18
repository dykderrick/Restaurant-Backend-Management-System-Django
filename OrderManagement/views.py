from django.shortcuts import render

from .models import Order
from MenuManagement.models import Dish


def index(request):
    context = {
        'orders': Order.objects,
        'all_dishes': Dish.objects
    }

    return render(request, 'OrderManagement/index.html', context)
