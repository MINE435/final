from django.urls import path
from django.contrib.auth.views import LoginView
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('indexx/',views.doctor_index,name='doctor_index'),
    path('', views.HomeView.as_view(), name='index'),
    
    path('doctor/',views.doctor,name='doctor'),
    path('appointment/',views.appointment,name='appointment'),
    path('cardiologist/',views.cardiologist,name='cardiologist'),
    path('ecg/',views.ecg,name='ecg'),
    path('seniorheartsurger/',views.seniorheartsurger,name='seniorheartsurger'),
    path('gallery/',views.gallery,name='gallery'),
    path('home/',views.home,name='home'),
    path('success/',views.succes,name='success'),
    path('contactus/', views.contactus, name='contactus'),
    path('send-email-and-message/', views.send_email_and_message, name='send_email_and_message'),
    path('login/',views.login_user,name='login'),
    path('register/',views.registration,name='register'),
    path('display/',views.display_appointment,name="display_appointment"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)