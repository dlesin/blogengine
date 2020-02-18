from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import ListView, DetailView
from .models import *
from .forms import *
from django.db.models import Q
from django.core.mail import send_mail


class HomeView(ListView):
    model = Post
    queryset = Post.objects.order_by('-timestamp')
    template_name = 'home.html'
    paginate_by = 10
    context_object_name = 'posts_list'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        search_query = self.request.GET.get('search', '')
        context['categories_list'] = Category.objects.all()
        context['tops_list'] = Post.objects.order_by('-view_count')[:10]
        if search_query:
            context['posts_list'] = Post.objects.filter(
                Q(title__icontains=search_query) | Q(overview__icontains=search_query) | Q(
                    content__icontains=search_query))
        return context


class CategoryDetailView(ListView):
    model = Category
    template_name = 'category.html'

    def get_context_data(self, **kwargs):
        context = super(CategoryDetailView, self).get_context_data(**kwargs)
        category = get_object_or_404(Category, slug=self.kwargs.get('slug'))
        context['categories_list'] = Category.objects.all()
        context['tops_list'] = Post.objects.order_by('-view_count')[:5]
        context['posts_list'] = Post.objects.filter(
            categories=category).order_by('-timestamp')
        return context


class PostDetailView(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        post = get_object_or_404(Post, slug=self.kwargs.get('slug'))
        comment_count = Comment.objects.filter(post=post).count()
        context['comment_count'] = comment_count
        context['comments_list'] = Comment.objects.filter(post=post).order_by('-timestamp')
        context['categories_list'] = Category.objects.all()
        context['tops_list'] = Post.objects.order_by('-view_count')[:5]
        context['form'] = CommentForm
        post.view_count += 1
        if comment_count == post.comment_count:
            post.save(update_fields=['view_count'])
        else:
            post.comment_count = comment_count
            print(post.comment_count)
            post.save(update_fields=['view_count', 'comment_count'])
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        # context = self.get_context_data(**kwargs)
        post = get_object_or_404(Post, slug=self.kwargs.get('slug'))
        form = CommentForm(request.POST or None)
        comment = Comment()
        if form.is_valid():
            if request.user.is_authenticated:
                comment.user = request.user
            else:
                comment.guest_user = form.cleaned_data['user']
            comment.content = form.cleaned_data['content']
            comment.post = post
            comment.save()
            return redirect('post_detail_url', slug=self.kwargs.get('slug'), permanent=True)


class ContactView(View):
    def get(self, request, *args, **kwargs):
        form = ContactForm(self.request.POST or None)
        context = {
            'form': form,
        }
        return render(request, 'contacts.html', context=context)

    def post(self, request, *args, **kwargs):
        form = ContactForm(self.request.POST or None)
        if form.is_valid():
            message = Contact()
            message.guest_user = form.cleaned_data['user']
            message.content = form.cleaned_data['content']
            message.save()
            # send_mail('Сообщение с Сайта', message.content, 't3stb0x@yandex.ru', ['T0n0P@mail.ru'], fail_silently=False)
            return redirect('home_view_url', permanent=True)

