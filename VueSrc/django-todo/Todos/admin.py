from django.contrib import admin
from .models import Todo

# Register your models here.
to_register = [
    Todo,
]
admin.site.register(to_register)
