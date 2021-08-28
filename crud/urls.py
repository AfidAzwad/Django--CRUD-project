from django.urls import path
from crud import views

app_name = "crud"

urlpatterns = [
    path('', views.home, name="home"),
    path('admin/', views.home, name="admin"),
    path('userform/', views.userform, name="userform"),
    path('userprofile/<int:userid>/', views.userprofile, name="userprofile"),
    path('userupdate/<int:userid>/', views.userupdate, name="update"),
    path('delete/<int:userid>/', views.userdelete, name="delete"),


]