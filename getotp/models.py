import string
from datetime import timedelta
import random
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
import uuid


class User(AbstractUser):
    groups = models.ManyToManyField(Group, verbose_name=_('groups'), blank=True, related_name='getotp_users')
    user_permissions = models.ManyToManyField(Permission, related_name='getotp_user_set')


class Meta:
    verbose_name = _('user')
    verbose_name_plural = _('users')


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_date = models.DateTimeField(null=True)

    @receiver(post_save, sender=User)
    def create_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)


class OtpRequest(models.Model):
    class OtpChannel(models.TextChoices):
        ANDROID = _('android')
        IOS = _('ios')
        WEB = _('web')

    request_id = models.UUIDField(default=uuid.uuid4, editable=False)
    channel = models.CharField(_('channel'), max_length=12, choices=OtpChannel.choices)
    phone = models.CharField(max_length=12)
    password = models.CharField(max_length=14, null=True)
    valid_form = models.DateTimeField(default=timezone.now())
    valid_until = models.DateTimeField(default=timezone.now() + timedelta(seconds=120))
    receipt_id = models.CharField(max_length=255, null=True)

    def generate_password(self):
        self.password = self._random_password()
        self.valid_until = timezone.now() + timedelta(seconds=120)

    def _random_password(self):
        rand = random.SystemRandom()
        digits = rand.choices(string.digits, k=4)
        return ''.join(digits)

    class Meta:
        verbose_name = _('One Time Password')
        verbose_name_plural = _('One Time Passwords')
