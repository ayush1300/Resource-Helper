from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('delete/<list_id>', views.delete, name="delete"),
    path('delete2/<componentlist_id>/<list_id>', views.delete2, name="delete2"),
    path('cross_off/<list_id>', views.cross_off, name="cross_off"),
    path('uncross_off/<list_id>', views.uncross_off, name="uncross_off"),
    path('edit/<componentlist_id>/<list_id>', views.edit, name='edit'),
    path('component/<list_id>', views.component, name='component')
]
