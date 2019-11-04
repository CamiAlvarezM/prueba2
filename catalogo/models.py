from django.db import models
from django.urls import reverse # Used to generate URLs by reversing the URL patterns
import uuid # Required for unique book instances


# Create your models here.
class Index(models.Model):
    #Model representing a index."""
	name = models.CharField(max_length=200)
	
	def __str__(self):
		return self.name

class Info(models.Model):
    #Model representing a info."""
	name = models.CharField(max_length=200)
	
	def __str__(self):
		return self.name

class Formulario(models.Model):
	#Model representing a formulario."""
	name = models.CharField(max_length=200)
	
	def __str__(self):
		return self.name


class Galeria(models.Model):
	#Model representing a galeria."""
	name = models.CharField(max_length=200)
	
	def __str__(self):
		return self.name

class We(models.Model):
	#Model representing a nosotros."""
	name = models.CharField(max_length=200)
	
	def __str__(self):
		return self.name