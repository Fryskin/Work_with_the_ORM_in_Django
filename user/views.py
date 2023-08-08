import random

from django.conf import settings
from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView

from user.forms import UserRegisterForm, UserChangeForm, UserProfileForm
from user.models import User


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'user/register.html'
    success_url = reverse_lazy('user:login')

    def form_valid(self, form):
        new_user = form.save()
        send_mail(
            subject='Here we go.',
            message='Now you are registered, dear User.',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[new_user.email]

        )

        return super().form_valid(form)


class ProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('user:profile')

    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form):
        new_user = form.save()
        send_mail(
            subject='Here we go.',
            message='You are successfully changed your email, dear User.',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[new_user.email]

        )

        return super().form_valid(form)


def generate_new_password(request):
    chars = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x',
             'c', 'v', 'b', 'n', 'm', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H',
             'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    new_password = ''.join([random.choice(chars) for _ in range(10)])
    send_mail(
        subject='The new password.',
        message=f'Your new password is "{new_password}"',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[request.user.email]

    )
    request.user.set_password(new_password)
    request.user.save()
    return redirect(reverse('main:index'))