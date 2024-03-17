from django.shortcuts import render, HttpResponse
from onetoone.models import Place, Restaurant
# Create your views here.

def create(request):
  place1 = Place(name='PizzaStack', address='Cra 1 #24-27')
  place1.save()

  p = Place.objects.get(id=4)
  restaurant = Restaurant(place=p, employees=50)
  restaurant.save()

  print(restaurant.place.address)
  return render(request, 'onetoone.html', {})

def consult(request, id):
  place = Place.objects.get(id=id)
  print(place)
  return HttpResponse(f'Nombre: {place.name}Lugar: {place.address} ')

def modify(request, new, id):
  place = Place.objects.get(id=id)
  place.address = new
  place.save()

  return HttpResponse('Modificado')

def delete(request, id):
  place = Place.objects.get(id=id)
  place.delete()
  return HttpResponse("Eliminado")