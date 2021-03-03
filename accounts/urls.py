from django.urls import path

from . import views

# 名前空間を設定
app_name = 'accounts'

# 引数(url,処理する関数,reversで逆引きするためのname)
urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('profile/', views.profile, name='profile'),
]
