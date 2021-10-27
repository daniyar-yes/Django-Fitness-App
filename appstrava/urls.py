from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:record_id>/', views.detail, name='detail'),
    path('top/', views.top, name='top'),
    path('top/year/', views.year_top, name='year_top'),
    path('top/month/', views.month_top, name='month_top'),
    path('top/pullups/', views.top_pullups, name='top_pullups'),
    path('top/crunches/', views.top_crunches, name='top_crunches'),
    path('top/squats/', views.top_squats, name='top_squats'),
    path('top/pushups/', views.top_pushups, name='top_pushups'),
    path('<str:user_name>/', views.user_detail, name='user_detail'),
    path('<int:record_id>/', views.detail, name='detail'),
    #path('<str:user_name>/', views.homepage, name='homepage'),
    
]


"""path('add/', views.add_record, name='add_record),
    path('feed/', views.feed, name='feed'),
    path('top/', views.top, name='top'),
    path('friends/', views.friends, name='friends'),""" 