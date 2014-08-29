from post.models import Post
from category.models import Category


class UnicefPost(Post):
    class Meta:
        app_label = 'post'
        proxy = True

    def save(self, *args, **kwargs):
        if not self.primary_category:
            self.primary_category = Category.objects.get(
                slug=self.primary_category_slug)
        super(UnicefPost, self).save(*args, **kwargs)


class TheFactsPost(UnicefPost):
    primary_category_slug = 'the-facts'


class TreatmentPost(UnicefPost):
    primary_category_slug = 'treatment'


class SafeBurialPracticesPost(UnicefPost):
    primary_category_slug = 'safe-burial-practices'
