from bson import ObjectId
from django.shortcuts import render, redirect

from MenuManagement.models import Dish
from OrderManagement.models import Order


def index(request):
    context = {
        'orders': Order.objects,
        'all_dishes': Dish.objects
    }

    return render(request, 'KitchenTicket/index.html', context)


def edit_status(request, order_id, dish_id, new_status):
    # Querying list:
    # https://docs.mongoengine.org/guide/querying.html#querying-lists
    Order.objects.filter(id=order_id, dishes__dishID=ObjectId(dish_id)).update(set__dishes__S__status=new_status)

    return redirect('/kitchen')
