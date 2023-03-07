from django.db.models.signals import post_save
from django.dispatch import receiver
from django.apps import apps
from django.contrib.auth import get_user_model
from django.core.signals import setting_changed
from django.test import override_settings
from django.conf import settings
from rest_framework.authtoken.models import Token

from .models import User, Profile

# @override_settings(
#     AUTH_USER_MODEL = 'User.User'
# )

# @receiver(setting_changed)
# def user_model_swapped(**kwargs):
#     if kwargs['setting'] == 'AUTH_USER_MODEL':
#         apps.clear_cache()
#         from .models import User
#         User = get_user_model()


## Signal to Create Profile for each new User
@receiver(post_save, sender=User)
def create_profile_signal(sender, instance, created, **kwargs):
    if created:
        Token.objects.create(user=instance)
        Profile.objects.create(user=instance)
    instance.profile.save()
