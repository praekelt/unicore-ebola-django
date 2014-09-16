from category.models import Category

from django.conf import settings
from django.shortcuts import render

from jmbo.views import CategoryObjectList


def category_sort_key(category):
    first, dot, remainder = category.title.partition('.')
    if first.isdigit():
        return int(first)
    return category.title


def home(request):

    # NOTE: having to do this because category.Category doesn't have a
    #       notion of how to order stuff. Which is madness.
    categories = list(Category.objects.all())
    if settings.PATCH_CATEGORY_ORDERING:
        categories = sorted(categories, key=category_sort_key)

    return render(
        request,
        'unicef/home.html',
        {
            'categories': categories,
        })


class EbolaCategoryObjectList(CategoryObjectList):

    def get_queryset(self, *args, **kwargs):
        qs = super(EbolaCategoryObjectList, self).get_queryset(*args, **kwargs)
        return qs.order_by('-publish_on', '-created')

ebola_category_object_list = EbolaCategoryObjectList()
