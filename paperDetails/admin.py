from django.contrib import admin
from .models  import Faculty, Paper, BulkRequest

admin.site.register(Faculty)
admin.site.register(Paper)
admin.site.register(BulkRequest)
# Register your models here.