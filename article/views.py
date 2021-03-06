from django.shortcuts import render, reverse, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import View, ListView
from django.views.generic.edit import CreateView
from django.db.models import Q

from .models import Article, Comment
from .forms import CommentForm, ReplyForm
# Create your views here.


class IndexView(LoginRequiredMixin, ListView):
    template_name = 'article/index.html'
    context_object_name = 'articles'
    paginate_by = 4
    queryset = Article.objects.all().filter(is_public=True)


index = IndexView.as_view()

# class IndexView(LoginRequiredMixin, View):
#     def get(self, request, *args, **kwargs):
#         # queryset = Article.objects.all.()
#         queryset = Article.objects.all().filter(is_public=True)
# 
#         keyword = request.GET.get('keyword')
#         if keyword:
#             queryset = queryset.filter(
#                 Q(title__icontains=keyword) | Q(description__icontains=keyword)
#             )
#         context = {
#             'keyword': keyword,
#             'articles': queryset,
#         }
#         return render(request, 'article/index.html', context)
# 
# 
# index = IndexView.as_view()


class DetailView(LoginRequiredMixin, View):
    def get(self, request, article_id, *args, ** kwargs):
        article = Article.objects.get(pk=article_id)
        context = {
            'article': article,
            'commnet_form': CommentForm(),
            'reply_form': ReplyForm()
        }

        return render(request, 'article/detail.html', context)


detail = DetailView.as_view()


class SaveComment(View):
    def post(self, request, article_id, *args, **kwargs):
        form = CommentForm(request.POST)
        article = Article.objects.get(pk=article_id)
        comment = form.save(commit=False)
        comment.article = article
        comment.save()
        article_id = article_id

        return redirect('article:detail', article_id=article_id)


save_comment = SaveComment.as_view()


class SaveReply(View):
    def post(self, request, comment_id, *args, **kwargs):
        form = ReplyForm(request.POST)
        comment = Comment.objects.get(pk=comment_id)
        reply = form.save(commit=False)
        reply.comment = comment
        reply.save()
        article_id = comment.article.id

        return redirect('article:detail', article_id=article_id)


save_reply = SaveReply.as_view()



