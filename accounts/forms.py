'''
formはバリデータ(バリデーションを行う)
今回はCustomUserのバリデーションを行う
'''
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UsernameField
from django.core.exceptions import ObjectDoesNotExist
from .models import CustomUser


class RegisterForm(forms.ModelForm):
    '''ユーザー登録画面用のフォーム'''

    class Meta:
        '''詳細情報'''
        # accounts/models.pyで作ったモデルを使用
        model = CustomUser
        # 利用するモデルのフィールドを指定
        fields = ('username', 'email', 'password')
        # 
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'ユーザー名'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'パス位ワード'}),
        }

    # 確認用パスワードのfieldを追加
    password2 = forms.CharField(
        label='確認用パスワード',
        required=True,
        strip=False,
        widget=forms.PasswordInput(attrs={'placeholder': '確認用パスワード'}),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # emailフィールドを書き換え
        self.fields['email'].required = True
        self.fields['email'].widget.attrs = {'placeholder': 'メールアドレス'}

    # 各フィールドのバリデーション
    def claem_username(self):
        value = self.cleaned_data['username']
        # 2文字以下を弾く
        if len(value) < 3:
            raise forms.ValidationError(
                '%(min_length)s文字以上で入力してください', params={'min_length', 3})
        return value

    def clean_email(self):
        value = self.cleaned_data['email']
        return value

    def clean_password(self):
        value = self.cleaned_data['password']
        return value

    # 全体のバリデーション
    def clean(self):
        password = self.cleaned_data['password']
        password2 = self.cleaned_data['password2']
        if password != password2:
            raise forms.ValidationError('パスワードと確認用パスワードが合致しません')
        # ユニーク制約を課す時はsuperのcleanを予備だす(_validae_unique=True)になる
        super().clean()


class LoginForm(forms.Form):
    '''ログイン画面用のフォーム'''

    username = UsernameField(
        label='ユーザー名',
        max_length=255,
        widget=forms.TextInput(attrs={'placeholder': 'ユーザー名',
                                      'autofocus': True}))

    password = forms.CharField(
        label='パスワード',
        strip=False,
        widget=forms.PasswordInput(attrs={'placeholder': 'パスワード'},
                                   render_value=True))

    def __init__(self, *args, ** kwargs):
        super.__init__(*args, **kwargs)
        self.user_cache = None
    
    def clean_password(self):
        value = self.cleaned_data['password']
        return value

    def clean_username(self):
        value = self.cleaned_data['username']
        return value

    def clean(self):
        # .getで取ってくるとなかった場合に空を返す、[]でなかった場合はエラー
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        try:
            user = get_user_model().objects.get(username=username)
        except ObjectDoesNotExist:
            raise forms.ValidationError('正しいユーザー名を入れてください')

        # パスワードはハッシュ化されて保存されているので平文での検索はできない
        if not user.check_password(password):
            raise forms.ValidationError('正しいユーザー名とパスワードを入力してください')

        # 取得したユーザーオブジェクトを使いまわせるように内部に保存しておく
        self.user_cache = user

    def get_user(self):
        return self.user_cache


class ProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'last_name', 'first_name')

    def __init__(self, *aargs, **kwarg):
        self.fields['username'].widget.attrs = {'placeholder': 'ユーザー名'}
        self.fields['email'].required = True
        self.fields['email'].widget.attrs = {'placeholder': 'メールアドレス'}
        self.fields['lasr_name'].widget.attrs = {'placeholder': '苗字'}
        self.fields['first_name'].widget.attrs = {'placeholder': '名前'}

    def clean_username(self):
        value = self.cleaned_data['username']
        return value

    def clean_email(self):
        value = self.cleaned_data['email']
        return value

