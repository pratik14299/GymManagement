# views.py
from django.http import JsonResponse, HttpResponse
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import MembershipType, Member, Subscription, Payment
from .serializers import MembershipTypeSerializer, MemberSerializer, SubscriptionSerializer, PaymentSerializer
import csv
from .permissions import IsAdminOrReadOnly
from rest_framework.permissions import IsAuthenticated

class MembershipTypeViewSet(viewsets.ModelViewSet):
    queryset = MembershipType.objects.all()
    serializer_class = MembershipTypeSerializer
    permission_classes = [IsAuthenticated]

class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    permission_classes = [IsAdminOrReadOnly,IsAuthenticated]

    @action(detail=False, methods=['get'])
    def download_members(self, request):
        # Create CSV response for downloading members data
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="members.csv"'
        writer = csv.writer(response)
        writer.writerow(['ID', 'Full Name', 'Phone Number', 'Status'])
        for member in Member.objects.all():
            writer.writerow([member.id, member.full_name, member.phone_number, member.status])
        return response

class SubscriptionViewSet(viewsets.ModelViewSet):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    permission_classes = [IsAuthenticated]

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['get'])
    def download_receipt(self, request, pk=None):
        # Generate receipt as a downloadable text file
        payment = self.get_object()
        receipt_content = payment.get_receipt()
        response = HttpResponse(receipt_content, content_type='text/plain')
        response['Content-Disposition'] = f'attachment; filename="receipt_{payment.id}.txt"'
        return response
