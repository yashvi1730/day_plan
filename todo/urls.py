from django.urls import path
from todo import views

urlpatterns=[
    path('',views.index,name="todo"),
    path('del/<item_id>',views.remove,name="del")
]