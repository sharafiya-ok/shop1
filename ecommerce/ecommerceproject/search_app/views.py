from django.http import HttpResponse
from django.shortcuts import render
from shop.models import Products
from django.db.models import Q

# Create your views here.
def searchResult(request):
    Product=None
    Query=None
    if 'Q' in request.GET:
        Query=request.GET.get('Q')
        products=Products.objects.all().filter(Q(name__contains=Query) | Q(description__contains=Query))
        return render(request,'search.html',{'Query': Query,'products': products})