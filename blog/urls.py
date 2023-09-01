from django.urls import path

from .views import home, posts, new_post, list_reviews, create_review, prices

app_name = "blog"

urlpatterns = [
    path("", home, name="home"),
    path("blog/", posts, name="blog"),
    path("new_post/", new_post, name="new_post"),
    path("reviews/", list_reviews, name="list_reviews"),
    path("create_review/", create_review, name="create_review"),
    path("prices/", prices, name="prices"),
]