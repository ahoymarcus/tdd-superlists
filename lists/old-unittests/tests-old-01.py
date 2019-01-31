from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest

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

	def test_home_page_returns_correct_html(self):
		request = HttpRequest()
		response = home_page(request)
		
		# Decodificando os binários rel ao response.content
		html = response.content.decode('utf8')
		self.assertTrue(html.startswith('<html>'))
		
		# Refatorando
		#self.assertIn('<title>To-Do lists</title>', html)
		expected_html = render_to_string('home.html')
		self.assertEqual(html, expected_html)
		
		

	
