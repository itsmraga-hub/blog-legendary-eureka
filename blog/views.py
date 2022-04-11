from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import BlogPost, Tag
from .forms import PostForm, UpdateForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect


# Create your views here.
class HomeView(ListView):
    model = BlogPost
    template_name = 'home.html'
    ordering = ['-publication_date']

    def get_context_data(self, *args, **kwargs):
        tag_menu = Tag.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["tag_menu"] = tag_menu
        return context


class PostDetailView(DetailView):
    model = BlogPost
    template_name = "blog_detail.html"

    def get_context_data(self, *args, **kwargs):
        tag_menu = Tag.objects.all()
        context = super(DetailView, self).get_context_data(*args, **kwargs)

        blogpost_likes = get_object_or_404(BlogPost, id=self.kwargs['pk'])
        total_likes = blogpost_likes.totalLikes()

        liked = False
        if blogpost_likes.likes.filter(id=self.request.user.id).exists():
            liked = True

        context["tag_menu"] = tag_menu
        context["total_likes"] = total_likes
        context["liked"] = liked
        return context


class AddPostView(CreateView):
    model = BlogPost
    form_class = PostForm
    template_name = "post.html"
    # fields = '__all__'
    # fields = ('title', 'text', 'author')


def LikeView(request, pk):
    blogpost = get_object_or_404(BlogPost, id=request.POST.get('blogpost_id'))
    liked = False
    if blogpost.likes.filter(id=request.user.id).exists():
        blogpost.likes.remove(request.user)
        liked = False
    else:
        blogpost.likes.add(request.user)
        liked = True

    return HttpResponseRedirect(reverse('blog-detail', args=[str(pk)]))


class UpdatePostView(UpdateView):
    model = BlogPost
    form_class = UpdateForm
    template_name = "update_post.html"
    # fields = ("title", "title_tag", "text")


class DeletePostView(DeleteView):
    model = BlogPost
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')


class AddTagView(CreateView):
    model = Tag
    fields = "__all__"
    template_name = 'add_tag.html'


class UpdateTagView(UpdateView):
    model = Tag
    fields = "__all__"
    template_name = 'edit_tag.html'


def TagView(request, tags):
    tag_posts = BlogPost.objects.filter(tag=tags.replace('-', ' '))
    return render(request, 'tags.html',
                  {'tags': tags.title().replace('-', ' '), 'tag_posts': tag_posts})


def TagListView(request):
    tag_menu_list = Tag.objects.all()
    return render(request, 'tags_list.html',
                  {'tag_menu_list': tag_menu_list})
