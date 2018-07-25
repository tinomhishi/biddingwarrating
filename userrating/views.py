import urllib.request
import urllib.parse
import urllib.error
from datetime import datetime, timedelta
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.conf import settings


@login_required
def index(request):
    return render(request, 'userrating/index.html')