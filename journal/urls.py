from .views import CreatePost, EditPost, AdminPostDetail, DeletePost
from django.urls import path


app_name = 'journal'

urlpatterns = [
    # Post Admin URLs
    path('admin/create/', CreatePost.as_view(), name='createpost'),
    # path('admin/edit/postdetail/<int:pk>/', AdminPostDetail.as_view(), name='admindetailpost'),
    path('admin/edit/<int:pk>/', EditPost.as_view(), name='editpost'),
    path('admin/delete/<int:pk>/', DeletePost.as_view(), name='deletepost'),
]