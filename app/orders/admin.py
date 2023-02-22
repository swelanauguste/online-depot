import csv
import datetime
from django.utils.safestring import mark_safe
from django.contrib import admin
from django.http import HttpResponse
from django.urls import reverse

from .models import Order, OrderItem


def export_to_csv(modeladmin, request, queryset):
    opts = modeladmin.model._meta
    content_disposition = f"attachment; filename={opts.verbose_name}.csv"
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = content_disposition
    writer = csv.writer(response)
    fields = [
        field
        for field in opts.get_fields()
        if not field.many_to_many and not field.one_to_many
    ]
    # Write a first row with header information
    writer.writerow([field.verbose_name for field in fields])
    # Write data rows
    for obj in queryset:
        data_row = []
        for field in fields:
            value = getattr(obj, field.name)
            if isinstance(value, datetime.datetime):
                value = value.strftime("%d/%m/%Y")
            data_row.append(value)
        writer.writerow(data_row)
    return response


export_to_csv.short_description = "Export to CSV"


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ["product"]


def order_pdf(obj):
    url = reverse("order_pdf", args=[obj.id])
    return mark_safe(f'<a  target="_blank" href="{url}">PDF</a>')


order_pdf.short_description = "Invoice"


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "first_name",
        "last_name",
        "email",
        "address",
        "paid",
        "created_at",
        "updated_at",
        order_pdf,
    ]
    list_filter = ["paid", "created_at", "created_at"]
    inlines = [OrderItemInline]
    actions = [export_to_csv]
