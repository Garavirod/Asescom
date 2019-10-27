from django.shortcuts import render, HttpResponse #Nos permite responder una peicion devolviendo un código HTML

# Create your views here.
#código duro
# def home(request):
#     html_response = "<h1>MY first view made in Django2.0.2</h1>"
#     return HttpResponse(html_response)

def home(request):
    return render(request,"core/home.html") #Hacemos una llamada de renderizado de una plantilla html

def about(request):
    return render(request,"core/about.html")



def conatct(request):
    return render(request,"core/contact.html")    