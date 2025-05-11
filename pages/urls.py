from django.urls import path
from pages import views 

urlpatterns = [
    path('pages/', views.pages_req, name='PAGES'),
    path('pages/contacts', views.contact, name='CONTACTS'),
    path('pages/about', views.about, name='ABOUT'),
]