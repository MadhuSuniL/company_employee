from django.urls import path
from . import views

app_name = 'employees'
urlpatterns = [
    path('', views.home, name='home'),
    path('add_employee/<int:company_id>/', views.add_employee, name='add_employee'),
]
