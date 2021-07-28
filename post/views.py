from django.views.generic import ListView, DetailView

from post.models import Post
from django.db.models import Q


class HomeView(ListView):
    model = Post
    template_name = 'post/index.html'
    context_object_name = 'posts'
    paginate_by = 1


class PostDetailView(DetailView):
    model = Post
    template_name = 'post/post-detail.html'
    context_object_name = 'post'

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        post = self.object
        post.views = post.views + 1
        post.save()
        return response


class PostByCategory(ListView):
    model = Post
    template_name = 'post/index.html'
    context_object_name = 'posts'

    def get_queryset(self):
        category_slug = self.kwargs.get('slug')
        posts = Post.objects.filter(category__slug=category_slug)
        return posts


class SearchView(ListView):
    model = Post
    template_name = 'post/search.html'
    context_object_name = 'posts'

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get('search')
        if search:
            queryset = queryset.filter(Q(title__icontains=search) | Q(content__icontains=search))
            return queryset 
