from django.contrib import admin

# Register your models here.
from .models import Detail

class DetailAdmin(admin.ModelAdmin):
    class Meta:
        model = Detail
admin.site.register(Detail, DetailAdmin)
