from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import redirect
from django.utils.text import slugify

from catalog.models import Product
from .models import BlogPost
from .forms import BlogPostForm


class HomeView(ListView):
    model = Product
    template_name = 'catalog/home.html'
    context_object_name = 'object_list'

    def get_queryset(self):
        return super().get_queryset()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['blog_posts'] = BlogPost.objects.filter(published=True)
        return context


class ContactView(ListView):
    template_name = 'catalog/contact.html'


class ProductView(DetailView):
    model = Product
    template_name = 'catalog/product.html'
    context_object_name = 'product_info'


class BlogPostCreateView(CreateView):
    model = BlogPost
    form_class = BlogPostForm
    template_name = 'catalog/blog_create.html'

    def form_valid(self, form):
        blog_post = form.save(commit=False)
        blog_post.slug = slugify(blog_post.title)
        blog_post.save()
        return redirect('blog_detail', pk=blog_post.pk)


class BlogPostDetailView(DetailView):
    model = BlogPost
    template_name = 'catalog/blog_post_detail.html'
    context_object_name = 'blog_post'

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset=queryset)
        self.object.views += 1
        self.object.save()
        return self.object


class BlogPostUpdateView(UpdateView):
    model = BlogPost
    form_class = BlogPostForm
    template_name = 'catalog/blog_update.html'
    context_object_name = 'blog_post'

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blog_detail', kwargs={'pk': self.object.pk})


class BlogPostDeleteView(DeleteView):
    model = BlogPost
    template_name = 'catalog/blog_delete.html'
    context_object_name = 'blog_post'

    def get_success_url(self):
        return reverse('blog_list')


class BlogListView(ListView):
    model = BlogPost
    template_name = 'catalog/blog.html'
    context_object_name = 'blog_posts'

    def get_queryset(self):
        return super().get_queryset().filter(published=True)
