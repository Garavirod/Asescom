from django.contrib import admin
from .models import Project
# Register your models here

#we extend admin tools
class ProjectAdmin(admin.ModelAdmin):
    #redefinimos la varibale para que uestr en en panle de solo lectura
    readonly_fields = ('created','updated') 

#Pasamos la configuraacion extendida al admin.site
admin.site.register(Project,ProjectAdmin)

