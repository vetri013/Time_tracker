
from django.urls import path
from . import views
urlpatterns = [
    path('time/', views.timesheet,name='timesheet'),
]
