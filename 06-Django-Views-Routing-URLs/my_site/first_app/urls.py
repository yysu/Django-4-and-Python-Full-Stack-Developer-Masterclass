from django.urls import path
from . import views

urlpatterns = [
    path('',views.simple_view),
    path('<int:num1>/<int:num2>',views.add_view),
    path('<int:page_number>',views.page_num_view),
    path('<str:topic>/',views.news_view,name='topic-page'),
]