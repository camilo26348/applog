from django.conf.urls import url
from django.urls import path, include
from .views import pclogListApiView

urlpatterns = [
    path('api', pclogListApiView.as_view()),
]