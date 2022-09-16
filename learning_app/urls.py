from django.urls import path
from . import views
# Use app_name to replace namespace
app_name = 'learning_app'
urlpatterns = [
 # Home page
 path('', views.index, name='index'),
 path('topics/', views.topics, name='topics'),
 path('topics/<int:topic_id>/', views.topic, name='topic'), 
]