from django.contrib import admin

# Register your models here.
from .models import User

# This will show my registered users
admin.site.register(User)
