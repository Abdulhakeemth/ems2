from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from account.forms import RegistrationForm, AccountAuthenticationForm, AccountUpdateForm
from .models import *
from random import randint
from django.core import mail
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.http.response import HttpResponse
import json
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator


@login_required(login_url='account:login')
def create_event(request):     
    user = request.user
    if user.is_admin:
        if request.method == "POST":
            print("000")
            post_data = request.POST.copy()
            post_data["password2"] =post_data["password1"]  
            form = EventForm(post_data)
            print(form.data)
            if form.is_valid():
                print("1111")
                form_data = form.save(commit=False)
                form_data.is_event = True
                form_data.save()
                user = authenticate(username=form_data.username, password=form_data.password)
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
            form = EventForm(request.POST)
            context = {
                "form" : form,
                "page_name":"create_event",     
            }
            return render(request, 'dashboard/account/create_event.html',context)
    else:
        context = {}
        return render(request, '403.html',context)

# @login_required(login_url='account:login')
# def update_teacher(request,pk):     
#     user = request.user
#     if user.is_admin or user.is_teacher:
#         if request.method == "POST":
#             instance = Account.objects.filter(pk=pk).first()
#             form = UpdateTeacherForm(request.POST,request.FILES,instance=instance)
#             if (form.is_valid()):
#                 form.save()
#                 response_data = {
#                 "status" : "true",
#                 "title" : "Success",
#                 "reLoad" : "true",
#                 }
#             else:
#                 response_data = {
#                 "status" : "false",
#                 "title" : "Validation error !",
#                 "reLoad" : "true",
#                 }
#             return HttpResponse(json.dumps(response_data),content_type='application/javascript')
#         else:
#             instance = Account.objects.filter(pk=pk).first()
#             form = UpdateTeacherForm(instance = instance)
#             context = {
#                 "form" : form,
#                 "instance" :instance,
#                 "page_name": "update_teacher",
#             }
#             return render(request, 'dashboard/account/update_teacher.html',context)
#     else:
#         context = {}
#         return render(request, '403.html',context)


# @login_required(login_url='account:login')
# def teacher_list(request):     
#     user = request.user
#     if user.is_admin or user.is_teacher:
#         class_detiles = Account.objects.filter()
#         paginator = Paginator(class_detiles, 25)
#         page_number = request.GET.get('page')
#         page_obj = paginator.get_page(page_number)
#         context = {
#             "page_obj" : page_obj,
#             "page_name":"teacher_list",
#         }
#         return render(request, 'dashboard/account/list_teacher.html',context)
#     else:
#         context = {}
#         return render(request, '403.html',context)

# @login_required(login_url='account:login')
# def delete_teacher(request,pk):     
#     user = request.user
#     if user.is_admin:
#         Account.objects.get(pk=pk).delete()
#         return redirect("account:teacher_list")
#     else:
#         context = {}
#         return render(request, '403.html',context)









# def registration_view(request):
# 	context = {}
# 	user = request.user
# 	if user.is_authenticated: 
# 		logout(request)

# 	if request.POST:
# 		form = RegistrationForm(request.POST)
# 		if form.is_valid():
# 			data = form.save(commit=False)
# 			otp = str(randint(100000, 999999))
# 			request.session['username'] = data.username
# 			request.session['email'] = data.email
# 			request.session['password1'] = form.cleaned_data.get('password1')
# 			request.session['password2'] = form.cleaned_data.get('password2')
# 			request.session['address'] = data.address
# 			request.session['phone'] = data.phone
# 			request.session['otp'] = otp
# 			email = data.email
# 			name =  data.username

# 			try:
# 				message = 'your otp is : ' + otp + ','
# 				# resp =  sendSMS('YWMxYTJlM2FhZWRjZTQ1ZjJmYjI4ZDgxYWUyMjBjYmE=', '91' + data.phone,
# 				# 	"ECOLMS", message)
# 				print(message)
# 				return redirect('account:phone_otp')
# 			except:
# 				error = "somthing wrong !"
# 				print(error)
# 		else:
# 			context['registration_form'] = form
# 	else:
# 		form = RegistrationForm()
# 		context['registration_form'] = form
# 	return render(request, 'dashboard/account/register.html', context)


def phone_otp(request):
	phone = str(request.session['phone'])
	context = {
		"phone" : phone
		}
	if request.POST:
		real_otp = str(request.session['otp'])
		otp = request.POST['otp']

		updated_request = request.POST.copy()
		updated_request.update({
			'first_name': request.session['first_name'],
			'last_name': request.session['last_name'],
			'email': request.session['email'],
			'address': request.session['address'],
			'phone': request.session['phone'],
			'password1': request.session['password1'],
			'password2': request.session['password2'],
			'username': request.session['username'],
			})
		form =  RegistrationForm(updated_request)
		if (otp == real_otp) and form.is_valid():
			form.save()
			username = updated_request['username']
			password = updated_request['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			return redirect("overview:index")

	return render(request, "dashboard/account/phone_otp.html",context)

def logout_view(request):
	logout(request)
	return redirect('/')


def login_view(request):
	context = {}
	user = request.user
	if user.is_authenticated: 
		logout(request)
	if request.POST:
		form = AccountAuthenticationForm(request.POST)
		if form.is_valid():
			phone = request.POST['phone']
			password = request.POST['password']
			user = authenticate(phone=phone, password=password)
			if user:
				login(request, user)
				if user.is_admin:
					return redirect("lab:index")
				else:
					return redirect("lab:index")

	else:
		form = AccountAuthenticationForm()
	context['login_form'] = form
	return render(request, "dashboard/account/login.html", context)

def forgot_password(request):
	context = {}
	user = request.user
	if user.is_authenticated: 
		logout(request)
	if request.POST:
		try:
			request.session['otp_count'] = 5
			phone = request.POST['phone']
			if Account.objects.filter(phone=phone).exists():
				otp = str(randint(100000, 999999))
				request.session['otp'] = otp
				message = 'your otp is : ' + otp + ','
				# resp =  sendSMS('YWMxYTJlM2FhZWRjZTQ1ZjJmYjI4ZDgxYWUyMjBjYmE=', '91' + phone,
				# 	"ECOLMS", message)
				print(message)

				account = Account.objects.filter(phone=phone).first()
				request.session.set_expiry(300)
				request.session['account'] = account.pk
				return redirect("account:forgot_password_otp")
			else:
				messages.info(request, 'This number is not registerd')
				return redirect("account:forgot_password")
		except:
			messages.info(request, 'Your Session has time out. please try again')
			return redirect("account:forgot_password")
	return render(request, 'dashboard/account/forgot-password.html', context)


def forgot_password_otp(request):
	context = {}
	user = request.user
	if user.is_authenticated: 
		logout(request)
	if request.POST:
		try:
			input_otp = request.POST['otp']
			otp = request.session['otp']
			if input_otp == otp:
				if request.session['otp_count'] < 0:
					del request.session['account']
					del request.session['otp']
					messages.info(request, 'Too many attempts,Please Try again later')
					return redirect("account:forgot_password")
					
				account = request.session['account']	
				user = Account.objects.get(pk=account)			
				login(request, user)
				return redirect("account:forgot_password_new_password")
			else:
				otp_count = request.session['otp_count']
				request.session['otp_count'] = otp_count - 1
				messages.info(request, 'Incorrect OTP')
				if request.session['otp_count'] <= 0:
					del request.session['account']
					del request.session['otp']
					messages.info(request, 'Too many attempts,Please Try again later')
					return redirect("account:forgot_password")
		except:
			messages.info(request, 'Too many attempts,Please Try again later')
			return redirect("account:forgot_password")
	
	return render(request, 'dashboard/account/forgot_password_otp.html', context)

def forgot_password_new_password(request):
	context = {}
	user = request.user
	if request.POST:
		password = request.POST['password']
		try:
			account_pk = request.session["account"]
			account = Account.objects.get(pk = account_pk)
			account.set_password(password)
			account.save()
			login(request, account)
			return redirect("account:login")

		except:
			messages.info(request, 'Your Session has time out. please try again ')
			return redirect("account:forgot_password")

	return render(request, 'dashboard/account/forgot_password_new_password.html', context)



# def account_view(request):
# 	if not request.user.is_authenticated:
# 			return redirect("login")
# 	context = {}
# 	return render(request, "account/account.html", context)

# def must_authenticate_view(request):
# 	return render(request, 'account/must_authenticate.html', {})



def reset_password(request):
	context = {}
	user = request.user
	if user.is_authenticated: 
		if request.POST:
			old_password = request.POST['old_password']
			new_password = request.POST['new_password']
			print(old_password)
			print(new_password)

			if(user.check_password(old_password)):
				print("psswrd checked !!")
				account = Account.objects.get(pk=user.pk)
				print(account)
				account.set_password(new_password)
				account.save()
				logout(request)

				response_data = {
					"status" : "true",
					"title" : "Success",
					"reLoad" : "true",
					}
				return HttpResponse(json.dumps(response_data),content_type='application/javascript')
			else:
				response_data = {
					"status" : "false",
					"title" : "Form validation Error !",
					"reLoad" : "false",
					}
				return HttpResponse(json.dumps(response_data),content_type='application/javascript')
		else:	
			return render(request, 'dashboard/account/reset-password.html', context)

	return redirect('/')

# def check_username(request):
# 	user = request.user
 
# 	q = request.GET.get('q')
# 	print(q)
# 	if(Account.objects.filter(username=q).exists()):
# 		response_data = {
# 			"status" : "false",
# 		}
# 	else:
# 		response_data = {
# 			"status" : "true",
# 		}
# 	return HttpResponse(json.dumps(response_data),content_type='application/javascript')



# def check_email(request):
# 	user = request.user
 
# 	q = request.GET.get('q')
# 	if(Account.objects.filter(email=q).exists()):
# 		response_data = {
# 			"status" : "false",
# 		}
# 	else:
# 		response_data = {
# 			"status" : "true",
# 		}
# 	return HttpResponse(json.dumps(response_data),content_type='application/javascript')

