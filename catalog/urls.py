from django.urls import path

from catalog.views import HomeView, ContactView, ProductView
from .views import BlogPostCreateView, BlogPostDetailView, BlogPostUpdateView, BlogPostDeleteView, BlogListView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('product/<int:product_id>/', ProductView.as_view(), name='product'),
    path('blog/create/', BlogPostCreateView.as_view(), name='blog_create'),
    path('blog/<int:pk>/', BlogPostDetailView.as_view(), name='blog_detail'),
    path('blog/<int:pk>/update/', BlogPostUpdateView.as_view(), name='blog_update'),
    path('blog/<int:pk>/delete/', BlogPostDeleteView.as_view(), name='blog_delete'),
    path('blog/', BlogListView.as_view(), name='blog_list'),
]
