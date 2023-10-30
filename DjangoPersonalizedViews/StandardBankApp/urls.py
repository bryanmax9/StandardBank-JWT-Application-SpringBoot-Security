from django.urls import path
from .views import user_dashboard, landing_page  #import here the views(import functions from views.py)

urlpatterns = [
    path('', landing_page, name='landing_page'),
    path('dashboard/', user_dashboard, name='user_dashboard'),
]
