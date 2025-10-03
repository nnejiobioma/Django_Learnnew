from django.urls import path
from . import views #Imported views and view is in the same directory as url that is why (.) is used if not you navigate to the part where the file is located


urlpatterns = [
    path('', views.posts_list), #created the home page part
    path('about', views.posts_about),
]
