from django.contrib import admin
from .models import Complaint
# Register your models here.
@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    list_display = ["title","author","created_date"]
    list_display_links = ["title","author","created_date"]
    search_fields = ["title"]
    class Meta:
        model = Complaint