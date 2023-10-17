from django.conf import settings
from django.core.mail import send_mail
from django.urls import reverse


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
