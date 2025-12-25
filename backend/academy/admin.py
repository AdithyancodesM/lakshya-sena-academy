from django.contrib import admin
from django.http import HttpResponse
from datetime import datetime
import openpyxl

from .models import Enquiry


@admin.register(Enquiry)
class EnquiryAdmin(admin.ModelAdmin):

    list_display = ('name', 'phone', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('name', 'phone')
    ordering = ('-created_at',)

    readonly_fields = ('name', 'phone', 'message', 'created_at')

    actions = ['mark_contacted', 'mark_closed', 'export_as_excel']

    def mark_contacted(self, request, queryset):
        queryset.update(status='contacted')
    mark_contacted.short_description = "Mark selected as Contacted"

    def mark_closed(self, request, queryset):
        queryset.update(status='closed')
    mark_closed.short_description = "Mark selected as Closed"

    def has_delete_permission(self, request, obj=None):
        return False  # 🔒 Prevent deletion

    def export_as_excel(self, request, queryset):
        wb = openpyxl.Workbook()
        ws = wb.active
        ws.title = "Enquiries"

        ws.append(["Name", "Phone", "Message", "Status", "Created At"])

        for enquiry in queryset:
            ws.append([
                enquiry.name,
                enquiry.phone,
                enquiry.message,
                enquiry.status,
                enquiry.created_at.strftime("%Y-%m-%d %H:%M"),
            ])

        response = HttpResponse(
            content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
        response["Content-Disposition"] = (
            f"attachment; filename=enquiries_{datetime.now().date()}.xlsx"
        )

        wb.save(response)
        return response

    export_as_excel.short_description = "Export selected enquiries to Excel"
