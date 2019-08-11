from django.urls import path
from django.conf.urls import url

from .import views

app_name = 'music'

urlpatterns = [


     path('',views.IndexView.as_view(),name= 'index'),
      path('visitor/',views.VisitorView.as_view(),name= 'base-visitor'),
     path('<int:pk>',views.DetailView.as_view(),name='detail'),
    path('register/',views.UserFormView.as_view(),name='register'),
    path('logout/',views.LogoutView.as_view(),name='logout'),
    path('login/',views.LoginView.as_view(),name='login'),
    url('create_album/',views.create_album,name='create_album'),
     path('<int:pk>',views.AlbumUpdate.as_view(),name='album-update'),
     path('favorite/<int:pk>',views.AlbumUpdate.as_view(),name='album-favorite'),
     path('delete/<int:pk>',views.AlbumDelete.as_view(),name='album-delete'),
      path('add/song/', views.SongCreate.as_view(), name='create-song'),
      path('delete/song/<int:pk>',views.SongDelete.as_view(),name='delete-song'),
      path('',views.SongUpdate.as_view(),name='fav_song'),
      path('songs/<filter_by>',views.songs,name='songs'),
]
