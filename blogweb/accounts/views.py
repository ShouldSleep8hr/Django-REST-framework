
from django.views import generic
from django.urls import reverse_lazy

from .forms import CustomUserCreationForm
from .models import User

    
class LoginView(generic.TemplateView):
    template_name = 'registration/login.html'

class UserCreateView(generic.TemplateView):
    template_name = 'user_create.html'


class UserUpdateView(generic.TemplateView):
    template_name = 'user_update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_id = self.kwargs.get('pk')
        user = User.objects.get(pk=user_id)  # Fetch the user object from the database
        
        # Pass the user ID, username, and password to the template context
        context['user_id'] = user_id
        context['user_username'] = user.username
        context['user_email'] = user.email
        context['user_password'] = user.password  # Note: This should not be the raw password; consider passing a placeholder
        return context



class UserListView(generic.TemplateView):
    template_name = 'user_list.html'



class UserDetailView(generic.TemplateView):
    template_name = 'user_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Pass the user ID to the template context
        context['user_id'] = self.kwargs.get('pk')
        return context



class UserDeleteView(generic.TemplateView):
    template_name = 'user_delete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Pass the user ID to the template context
        context['user_id'] = self.kwargs.get('pk')
        return context
