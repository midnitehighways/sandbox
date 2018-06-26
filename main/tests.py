# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.utils import timezone

from main.models import Part

class PartTestCase(TestCase):
	def setUp(self):
		Part.objects.create(name='test name', content='some random content', pub_date=timezone.now())
	
	def test_part_name(self):
		part = Part.objects.get(name='test name')
		self.assertEqual(part.id, 1)
		self.assertEqual(part.content, 'some random content')


# if __name__ == '__main__':
#     unittest.main()