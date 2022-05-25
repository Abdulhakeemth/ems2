
from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    # path('', views.registration_view, name="home"),
    # # path('admin/', admin.site.urls),
    # path('account/', views.account_view, name="account"),
    # path('create-teacher/', views.create_teacher, name="create_teacher"),
    # path('teacher-list/', views.teacher_list, name="teacher_list"),
    # path('update-teacher/<pk>/', views.update_teacher, name="update_teacher"),
    # path('delete-teacher/<pk>/', views.delete_teacher, name="delete_teacher"),


    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    # path('must-authenticate/', views.must_authenticate_view, name="must_authenticate"),
    # path('register/', views.registration_view, name="register"),
    # path('phone-otp/', views.phone_otp, name="phone_otp"),
    path('forgot-password/', views.forgot_password, name="forgot_password"),
    path('forgot-password-otp/', views.forgot_password_otp, name="forgot_password_otp"),
    path('forgot-password-new-password/', views.forgot_password_new_password, name="forgot_password_new_password"),
    path('reset-password/', views.reset_password, name="reset_password"),
    # path('check-username/', views.check_username, name="check_username"),
    # path('check-email/', views.check_email, name="check_email"),

    # path('auto_register/', views.auto_registration_view, name="auto_register"),
]