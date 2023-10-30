from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.utils import timezone
from datetime import timedelta
from .models import User, AppUsage, Transactions
from django.shortcuts import render

from django.http import HttpResponse #Landing Page

def landing_page(request):
    return HttpResponse("Welcome to Standard Bank App!")



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_dashboard(request):
    end_date = timezone.now()
    start_date = end_date - timedelta(days=30)
    
    user_transactions = Transactions.objects.filter(sender=request.user, timestamp__range=[start_date, end_date])
    app_usages = AppUsage.objects.filter(user=request.user, timestamp__range=[start_date, end_date])
    
    total_time_spent = sum([usage.session_end - usage.session_start for usage in app_usages], timedelta())

    data = {
        'first_name': request.user.first_name,
        'transactions': [{'id': trans.id, 'amount': trans.amount, 'status': trans.status} for trans in user_transactions],
        'time_spent_in_app': str(total_time_spent),
    }

    return render(request, 'dashboard.html', data)
