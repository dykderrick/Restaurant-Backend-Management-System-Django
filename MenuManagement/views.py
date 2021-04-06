import os

from django.shortcuts import render, redirect

from .models import Dish


def _get_dish_info(request):
    if request.method == 'POST':
        name = request.POST.get('name', None)
        description = request.POST.get('description', None)
        category = request.POST.get('category', None)
        price = request.POST.get('price', None)
        ETP = request.POST.get('ETP', None)
        image = request.FILES.get('image', None)

        return name, description, category, price, ETP, image
    else:
        return None


def index(request):
    context = {
        'dishes': Dish.objects
    }
    return render(request, 'MenuManagement/index.html', context)


def add_dish(request):
    name, description, category, price, ETP, image = _get_dish_info(request)

    new_dish = Dish(name=name, description=description, category=category, price=price, ETP=ETP, _partitionKey="ding")
    new_dish.save()

    the_dish_id = Dish.objects.filter(name=name)[0].id
    with open("static/images/dishes/" + str(the_dish_id) + "." + image.content_type[6:], mode="wb") as image_file:
        for content in image:
            image_file.write(content)

    return redirect('/menu')


def edit_dish(request, oid):
    name, description, category, price, ETP, image = _get_dish_info(request)

    Dish.objects.filter(id=oid).update(name=name,
                                       description=description,
                                       category=category,
                                       price=price,
                                       ETP=ETP,
                                       _partitionKey="ding")

    return redirect('/menu')


def delete_dish(request, oids):
    oids_list = oids.split(',')
    for oid in oids_list:
        Dish.objects.filter(id=oid).delete()

        dish_dir = 'static/images/dishes/'
        for file_name in os.listdir(dish_dir):
            if file_name.startswith(oid):
                os.remove(os.path.join(dish_dir, file_name))

    return redirect('/menu')


def delete_null_dish(request):
    return redirect('/menu')
