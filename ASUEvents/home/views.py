from django.shortcuts import render, render
from django.http import HttpResponse
from django.conf import settings

import os

def index(request):
    context = {'message': 'Hello, World!'}
    return render(
        request,
        os.path.join(settings.TEMPLATE_PATH, 'index.html'),
        context
    )
