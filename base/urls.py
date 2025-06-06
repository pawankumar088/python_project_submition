from django.urls import path, include
from .views import authView, home
from . import views
urlpatterns = [
    path("", home, name="home"),
    path("signup/", authView, name="authView"),
    path("accounts/", include("django.contrib.auth.urls")),
    path('add-student/', views.add_student, name='add_student'),
    path('update-student/', views.update_student, name='update_student'),
    path('delete_student/<int:id>/', views.delete_student, name='delete_student'),

]
