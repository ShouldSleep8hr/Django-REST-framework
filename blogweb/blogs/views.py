from django.shortcuts import get_object_or_404, redirect, render

from django.views import generic
from django.urls import reverse_lazy

from .models import Blog, User, Tag, Comment

class HomeView(generic.TemplateView):
    template_name = 'home.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('index')
        return super().dispatch(request, *args, **kwargs)

class IndexView(generic.TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_id'] = self.request.user.id
        context['user_username'] = self.request.user.username
        return context



class BlogDetailView(generic.TemplateView):
    template_name = "blogs/detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['blog_id'] = self.kwargs['pk']  # Pass the user ID to the context
        return context
    
class BlogCreateView(generic.TemplateView):
    template_name = "blogs/create.html"

class BlogUpdateView(generic.TemplateView):
    template_name = "blogs/update.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        blog_id = self.kwargs.get('pk')
        blog = Blog.objects.get(pk=blog_id)
        
        context['blog_id'] = blog_id
        context['blog_title'] = blog.title_text
        context['blog_content'] = blog.content_text
        return context
    

class CommentUpdateView(generic.TemplateView):
    template_name = "comment_update.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        blog_id = self.kwargs.get('blog_id')
        comment_id = self.kwargs.get('pk')
        comment = Comment.objects.get(pk=comment_id)
        
        context['blog_id'] = blog_id
        context['comment_text'] = comment.text
        context['comment_id'] = comment_id
        context['user_username'] = comment.user.username
        return context

# def blog_detail(request, pk):
#     # Pass the blog ID to the template context
#     context = {'blog_id': pk}
#     return render(request, "blogs/detail.html", context)

# class DetailView(generic.DetailView):
#     model = Blog
#     template_name = "blogs/detail.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         blog = self.get_object()
#         comments = Comment.objects.filter(blog=blog)
#         context['comment_list'] = comments
#         return context

# class CommentCreateView(generic.TemplateView):
#     template_name = "blogs/create.html"    

# class CommentCreateView(generic.CreateView):
#     model = Comment
#     template_name = "blogs/detail.html"
#     fields = ['text']

#     def get_success_url(self):
#         # Redirect back to the detail view of the blog
#         return reverse_lazy('blogs:detail', kwargs={'user_id': self.kwargs['user_id'], 'pk': self.kwargs['pk']})

#     def form_valid(self, form):
#         form.instance.user_id = self.kwargs['user_id']
#         form.instance.blog_id = self.kwargs['pk']
#         return super().form_valid(form)
    
# class CommentUpdateView(generic.UpdateView):
#     model = Comment
#     template_name = "blogs/detail.html"
#     fields = ['text']

#     def get_success_url(self):
#         # Redirect back to the detail view of the blog
#         return reverse_lazy('blogs:detail', kwargs={'user_id': self.kwargs['user_id'], 'pk': self.kwargs['blog_id']})

# class CommentDeleteView(generic.DeleteView):
#     model = Comment
#     template_name = "blogs/detail.html"

#     def get_success_url(self):
#         return reverse_lazy('blogs:detail', kwargs={'user_id': self.kwargs['user_id'],'pk': self.kwargs['blog_id']})
    

# class BlogCreateView(generic.CreateView):
#     model = Blog
#     #form_class = BlogForm
#     template_name = "blogs/create.html"
#     fields = ['title_text', 'content_text', 'tag']

#     def get_success_url(self):
#         user_id = self.kwargs['user_id']  # Retrieve the user_id from the URL parameters
#         return reverse_lazy('blogs:index', kwargs={'user_id': user_id})

#     def form_valid(self, form):
#         form.instance.user_id = self.kwargs['user_id']  # Set the user_id from the URL parameter
#         return super().form_valid(form)
    
# class AuthorUpdateView(generic.UpdateView):
#     model = Blog
#     fields = ['title_text', 'content_text', 'tag']
#     template_name = "blogs/create.html"

#     def get_success_url(self):
#         user_id = self.kwargs['user_id']  # Retrieve the user_id from the URL parameters
#         pk = self.kwargs['pk']
#         return reverse_lazy('blogs:detail', kwargs={'user_id': user_id, 'pk': pk})

# class AuthorDeleteView(generic.DeleteView):
#     model = Blog
#     template_name = "blogs/delete.html"

#     def get_success_url(self):
#         user_id = self.kwargs['user_id']  # Retrieve the user_id from the URL parameters
#         return reverse_lazy('blogs:index', kwargs={'user_id': user_id})