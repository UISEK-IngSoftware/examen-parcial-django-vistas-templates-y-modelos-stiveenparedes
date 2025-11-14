from django.urls import path
from . import views

app_name = "movies"

urlpatterns = [
    path("", views.index, name="index"),
    path("add/", views.add_movie, name="add_movie"),
    path("edit/<int:movie_id>/", views.edit_movie, name="edit_movie"),
    path("delete/<int:movie_id>/", views.delete_movie, name="delete_movie"),
    path("<int:movie_id>/", views.detail, name="detail"),
]
