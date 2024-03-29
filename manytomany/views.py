from django.shortcuts import render, HttpResponse
from manytomany.models import *

# Create your views here.
def create(request):
  p1 = Publication(title='The Python Journal')
  p2 = Publication(title='Science News')
  p3 = Publication(title='Science Weekly')

  p1.save()
  p2.save()
  p3.save()

  a1 = Article(headline='Django lets you build web apps easily.')
  a2 = Article(headline='NASA uses Python')

  a1.save()
  a2.save()

  a1.publications.add(p1)
  a2.publications.add(p2)


  return render(request, 'manytomany.html', {})

def consult(request, id):
  public = Publication.objects.get(id=id)
  return HttpResponse(f'Publicacion: {public}')

def modify(request, new, id):
  public = Publication.objects.get(id=id)
  public.title = new

  return render(request, 'modify.html')

def delete(request, id):
  public = Publication.objects.aget(id=id)
  public.delete()
  return HttpResponse("Eliminado")