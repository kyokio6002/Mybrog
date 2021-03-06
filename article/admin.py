from django.contrib import admin

# Register your models here.
from .models import Article, Comment, Reply

admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(Reply)

