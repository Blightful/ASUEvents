from django.db import models


class Building(models.Model):
    buildingid = models.CharField(max_length=128, unique=True, primary_key=True)
    name = models.CharField(max_length=128)
    roomcount = models.IntegerField()
    floorcount = models.IntegerField()

    def __unicode__(self):
        return '{} ({})'.format(self.buildingid, self.name)


class Room(models.Model):
    roomid = models.CharField(max_length=10, unique=True, primary_key=True)
    name = models.CharField(max_length=128, unique=True)
    capacity = models.IntegerField(null=True)

    buildingid = models.ForeignKey(Building)

    def __unicode__(self):
        return '{} ({})'.format(self.roomid, self.name)


class Peripheral(models.Model):
    peripheralid = models.CharField(max_length=35, unique=True, primary_key=True)
    name = models.CharField(max_length=128)
    working = models.NullBooleanField(null=True)

    roomid = models.ForeignKey(Room)

    def __unicode__(self):
        return self.peripheralid


class Event(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.CharField(max_length=1024, null=True)
    timestart = models.DateTimeField()
    timeend = models.DateTimeField()
    yearly = models.BooleanField(default=False)
    monthly = models.BooleanField(default=False)
    weekly = models.BooleanField(default=False)
    daily = models.BooleanField(default=False)

    managerid = models.ForeignKey('managers.Manager')
    roomid = models.ForeignKey(Room)
    buildingid = models.ForeignKey(Building)

    def __unicode__(self):
        return self.name

