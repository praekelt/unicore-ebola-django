from django.core.cache import cache
from django.db.models.signals import post_save
from django.dispatch import receiver
from post.models import Post


@receiver(post_save)
def cache_clearer(instance, *args, **kwargs):
    """
    Clears the entire cache whenever a content object is changed/saved.
    """
    if isinstance(instance, Post):
        cache.clear()
