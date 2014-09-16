from category.models import Category

from django.core.urlresolvers import reverse
from django.test import TestCase
from django.test.client import Client
from django.test.utils import override_settings

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
