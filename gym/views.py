from rest_framework import viewsets
from .models import Member, Payment
from .serializers import MemberSerializer, PaymentSerializer
from rest_framework.decorators import action
from django.http import HttpResponse
from openpyxl import Workbook
from reportlab.pdfgen import canvas
from io import BytesIO
from django.db.models import Sum
from django.utils import timezone


# Member Viewset (for registering members, exporting to Excel)
class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

    # Custom action to export member details to Excel
    @action(detail=False, methods=['get'])
    def export_to_excel(self, request):
        wb = Workbook()
        ws = wb.active
        ws.title = "Members List"
        
        # Add header row
        ws.append(["Member ID", "Full Name", "Phone Number", "Membership Type", "Membership Start Date", "Membership End Date", "Total Payments"])

        # Add data for each member
        for member in Member.objects.all():
            total_payments = Payment.objects.filter(member=member).aggregate(Sum('amount'))['amount__sum'] or 0
            ws.append([member.id, member.full_name, member.phone_number, member.membership_type, member.membership_start_date, member.membership_end_date, total_payments])

        # Send the Excel file as response
        response = HttpResponse(content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
        response['Content-Disposition'] = 'attachment; filename=members.xlsx'
        wb.save(response)
        return response

    # Custom action to get members with pending payments (members whose membership has expired)
    @action(detail=False, methods=['get'])
    def pending_payments(self, request):
        today = timezone.now().date()
        members_with_pending_payments = Member.objects.filter(
            membership_end_date__lt=today
        ).exclude(
            id__in=Payment.objects.filter(payment_date__gte=today).values('member')
        )
        member_serializer = MemberSerializer(members_with_pending_payments, many=True)
        return HttpResponse(member_serializer.data)


# Payment Viewset (for recording payments, generating receipts)
class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

    # Custom action to generate payment receipt as PDF
    @action(detail=True, methods=['get'])
    def generate_receipt(self, request, pk=None):
        payment = self.get_object()

        # Create an in-memory buffer for PDF
        buffer = BytesIO()
        p = canvas.Canvas(buffer)

        # Add details to the receipt
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
