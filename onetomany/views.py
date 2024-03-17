from django.shortcuts import render, HttpResponse
from onetomany.models import *

# Create your views here.
def create(request):
  reporter1 = Reporter(first_name='Jhon', last_name='Smith', email='jhon@gmail.com')
  reporter2 = Reporter(first_name='Paul', last_name='Jones', email='paul@gmail.com')

  reporter1.save()
  reporter2.save()
  
  art1 = Article(headline='No hay nadie que ame el dolor mismo, que lo busque, lo encuentre y lo quiera, simplemente porque es el dolor.', reporter=reporter1)
  art2 = Article(headline='El trozo de texto estándar de Lorem Ipsum usado desde el año 1500 es reproducido debajo para aquellos interesados. Las secciones 1.10.32 y 1.10.33 de "de Finibus Bonorum et Malorum" por Cicero son también reproducidas en su forma original exacta, acompañadas por versiones en Inglés de la traducción realizada en 1914 por H. Rackham.', reporter=reporter2)

  art1.save()
  art2.save()

  return render(request, 'onetomany.html', {})

def consultas(request):
  repo1 = Reporter.objects.get(id=1)
  repo2 = Reporter.objects.get(id=2)
  #repo3 = Reporter.objects.all()

  query1 = repo1.article_set.all()
  query2 = repo2.article_set.all()

  return render(request, 'consultas.html', {'repo1':repo1, 'query1':query1, 'repo2':repo2, 'query2':query2})

def modify(request, new, id):
  report = Reporter.objects.get(id = id)
  report.first_name = new
  return HttpResponse("Modificado")

def delete(request, id):
  report = Reporter.objects.get(id = id)
  report.delete()
  return HttpResponse('Eliminado')