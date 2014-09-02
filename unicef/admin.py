from django.contrib import admin
from django.contrib.admin.sites import NotRegistered

from post.models import Post
from jmbo.admin import ModelBaseAdmin


class PostAdmin(ModelBaseAdmin):
    raw_id_fields = ('owner', )
    inlines = ModelBaseAdmin.inlines
    list_display = (
        'title', 'primary_category', 'publish_on', 'retract_on',
        '_get_absolute_url', 'is_featured', 'created', '_actions',
        '_view_comments'
    )
    ordering = ('-publish_on', '-created')
    list_per_page = 10

    def is_featured(self, obj, *args, **kwargs):
        return obj.categories.filter(slug='featured').exists()
    is_featured.boolean = True

    def _view_comments(self, article):
        return '<a href="/admin/post/%s/%s/moderate/">View (%s)</a>' % (
            article._meta.module_name,
            article.pk, article.comment_count)

    _view_comments.short_description = 'Comments'
    _view_comments.allow_tags = True


try:
    admin.site.unregister(Post)
except NotRegistered:
    pass

admin.site.register(Post, PostAdmin)
