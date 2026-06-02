from django.contrib import admin
from .models import Enquiry

@admin.register(Enquiry)
class EnquiryAdmin(admin.ModelAdmin):
    list_display    = ['company_name', 'person_name', 'email', 'phone', 'submitted_at', 'is_read']
    list_filter     = ['is_read', 'submitted_at']
    search_fields   = ['company_name', 'person_name', 'email']
    list_editable   = ['is_read']
    readonly_fields = ['submitted_at']