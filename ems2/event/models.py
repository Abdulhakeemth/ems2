from __future__ import unicode_literals
from django.db import models
from datetime import datetime
from main.models import BaseModel
from django.utils.translation import ugettext_lazy as _
from versatileimagefield.fields import VersatileImageField
from account.models import Account,District

class Event(BaseModel):    
    event_name = models.CharField(max_length=128,null=True,blank=True)
    venue = models.CharField(max_length=128,null=True,blank=True)
    date = models.DateField()
    time = models.TimeField()
    duration = models.DurationField()
    end_time = models.CharField(max_length=128,null=True,blank=True)
    reg_end_time = models.DateTimeField(default=datetime.now)
    reg_fee = models.PositiveIntegerField(default=0)

    class Meta:
        db_table = 'Event'
        verbose_name = _('Event')
        verbose_name_plural = _('Events')
        ordering = ('-date_added',)

    def __str__(self):
        return str(self.event_name)

class Banner(BaseModel):
 
    title= models.CharField(max_length=255)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    description = models.TextField()
    mobile_image = VersatileImageField(
        'mobile_image',
        upload_to='images/event/banner/mobile/',
        # width_field='width',
        # height_field='height'
    )
    web_image = VersatileImageField(
        'web_image',
        upload_to='images/event/banner/web/',
        # width_field='width',
        # height_field='height'
    )
    order= models.IntegerField(default=0)

    class Meta:
        db_table = 'Banner'
        verbose_name = _('Banner')
        verbose_name_plural = _('Banners')
        ordering = ('-date_added',)

    def __str__(self):
        return str(self.title)    

class EventTicket(BaseModel):    
    event = models.ForeignKey(Event, on_delete=models.CASCADE,blank=True,null=True)
    payment_status =(
        ('Paid', 'Paid'),
        ('Cancel', 'Cancel'),
        ('Pending', 'Pending')
        )
    payment_status = models.CharField(choices=payment_status,max_length=10)
    attandance_status=(
        ('Present','Present'),
        ('Absent', 'Absent'),
        ('Pending', 'Pending')

    )
    attandance = models.CharField(choices=attandance_status,max_length=14)
    email = models.EmailField(verbose_name="email", max_length=60,)
    full_name = models.CharField(max_length=140)
    phone_code = models.CharField(max_length=30,default="91")
    phone = models.PositiveIntegerField()
    address = models.TextField()
    district = models.ForeignKey(District, on_delete=models.CASCADE,blank=True,null=True)

    class Meta:
        db_table = 'Event_Ticket'
        verbose_name = _('Event Ticket')
        verbose_name_plural = _('Event Tickets')
        ordering = ('-date_added',)

    def __str__(self):
        return str(self.event)