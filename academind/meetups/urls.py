from django.urls import path
from . import views

urlpatterns = [
    path('', views.index), # my-domain.com/meetups
    path('<slug:meetup_slug>/success', views.confirmed, name='confirmreg'),
    path('<slug:meetup_slug>', views.details, name='details'),
]