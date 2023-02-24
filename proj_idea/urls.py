from django.urls import path
from . import views
app_name = "Proj_idea"
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:proj_idea_id>/', views.show, name='show'),
]
