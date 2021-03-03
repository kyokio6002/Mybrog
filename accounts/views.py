import logging

from django.conf import settings
from django.contrib import messages
from django.contrib.auth import login as auth_login, logout as auth_logout 
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from .forms import LoginForm, RegisterForm, ProfileForm

# Create your views here.
logger = logging.getLogger(__name__)


class RegisterView(View):
    '''登録用のView'''
    def get(self, request, *args, **kwargs):
        # ログイン済みは記事画面へリダイレクト
        if request.user.is_authenticated:
            return redirect(reverse('article:index'))

        context = {
                'form': RegisterForm(),
        }
        return render(request, 'accounts/register.html', context)

    def post(self, request, *args, **kwargs):
        logger.info('You are in post!!!')

        # リクエストからフォームを作成
        form = RegisterForm(request.POST)
        # バリデーション
        if not form.is_valid():
            # バリデーションNGの場合はアカウント登録画面のテンプレートを再表示
            return render(request, 'acocunts/register.html', {'form': form})

        # 保存する前に一旦取り出す(commit=Falseで保存はしない)
        user = form.save(commit=False)
        # パスワードをハッシュ化
        user.set_password(form.cleaned_data['password'])
        # ユーザーオブジェクトを保存
        user.save()

        # ログイン処理(取得したUserオブジェクトをセッションに保存&Userデータを更新
        auth_login(request, user)

        return redirect(settings.LOGIN_REDIRECT_URL)


# 関数化
register = RegisterView.as_view()


class LoginView(View):
    def get(self, request, *args, **kwargs):
        # ログイン済みは記事画面へリダイレクト
        if request.user.is_authenticated:
            return redirect(reverse('article:index'))

        context = {
            'forms': LoginForm(),
        }

        # ログイン画面用のテンプレートに値がからのフォームをレンダリング
        return render(request, 'accounts/login.html', context)

    def post(self, request, *args, **kwargs):
        # リクエストからフォームを作成
        form = LoginForm(request.POST)
        # バリデーション(ユーザーの認証も)
        if not form.is_valid():
            return render(request, 'accounts/login.html', {'form': form})

        # ユーザーオブジェクトをフォームから取得
        user = form.get_user()

        # ログイン処理(セッションに保存&ユーザーデータを更新)
        auth_login(request, user)
        # ログイン回数をカウント
        user.post_login()
        
        # フラッシュメッセージを表示
        messages.info(request, 'ログインしました')

        # 記事画面にリダイレクト
        return redirect(reverse('article:index'))


# 関数化
login = LoginView.as_view()


class LogoutView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            # ロギング
            logger.info('User(id={}) has logged out.'.format(request.user.id))
            # ログアウト処理
            auth_logout(request)

        # フラッシュメッセージを表示
        messages.info(request, 'ログアウトしました')

        return redirect(reverse('accounts:login'))


logout = LogoutView.as_view()


class ProfileView(View):
    def get(self, request, *args, **kwargs):
        form = ProfileForm(None, instance=request.user)
        context = {
            'form': form,
        }
        return render(request, 'accounts:profile.html', context)

    def post(self, request, *args, **kwargs):
        logger.info('You are in post!!!')

        # フォームを使ってバリデーション
        form = ProfileForm(request.POST, instance=request.user)
        if not form.is_valid():
            return render(request, 'accounts/profile.html', {'form': form})

        # 変更を保存
        form.save()

        # フラッシュメッセージを画面に表示
        messages.info(request, 'プロフィールを更新しました')

        return redirect('/accounts/profile')


# 関数化
profile = ProfileView.as_view()
