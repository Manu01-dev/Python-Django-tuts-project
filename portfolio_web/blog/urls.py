from django.urls import path
from . import views

urlpatterns = [
    path("", views.blog_index, name="blog_index"),
    path("add_post", views.add_post, name="add_post"),
    path("<int:pk>/", views.blog_detail, name="blog_detail"),
    path("<category>/", views.blog_category, name="blog_category"),
    path('delete/<int:pk>',views.delete_post,name='delete_post')
]