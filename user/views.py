from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from user.forms import UserRegisterForm, UserChangeForm, UserProfileForm
from user.models import User


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'user/register.html'
    success_url = reverse_lazy('user:login')


class ProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('user:profile')

    def get_object(self, queryset=None):
        return self.request.user

