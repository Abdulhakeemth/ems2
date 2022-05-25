from django import forms
from django.forms import ModelForm
from event.models import Event
from dal import autocomplete
from .models import Event ,Banner, EventTicket
from django.forms.widgets import TextInput,FileInput,NumberInput,Textarea
    
class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['event_name','venue','date','time','duration','end_time','reg_end_time','reg_fee']
        widgets = {
            'event_name': forms.TextInput(attrs={'class': 'form-control',}),
            'venue' : forms.TextInput(attrs={'class': 'form-control',}),
            'date' : forms.DateInput(attrs={'class': 'form-control','type':'date'}),
            'time' : forms.TimeInput(attrs={'class': 'form-control','type':'time','min':0.00,'max':24.00}),
            'duration' : forms.TextInput(attrs={'class': 'form-control'}),
            'end_time': forms.DateTimeInput(attrs={'class': 'form-control'}),
            'reg_end_time': forms.DateTimeInput(attrs={'class': 'form-control'}),
            'reg_fee' : forms.TextInput(attrs={'class': 'form-control',})

            # 'start_date': forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}),
            # 'end_date': forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
            # 'title' : TextInput(attrs={'class': 'form-control',}),    
class  BannerForm(forms.ModelForm):
    class Meta:
        model = Banner
        fields =['title','description','mobile_image','web_image','order']
        widgets = {
           'title' : TextInput(attrs={'class': 'form-control',}),
           'mobile_image' :  FileInput(attrs={'class': 'form-control',}),
           'web_image' :  FileInput(attrs={'class': 'form-control',}),
           'order' :  NumberInput(attrs={'class': 'form-control','type':'nubmber',',min':'0'}),
           'description' : Textarea(attrs={'class': 'required form-control',}),         
        }
class EventTicketForm(forms.ModelForm):
    class Meta:
        model = EventTicket
        fields =['event','payment_status','attandance','email','full_name','phone','address','district']
        widgets = {
            'event' : forms.Select(attrs={'class': 'form-control',}),
            'payment_status' :forms.Select(attrs={'class': 'form-control',}),
            'attandance' :forms.Select(attrs={'class': 'form-control',}),
            'email' : forms.EmailInput(attrs={'class': 'form-control',}),
            'full_name' : forms.TextInput(attrs={'class' : 'form-control' ,}),
            # 'phone_code' : forms.NumberInput(attrs={'class' : 'form-control' , 'type':'number',}),
            'phone' : forms.TextInput(attrs={'class': 'form-control','type':'tele','minlength':'10','maxlength':'10'}),
            'address' : forms.TextInput(attrs={'class' : 'form-control' ,}),
            'district' : forms.Select(attrs={'class' : 'form-control' ,}),
            
        }  
