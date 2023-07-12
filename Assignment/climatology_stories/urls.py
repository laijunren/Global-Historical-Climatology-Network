from django.urls import path
from climatology_stories import views

urlpatterns = [
    path('', views.index, name='index'),
    path('years/', views.years, name='years'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('climate-data/', views.climate_data, name='climate_data'),
    path('settings/', views.settings, name='settings'),
    path('climate_data/<yearid>/<monthid>/<latid>/', views.climate_data_graph,
         name='climate_data_graph'),
    path('climate_data/<yearid>/', views.year_detail, name='year_detail'),
    path('download/', views.download, name='download'),

]