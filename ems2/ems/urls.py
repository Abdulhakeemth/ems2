from audioop import reverse
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path,include,re_path
from django.urls import path,include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('event/', include('event.urls',namespace='event')),
    path('auth/', include('account.urls',namespace='account')),
    # path('student/', include('student.urls',namespace='student')),
    # path('banner/', include('banner.urls',namespace='banner')),
    # path('',include("lab.urls")),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)