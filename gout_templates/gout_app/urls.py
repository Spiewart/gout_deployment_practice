from django.conf.urls import include
from django.urls import path
from gout_app import views

#TEMPLATE TAGGING
app_name = 'gout_app'

urlpatterns = [
    path('relative/',views.relative,name='relative'),
    path('other',views.other,name="other"),
]
