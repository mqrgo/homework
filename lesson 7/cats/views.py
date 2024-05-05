from django.shortcuts import render, get_object_or_404
from cats.models import Cat

# Create your views here.
def index(request):
    cats = Cat.objects.all()
    return render(request, 'index.html', {'cats': cats})

def about(request, cat_id):
    cat = get_object_or_404(Cat, pk=cat_id)
    return render(request, 'about.html', {'cat': cat})