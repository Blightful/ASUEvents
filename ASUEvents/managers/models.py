from django.db import models


class Manager(models.Model):
    managerid = models.CharField(max_length=25, unique=True, primary_key=True)
    fname = models.CharField(max_length=35)
    mname = models.CharField(max_length=35)
    lname = models.CharField(max_length=35)
    email = models.EmailField(max_length=254)
    sex = models.CharField(max_length=1, null=True, default=None)

    def __unicode__(self):
        return '{} ({} {})'.format(self.managerid, self.fname, self.lname)