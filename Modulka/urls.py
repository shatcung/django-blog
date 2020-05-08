from django.urls import path,re_path
from . import views
from django.conf.urls import url
from .views import ArticleView,CommentView,CommDetailAp,Get_update_comm

app_name = "Modulka"




urlpatterns = [
    
    path('article/<int:pk>/', views.PostDetailAp.as_view()),
    path('article/', ArticleView.as_view()),
    path('article/comments',CommentView.as_view()),
   
    path('article/comments/<int:pk>', CommDetailAp.as_view()),
   
    path('', views.post_list, name='post_list'),
 
    
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',
         views.post_detail,
         name='post_detail'),
    url(r'^tag/(?P<slug>)/$',views.post_list, name='post_list_by_tag'),
    path('tag/<slug:tag_slug>/',
         views.post_list, name='post_list_by_tag'),
    
]
    

