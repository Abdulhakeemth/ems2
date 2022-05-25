from django.contrib import admin
from event.models import *
from .models import Event,Banner,EventTicket


class EventAdmin(admin.ModelAdmin):
    list_display = ['event_name','venue','date','time','duration','end_time','reg_end_time','reg_fee']
admin.site.register(Event,EventAdmin)

class BannerAdmin(admin.ModelAdmin):
    list_display = ['title','event','description','mobile_image','web_image','order']
admin.site.register(Banner,BannerAdmin) 

class EventTicketAdmin(admin.ModelAdmin):
    list_display = ['event','payment_status','attandance','email','phone','full_name','address','district']
admin.site.register(EventTicket,EventTicketAdmin)    
