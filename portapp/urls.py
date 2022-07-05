from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.home, name='home'),
    path('about',views.about, name='about'),
    path('portfolio',views.portfolio, name='portfolio'),
    path('services',views.services, name='services'),
    path('contact',views.contact, name='contact'),
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)