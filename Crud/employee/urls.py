from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('emp',views.emp),
    path('show',views.show),
    #path('edit',views.edit),
    path('edit/<int:id>',views.edit),
    path('update/<int:id>',views.update),

    path('destroy',views.destroy),
]