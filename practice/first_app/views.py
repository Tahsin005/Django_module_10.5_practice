from django.shortcuts import render

# Create your views here.

def about(request):
    return render(request, 'first_app/about.html')
def contact (request):
    return render(request, 'first_app/contact.html')
def poke (request):
    return render(request, 'first_app/poke.html')
