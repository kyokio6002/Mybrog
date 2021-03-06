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


class Comment(models.Model):
    article = models.ForeignKey(
        'Article',
        on_delete=True,
        related_name='comments')
    author = models.CharField(max_length=50)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return str(self.text)


class Reply(models.Model):
    comment = models.ForeignKey(
        'Comment',
        on_delete=True,
        related_name='replies')
    author = models.CharField(max_length=50)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return str(self.text)
