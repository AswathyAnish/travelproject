from django.shortcuts import render
from django.shortcuts import render
from . models import Details


# Create your views here.
def index(request):
    obj = Details.objects.all()
    return render(request, "index.html", {'detail': obj})

# Create your views here.

# Create your views here.
