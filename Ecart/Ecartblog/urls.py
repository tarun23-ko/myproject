from django.urls import path
from .import views
urlpatterns = [
    path("",views.blogview,name="bloghome"),
    path("blogpost/<int:id>", views.blogpost, name="blogpost")
]

