from .views import CreatePost, EditPost, DeletePost, AdminPostDetail
from django.urls import path


app_name = 'journal'

urlpatterns = [
    # Post Admin URLs
    path('create/', CreatePost.as_view(), name='createpost'),
    path('edit/postdetail/<int:pk>/', AdminPostDetail.as_view(), name='admindetailpost'),
    path('edit/<int:pk>/', EditPost.as_view(), name='editpost'),
    path('delete/<int:pk>/', DeletePost.as_view(), name='deletepost'),
]