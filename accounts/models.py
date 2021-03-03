from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class CustomUser(AbstractUser):
    '''拡張ユーザーモデル'''

    class Meta(object):
        # table名を定義
        db_table = 'custom_user'

    # login回数を記録する
    login_count = models.IntegerField(verbose_name='ログイン回数', default=0)

    def post_login(self):
        '''ログイン回数を増やす'''
        self.login_count += 1
        # Absutruct.save()でsaveを実行
        self.save()
