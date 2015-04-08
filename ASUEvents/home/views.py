from django.shortcuts import render, render
from django.http import HttpResponse
from django.conf import settings
import elements

import os

def index(request):
    context = {
        'stat': elements.DashboardStat(
            'Events', '1349',
            color='red-intense', icon='calendar',
            link='javascript:;', link_text='View events'
        ),
        'calendar': elements.CalendarPortlet('Calendar', color='red-intense')
    }
    return render(
        request,
        os.path.join(settings.TEMPLATE_PATH, 'index.html'),
        context
    )
