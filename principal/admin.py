from django.contrib import admin
from .models import *

# Register your models here.

class ServicioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'orden')
    list_editable = ('orden',)
    ordering = ('orden',)

admin.site.register(Servicio, ServicioAdmin)

from .models import BlogPost

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha_publicacion', 'orden')
    list_editable = ('orden',)
    ordering = ('orden',)

admin.site.register(BlogPost, BlogPostAdmin)
