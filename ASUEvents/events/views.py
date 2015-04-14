from django.shortcuts import render
from django.views.generic import TemplateView
from django.conf import settings
from events.models import Event

import os


class EventView(TemplateView):

    def __init__(self):
        self.template_name = os.path.join(settings.TEMPLATE_PATH, 'event.html')
        self.context = {
            'title': 'Event',
            'subtitle': 'example event',
            'addfonts': [

            ],
            'addstyles': [

            ],
            'addscripts': [

            ]
        }

    def get_context_data(self, eventid):
        event = Event.objects.filter(id=eventid)[0]
        self.context['title'] = event.name
        self.context['subtitle'] = event.description
        return self.context