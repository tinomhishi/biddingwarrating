import urllib.request
import urllib.parse
import urllib.error
from datetime import datetime, timedelta
from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib import messages
from django.conf import settings
from datetime import datetime, timedelta
from django.http import HttpResponseRedirect
from django.utils import timezone

from .models import *
from .forms import UserReviewForm


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

@login_required
def purchase_detail(request, pk):
	purchase = ItemSale.objects.get(pk=pk)
	
	if request.method == 'POST':
		form = UserReviewForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('userrating:purchase_detail', args=[purchase.pk]))
	else:
		data = {'itemsale': purchase , 'user': purchase.buyer}
		form = UserReviewForm(initial=data)

	try:
		review = UserReview.objects.get(itemsale=purchase)
	except:
		review = None

	deadline =  purchase.created + timedelta(days=31)
	
	if deadline >= timezone.now():
		show = True
	else:
		show = False	

	return render(request, 'userrating/purchase_detail.html', {'purchase': purchase, 'form': form, 'show': show, 'review': review})

@login_required
def purchase_review_edit(request, pk):
	purchase = ItemSale.objects.get(pk=pk)
	review = UserReview.objects.get(itemsale=purchase)
	form = UserReviewForm(request.POST or None, instance=review)
	if form.is_valid():
		form.save()
		return HttpResponseRedirect(reverse('userrating:purchase_detail', args=[purchase.pk]))

	try:
		review = UserReview.objects.get(itemsale=purchase)
	except:
		review = None

	deadline =  purchase.created + timedelta(days=31)
	
	if deadline >= timezone.now():
		show = True
	else:
		show = False
		
	return render(request, 'userrating/purchase_review_edit.html', {'purchase': purchase, 'form': form, 'show': show, 'review': review})	



@login_required
def sale_detail(request, pk):
	sale = ItemSale.objects.get(pk=pk)

	if request.method == 'POST':
		form = UserReviewForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('userrating:sale_detail', args=[sale.pk]))
	else:
		data = {'itemsale': sale , 'user': sale.seller}
		form = UserReviewForm(initial=data)

	try:
		review = UserReview.objects.get(itemsale=sale)
	except:
		review = None

	deadline =  sale.created + timedelta(days=31)

	if deadline >= timezone.now():
		show = True
	else:
		show = False	

	return render(request, 'userrating/sale_detail.html', {'sale': sale, 'form': form, 'show': show, 'review': review})

@login_required
def sale_review_edit(request, pk):
	sale = ItemSale.objects.get(pk=pk)
	review = UserReview.objects.get(itemsale=sale)
	form = UserReviewForm(request.POST or None, instance=review)
	if form.is_valid():
		form.save()
		return HttpResponseRedirect(reverse('userrating:sale_detail', args=[sale.pk]))

	try:
		review = UserReview.objects.get(itemsale=sale)
	except:
		review = None

	deadline =  sale.created + timedelta(days=31)
	
	if deadline >= timezone.now():
		show = True
	else:
		show = False
		
	return render(request, 'userrating/sale_review_edit.html', {'sale': sale, 'form': form, 'show': show, 'review': review})	



