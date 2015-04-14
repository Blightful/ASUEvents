from django.contrib import admin
from events.models import Building, Room, Event, Peripheral
from managers.models import Manager

admin.site.register(Building)
admin.site.register(Room)
admin.site.register(Manager)
admin.site.register(Event)
admin.site.register(Peripheral)
