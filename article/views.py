from django.shortcuts import render, reverse, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import View, ListView
from django.views.generic.edit import CreateView
from django.db.models import Q

from .models import Article, Comment
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
        }

        return render(request, 'article/detail.html', context)


detail = DetailView.as_view()
