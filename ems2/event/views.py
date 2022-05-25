
from django.shortcuts import render,redirect
from django.http.response import HttpResponse
from django.contrib.auth.decorators import login_required
from django.forms import formset_factory,modelformset_factory

from .forms import *
from .models import *
import json
from django.core.paginator import Paginator


@login_required(login_url='account:login')
def create_event(request):     
    user = request.user
    if user.is_admin:
        if request.method == "POST":
            form = EventForm(request.POST,request.FILES)
            BannerFormset = formset_factory(BannerForm,extra=1)
            formset = BannerFormset(request.POST,request.FILES, prefix="banner-formset")
            if (form.is_valid() and formset.is_valid()):
                form_data = form.save(commit=False)
                form_data.save()
                for formset_item in formset:
                    formset_data = formset_item.save(commit=False)
                    formset_data.event = form_data
                    # investor = formset_data.investor.pk
                    # data = Investor.objects.filter(pk = investor).update(investor_group=form_data)
                    formset_data.save()
                response_data = {
                    "status" : "true",
                    "title" : "Success",
                    "reLoad" : "true",
                }
            else:
                response_data = {
                    "status" : "false",
                    "title" : "Form validation error",
                    "reLoad" : "false",
                }
            return HttpResponse(json.dumps(response_data),content_type='application/javascript')
        else:
            BannerFormset = formset_factory(BannerForm,extra=1)
            formset =BannerFormset(prefix="banner-formset")
            form = EventForm()
            context = {
                "form" : form,
                "formset":formset,
                "page_name":"create_event",     
            }
            return render(request, 'dashboard/event/create_event.html',context)
    else:
        context = {}
        return render(request, '403.html',context)     



@login_required(login_url='account:login')
def event_list(request):     
    user = request.user
    if user.is_admin:
        event = Event.objects.filter(is_deleted=False)
        paginator = Paginator(event, 25)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context = {
            "page_obj" : page_obj,
            "page_name":"event_list",
        }
        return render(request, 'dashboard/event/list_event.html',context)
    else:
        context = {}
        return render(request, '403.html',context)

@login_required(login_url='account:login')
def view_event(request,pk): 
    user = request.user
    if user.is_admin:
        event = Event.objects.get(pk=pk)
        banners = Banner.objects.filter(event=event)
        context = {
            "banners":banners,
            "event" : event,   
            "page_name": "view_event",
        }
        return render(request, 'dashboard/event/view_event.html',context)
    else:
        context = {}
        return render(request, '403.html', context)
    

@login_required(login_url='account:login')
def update_event(request,pk):     
    user = request.user
    if user.is_admin:
        if request.method == "POST":
            instance = Event.objects.get(pk=pk)
            form = EventForm(request.POST,request.FILES,instance=instance)
            banners =  Banner.objects.filter(event = instance).values()
            
            BannerFormset = formset_factory(Banner,extra=1)
            formset = BannerFormset(request.POST,request.FILES,initial=banners , prefix="banner-formset")

            # if (form.is_valid()): 
            # and 
            if(formset.is_valid()):
                print("validdd")
                # form_data=form.save(commit=False)
                # form_data.save()

            #     for formset_item in formset:
            #         formset_data = formset_item.save()

            response_data = {
                "status" : "true",
                "title" : "Success",
                "reLoad" : "true",
                }
            return HttpResponse(json.dumps(response_data),content_type='application/javascript')
        else:
            instance = Event.objects.get(pk=pk)
            banners =  Banner.objects.filter(event = instance).values()
            BannerFormset = formset_factory(BannerForm,extra= 0)
            formset = BannerFormset(prefix="banner-formset", initial = banners)
            form = EventForm(instance = instance)
            
            context = {
                "form" : form,
                "formset":formset,
                "instance" :instance,
                "page_name": "update_event",
 
            }
            return render(request, 'dashboard/event/update_event.html',context)
    else:
        context = {}
        return render(request, '403.html',context)


@login_required(login_url='account:login')
def delete_event(request,pk):     
    user = request.user
    if user.is_admin:
        Event.objects.get(pk=pk).delete()
        return redirect("event:list_event")
    else:
        context = {}
        return render(request, '403.html',context)

# /////////////////////////////////////////

@login_required(login_url='account:login')
def banner_list(request):     
    user = request.user
    if user.is_admin:
        banner = banner.objects.filter(is_deleted=False)
        paginator = Paginator(banner,25)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context = {
            "page_obj" : page_obj,
            "page_name":"banner_list",
        }
        return render(request, 'dashboard/banner/list_banner.html',context)
    else:
        context = {}
        return render(request, '403.html',context)  



@login_required(login_url='account:login')
def view_banner(request,pk): 
    user = request.user
    if user.is_admin:
        banner = Banner.objects.get(pk=pk)
        context = {
            "banner" : "banner",   
            "page_name": "view_banner",
        }
        return render(request, 'dashboard/banner/view_banner.html',context)
    else:
        context = {}
        return render(request, '403.html', context) 

@login_required(login_url='account:login')
def update_banner(request,pk):     
    user = request.user
    if user.is_admin:
        if request.method == "POST":
            instance = Banner.objects.get(pk=pk)
            form = BannerForm(request.POST,request.FILES,instance=instance)
            
            if (form.is_valid()):
                form.save()
                response_data = {
                "status" : "true",
                "title" : "Success",
                "reLoad" : "true",
                }
            return HttpResponse(json.dumps(response_data),content_type='application/javascript')
        else:
            instance = Banner.objects.get(pk=pk)
            form = BannerForm(instance = instance)
            context = {
                "form" : form,
                "instance" :instance,
                "page_name": "update_banner",
 
            }
            return render(request, 'dashboard/banner/update_banner.html',context)
    else:
        context = {}
        return render(request, '403.html',context) 


@login_required(login_url='account:login')
def delete_banner(request,pk):     
    user = request.user
    if user.is_admin:
        Banner.objects.get(pk=pk).delete()
        return redirect("banner:list")
    else:
        context = {}
        return render(request, '403.html',context)                                            
# ///////////////////////////////////////////////////////
@login_required(login_url='account:login')
def create_eventticket(request):     
    user = request.user
    if user.is_admin:
        if request.method == "POST":
            form = EventTicketForm(request.POST,request.FILES)
            if form.is_valid():
                print("valid 00000000000")
                form_data = form.save(commit=False)
                form_data.save()
                response_data = {
                    "status" : "true",
                    "title" : "Success",
                    "reLoad" : "true", 
                }
            else:
                response_data = {
                    "status" : "false",
                    "title" : "Form validation error",
                    "reLoad" : "false",
                }
            return HttpResponse(json.dumps(response_data),content_type='application/javascript')
        else:
            form = EventTicketForm(request.POST)
            context = {
                "form" : form,
                "page_name":"create_eventticket",     
            }
            return render(request, 'dashboard/event_ticket/create_eventticket.html',context)
    else:
        context = {}
        return render(request, '403.html',context)

@login_required(login_url='account:login')
def eventticket_list(request):     
    user = request.user
    if user.is_admin:
        eventticket = EventTicket.objects.filter(is_deleted=False)
        paginator = Paginator(eventticket, 25)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context = {
            "page_obj" : page_obj,
            "page_name":"eventticket_list",
        }
        return render(request, 'dashboard/event_ticket/list_eventticket.html',context)
    else:
        context = {}
        return render(request, '403.html',context)

@login_required(login_url='account:login')
def view_eventticket(request,pk): 
    user = request.user
    if user.is_admin:
        eventticket = EventTicket.objects.get(pk=pk)
        context = {
            "eventticket" : eventticket,   
            "page_name": "view_eventticket",
        }
        return render(request, 'dashboard/event_ticket/view_eventticket.html',context)
    else:
        context = {}
        return render(request, '403.html', context) 


@login_required(login_url='account:login')
def update_eventticket(request,pk):     
    user = request.user
    if user.is_admin:
        if request.method == "POST":
            instance = EventTicket.objects.get(pk=pk)
            form = EventTicketForm(request.POST,request.FILES,instance=instance)
            
            if (form.is_valid()):
                form.save()
                response_data = {
                "status" : "true",
                "title" : "Success",
                "reLoad" : "true",
                }
            return HttpResponse(json.dumps(response_data),content_type='application/javascript')
        else:
            instance = EventTicket.objects.get(pk=pk)
            form = EventTicketForm(instance = instance)
            context = {
                "form" : form,
                "instance" :instance,
                "page_name": "update_eventticket",
 
            }
            return render(request, 'dashboard/event_ticket/update_eventticket.html',context)
    else:
        context = {}
        return render(request, '403.html',context)  
@login_required(login_url='account:login')
def delete_eventticket(request,pk):     
    user = request.user
    if user.is_admin:
        EventTicket.objects.get(pk=pk).delete()
        return redirect("eventticket:list")
    else:
        context = {}
        return render(request, '403.html',context)                      



    

