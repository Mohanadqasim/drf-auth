from django.urls import path
from .views import MoviesList,MoviesDetail,PostsDetail,PostsList
# from .views import GameList,GameDetail

urlpatterns=[
    path('',MoviesList.as_view(),name='movies_list'),
    path('/<int:pk>/',MoviesDetail.as_view(),name='movie_detail'),
    path('/post/',PostsList.as_view(),name='posts_list'),
    path('/post/<int:pk>/',PostsDetail.as_view(),name='post_detail')

]