from django.urls import path

from . import views

app_name = 'server'

urlpatterns = [
    path('api/illuminations/getlast', views.GetLastInfoView.as_view()),
    path('api/illuminations/getalltime', views.GetAllTimeInfoView.as_view()),
    path('api/illuminations/getforweek', views.GetInfoForWeekView.as_view()),
    path('api/illuminations/getforday', views.GetInfoForDayView.as_view()),
    path('api/illuminations/getformonth', views.GetInfoForMonthView.as_view()),
    path('api/illuminations/postinfo', views.PostInfoView.as_view()),

    # path('addtestinfo', views.AddTestInfo, name='addtestinfo'),
    path('', views.index, name='index'),
]
