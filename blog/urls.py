from django.urls import path
from .views import BlogListVista

app_name="blog"

urlpatterns = [
    path('Inicio/',BlogListVista.as_view(), name="Home")
]