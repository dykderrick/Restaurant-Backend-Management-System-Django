from django.shortcuts import render

from MenuManagement.models import Dish
from OrderManagement.models import Order


def index(request):
    context = {
        'orders': Order.objects,
        'all_dishes': Dish.objects
    }

    return render(request, 'KitchenTicket/index.html', context)
