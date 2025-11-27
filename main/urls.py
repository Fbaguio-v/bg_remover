from django.urls import path
from . import views

app_name = "main"
urlpatterns = [
    path('', views.index, name='index'),
    path('remove', views.upload_image, name='remove'),
]
