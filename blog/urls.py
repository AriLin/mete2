from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView
)


from . import views as mete_views

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', mete_views.about, name='blog-about'),
    path('calc/', mete_views.calc, name='def-calc'),
    path('calc_lam/', mete_views.calc_lam, name='def-calc_lam'),
    path('calc_lam/edit/', mete_views.calc_lam_edit, name='def-calc_lam_edit'),
    path('calc_iv/', mete_views.calc_iv, name='def-calc_iv'),
    path('calc_iv/edit/', mete_views.calc_iv_edit, name='def-calc_iv_edit'),
    path('calc_lkv/', mete_views.calc_lkv, name='def-calc_lkv'),
    path('calc_lkv/edit/', mete_views.calc_lkv_edit, name='def-calc_lkv_edit'),
    path('calc_rak/', mete_views.calc_rak, name='def-calc_rak'),
    path('calc_kayt/', mete_views.calc_kayt, name='def-calc_kayt'),
    path('calc_kayt/edit', mete_views.calc_kayt_edit, name='def-calc_kayt_edit'),
    path('calc_yht/', mete_views.calc_yht, name='def-calc_yht'),
    path('calc2/', mete_views.aurinko_data, name='def-calc2'),
    path('calc2/edit/', mete_views.aurinko_data, name='edit-calc2'),
    path('calc3/', mete_views.pumppu_data, name='def-calc3'),
    path('calc3/edit/', mete_views.pumppu_data, name='edit-calc3'),
    path('calc4/', mete_views.valaisin_data, name='def-calc4'),
    path('calc4/edit/', mete_views.valaisin_data, name='edit-calc4'),

 # urls from iot.research.hamk.fi/mete
    path('mete/', PostListView.as_view(), name='blog-home'),
    path('mete/user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('mete/post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('mete/post/new/', PostCreateView.as_view(), name='post-create'),
    path('mete/post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('mete/post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('mete/about/', mete_views.about, name='blog-about'),
    path('mete/calc/', mete_views.calc, name='def-calc'),
    path('mete/calc_lam/', mete_views.calc_lam, name='def-calc_lam'),
    path('mete/calc_lam/edit/', mete_views.calc_lam_edit, name='def-calc_lam_edit'),
    path('mete/calc_iv/', mete_views.calc_iv, name='def-calc_iv'),
    path('mete/calc_iv/edit/', mete_views.calc_iv_edit, name='def-calc_iv_edit'),
    path('mete/calc_lkv/', mete_views.calc_lkv, name='def-calc_lkv'),
    path('mete/calc_lkv/edit/', mete_views.calc_lkv_edit, name='def-calc_lkv_edit'),
    path('mete/calc_rak/', mete_views.calc_rak, name='def-calc_rak'),
    path('mete/calc_kayt/', mete_views.calc_kayt, name='def-calc_kayt'),
    path('mete/calc_kayt/edit', mete_views.calc_kayt_edit, name='def-calc_kayt_edit'),
    path('mete/calc_yht/', mete_views.calc_yht, name='def-calc_yht'),
    path('mete/calc2/', mete_views.aurinko_data, name='def-calc2'),
    path('mete/calc2/edit/', mete_views.aurinko_data, name='edit-calc2'),
    path('mete/calc3/', mete_views.pumppu_data, name='def-calc3'),
    path('mete/calc3/edit/', mete_views.pumppu_data, name='edit-calc3'),
    path('mete/calc4/', mete_views.valaisin_data, name='def-calc4'),
    path('mete/calc4/edit/', mete_views.valaisin_data, name='edit-calc4'),
]