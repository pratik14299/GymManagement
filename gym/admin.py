from django.contrib import admin
from .models import Member, Payment
from django.http import HttpResponse
from openpyxl import Workbook
from reportlab.pdfgen import canvas
from io import BytesIO

# Action to export members to Excel
def export_members_to_excel(modeladmin, request, queryset):
    wb = Workbook()
    ws = wb.active
    ws.title = "Members List"
    
    # Add header row
    ws.append(["Member ID", "Full Name", "Phone Number", "Membership Type", "Membership Start Date", "Membership End Date", "Total Payments"])

    for member in queryset:
        total_payments = Payment.objects.filter(member=member).aggregate(sum('amount'))['amount__sum'] or 0
        ws.append([member.id, member.full_name, member.phone_number, member.membership_type, member.membership_start_date, member.membership_end_date, total_payments])

    response = HttpResponse(content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
    response['Content-Disposition'] = 'attachment; filename=members.xlsx'
    wb.save(response)
    return response

export_members_to_excel.short_description = "Export Selected Members to Excel"

# Action to generate payment receipt PDF
def generate_payment_receipt(modeladmin, request, queryset):
    payment = queryset.first()
    buffer = BytesIO()
    p = canvas.Canvas(buffer)
    p.drawString(100, 800, f"Payment Receipt")
    p.drawString(100, 780, f"Member: {payment.member.full_name}")
    p.drawString(100, 760, f"Amount: {payment.amount}")
    p.drawString(100, 740, f"Payment Date: {payment.payment_date}")
    p.drawString(100, 720, f"Payment Method: {payment.payment_method}")
    p.showPage()
    p.save()

    buffer.seek(0)
    response = HttpResponse(buffer.getvalue(), content_type="application/pdf")
    response['Content-Disposition'] = f'attachment; filename=receipt_{payment.id}.pdf'
    return response

generate_payment_receipt.short_description = "Generate Receipt for Payment"

# Register Models
class MemberAdmin(admin.ModelAdmin):
    actions = [export_members_to_excel]

class PaymentAdmin(admin.ModelAdmin):
    actions = [generate_payment_receipt]

admin.site.register(Member, MemberAdmin)
admin.site.register(Payment, PaymentAdmin)
