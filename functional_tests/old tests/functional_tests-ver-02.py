"""
	Teste Funcional:
		Estes tipos de testes aqui com a bibli Selenium permite todo um controle sobre o Navegador, de modo a permitir testar toda a funcionalidade do ponto de vista do User.
		Também conhecido por Teste de Aceitação, Teste Fim-A-Fim ou Black-box-Test (Caixa-Preta), pois tem como escopo observar o funcionamento da apliação no todo e do ponto de vista externo (ou seja, sem nada saber ou inquirir sobre a parte interna dos processos).
"""
from selenium import webdriver
import unittest

class NewVisitor(unittest.TestCase):
	def setUp(self):
		self.browser = webdriver.Firefox()

	def tearDrow(self):
		self.browser.quit()
		
	def test_can_start_a_list_and_retrieve_it_later(self):
		# Edith ouvir falar de uma nova apicação online interessante para lista de tarefas. Ela decide verificar sua homepage
		self.browser.get('http://127.0.0.1:8000')
		
		# Ela percebe que o título da página e o cabeçalho menscionam listas de tarefas (to-do)
		self.assertIn('To-Do lists', self.browser.title)
		self.fail('Finish the test')

	# Ela é convidade a inserir um item de tarefa imediatamente
	

	# Ela digita "Buy peacock feathers" em um caixa de texto (o hobby de Edith é fazer iscas para pesca com fly)


	# Quando ela tecla enter, a página é atualizada, e agora a página lista "1: Buy peacock feathers" como um item em uma lista de tarefas


	# Ainda continua havendo uma caixa de texto convidando-a a acrescentar outro item. Ela insere "Use peacock feathers to make a fly" (Edith é bastante metódica)


	# A página é atualizada novamente e agora mostra os dois itens em sua lista


	# Edith se pergunta se o site lembrará de sua lista. Então ela nota que o site gerou um URL único para ela -- há um pequeno texto explicativo para isso


	# Ela acessa esse URL - sua lista de tarefas continua lá.


	# Satisfeita, ela volta a dormir

if __name__ == '__main__':
	unittest.main(warnings='ignore')
	






