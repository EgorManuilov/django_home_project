import random

from django.core.mail import send_mail
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView
from config import settings
from users.forms import UserRegisterForm, UserProfileForm
from users.models import User


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        new_user = form.save()
        verification_key = new_user.verification_key
        verification_url = self.request.build_absolute_uri(reverse("users:verify_email",
                                                                   kwargs={"key": verification_key}))
        send_mail(
            subject='Регистрация',
            message=verification_url,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[new_user.email]
        )
        return super().form_valid(form)


def verify_email(request, key):
    user = get_object_or_404(User, verification_key=key)
    user.is_active = True
    user.verification_key = ''
    user.save()
    return redirect('users:login')


class ProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user


def generate_new_password(request):
    new_password = ''.join(str(random.randint(0, 9)) for _ in range(6))
    send_mail(
        subject='Изменение пароля',
        message=f'Ваш новый пароль {new_password}',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[request.user.email]
    )
    request.user.set_password(new_password)
    request.user.save()
    return redirect(reverse_lazy('users:login'))
