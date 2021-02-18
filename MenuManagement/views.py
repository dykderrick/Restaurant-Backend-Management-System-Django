from django.shortcuts import render, redirect

from .models import Dish


def index(request):
    context = {
        'dishes': Dish.objects
    }
    return render(request, 'MenuManagement/index.html', context)


def add_dish(request):
    name, description, category, price, ETP = Utils.get_dish_info(request)

    new_dish = Dish(name=name, description=description, category=category, price=price, ETP=ETP)
    new_dish.save()

    return redirect('/menu')


def edit_dish(request, oid):
    name, description, category, price, ETP = Utils.get_dish_info(request)

    Dish.objects.filter(id=oid).update(name=name, description=description, category=category, price=price, ETP=ETP)

    return redirect('/menu')


def delete_dish(request, oids):
    oids_list = oids.split(',')
    for oid in oids_list:
        Dish.objects.filter(id=oid).delete()

    return redirect('/menu')


def delete_null_dish(request):
    return redirect('/menu')


class Utils:
    @staticmethod
    def get_dish_info(request):
        if request.method == 'POST':
            name = request.POST.get('name', None)
            description = request.POST.get('description', None)
            category = request.POST.get('category', None)
            price = request.POST.get('price', None)
            ETP = request.POST.get('ETP', None)

            return name, description, category, price, ETP
        else:
            return None
