from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from pytils.translit import slugify

from blog.models import Blog


class BlogCreateView(CreateView):
    model = Blog
    fields = ["title", "content", "preview"]
    success_url = reverse_lazy("blog:list")

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.title)
            new_mat.save()

        return super().form_valid(form)


class BlogListView(ListView):
    model = Blog
    extra_context = {'title': 'Blogs'}

    def get_queryset(self, *args, **kwargs):
        """Выводить только те, у которых положительный признак публикации"""
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ["title", "content", "preview", "is_published"]

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.title)
            new_mat.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blog:view', args=[self.kwargs.get('pk')])


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy("blog:list")


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        """  Увеличивает количество просмотров """

        self.object = super().get_object(queryset)
        self.object.count_of_views += 1
        self.object.save(update_fields=['count_of_views'])
        return self.object




