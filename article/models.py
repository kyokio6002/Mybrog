from django.db import models
# Create your models here.
import markdown as md
from mdeditor.fields import MDTextField


class Article(models.Model):
    '''記事クラス'''
    class Meta(object):
        db_table = 'article'

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    contents = MDTextField()
    create_at = models.DateTimeField(auto_now_add=True)
    is_public = models.BooleanField(default=True)

    def __str__(self):
        return str(self.id) + ")" + str(self.title)

    def markdown(self):
        '''markdown形式に変換する'''
        return md.markdown(self.contents, extensions=[
            'markdown.extensions.fenced_code',
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            'markdown.extensions.toc',
            'markdown.extensions.tables'])

