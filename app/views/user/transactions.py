
from django.db import models
from django.forms.models import model_to_dict
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django import template
from app.models import Transaction, NormalUser, PickupMan

@login_required
def TranactionVeiw(request,queryset=None):
    userid = request.user.id
    user = NormalUser.objects.filter(pk=userid).first()
    total_amount = user.total_amount
    print(total_amount)
    all_transactions = Transaction.objects.filter(user = user)

    transactions = []

    for i in all_transactions:
        data = model_to_dict(i)
        print(data)
        pickup_man_name = i.pickup_man.user.name
        data['name'] = pickup_man_name
        
        transactions.append(data)
        print("all", transactions)
    return render(request, 'transactions.html', { 'transactions': transactions})


def pages(request):
    context = {}

    try:
        
        load_template      = request.path.split('/')[-1]
        context['segment'] = load_template
        
        html_template = loader.get_template( load_template )
        return HttpResponse(html_template.render(context, request))
        
    except template.TemplateDoesNotExist:

        html_template = loader.get_template( 'page-404.html' )
        return HttpResponse(html_template.render(context, request))

    except:
    
        html_template = loader.get_template( 'page-500.html' )
        return HttpResponse(html_template.render(context, request))
