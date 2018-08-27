from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import requests
import json

# Create your views here.
from KIA_auth.models import Profile


def about(request):
    if not request.user.is_authenticated:
        context = {}
    else:
        context = {'role': Profile.objects.get(user=request.user).role}

    template = loader.get_template('KIA_general/about.html')
    return HttpResponse(template.render(context, request))


def contact_us(request):
    if not request.user.is_authenticated:
        context = {}
    else:
        context = {'role': Profile.objects.get(user=request.user).role}

    template = loader.get_template('KIA_general/contact_us.html')
    return HttpResponse(template.render(context, request))


def not_found(request):
    if not request.user.is_authenticated:
        context = {}
    else:
        context = {'role': Profile.objects.get(user=request.user).role}

    template = loader.get_template('KIA_general/404.html')
    return HttpResponse(template.render(context, request))


def not_authorized(request):
    if not request.user.is_authenticated:
        context = {}
    else:
        context = {'role': Profile.objects.get(user=request.user).role}

    template = loader.get_template('KIA_general/not_authorized.html')
    return HttpResponse(template.render(context, request))


def access_denied(request):
    if not request.user.is_authenticated:
        context = {}
    else:
        context = {'role': Profile.objects.get(user=request.user).role}

    template = loader.get_template('KIA_general/access_denied.html')
    return HttpResponse(template.render(context, request))


def user_restricted(request):
    if not request.user.is_authenticated:
        context = {}
    else:
        context = {'role': Profile.objects.get(user=request.user).role}

    template = loader.get_template('KIA_general/user_restricted.html')
    return HttpResponse(template.render(context, request))


def faq(request):
    if not request.user.is_authenticated:
        context = {}
    else:
        context = {'role': Profile.objects.get(user=request.user).role}

    template = loader.get_template('KIA_general/FAQ.html')
    return HttpResponse(template.render(context, request))


# def services(request):
#     ss = [
#         {'name': 'خفن',
#          'info': 'سرویس عادی'},
#         {'name': 'ایزی',
#          'info': 'سرویس نرمال'},
#         {'name': 'شاخ',
#          'info': 'سرویس عجیب'},
#         {'name': 'عالی',
#          'info': 'سرویس خوب'},
#         {'name': 'معمولی',
#          'info': 'سرویس بد'},
#         {'name': 'ساده',
#          'info': 'سرویس پیچیده'},
#         {'name': 'ایول',
#          'info': 'سرویس کارکرد'},
#     ]
#     return render(request, 'KIA_general/services.html', {'ss': ss})
#     # context = {}
#     # template = loader.get_template('KIA_general/services.html')
#     # return HttpResponse(template.render(context, request))


def currency_rates(request):
    response = requests.get('http://core.arzws.com/api/core?Token=a6d2b63a-5abf-42c0-bdb7-08d609cedc20&what=exchange')
    data = json.loads(response.text)
    all_currency_list = data['currencyBoard']
    our_currency_list = []

    if all_currency_list is None:
        all_currency_list = []
        our_currency_list = [{'name': 'دلار آمریکا', 'to_rial': 100000},
                             {'name': 'یورو', 'to_rial': 120000},
                             {'name': 'پوند انگلیس', 'to_rial': 130000}]

    for currency in all_currency_list:
        if currency['name'] == 'دلار آمریکا تهران':
            our_currency_list.append({'name': 'دلار آمریکا', 'to_rial': int(currency['maxVal'])})
        if currency['name'] == 'یورو':
            our_currency_list.append({'name': 'یورو', 'to_rial': int(currency['maxVal'])})
        if currency['name'] == 'پوند انگلیس':
            our_currency_list.append({'name': 'پوند انگلیس', 'to_rial': int(currency['maxVal'])})

    return render(request, 'KIA_general/currency_rates.html',
                  {'rates': our_currency_list, 'role': Profile.objects.get(user=request.user).role})


def service_info(request):
    info = {
        'name': 'TOEFL',
        'price': '215',
        'currency': 'Dollar',
        'detail': 'An English exam',
    }
    return render(request, 'KIA_general/service_info.html',
                  {'info': info, 'role': Profile.objects.get(user=request.user).role})


def purchase(request):
    name = 'TOEFL'
    info = [
        'مرکز مورد نظر',
        'تاریخ ثبت نام',
        'پول',
        'ملاحظات',
    ]
    return render(request, 'KIA_general/purchase.html',
                  {'name': name, 'info': info, 'role': Profile.objects.get(user=request.user).role})
