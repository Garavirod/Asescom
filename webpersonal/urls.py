"""webpersonal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core import views as core_views #this going to import from our app calld "core" the file "views"
from portfolio import views as portfolio_views
from django.conf import settings #cargará el archivos settings dentro de la memoria, y de setting podemos acceder a ls varibles MEDIA_URL Y MEDIA_ROOT
urlpatterns = [
    path('',core_views.home, name="home"), #string is empty beacuse is program's root
    path('about-me/',core_views.about, name="about"),
    path('suitcase/',portfolio_views.suitcase, name="suitcase"),
    path('contact/',core_views.conatct, name="contacts"),
    path('admin/', admin.site.urls),
]

# Si estamos en modo DEBUG = TRUE (codeando)
#Es una forma o truco para servir ficehros e modo DEBUG como sifuera un servidor normal
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

  #from django.conf.urls.static import static 
    #Nos permite servir fiechoer estáticos
    #Intentamos decir que si alguien intenta acceder a la ruta de la imagen media/projects/files le sirva
    #Agregamos al urlpatterns el nuevo patron de un path normal
    #urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)