from django.urls import resolve
from django.test import TestCase
from django.template.loader import render_to_string

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
		# Em vez de se construir um obj HttpRequest manual, usa-se self.client.get
		response = self.client.get('/')
		
		# Decodificando os binários rel ao response.content
		html = response.content.decode('utf8')
		self.assertTrue(html.startswith('<html>'))
		self.assertIn('<title>To-Do lists</title>', html)
		self.assertTrue(html.strip().endswith('</html>'))
		
		self.assertTemplateUsed(response, 'home.html')
		
		# Provocando um erro propositadamente
		self.assertTemplateUsed(response, 'wrong-template.html')
		
		

	
