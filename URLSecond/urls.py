from django.urls import path
from .views import url_view

urlpatterns = [
    path('', url_view, name='url_view'),
    path('<str:short_url>/', url_view, name='redirect_view'),
]
