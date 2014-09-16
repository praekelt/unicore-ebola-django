from category.models import Category

from django.core.urlresolvers import reverse
from django.test import TestCase
from django.test.client import Client
from django.test.utils import override_settings
from post.models import Post

import string


class OrderingTest(TestCase):

    def setUp(self):
        for letter, index in zip(string.ascii_lowercase, range(26, 0, -1)):
            Category.objects.create(title='%d. title %s' % (index, letter,),
                                    slug='%d-slug-%s' % (index, letter,))

    def assertBefore(self, response, a, b):
        self.assertContains(response, a)
        self.assertContains(response, b)
        self.assertTrue(
            response.content.index(a) < response.content.index(b),
            'a does not come before b.')

    @override_settings(PATCH_CATEGORY_ORDERING=True)
    def test_order_patching(self):
        """
        patching query to order on digits in title
        """
        client = Client()
        response = client.get(reverse('home'))
        self.assertBefore(response, '2. title y', '10. title q')

    @override_settings(PATCH_CATEGORY_ORDERING=False)
    def test_order_default(self):
        client = Client()
        response = client.get(reverse('home'))
        self.assertBefore(response, '10. title q', '2. title y')

    @override_settings(PATCH_CATEGORY_ORDERING=True)
    def test_category_link_for_1_post(self):
        p = Post.objects.create(
            title='only 1 post',
            content='sample content')
        p.primary_category = Category.objects.all()[0]
        p.save()
        p = Post.objects.create(
            title='sample title for multiple',
            content='sample content')
        p.primary_category = Category.objects.all()[1]
        p.save()
        p = Post.objects.create(
            title='sample title for multiple 2',
            content='sample content')
        p.primary_category = Category.objects.all()[1]
        p.save()

        client = Client()
        response = client.get(reverse('home'))

        # the homepage will show a link directly to this post
        self.assertContains(response, 'only-1-post')
        self.assertNotContains(response, 'sample-title-for-multiple')
        self.assertNotContains(response, 'sample-title-for-multiple-2')
