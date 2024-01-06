from django.shortcuts import render

from django.http import HttpResponse
from .models import *

# Choose

def get_Choose(request):
    choose = Choose.objects.all()
    context = {"chooses":choose}
    return HttpResponse('Data qaytdi')

def create_Choose(request):
    choose = Choose.objects.create()
    return HttpResponse('Data yaraldi')

def update_Choose(request):
    choose = Choose.objects.get(id=1)
    choose.title="Tanlov"
    choose.save()
    return HttpResponse('Data yangilandi')

def delete_Choose(request):
    choose = Choose.objects.get(id=1)
    choose.delete()
    return HttpResponse("data o'chirildi")

# Choose_enjoy

def get_Choose_enjoy(request):
    choose_en = Choose_enjoy.objects.all()
    context = {"chooses":choose_en}
    return HttpResponse('Data qaytdi')

def create_Choose_enjoy(request):
    choose_en = Choose_enjoy.objects.create()
    return HttpResponse('Data yaraldi')

def update_Choose_enjoy(request):
    choose_en = Choose_enjoy.objects.get(id=1)
    choose_en.title="Tanlov"
    choose_en.save()
    return HttpResponse('Data yangilandi')

def delete_Choose_enjoy(request):
    choose_en = Choose_enjoy.objects.get(id=1)
    choose_en.delete()
    return HttpResponse("data o'chirildi")

#gallery

def get_gallery(request):
    gallery = gallery.objects.all()
    context = {"images":gallery}
    return HttpResponse('Data qaytdi')

def create_gallery(request):
    gallery = gallery.objects.create(icon='image.jpg')
    # ikonka bilan ishlashni hali o'rganmadik shunga oddiy string berib turipman
    return HttpResponse('Rasm qoshildi')

def update_gallery(request):
    gallery = gallery.objects.get(id=1)
    gallery.title="Burgers"
    gallery.save()
    return HttpResponse('Rasm yangilandi')

def delete_gallery(request):
    gallery = gallery.objects.get(id=1)
    gallery.delete()
    return HttpResponse("Rasm o'chirildi")

#order

def get_order(request):
    order = Order.objects.all()
    context = {"orders":order}
    return HttpResponse('Data qaytdi')

def create_order(request):
    order = Order.objects.create()
    return HttpResponse('Buyurtma qoshildi')

def update_order(request):
    order = Order.objects.get(id=1)
    order.title="Buyurtmalar"
    order.save()
    return HttpResponse('Buyurtma yangilandi')

def delete_order(request):
    order = Order.objects.get(id=1)
    order.delete()
    return HttpResponse("Buyurtma o'chirildi")