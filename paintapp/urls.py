from django.urls import path
from . import views

app_name = "paintapp"

urlpatterns = [
    path("", views.index, name="index"),
    path('drawings/', views.drawing_list, name='drawing_list'),
]
