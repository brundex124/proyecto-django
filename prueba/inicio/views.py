from django.shortcuts import render

# Create your views here.

def pagina_principal(request):
     return render (request,"inicio/index.html")
