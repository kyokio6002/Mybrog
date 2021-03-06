'''
コメント、返信用のフォームを作成
'''

from django.forms import ModelForm, TextInput, Textarea

from .models import Comment, Reply


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'text')
        widgets = {
            'author': TextInput(attrs={'placeholder': 'name'}),
            'text': Textarea(attrs={'placeholder': 'コメント内容'}),
        }

        # これは何に使うの？
        labels = {
            'author': '',
            'text': '',
        }


class ReplyForm(ModelForm):
    class Meta:
        model = Reply
        fields = ('author', 'text')
        widgets = {
            'author': TextInput(attrs={'placeholder': 'name'}),
            'text': Textarea(attrs={'placeholder': '返信内容'}),
        }

        # これは何に使うの？
        labels = {
            'author': '',
            'text': '',
        }
