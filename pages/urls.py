from django.urls import path
from pages import views 
from pages import urls


urlpatterns = [
		path("", views.HomePageView.as_view(), name ="home"),
		path("about/", views.AboutPageView.as_view(), name="about"),
]