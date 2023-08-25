from django.shortcuts import render, get_object_or_404, redirect
from django.utils.text import slugify
from django.views import View

from catalog.models import Product
from .models import BlogPost
from .forms import BlogPostForm


class HomeView(View):
    @staticmethod
    def get(request):
        product_list = Product.objects.all()
        blog_posts = BlogPost.objects.filter(published=True)  # фильтруем только опубликованные статьи
        context = {
            'object_list': product_list,
            'blog_posts': blog_posts
        }
        return render(request, 'catalog/home.html', context)


class ContactView(View):
    @staticmethod
    def get(request):
        return render(request, 'catalog/contact.html')


class ProductView(View):
    @staticmethod
    def get_product_info(product_id):
        product = Product.objects.get(id=product_id)
        return product

    @staticmethod
    def get(request, product_id):
        product_info = ProductView.get_product_info(product_id)
        return render(request, 'product.html', {'product_info': product_info})


class BlogPostCreateView(View):
    @staticmethod
    def get(request):
        form = BlogPostForm()
        return render(request, 'blog_post_create.html', {'form': form})

    @staticmethod
    def post(request):
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            blog_post = form.save(commit=False)
            blog_post.slug = slugify(blog_post.title)  # формируем slug name из заголовка
            blog_post.save()
            return redirect('blog_detail', pk=blog_post.pk)
        return render(request, 'blog_post_create.html', {'form': form})


class BlogPostDetailView(View):
    @staticmethod
    def get(request, pk):
        blog_post = get_object_or_404(BlogPost, pk=pk)
        blog_post.views += 1  # увеличиваем счетчик просмотров на 1
        blog_post.save()  # сохраняем изменения
        return render(request, 'blog_post_detail.html', {'blog_post': blog_post})


class BlogPostUpdateView(View):
    @staticmethod
    def get(request, pk):
        blog_post = get_object_or_404(BlogPost, pk=pk)
        form = BlogPostForm(instance=blog_post)
        return render(request, 'blog_post_update.html', {'form': form})

    @staticmethod
    def post(request, pk):
        blog_post = get_object_or_404(BlogPost, pk=pk)
        form = BlogPostForm(request.POST, request.FILES, instance=blog_post)
        if form.is_valid():
            form.save()
            return redirect('blog_detail', pk=pk)
        return render(request, 'blog_post_update.html', {'form': form})


class BlogPostDeleteView(View):
    @staticmethod
    def get(request, pk):
        blog_post = get_object_or_404(BlogPost, pk=pk)
        return render(request, 'blog_post_delete.html', {'blog_post': blog_post})

    @staticmethod
    def post(pk):
        blog_post = get_object_or_404(BlogPost, pk=pk)
        blog_post.delete()
        return redirect('blog_list')
