from django.db import models


# Create your models here.
# Veja que como o modelo Item insere chave estrangeira daqui na forma de objeto, este modelo, então, tem de vir primeiro
class List(models.Model):
	pass
	
class Item(models.Model):
	text = models.TextField(default='')
	
	# Veja que o objetivo não é criar uma coluna de texto 'list', simplesmente, mas criar um relacionamento de chave estrangeira nesta coluna
	#list = models.TextField(default='')
	list = models.ForeignKey(List, default=None)
	












