from django.contrib import admin
from .models import *

admin.site.register(Pessoa)
admin.site.register(Gerente)
admin.site.register(Empresa)
admin.site.register(Vendedor)
