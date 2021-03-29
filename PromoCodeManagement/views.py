from django.shortcuts import render, redirect

from .models import PromoCode, Discount


def index(request):
    context = {
        'codes': PromoCode.objects
    }

    return render(request, 'PromoCodeManagement/index.html', context)


def edit_code(request, oid):
    code, description, valid_start, valid_end, discount_type, discount_amount = Utils.get_code_info(request)

    PromoCode.objects.filter(id=oid).update(code=code,
                                            description=description,
                                            validStart=valid_start,
                                            validEnd=valid_end,
                                            discount=Discount(type=discount_type, amount=discount_amount),
                                            _partitionKey='ding')

    return redirect('/promo')


def delete_code(request, oids):
    oids_list = oids.split(',')
    for oid in oids_list:
        PromoCode.objects.filter(id=oid).delete()

    return redirect('/promo')


def delete_null_code(request):
    return redirect('/promo')


def add_code(request):
    code, description, valid_start, valid_end, discount_type, discount_amount = Utils.get_code_info(request)

    new_code = PromoCode(code=code,
                         description=description,
                         validStart=valid_start,
                         validEnd=valid_end,
                         discount=Discount(type=discount_type, amount=discount_amount),
                         _partitionKey='ding')
    new_code.save()

    return redirect('/promo')


class Utils:
    @staticmethod
    def get_code_info(request):
        if request.method == 'POST':
            code = request.POST.get('code', None)
            description = request.POST.get('description', None)
            valid_start = request.POST.get('validStart', None)
            valid_end = request.POST.get('validEnd', None)
            discount_type = request.POST.get('type', None)
            discount_amount = request.POST.get('amount', None)

            return code, description, valid_start, valid_end, discount_type, discount_amount
        else:
            return None
