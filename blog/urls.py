from . import views
from django.urls import path

urlpatterns = [

    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    patch('like/<slug:slug>', view.PostLike.as_view(), name='post_like')
    
]