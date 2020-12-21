from django.urls import path
from .import views

urlpatterns=[
 path('', views.insert, name='insert'),
 path('display',views.display, name='display'),
 path('update/<int:id>', views.update, name='update'),
 path('delete/<int:id>', views.delete, name='delete'),
]



































































#
# path('update', views.update, name='update'),
# path('delete', views.delete, name='delete')
