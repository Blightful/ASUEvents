from django.shortcuts import render, render
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.conf import settings

import os

from MetronicElements import DashboardStat, CalendarPortlet


class IndexView(TemplateView):

    def __init__(self):
        self.template_name = os.path.join(settings.TEMPLATE_PATH, 'index.html')
        self.context = {
            'title': 'Dashboard',
            'subtitle': 'current scheduled events',
            'addfonts': [
                # No additional fonts
            ],
            'addstyles': [
                os.path.join(
                    settings.ASSETS_GLOBAL,
                    'plugins', 'fullcalendar', 'fullcalendar.min.css'
                )
            ],
            'addscripts': [
                os.path.join(
                    settings.ASSETS_GLOBAL,
                    'plugins', 'moment.min.js'
                ),
                os.path.join(
                    settings.ASSETS_GLOBAL,
                    'plugins', 'fullcalendar', 'fullcalendar.min.js'
                ),
                os.path.join(
                    settings.ASSETS_ADMIN,
                    'pages', 'scripts', 'calendar.js'
                ),
            ],
            'stat': DashboardStat('Events', 1349, icon='calendar', link='www.google.com', linktext='View More'),
            'calendar': CalendarPortlet('Calendar'),
        }

    def get_context_data(self):
        return self.context
