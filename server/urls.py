from django.urls import path

from . import views

urlpatterns = [
    path('api/illuminations/getlast', views.GetLastInfoView.as_view()),
    path('api/illuminations/getalltime', views.GetAllTimeInfoView.as_view()),
    path('api/illuminations/getforweek', views.GetInfoForWeekView.as_view()),
    path('api/illuminations/postinfo', views.PostInfoView.as_view()),
    path('', views.index, name='index'),

]
