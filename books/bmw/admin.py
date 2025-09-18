from django.contrib import admin

# Register your models here.

from .models import Registration

admin.site.register(Registration)

from .models import ContactMessage

admin.site.register(ContactMessage)
