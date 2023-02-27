from django.contrib import admin
from .models import Reserve

class ReserveAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Reserve._meta.fields]
    list_filter = ["time", "name"]
    search_fields = ["name", "phone"]

    class Meta:
        model = Reserve

admin.site.register(Reserve, ReserveAdmin)

# Register your models here.
