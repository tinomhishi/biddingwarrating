import urllib.request
import urllib.parse
import urllib.error
from datetime import datetime, timedelta
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.conf import settings

from .models import *


@login_required
def index(request):
    return render(request, 'userrating/index.html')


@login_required
def sales_list(request):
    sales = ItemSale.objects.filter(seller=request.user)
    return render(request, 'userrating/sales.html', {'sales': sales})


@login_required
def purchases_list(request):
    purchases = ItemSale.objects.filter(buyer=request.user)
    return render(request, 'userrating/purchases.html',
                    {'purchases': purchases})