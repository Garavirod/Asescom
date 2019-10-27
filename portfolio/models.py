from django.db import models

# Create your models here.
class Project(models.Model):
    title=models.CharField(max_length=100,verbose_name="Título")
    description = models.TextField(verbose_name="Descripción")
    link = models.URLField(null=True, blank=True,verbose_name="Dirección web")
    image = models.ImageField(verbose_name="Imagen",upload_to="projects") #upload_to todas la imagenes que suban los usarios se subiran en el directorio projects para tenrlo separado de otros posbibles modelsque pudiesen existir
    created = models.DateTimeField(auto_now_add=True,verbose_name="Fecha de creación") #Campo de fecha y hora una vez que se crea "once"
    updated = models.DateTimeField(auto_now=True,verbose_name="Fecha de modificación") #Cada vez que se actualiza una instacncia
    
    #Extended metadata
    class Meta:
        verbose_name='Proyecto'
        verbose_name_plural ='Proyectos' #This does not add 's', instead of take this
        ordering = ["-created"] #we order by creation of project, '-' means reverse its starts with newest
    def __str__(self):
        return self.title    
