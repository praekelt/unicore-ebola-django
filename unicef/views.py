from category.models import Category
from django.shortcuts import render
from jmbo.views import CategoryObjectList


def home(request):
    return render(
        request,
        'unicef/home.html',
        {'categories': Category.objects.all()})


class EbolaCategoryObjectList(CategoryObjectList):

    def get_queryset(self, *args, **kwargs):
        qs = super(EbolaCategoryObjectList, self).get_queryset(*args, **kwargs)
        return qs.order_by('-publish_on', '-created')

ebola_category_object_list = EbolaCategoryObjectList()
