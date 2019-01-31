"""
	Teste Funcional:
		Estes tipos de testes aqui com a bibli Selenium permite todo um controle sobre o Navegador, de modo a permitir testar toda a funcionalidade do ponto de vista do User.
		Também conhecido por Teste de Aceitação, Teste Fim-A-Fim ou Black-box-Test (Caixa-Preta), pois tem como escopo observar o funcionamento da apliação no todo e do ponto de vista externo (ou seja, sem nada saber ou inquirir sobre a parte interna dos processos).
		Retirando da qui em diante as esperas explícitas e usando uma lóg de polling/retentiva.
"""
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException

import time
#import unittest

# Inserindo lóg de polling/retentiva para supri a faltas das esperas explícitas (ou implícitas)
MAX_WAIT = 10

"""
	Esta é a conf inicial da classe antes da refatoração para o diretório de pacotes python functional_tests/
class NewVisitorTest(unittest.TestCase):
"""
class NewVisitorTest(LiveServerTestCase):	
	def setUp(self):
		self.browser = webdriver.Firefox()
	
	def tearDrow(self):
		self.browser.quit()
	
	"""
		Méts Auxiliares
	"""
	# Lembrando que apenas mets que começam com test... são acionados diretamente nos testes
	
	# Neste ponto nós substituímos o mét check_for_row_in_list_table() por wait_for_row_in_list_table() para lidar com o problema de espera para o código
	def wait_for_row_in_list_table(self, row_text):
		start_time = time.time()
		while True:
			try:
				table = self.browser.find_element_by_id('id_list_table')
				rows = table.find_elements_by_tag_name('tr')
				self.assertIn(row_text, [row.text for row in rows])
				return
			except (AssertionError, WebDriverException) as e:
				# Aqui está o counter que permitirá a saída do laço caso a exceção exaurir o limite def MAX_WAIT
				if time.time() - start_time > MAX_WAIT:
					raise e
				time.sleep(0.5)
	
	"""
		Méts de Testes
	"""
	def test_can_start_a_list_and_retrieve_it_later(self):
		# Edith ouvir falar de uma nova apicação online interessante para lista de tarefas. Ela decide verificar sua homepage
		#self.browser.get('http://127.0.0.1:8000')
		self.browser.get(self.live_server_url)
		
		# Ela percebe que o título da página e o cabeçalho menscionam listas de tarefas (to-do)
		self.assertIn('To-Do lists', self.browser.title)
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('To-Do', header_text)
		
		# Ela é convidade a inserir um item de tarefa imediatamente
		inputbox = self.browser.find_element_by_id('id_new_item')
		self.assertEqual(
			inputbox.get_attribute('placeholder'),
			'Enter a to-do item'
		)
		
		# Ela digita "Buy peacock feathers" em um caixa de texto (o hobby de Edith é fazer iscas para pesca com fly)
		inputbox.send_keys('Buy peacock feathers')
		
		# Quando ela tecla enter, a página é atualizada, e agora a página lista "1: Buy peacock feathers" como um item em uma lista de tarefas
		inputbox.send_keys(Keys.ENTER)
		# Esta é uma função de "espera explícita", e serve para prover à nova pág tempo de carregamento inicial
		# Veja ainda que além do problema de determinar o melhor tempo, se um recurso qq não é usado nestes pontos, será dado erro porque haverá problema na sincronia dos processos.
		
		"""
			Antigo cód com espera explicita
		#time.sleep(5)
		#self.check_for_row_in_list_table('1: Buy peacock feathers')
		"""
		self.wait_for_row_in_list_table('1: Buy peacock feathers')
		
		# Ainda continua havendo uma caixa de texto convidando-a a acrescentar outro item. Ela insere "Use peacock feathers to make a fly" (Edith é bastante metódica)
		inputbox = self.browser.find_element_by_id('id_new_item')
		inputbox.send_keys('Use peacock feathers to make a fly')
		inputbox.send_keys(Keys.ENTER)
		#time.sleep(5)
		
		# A pág é atualizada novamente e agora mostra os dois itens em sua lista
		"""
			Chamadas antigas para o mét que auxiliava com a espera explícita
		self.check_for_row_in_list_table('1: Buy peacock feathers')
		self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')
		"""
		self.wait_for_row_in_list_table('1: Buy peacock feathers')
		self.wait_for_row_in_list_table('2: Use peacock feathers to make a fly')
		
		# Edith se pergunta se o site lembrará de sua lista. Então ela nota que o site gerou um URL único para ela -- há um pequeno texto explicativo para isso
		self.fail('Finish the test')


	# Ela acessa esse URL - sua lista de tarefas continua lá.


	# Satisfeita, ela volta a dormir


""" 
	Tirando if name == 'main', que era necessário para inicializar um arq manualmente, pois agora o arq será iniciado pelo executor de testes diretamente.
	Lembrando que como temos agora um marcador de diretório de pacotes válido com __init__, Django pode lidar com o diretório diretamente.
if __name__ == '__main__':
	unittest.main(warnings='ignore')
"""






