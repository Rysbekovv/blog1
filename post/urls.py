from django.urls import path, include
from post import views


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('post/search/', views.SearchView.as_view(), name='post_search'), 
    path('post/<slug:slug>/', views.PostDetailView.as_view(), name='post_detail'),
    path('post/category/<slug:slug>/', views.PostByCategory.as_view(), name='posts_by_category'),
    path('api/', include('post.api.urls')),
]