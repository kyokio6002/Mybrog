from django.urls import path

from . import views

# 名前空間を設定
app_name = 'article'

# 引数(url,処理する関数,reversで逆引きするためのname)
urlpatterns = [

    path('index/', views.index, name='index'),
    path('<int:article_id>/', views.detail, name='detail'),

    path('<int:article_id>/comment/', views.save_comment, name='comment'),
    path('<int:comment_id>/reply/', views.save_reply, name='reply'),
]
