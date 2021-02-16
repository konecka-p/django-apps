from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

app_name = "blog"

urlpatterns = [
    path("posts/", views.post_list, name="post_list"),
    path(
        "<slug:slug>/<int:id>/",
        views.post_detail,
        name="post_detail",
    ),
    path("<int:post_id>/share/", views.post_share, name="post_share"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("register/", views.register, name="register"),
]