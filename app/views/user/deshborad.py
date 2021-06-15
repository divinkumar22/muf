

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django import template
from app.models import Transaction,User


@login_required
def DeshboradVeiw(request):
    data = {}
    userid = request.user.id
    user = User.objects.filter(id=userid).first()
    total_amount = user.total_amount
    data['total_amount'] = total_amount
    
    last_transactions = Transaction.objects.filter(user=user).latest('created_at')
    data['last_transactions'] = last_transactions.transaction_amount
    data['type'] = last_transactions.transaction_type
    
    print("heyyy",data)
    return render(request, 'deshborad.html', {'data': data})


def pages(request):
    context = {}
    try:
        load_template = request.path.split('/')[-1]
        context['segment'] = load_template
        
        html_template = loader.get_template( load_template )
        return HttpResponse(html_template.render(context, request))
        
    except template.TemplateDoesNotExist:

        html_template = loader.get_template( 'page-404.html' )
        return HttpResponse(html_template.render(context, request))

    except:
    
        html_template = loader.get_template( 'page-500.html' )
        return HttpResponse(html_template.render(context, request))
