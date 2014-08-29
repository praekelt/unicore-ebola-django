from django.core.cache import cache
from django.db.models.signals import post_save
from django.dispatch import receiver
from post.models import Post
from category.models import Category


class TheFactsPost(Post):
    class Meta:
        app_label = 'post'
        proxy = True

    primary_category_slug = 'the-facts'

    def save(self, *args, **kwargs):
        if not self.primary_category:
            self.primary_category = Category.objects.get(
                slug=self.primary_category_slug)
        super(TheFactsPost, self).save(*args, **kwargs)


class TreatmentPost(Post):
    class Meta:
        app_label = 'post'
        proxy = True

    primary_category_slug = 'treatment'

    def save(self, *args, **kwargs):
        if not self.primary_category:
            self.primary_category = Category.objects.get(
                slug=self.primary_category_slug)
        super(TreatmentPost, self).save(*args, **kwargs)


class SafeBurialPracticesPost(Post):
    class Meta:
        app_label = 'post'
        proxy = True

    primary_category_slug = 'safe-burial-practices'

    def save(self, *args, **kwargs):
        if not self.primary_category:
            self.primary_category = Category.objects.get(
                slug=self.primary_category_slug)
        super(SafeBurialPracticesPost, self).save(*args, **kwargs)


@receiver(post_save)
def cache_clearer(instance, *args, **kwargs):
    """
    Clears the entire cache whenever a content object is changed/saved.
    """
    if isinstance(instance, Post):
        cache.clear()
