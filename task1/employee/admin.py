from django.contrib import admin
from .models import empleave_model,empregister_model

# Register your models here.
admin.site.register(empregister_model)  
admin.site.register(empleave_model)

