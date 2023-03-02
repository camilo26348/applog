from django.db import models

# Create your models here.
class pclog (models.Model):
    date = models.DateTimeField(blank=False, null=False)
    pc =  models.CharField(max_length=255, unique=False, blank=False, null=False, help_text='')
    ip = models.CharField(max_length=255, unique=False, blank=True, null=True, help_text='')
    user = models.CharField(max_length=255, unique=False, blank=False, null=False, help_text='')
    app_name = models.CharField(max_length=255, unique=False, blank=False, null=False, help_text='')
    app_title = models.CharField(max_length=255, unique=False, blank=False, null=False, help_text='')
    open_time = models.TimeField(blank=False, null=False)
    def __str__(self):
        return self.date.__str__() + ' ' + \
               self.pc.__str__() + ' ' + \
               self.ip.__str__() + ' ' +\
               self.user.__str__() + ' ' +\
               self.app_name.__str__() + ' ' +\
               self.app_title.__str__() + ' ' +\
               self.open_time.__str__()