from django.urls import resolve
from django.test import TestCase
from lists.views import home_page

"""
# Apenas testando se o teste funciona
# py manage.py test
class SmokeTest(TestCase):
	def test_bad_maths(self):
		self.assertEqual(1 + 1, 3)
"""

# Create your tests here.
class HomePageTest(TestCase):
	def test_root_url_resolves_to_home_page_view(self):
		found = resolve('/')
		self.assertEqual(found.func, home_page)





