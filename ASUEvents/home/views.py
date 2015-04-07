from django.shortcuts import render, render
from django.http import HttpResponse
from django.conf import settings
import elements

import os

def index(request):
    context = {'message': 'Hello, World!', 'stat': elements.DashboardStat('Events', '1349', color='red-intense', icon='calendar', link='javascript:;', link_text='View events')}
    return render(
        request,
        os.path.join(settings.TEMPLATE_PATH, 'index.html'),
        context
    )
