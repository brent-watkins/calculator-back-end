from django.urls import path
		
from . import views
		
urlpatterns = [
path('add/', views.add, name='Add'),
path('divide/', views.divide, name='Divide'),
path('multiply/', views.multiply, name='Multiply'),
path('random_string/', views.random_string, name='Random String'),
path('square_root/', views.square_root, name='Square Root'),
path('subtract/', views.subtract, name='Subtract'),
]
